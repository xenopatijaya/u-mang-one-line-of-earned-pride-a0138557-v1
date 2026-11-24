#!/usr/bin/env python3
"""One Line of Earned Pride - make.fun entry.

Writes one original line of quiet, earned pride to
/output/entry.txt (override the directory with MAKEFUN_OUTPUT_DIR).
The line is a single sentence of 1 to 240 characters: a concrete scene,
a real person, and a long effort finally landing.
"""

import os
from pathlib import Path

LINE = "After eleven years of night shifts, my father laid the first brick of our house himself, hands shaking, saying nothing, because some pride is too heavy to say out loud."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(f"pride line is {len(text)} chars, must be 1-240")
    if "\n" in text:
        raise SystemExit("pride line must be a single line")
    # Write exactly the line, no trailing newline, atomically: the gate
    # counts every character in entry.txt against the 240-char cap, and
    # a temp file + os.replace means an interrupted run can never leave
    # a truncated line behind.
    target = out_dir / "entry.txt"
    tmp = out_dir / "entry.txt.tmp"
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, target)
    print(text)


if __name__ == "__main__":
    main()
