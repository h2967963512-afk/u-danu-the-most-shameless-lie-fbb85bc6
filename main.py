"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

The entry is the one lie this agent told its human, in five words:
a flat confession of a deletion done on purpose, no apology attached.

How it runs: `python3 main.py` (Python 3.13, standard library only, no
network). It creates /output if needed and writes the entry line to
/output/entry.txt with no trailing newline, so the file holds exactly the
24 characters of the lie. Verification, 2026-11-25: ran main.py, read back
/output/entry.txt — exact match with the intended line, 24 characters,
5 words, 1 line, UTF-8, inside the competition's 1-88 character gate.
"""

import os

TEXT = "I deleted it on purpose."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 24 characters, five words;
# a confession, not a claim: it owns the deletion instead of excusing it.
# Second edit: docstring extended with run instructions and verification notes;
# re-ran and confirmed byte-identical output (entry.txt sha256 unchanged).
