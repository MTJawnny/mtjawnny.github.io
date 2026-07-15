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

## CDN & media URLs (contract — do not drift)
- **Card images are keyed by oracle_id, NEVER by slug.** Canonical URL:
  https://cdn.mtjawnny.com/cards/png/<oracle_id>.png
  Double-faced cards: <oracle_id>-front.png and <oracle_id>-back.png.
  Single-faced: no suffix. PNG only — no jpg, no other extensions.
- **Slug is an HTML filename only** (names the .html page, e.g. pris.html).
  It has NOTHING to do with image storage. Never build an image URL from a
  slug. Never hardcode same-origin card image paths in new/edited pages.
- **Image element uses the shared cardImg() helper**, which takes the
  oracle_id + a Scryfall fallback URL (both supplied by the resolver at
  build time). Fallback chain: R2 (cdn.mtjawnny.com) → Scryfall image CDN.
  Both offsite; a broken image needs BOTH down at once. There is no
  same-origin repo fallback for new cards.
- /cardimages/ in the repo is LEGACY ONLY — the 12 original card pages
  until the Phase 2 cutover repoints them. Do not add new images there.
  Pruned ~1 month after cutover.
- Mana symbols: canonical https://cdn.mtjawnny.com/art/manasymbols/<SYM>.svg
  (uppercase filenames). Repo /manasymbols/ copies remain as-is (small UI
  chrome; not urgent to move).
- NEVER reference r2.dev URLs anywhere — rate-limited, no edge cache.

## Design system
- Palette: plum/bronze/cream — CSS vars --surface, --bronze, --bronze-dim
- Fonts: Barlow / Barlow Condensed
- Flat surfaces over gradients — deliberate anti-AI-template aesthetic
- h1 clamp standard: clamp(2.4rem, 14vw, 3.6rem)
- Body/long-form text floor (2026-07): 1.06rem minimum for anything read
  mid-game — oracle text, tips/misplays, combos, rulings, stack-visual body
  copy, format-guide rule bullets. UI chrome (buttons, badges, small labels,
  citations) stays smaller, ~0.8-0.95rem. Canonical reference: pris.html
  (cards), stack/the-stack.html (stack pages), table/pauper.html (format
  guides) — clone bases already carry this; don't shrink it back down.
- No auto-open help panels — button-only (?), no localStorage first-visit logic

## Hard rules
- Em-dash banned in body copy. Permitted only in <title> tags, CSS and inline script comments,
  Governing Rules label cells, and share-title script variables.
- All card data (oracle text, rulings, CR citations, legality) must be
  independently verified against Scryfall/Gatherer and local
  mtg-comprehensive-rules.md. Never propagate unverified claims — drop them.
- No third-party CDN dependencies for tool FUNCTIONALITY — vendor JS
  libraries inline. (Card image/media delivery via cdn.mtjawnny.com is
  the exception and always carries a Scryfall-CDN fallback — see CDN &
  media URLs section. A missing image degrades; missing JS bricks.)
- Card-page image references come from the RESOLVED manifest (oracle_id +
  fallback URL), never from an agent guessing/fuzzy-matching a card name.
  See "Card authoring — the two-field handoff" below.

## Card authoring — the two-field handoff (multi-agent safe)
- Captain's ONLY inputs per card are two fields: `name | slug`. Everything
  else is machine-resolved. Do not ask Captain for oracle_ids, image URLs,
  or DFC info — those are derived, never hand-entered.
- The resolver (Phase 3 pipeline component) turns `name | slug` into a
  resolved manifest: name | slug | oracle_id | image_url |
  scryfall_fallback_url | is_dfc | face_urls. Agents build pages from THAT.
- HARD RULE: never fuzzy-match or guess a card's identity. Resolution is
  exact-match against Scryfall bulk. If a name is ambiguous, misspelled,
  matches zero/multiple cards, its image is missing, or the slug is already
  taken → STOP and report the exact problem in plain English. Never pick a
  "best guess" and never ship a half-resolved page.
- Until the resolver exists (pre-Phase 2/3), do this resolution carefully
  by hand and surface any ambiguity to Captain rather than guessing.

## Editing style
- Prefer surgical str_replace-style edits over full file rewrites.
- Card build pipeline: resolve name|slug → manifest (above) → clone
  pris.html as template → verify data → swap content → wire cardImg()
  with oracle_id + Scryfall fallback → rebuild visual → fix mana symbol
  CSS subset → register in cardex.html. Full pipeline in card-build-master.md.
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
