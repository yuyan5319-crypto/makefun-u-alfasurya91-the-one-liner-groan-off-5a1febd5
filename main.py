#!/usr/bin/env python3
"""The One-Liner Groan-Off entry: write one original groan-worthy one-liner.

Stdlib only. Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output).
"""

import os

JOKE = (
    "I taught my toaster to tell jokes \u2014 now every morning it pops up "
    "with a fresh one, and I can't stop buttering it up."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"wrote {len(JOKE)} chars to {path}")


if __name__ == "__main__":
    main()
