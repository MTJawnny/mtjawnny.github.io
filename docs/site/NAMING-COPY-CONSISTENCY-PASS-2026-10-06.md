# Naming & Copy Consistency Pass

**Date:** 2026-10-06  
**Status:** READY FOR SURGICAL APPLICATION  
**Parent direction:** `docs/site/SITE-PERSONALITY-AND-CONSISTENCY-2026-10-06.md`

## Scope

This is the first bounded implementation pass from the site personality/consistency direction.

This pass changes **copy and naming conventions only**. It does not add the category eyebrow, creator block, discovery surfaces, animation, new tools, or Foundry behavior.

## Canonical naming hierarchy

### Navigation/category labels

Use these generic labels when the UI is acting as navigation among the five top-level site areas:

- Table
- Cards
- Tools
- Stack
- Coffers

### Destination/product names

Use these names for the actual section/product identity:

- Tablekeep
- Cardex
- Deck Tech
- Stack It Up
- Coffers

The two layers are intentional. Do not flatten them into one naming system.

## Copy conventions

1. Product/section names do not take terminal punctuation.
2. Descriptive hub taglines are normally sentence case and do not use exclamation marks.
3. Exclamation marks remain appropriate for deliberate jokes, surprises, celebrations, or first-person enthusiasm.
4. Avoid ALL-CAPS emphasis in ordinary descriptive taglines.
5. Browser hub-title pattern: `<Product Name> — MTJawnny`.
6. OG/social titles may remain more descriptive because they must make sense out of site context.
7. Existing article/card/tool title structures are not being normalized in this pass unless a concrete inconsistency is identified.

## Exact first-pass edits

### `index.html`

Browser title:

- CURRENT: `MTJawnny`
- TARGET: `MTJawnny — Free MTG Toolbox`

Homepage tagline:

- CURRENT: `Your Free Magic: The Gathering Toolbox!`
- TARGET: `Your free Magic: The Gathering toolbox.`

Reason: the OG title already uses the descriptive form. The visible tagline should read as normal descriptive copy rather than an accidental shout.

### `cards/index.html`

Meta description punctuation:

- CURRENT: `Search MTJawnny's card explainers: rulings, interactions and common misconceptions, one card at a time.`
- TARGET: `Search MTJawnny's card explainers: rulings, interactions, and common misconceptions, one card at a time.`

Visible tagline:

- CURRENT: `When reading the card does NOT explain the card!`
- TARGET: `When reading the card still doesn't explain the card.`

Reason: preserves the joke/idea while removing ALL-CAPS emphasis and a non-deliberate exclamation.

### `stack/index.html`

Visible tagline:

- CURRENT: `Split Second Game Info!`
- TARGET: `Split-second game info.`

Reason: normal sentence case; `split-second` is acting adjectivally here.

### `tools/index.html`

Visible tagline:

- CURRENT: `Research, Proxy, Print. Free Browser & Desktop Tools.`
- TARGET: `Research, proxy, print. Free browser & desktop tools.`

Reason: preserve the clipped cadence while moving descriptive words to sentence case. Keep `&` because it functions as compact UI copy and is already part of the site's tool vocabulary.

### `coffers/index.html`

Browser title:

- CURRENT: `Coffers — Free MTG Proxy Assets — MTJawnny`
- TARGET: `Coffers — MTJawnny`

OG title remains:

- `Coffers — Free MTG Proxy Assets`

Reason: hub browser titles should follow the same product-name pattern while OG/social copy carries the descriptive purpose.

### `table/index.html`

No visible-copy change in this pass.

Current naming and metadata already fit the intended hierarchy:

- H1/product: `Tablekeep`
- navigation category: `Table`
- browser title: `Tablekeep — MTJawnny`
- OG title remains descriptive: `Tablekeep — MTG Game Tracker`

## Explicitly unchanged in this pass

- homepage navigation labels remain `Table`, `Cards`, `Tools`, `Stack`, `Coffers`;
- shared footer/pip navigation remains category-oriented;
- product H1s remain `Tablekeep`, `Cardex`, `Deck Tech`, `Stack It Up`, `Coffers`;
- `Coffers` section copy `Free stuff from me to you!` keeps its exclamation because it is deliberate first-person enthusiasm;
- individual Stack article subtitles are not being mechanically sentence-cased because many function as categorical labels rather than prose sentences;
- format-guide taglines such as `Constructed · Eternal` are categorical labels and therefore outside this sentence-case rule;
- tool-specific taglines such as QR Coder's `Turn any link into a scannable code.` already fit the convention.

## Next pass after application

**Pass 2 — Category eyebrow hierarchy**

Once these naming rules are live, visually express the category/product relationship on the five destination hubs, e.g.:

`CARDS`  
`CARDEX`

That visual change is intentionally separate from this copy-only pass.
