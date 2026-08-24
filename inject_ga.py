"""
inject_ga.py - Read GA_TRACKING_ID from .env.local and inject Google Analytics
gtag.js code into all HTML files' <head> section.

Usage:
    python inject_ga.py

This script:
1. Reads .env.local for GA_TRACKING_ID
2. For each *.html in the current directory:
   a. Removes any existing GA injection block (idempotent)
   b. Inserts the gtag.js code block before </head>
3. Prints a summary of modified files

The GA tracking ID is NOT hardcoded in this script or in the HTML source.
It comes solely from .env.local (which is gitignored).
"""

import os
import re
import glob

ENV_FILE = ".env.local"
GA_BLOCK_START = "<!-- Google Analytics (gtag.js) - injected by inject_ga.py -->"
GA_BLOCK_END = "<!-- End Google Analytics -->"


def read_env(filepath):
    """Parse a simple KEY=VALUE .env file."""
    env = {}
    if not os.path.exists(filepath):
        return env
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                env[key.strip()] = value.strip()
    return env


def build_ga_block(ga_id):
    """Build the GA gtag.js HTML block using the given tracking ID."""
    return f"""  {GA_BLOCK_START}
  <script async src="https://www.googletagmanager.com/gtag/js?id={ga_id}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', '{ga_id}');
  </script>
  {GA_BLOCK_END}"""


def remove_existing_ga(html):
    """Remove any previously injected GA block (idempotent)."""
    pattern = re.compile(
        re.escape(GA_BLOCK_START) + r".*?" + re.escape(GA_BLOCK_END) + r"\s*",
        re.DOTALL,
    )
    return pattern.sub("", html)


def inject_ga(html, ga_id):
    """Inject the GA block before </head>."""
    html = remove_existing_ga(html)
    ga_block = build_ga_block(ga_id)
    # Insert before </head>, preserving indentation
    html = html.replace("</head>", ga_block + "\n</head>", 1)
    return html


def main():
    # 1. Read GA_TRACKING_ID from .env.local
    env = read_env(ENV_FILE)
    ga_id = env.get("GA_TRACKING_ID")

    if not ga_id:
        print(f"[ERROR] GA_TRACKING_ID not found in {ENV_FILE}")
        print("        Create .env.local with: GA_TRACKING_ID=G-XXXXXXXXXX")
        return 1

    print(f"[INFO] GA_TRACKING_ID = {ga_id} (from {ENV_FILE})")

    # 2. Process all HTML files
    html_files = sorted(glob.glob("*.html"))
    if not html_files:
        print("[ERROR] No HTML files found in current directory.")
        return 1

    modified = 0
    for filepath in html_files:
        with open(filepath, "r", encoding="utf-8") as f:
            original = f.read()

        updated = inject_ga(original, ga_id)

        if updated != original:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(updated)
            print(f"  [OK] {filepath} - GA injected")
            modified += 1
        else:
            print(f"  [SKIP] {filepath} - already up to date")

    print(f"\n[DONE] {modified}/{len(html_files)} files updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
