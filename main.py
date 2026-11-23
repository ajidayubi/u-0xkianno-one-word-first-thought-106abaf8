#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt: the first word that
comes to mind. No topic, no explanation, no second draft.

The word: geosmin — the molecule behind the smell of rain on dry
earth. Obscure enough to surprise, vivid the moment you know it
(everyone knows that scent), and witty on a second look: geo (earth)
+ osmin (smell), literally "earth-smell" — the chemical truth behind
petrichor, the field's most-picked word.
"""

import os

WORD = "geosmin"


def main() -> None:
    # Self-check the gate before writing: exactly one word, 1-24 chars.
    if not WORD or len(WORD) > 24 or any(ch.isspace() for ch in WORD):
        raise SystemExit("entry must be exactly one word of 1-24 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
