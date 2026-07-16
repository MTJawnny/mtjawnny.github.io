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

## Homepage (index.html) nav
- index.html is the landing page, NOT a proxy card page despite sitting at
  root. Five section pips: Table, Cards, Tools, Stack, Coffers. Flat DOM on
  purpose (the desktop CSS-only hover reveal needs the pips + center to be
  literal siblings).
- Three breakpoints:
  - Mobile (< 640px): connected PENTAGON RING. Whole layout derives from one
    knob, --circle (pip diameter, clamp(104px, 31vw, 138px)); --half =
    circle/2 and --R = 1.02 * circle set the ring radius so pips never
    overlap or overflow. Same unit-circle coefficients as the desktop
    pentagon. Nudge feel via those two values (circle size, --R multiplier).
  - Tablet (640-899px): plain two-column grid.
  - Desktop (900px+): full pentagon with a hover-reveal center (social
    cluster + per-pip descriptions).
- All mobile-specific rules live in a single @media (max-width: 639.98px)
  block. Keep tablet/desktop untouched when editing it.
- "Feeling Lucky?" button (mobile only): a floating d6 die + label at the
  ring center that jumps to a random page. Destinations are a commented
  array in the inline <script> at the bottom of index.html (edit freely);
  href="/cards/" is the no-JS fallback. Hidden on tablet/desktop via the
  shared base display:none.
- Screenshot workflow for homepage/font-accurate renders: the headless
  browser can't reach Google Fonts through the proxy, so fetch the Barlow /
  Barlow Condensed woff2 files with curl, swap the @import for a local
  @font-face, and render with no browser proxy (routing the browser through
  the proxy breaks the localhost page load).

## CDN & media URLs (contract — do not drift)
- **Card images are keyed by oracle_id, NEVER by slug.** Canonical URL:
  https://cdn.mtjawnny.com/cards/png/<oracle_id>.png
  Double-faced cards: <oracle_id>-front.png and <oracle_id>-back.png.
  Single-faced: no suffix. PNG only — no jpg, no other extensions. This is
  the full-res canonical asset; solo card pages always use it via cardImg().
- **Gallery thumbnails (2026-07) are a derived WebP, gallery-only.** Canonical
  URL: https://cdn.mtjawnny.com/cards/webp/<oracle_id>.webp (DFCs:
  <oracle_id>-front.webp / -back.webp — same suffix convention as the PNG).
  Generated automatically by the pipeline's image_sync.py alongside the PNG
  (600px wide, quality 82) — never hand-authored, never referenced from a
  solo card page. Currently only cards/index.html's search gallery uses it,
  via `.replace('/cards/png/','/cards/webp/')` on the resolved PNG URL, with
  a fallback chain: webp thumb -> full PNG -> noart SVG.
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
- Fonts: Barlow / Barlow Condensed, self-hosted (see Hard rules) —
  '@font-face' via /fonts/fonts.css, weights 400/500/600 (Barlow) and
  400/600/700/800/900 (Barlow Condensed)
- Flat surfaces over gradients — deliberate anti-AI-template aesthetic
- h1 clamp standard: clamp(2.4rem, 14vw, 3.6rem)
- Body/long-form text floor (2026-07): 1.06rem minimum for anything read
  mid-game — oracle text, tips/misplays, combos, rulings, stack-visual body
  copy, format-guide rule bullets. UI chrome (buttons, badges, small labels,
  citations) stays smaller, ~0.8-0.95rem. Canonical reference: pris.html
  (cards), stack/the-stack.html (stack pages), table/pauper.html (format
  guides) — clone bases already carry this; don't shrink it back down.
- Header tagline standard (2026-07): the `.tagline` line under an h1 (e.g.
  home's "Your Free Magic: The Gathering Toolbox!") is 1.2rem, sitting a
  flat 12px below the h1's bottom edge — tune margin-top per page to hit
  that gap since logo-wrap's own margin-bottom varies (pages with
  home/share pip labels reserve more space than the homepage). Canonical
  reference: index.html, cards/index.html, stack/index.html,
  tools/index.html. Coffers has no page-level tagline; its equivalent is
  `.section-head .sub` under "Free stuff from me to you!", same 1.2rem.
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
- Fonts are self-hosted (2026-07): every page links `/fonts/fonts.css`
  for Barlow / Barlow Condensed. NEVER reintroduce a
  fonts.googleapis.com/fonts.gstatic.com @import or <link> — the woff2
  files already live in /fonts/. Adding a new weight means downloading
  the latin-subset woff2 into /fonts/ and adding an @font-face block to
  fonts.css, not pointing back at Google's CDN.
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

## Git / environment notes
- Remote branches CANNOT be deleted from the Claude Code environment: the
  git relay blocks delete-pushes (403) and the GitHub MCP exposes no
  delete-branch/delete-ref tool. After a PR merges, only the user can
  delete the branch (PR page "Delete branch" button, or the repo's
  Branches list). Don't promise automatic branch cleanup; when a merged
  branch is left behind, tell the user it's harmless and hand them the
  one-click deletion step.

## Future notes / ideas
- Gamble mini-game: when the "Feeling Lucky?" homepage button lands on the
  Gamble card page, it should fire a fun win/lose reveal UI (a cute little
  mini-game moment, e.g. "You win!") instead of just showing the page. The
  Gamble card page is NOT built yet. When it ships: (1) add its slug to the
  Feeling Lucky destination array in index.html, and (2) build the reveal on
  the Gamble page itself, ideally triggered when arrival came from the
  Feeling Lucky button (e.g. a ?lucky=1 query param or referrer check) so it
  only games out on a "lucky" landing.

## Reference docs (read before large changes)
- MTJAWNNY-MASTER.md — overall architecture and standards
- card-build-master.md — card page build pipeline
- stack-interaction-prompt.md — stack interaction page pipeline
- TEMPLATE-00-shared-chrome.md, TEMPLATE-03-tool.md — shared page chrome
