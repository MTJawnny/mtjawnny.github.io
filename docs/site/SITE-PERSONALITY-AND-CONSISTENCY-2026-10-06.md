# MTJawnny Site Personality & Consistency Direction

**Date:** 2026-10-06  
**Status:** Captain-approved direction; implementation to proceed in bounded passes  
**Scope:** `MTJawnny/mtjawnny.github.io` only

## 1. Goal

Make MTJawnny feel more fun, inviting, personal, and discoverable without giving up the existing visual identity or making active tools harder to use.

The desired feeling is:

> You found a Magic player's workbench on the internet, and it happens to contain a surprising number of useful things.

Not:

> An all-in-one MTG productivity platform.

The deep technology should remain underneath. The surface should still feel like: "oh, this is neat."

## 2. What should be preserved

Do not redesign the site into a generic game portal or SaaS landing page.

Preserve:

- plum / bronze / cream visual identity;
- flat surfaces over gradients;
- Barlow / Barlow Condensed typography;
- pip-ring language and five-color section accents;
- pentagonal homepage navigation;
- the unusual product names: Tablekeep, Cardex, Deck Tech, Stack It Up, Coffers;
- Deck Tech's Magic-card-like tool presentation;
- Cardex's real-card-art gallery;
- Coffers' personal, maker-oriented voice;
- Tablekeep's usability-first behavior;
- Feeling Lucky? as a discovery motif;
- accessibility and reduced-motion behavior.

## 3. Research takeaways

A broad review of small/independent playful sites and utility collections suggested several recurring strengths:

1. **Visible authorship.** Sites such as Neal.fun, Nicky Case, Orteil/DashNet, Pippin Barr, and A Soft Murmur feel personal because the creator is visibly present in the copy.
2. **Immediate interaction.** The strongest game/tool sites let the visitor do the thing quickly instead of forcing an explanatory landing funnel first.
3. **Discovery and surprise.** Random-project, random-combo, featured-item, and "what should I click?" mechanics make collections enjoyable to browse.
4. **Simplicity protects affection.** Fun should live around the task, not obstruct the task.
5. **Different things may coexist.** Games, tools, reference material, art, and experiments can share a home when a strong authorial voice and visual world hold them together.
6. **Consistency still matters.** Playful language works best when navigation labels, product names, titles, punctuation, and hierarchy are intentional rather than accidental.

Commander Spellbook was a useful MTG-specific comparison: serious reference/search utility can coexist with Random Combo, Combo of the Day, featured material, and other discovery surfaces without undermining trust.

## 4. Site strengths observed

### Homepage

- The pentagon/pip-ring navigation is distinctive and should remain.
- Feeling Lucky? is a strong native discovery idea and should be expanded as a motif rather than replaced.
- The five-section color treatment creates a coherent visual world.

### Tablekeep

- Current work strongly prioritizes actual play usability: touch behavior, tablet layout, commander damage, back-button protection, active-turn visibility, and readable controls.
- During an active game, delight should remain restrained and never interfere with state visibility.

### Cardex

- Real card art makes browsing inherently satisfying.
- Search is direct and useful.
- No-result submission behavior already turns failure into participation.

### Deck Tech

- Tool cards visually resembling Magic cards are a strong bespoke design choice.
- Do not normalize these into generic SaaS cards.

### Stack It Up

- Bite-sized interaction/reference pages make rules material approachable.
- This section can carry somewhat more playful framing than raw rules documentation, as long as the rules content stays precise.

### Coffers

- "Free stuff from me to you!" is one of the clearest examples of personal voice already on the site.
- It reinforces that MTJawnny is made by a person, not a faceless product.

## 5. Core consistency problem

MTJawnny currently uses two overlapping naming systems.

Navigation categories:

- Table
- Cards
- Tools
- Stack
- Coffers

Destination/product names:

- Tablekeep
- Cardex
- Deck Tech
- Stack It Up
- Coffers

Both systems are useful:

- the generic category names are immediately understandable in navigation;
- the product names carry personality.

The problem is not that both exist. The problem is that the relationship is not formally expressed.

### Intended hierarchy

Use the generic word as the **category** and the personality name as the **product/section title**:

- TABLE -> TABLEKEEP
- CARDS -> CARDEX
- TOOLS -> DECK TECH
- STACK -> STACK IT UP
- COFFERS -> COFFERS

A later visual pass may express this with a small category eyebrow above the H1. The naming/copy pass should first establish the underlying terminology consistently.

## 6. Editorial conventions

### 6.1 Section/product names

Canonical product names:

- `Tablekeep`
- `Cardex`
- `Deck Tech`
- `Stack It Up`
- `Coffers`

Canonical navigation/category names:

- `Table`
- `Cards`
- `Tools`
- `Stack`
- `Coffers`

Do not casually substitute one system for the other in UI labels.

### 6.2 Punctuation and energy

