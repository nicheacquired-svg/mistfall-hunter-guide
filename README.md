# Mistfall Hunter Guide

An SEO-optimized fan guide website for **Mistfall Hunter** — a dark fantasy PvPvE extraction ARPG by Bellring Games / Skystone Games.

## Site Structure

| Page | Content |
|------|---------|
| `index.html` | Homepage — hero, tabbed sections, content cards, codes status |
| `guide.html` | Guides hub — categorized link cards |
| `classes.html` | All 6 classes with dual weapon stances |
| `tier-list.html` | Community tier list (with source caveats) |
| `codes.html` | Redeem codes status (verified, no fabrication) |
| `crossplay.html` | Crossplay & cross-save details |
| `player-count.html` | Live player stats & milestones |
| `review.html` | Review aggregation & reception |
| `release-date.html` | Release date, editions & pricing |
| `builds.html` | Builds hub |
| `solo-mode.html` | Solo play guide |
| `patch-notes.html` | Patch notes & roadmap |
| `twitch-drops.html` | Twitch Drops campaigns & how to claim |
| `sorcerer-build.html` | Sorcerer build guide (incl. IGN share code) |

## Tech

- Pure HTML/CSS/JS — no framework, no build step
- Dark fantasy theme (Cinzel + Inter fonts)
- Responsive design with mobile hamburger menu (768px breakpoint)
- Full favicon kit (`favicon/`)
- SEO: unique title (50-60 chars) & meta description (140-160 chars) per page, single H1 per page, proper H2/H3 hierarchy, Open Graph tags

## Local Preview

```bash
cd mistfall-hunter-guide
python -m http.server 8080
# open http://localhost:8080
```

## Content Policy

All facts on this site were cross-verified from at least 2 independent sources during research. Where sources disagree (e.g., tier list rankings), the disagreement is noted rather than fabricated.

_Mistfall Hunter is a trademark of Bellring Games / Skystone Games. This is an unofficial fan site._
