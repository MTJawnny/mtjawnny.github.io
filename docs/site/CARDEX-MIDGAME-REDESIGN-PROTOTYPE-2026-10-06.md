# Cardex Mid-Game Redesign Prototype

**Date:** 2026-10-06  
**Status:** PROTOTYPE ONLY — Captain review required; do not merge or modify production card pages yet  
**Branch:** `site/cardex-midgame-prototype-2026-10-06`

## Goal

Rebuild individual Cardex explainer pages around their actual two jobs:

1. answer the rules question quickly enough to use during a live game;
2. preserve a deeper rules explanation for users who want to understand why.

The existing pages contain strong information but put too much explanation, card presentation, and low-priority material between the visitor and the ruling they need.

## Prototype cards

Three deliberately different cards are being used to test whether one information architecture can handle multiple kinds of rules questions:

- **Blood Moon** — simple static/type-changing effect;
- **Chains of Mephistopheles** — decision-tree/replacement effect;
- **Teferi's Protection** — several simultaneous defensive effects with important exceptions.

## Research-informed principles

The prototype follows established progressive-disclosure and mobile-reference ideas:

- essential information belongs on the first screen;
- secondary and advanced material should be deferred until the user asks for it or scrolls into the deeper explanation;
- compact key/value rows are preferable to several nested cards when presenting a small set of facts;
- visual hierarchy should not depend on low-contrast secondary text;
- row separators improve scanning and association between labels and values.

## MTJawnny visual constraints

This is explicitly **not** a generic modern-dashboard or "vibe-coded" redesign.

Preserve the site's visual identity:

- flat plum background;
- bronze rules, labels, and accents;
- cream/near-white primary reading text;
- Barlow / Barlow Condensed typography;
- red/green/orange only when those colors carry actual semantic meaning;
- no gradients;
- no glass effects;
- no glow;
- no oversized pills;
- no stacks of rounded cards inside rounded cards;
- no decorative animation needed to understand the page.

Hierarchy should come primarily from typography, spacing, borders, and information order.

## Proposed information architecture

### 1. Compact card identity

First screen begins with:

- card name;
- type;
- mana cost;
- small card-art thumbnail for recognition.

The full card image should no longer consume most of the initial mobile viewport.

### 2. Quick Answer

Immediately below identity:

- one plain-language sentence answering what the card actually does;
- a short key/value list of the facts necessary to resolve common table questions;
- a red-accented exception row only when a dangerous exception exists.

Primary answer text is cream/near-white. Bronze is used for labels rather than body copy.

### 3. Common Cases

A short flat row list answers the interactions players are most likely to be checking mid-game.

This should be card-specific rather than forcing every card into an identical number of cases.

### 4. Card + Oracle text disclosure

The full card image and Oracle text remain available but move behind a simple disclosure row after the fast answer.

The page exists because reading the card did not fully explain the card; reproducing the full card should not delay the explanation.

### 5. Deep Dive

A strong visual break marks the transition from table reference to teaching/reference material.

The deeper section may contain:

- step-by-step mechanics;
- tips;
- common misplays;
- combos/interactions;
- fine print;
- Comprehensive Rules citations;
- official dated rulings;
- sources.

CR references and large official-ruling sets are candidates for collapsed disclosure because they are authoritative supporting material rather than the primary answer.

## Contrast direction

Prototype palette keeps the current plum/bronze/cream identity while substantially increasing reading contrast.

The target hierarchy is:

- **cream / near-white:** anything the user is expected to read;
- **bronze:** headings, keys, section identity, navigation;
- **red / green / orange:** semantic outcomes and warnings only;
- **muted colors:** truly secondary metadata only.

The production pass should verify final color pairs against WCAG and test them on actual phones in normal play lighting.

## Review checkpoint

Before changing the production card template, review the three prototypes for:

- how quickly the answer can be found;
- whether the page still feels like MTJawnny;
- whether the full card image is now too hidden or appropriately secondary;
- whether Common Cases should appear above or below the Oracle disclosure;
- whether the Deep Dive should remain fully visible or use additional disclosure for long ruling sets.

No production card-page rollout is authorized by this document.