- Product/section names themselves do not take terminal punctuation.
- **Main hub taglines should use exclamation marks consistently.** Enthusiasm is part of MTJawnny's personality, not something to flatten out.
- Hub taglines should read like invitations into that section, not corporate descriptors.
- Avoid ALL-CAPS word emphasis in ordinary descriptive taglines unless the capitalization itself is a deliberate joke.
- Article, rules-reference, format-guide, and tool-detail subtitles do not automatically inherit the hub exclamation rule. They may remain calmer or categorical when that improves clarity.

The objective is **consistent enthusiasm**, not punctuation minimalism.

### 6.3 Browser and social titles

Browser `<title>` and social/SEO titles do **not** need to be literal copies of the H1. They should be descriptive enough to make sense outside the site.

Preferred patterns:

- Hub page browser title: `<Product Name> — MTJawnny`
- Hub page OG title: `<Product Name> — <plain-English purpose>`
- Card page: `<Card Name> — How It Works — MTJawnny`
- Stack article: `<Topic> — Stack It Up — MTJawnny`
- Tool page: `<Tool Name> — Deck Tech — MTJawnny` when useful

### 6.4 Voice

Prefer clear, conversational language over corporate product language.

The site may use first person where it improves authorship and warmth. A future bounded pass should add a compact creator presence to the homepage and evaluate small "why I made this" notes where appropriate.

## 7. Delight gradient

Fun should scale with task sensitivity.

| Surface | Target delight level |
| --- | --- |
| Homepage | High |
| Coffers | High |
| Cardex / Stack indexes | Medium-high |
| Card / interaction articles | Medium |
| Deck Tech index | Medium-high |
| Tool during active use | Low-medium |
| Tablekeep during active game | Low |

Rule:

> Put delight around the task, not in the way of the task.

## 8. Approved implementation sequence

Work through these as separate bounded passes rather than one large redesign.

### Pass 1 — Naming & copy consistency

- inventory the five main hubs and shared navigation language;
- formalize category vs product-name usage;
- make main hub taglines consistently enthusiastic, including `!`;
- remove accidental shoutiness such as unnecessary ALL-CAPS emphasis while preserving playful energy;
- normalize browser/social title patterns where they drift;
- document editorial rules so they do not drift again;
- no layout redesign and no new features.

### Pass 2 — Category eyebrow hierarchy

Visually express the category/product relationship on the five main destination pages, e.g. `CARDS` above `CARDEX`.

### Pass 3 — Creator presence

Add one compact first-person homepage block so the collection feels visibly authored without interrupting the pentagon.

### Pass 4 — Discovery layer

Expand Feeling Lucky? as a motif with contextual discovery actions such as random card / weird rule / future semantic rabbit holes.

### Pass 5 — Rotating discovery surface

Consider a tiny deterministic daily/rotating homepage discovery area instead of a news feed or dashboard.

### Pass 6 — Latest thing I made

Add a compact manually maintained "latest" / "currently tinkering with" surface if it remains low-maintenance.

### Pass 7 — Microcopy delight

Audit empty states, toasts, confirmations, 404s, sharing, download success, and other low-risk moments for restrained personality.

### Pass 8 — Gamble / Feeling Lucky Easter egg

When the Gamble card page exists, preserve the existing plan for a special Lucky-arrival reveal rather than making the normal card page permanently game-like.

### Pass 9 — Optional Jawnny notes

Evaluate compact first-person "why I made this" or "what annoyed me enough to build this" notes for selected tools.

### Pass 10 — Experiments/Lab only when justified

Do not create an empty experiments section. If enough odd Magic toys, simulations, mini-games, or visualizers accumulate later, create a dedicated home then.

## 9. Future Foundry-native playful opportunities

Once Foundry outputs are stable, consider experiences where the semantic substrate itself becomes play:

- **Card Rabbit Hole** — wander through mechanically related cards;
- **Mechanical Doppelgänger** — surprising cards that perform closely related jobs through very different wording/mechanisms;
- **How Weird Is This Card?** — corpus-relative semantic unusualness;
- **What Else Does This?** — one-click functional neighborhood from a Cardex page;
- **Function Roulette** — prompts such as "removal that doesn't destroy" or "ramp that doesn't look like ramp."

These should consume Foundry truth, not create a second semantic model in the website repo.

## 10. Explicit non-goals

Do not add merely for "fun":

- accounts;
- XP;
- streaks;
- daily-login rewards;
- badge systems;
- global confetti;
- large animated page transitions;
- background particles;
- parallax;
- glassmorphism;
- generic dashboards;
- decorative motion that interferes with active tools;
- a mascot without a real reason;
- generic AI/SaaS visual language.

## 11. Working rule

The website and Foundry are separate repositories and may advance in parallel.

Website work should not redefine Foundry semantics. Foundry-powered site features should consume stable outputs/contracts when available.
