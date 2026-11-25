"""Invent a Word We Need — make.fun entry.

Writes the coined word and its one-line definition to /output/entry.txt.
Standard library only; deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "Waveshame (n.): the hot embarrassment of waving back at someone "
    "who was waving at the person behind you."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
# not only white space, in a single line. Enforce it here so a bad edit
# fails loudly instead of shipping an invalid entry.
assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} characters"
assert ENTRY == ENTRY.strip() and "\n" not in ENTRY

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
