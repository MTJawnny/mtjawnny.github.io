# MTJawnny — Claude Code Instructions

## What this is
Free Commander-focused MTG resource site (mtjawnny.com). Static GitHub Pages
repo — no build step, no framework, no shared stylesheet. Each HTML page
inlines its own CSS. Solo-maintained.

## Brand positioning (do not violate)
Proxies are framed as playtesting/budget/accessibility tools — NEVER as
counterfeits. Site operates under WotC's Fan Content Policy: proper
attribution required, content must stay free. This is a values decision,
not just legal positioning.

## Architecture
- Root-level HTML files are card pages meant to get printed on physical
  QR-coded proxies. Do not add unrelated pages at root.
- Tools live under /tools/
- Card explainers live under /cards/, indexed via cardex.html
- Rules interaction pages live under /stack/
- /coffers/ = free assets + Ko-fi monetization
- Global pip-ring footer nav appears on all section pages

## Design system
- Palette: plum/bronze/cream — CSS vars --surface, --bronze, --bronze-dim
- Fonts: Barlow / Barlow Condensed
- Flat surfaces over gradients — deliberate anti-AI-template aesthetic
- h1 clamp standard: clamp(2.4rem, 14vw, 3.6rem)
- No auto-open help panels — button-only (?), no localStorage first-visit logic

## Hard rules
- Em-dash banned in body copy. Permitted only in <title> tags, CSS comments,
  Governing Rules label cells, and share-title script variables.
- All card data (oracle text, rulings, CR citations, legality) must be
  independently verified against Scryfall/Gatherer and local
  mtg-comprehensive-rules.md. Never propagate unverified claims — drop them.
- No CDN dependencies for tool functionality — vendor libraries inline.

## Editing style
- Prefer surgical str_replace-style edits over full file rewrites.
- Card build pipeline: clone pris.html as template → verify data → swap
  content → rebuild visual → fix mana symbol CSS subset → register in
  cardex.html. Full pipeline in card-build-master.md.
- Stack interaction pages follow stack-interaction-prompt.md.

## Validation ritual — run before every ship
1. Python HTMLParser tag-balance check on changed files
2. `node --check` on all inline <script> blocks
3. Em-dash grep in body copy: grep -rn '—' *.html (excluding permitted spots)
4. GA4 tag count check: grep -c G-WKH3Y62H5H <file>
5. Functional smoke test of any interactive tool changed

## Reference docs (read before large changes)
- MTJAWNNY-MASTER.md — overall architecture and standards
- card-build-master.md — card page build pipeline
- stack-interaction-prompt.md — stack interaction page pipeline
- TEMPLATE-00-shared-chrome.md, TEMPLATE-03-tool.md — shared page chrome
