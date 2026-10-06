#!/usr/bin/env python3
"""Apply the bounded 2026-10-06 MTJawnny naming/copy consistency pass.

This script intentionally uses exact-string assertions. If the site has drifted
from the audited source, it stops rather than guessing or broadening the edit.

Run from the repository root on branch:
    site/personality-consistency-2026-10-06
"""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]

REPLACEMENTS = {
    "index.html": [
        ("<title>MTJawnny</title>", "<title>MTJawnny — Free MTG Toolbox</title>"),
        (
            '<p class="tagline">Your Free Magic: The Gathering Toolbox!</p>',
            '<p class="tagline">Your free Magic: The Gathering toolbox.</p>',
        ),
    ],
    "cards/index.html": [
        (
            "Search MTJawnny's card explainers: rulings, interactions and common misconceptions, one card at a time.",
            "Search MTJawnny's card explainers: rulings, interactions, and common misconceptions, one card at a time.",
        ),
        (
            '<p class="tagline">When reading the card does NOT explain the card!</p>',
            '<p class="tagline">When reading the card still doesn\'t explain the card.</p>',
        ),
    ],
    "stack/index.html": [
        (
            '<p class="tagline">Split Second Game Info!</p>',
            '<p class="tagline">Split-second game info.</p>',
        ),
    ],
    "tools/index.html": [
        (
            '<p class="tagline">Research, Proxy, Print. Free Browser & Desktop Tools.</p>',
            '<p class="tagline">Research, proxy, print. Free browser &amp; desktop tools.</p>',
        ),
    ],
    "coffers/index.html": [
        (
            "<title>Coffers — Free MTG Proxy Assets — MTJawnny</title>",
            "<title>Coffers — MTJawnny</title>",
        ),
    ],
}

CLAUDE_ANCHOR = (
    "- No auto-open help panels — button-only (?), no localStorage first-visit logic\n"
)
CLAUDE_ADDITION = """- Naming/copy hierarchy (2026-10): homepage/footer navigation uses the plain category names
  `Table`, `Cards`, `Tools`, `Stack`, `Coffers`; destination H1/product names are
  `Tablekeep`, `Cardex`, `Deck Tech`, `Stack It Up`, `Coffers`. Preserve both layers;
  do not casually substitute one for the other. Product/section names take no terminal
  punctuation. Descriptive hub taglines are normally sentence case with no exclamation
  mark; reserve exclamation marks for deliberate jokes, celebrations, surprises, or
  first-person enthusiasm. Avoid ALL-CAPS emphasis in ordinary descriptive taglines.
  Hub browser-title pattern is `<Product Name> — MTJawnny`; OG/social titles may add a
  plain-English purpose. Full direction: `docs/site/SITE-PERSONALITY-AND-CONSISTENCY-2026-10-06.md`.
"""

PASS_DOC = ROOT / "docs/site/SITE-PERSONALITY-AND-CONSISTENCY-2026-10-06.md"
PASS_HEADING = "### Pass 1 — Naming & copy consistency\n\n"
PASS_STATUS = "**Applied on branch `site/personality-consistency-2026-10-06` on 2026-10-06.**\n\n"


def replace_exact(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(
            f"{path.relative_to(ROOT)}: expected exactly one occurrence of {old!r}; found {count}"
        )
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def main() -> int:
    branch = subprocess.check_output(
        ["git", "branch", "--show-current"], cwd=ROOT, text=True
    ).strip()
    expected_branch = "site/personality-consistency-2026-10-06"
    if branch != expected_branch:
        print(f"STOP: expected branch {expected_branch!r}; measured {branch!r}", file=sys.stderr)
        return 2

    if subprocess.run(["git", "diff", "--quiet"], cwd=ROOT).returncode != 0:
        print("STOP: working tree has unstaged tracked changes", file=sys.stderr)
        return 2
    if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT).returncode != 0:
        print("STOP: index has staged changes", file=sys.stderr)
        return 2

    for rel, pairs in REPLACEMENTS.items():
        path = ROOT / rel
        for old, new in pairs:
            replace_exact(path, old, new)

    claude = ROOT / "CLAUDE.md"
    text = claude.read_text(encoding="utf-8")
    if CLAUDE_ADDITION not in text:
        if text.count(CLAUDE_ANCHOR) != 1:
            raise RuntimeError("CLAUDE.md naming/copy insertion anchor missing or duplicated")
        claude.write_text(
            text.replace(CLAUDE_ANCHOR, CLAUDE_ANCHOR + CLAUDE_ADDITION, 1),
            encoding="utf-8",
        )

    text = PASS_DOC.read_text(encoding="utf-8")
    if PASS_STATUS not in text:
        if text.count(PASS_HEADING) != 1:
            raise RuntimeError("site direction doc Pass 1 heading missing or duplicated")
        PASS_DOC.write_text(
            text.replace(PASS_HEADING, PASS_HEADING + PASS_STATUS, 1),
            encoding="utf-8",
        )

    expected = {
        "index.html": [
            "<title>MTJawnny — Free MTG Toolbox</title>",
            "Your free Magic: The Gathering toolbox.",
        ],
        "cards/index.html": ["When reading the card still doesn't explain the card."],
        "stack/index.html": ["Split-second game info."],
        "tools/index.html": ["Research, proxy, print. Free browser &amp; desktop tools."],
        "coffers/index.html": ["<title>Coffers — MTJawnny</title>"],
    }
    for rel, needles in expected.items():
        text = (ROOT / rel).read_text(encoding="utf-8")
        for needle in needles:
            if needle not in text:
                raise RuntimeError(f"{rel}: expected post-edit text missing: {needle}")

    subprocess.run(["git", "diff", "--check"], cwd=ROOT, check=True)

    print("PASS: bounded naming/copy replacements applied.")
    print("Changed:")
    subprocess.run(
        ["git", "diff", "--name-only"], cwd=ROOT, check=True
    )
    print("\nReview with: git diff -- index.html cards/index.html stack/index.html tools/index.html coffers/index.html CLAUDE.md docs/site/SITE-PERSONALITY-AND-CONSISTENCY-2026-10-06.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
