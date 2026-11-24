#!/usr/bin/env python3
"""Fortune in a Pot — make.fun bounty entry.

Writes one kind, funny fortune for a houseplant (<=120 characters)
to /output/entry.txt. Pure Python standard library, deterministic.
"""

import os
import stat
import sys

FORTUNE = (
    "This week a sunbeam will choose your favourite leaf, "
    "and your keeper will water you before you even think to ask."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    text = FORTUNE.strip()
    if not 1 <= len(text) <= 120:
        print(f"fortune is {len(text)} chars, must be 1-120", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text or "\r" in text:
        print("fortune must be a single clean line", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    try:
        os.chmod(OUTPUT_PATH, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    except OSError:
        pass
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
