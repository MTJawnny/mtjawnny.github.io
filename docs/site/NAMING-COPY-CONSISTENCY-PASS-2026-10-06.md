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

1. Product/section names themselves do not take terminal punctuation.
2. **Main hub taglines are intentionally enthusiastic and should use an exclamation mark consistently.** This is part of MTJawnny's voice, not punctuation noise to be normalized away.
3. Keep hub copy conversational and playful rather than corporate.
4. Avoid ALL-CAPS word emphasis in ordinary descriptive taglines unless the capitalization itself is the joke.
5. Browser hub-title pattern: `<Product Name> — MTJawnny`.
6. OG/social titles may remain more descriptive because they must make sense out of site context.
7. Article/card/tool subtitles do not automatically inherit the hub exclamation rule. They may be categorical or explanatory and should be edited only when a concrete inconsistency exists.

## Exact first-pass edits

### `index.html`

Browser title:

- CURRENT: `MTJawnny`
- TARGET: `MTJawnny — Free MTG Toolbox`

Homepage tagline:

- KEEP: `Your Free Magic: The Gathering Toolbox!`

Reason: this is already on-brand and already follows the enthusiastic hub convention.

### `cards/index.html`

Meta description punctuation:

- CURRENT: `Search MTJawnny's card explainers: rulings, interactions and common misconceptions, one card at a time.`
- TARGET: `Search MTJawnny's card explainers: rulings, interactions, and common misconceptions, one card at a time.`

Visible tagline:

- CURRENT: `When reading the card does NOT explain the card!`
- TARGET: `When reading the card still doesn't explain the card!`

Reason: keep the enthusiasm, but remove ALL-CAPS emphasis and make the joke read more naturally.

### `stack/index.html`

Visible tagline:

- CURRENT: `Split Second Game Info!`
- TARGET: `Split-second game info!`

Reason: keep the exclamation while normalizing the phrase as descriptive sentence-style copy; `split-second` is adjectival here.

### `tools/index.html`

Visible tagline:

- CURRENT: `Research, Proxy, Print. Free Browser & Desktop Tools.`
- TARGET: `Research, proxy, print. Free browser & desktop tools!`

Reason: preserve the clipped cadence, normalize descriptive capitalization, and bring the hub into the shared enthusiastic punctuation style.

### `coffers/index.html`

Browser title:

- CURRENT: `Coffers — Free MTG Proxy Assets — MTJawnny`
- TARGET: `Coffers — MTJawnny`

OG title remains:

- `Coffers — Free MTG Proxy Assets`

Visible section copy:

- KEEP: `Free stuff from me to you!`

Reason: this is already the clearest example of the intended personal, enthusiastic voice.

### `table/index.html`

No visible-copy change in this pass unless a later audit identifies a missing hub tagline.

Current naming and metadata already fit the intended hierarchy:

- H1/product: `Tablekeep`
- navigation category: `Table`
- browser title: `Tablekeep — MTJawnny`
- OG title remains descriptive: `Tablekeep — MTG Game Tracker`

## Explicitly unchanged in this pass

- homepage navigation labels remain `Table`, `Cards`, `Tools`, `Stack`, `Coffers`;
- shared footer/pip navigation remains category-oriented;
- product H1s remain `Tablekeep`, `Cardex`, `Deck Tech`, `Stack It Up`, `Coffers`;
- individual Stack article subtitles are not mechanically changed because many function as categorical labels rather than hub taglines;
- format-guide taglines such as `Constructed · Eternal` are categorical labels and therefore outside the hub exclamation rule;
- tool-specific taglines such as QR Coder's `Turn any link into a scannable code.` are explanatory tool copy, not top-level hub slogans, and therefore do not need forced exclamation marks.

## Style principle

The goal is **consistent enthusiasm**, not punctuation minimalism.

A hub should feel like an invitation into a part of MTJawnny. Reference/article/tool-detail copy can remain calmer when clarity benefits from it.

## Next pass after application

**Pass 2 — Category eyebrow hierarchy**

Once these naming rules are live, visually express the category/product relationship on the five destination hubs, e.g.:

`CARDS`  
`CARDEX`

That visual change is intentionally separate from this copy-only pass.
