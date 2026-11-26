#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message — one commit line.

Deterministic: two runs produce byte-identical entry.txt.
Uses only the Python 3.13 standard library, no network.
"""

import os
from pathlib import Path

LINE = "fix: after 47 rewrites at 4am, the bug is gone, the code is worse, and I have decided we will never speak of the function that caused this again"

def main() -> None:
    # Guard the bounty rules at runtime: one line, at most 200 chars, no em-dash,
    # no exclamation mark, no hidden line break of any kind, and real text,
    # not only whitespace. A carriage return would smuggle in a second line.
    if (
        len(LINE) > 200
        or "\n" in LINE
        or "\r" in LINE
        or "\u2014" in LINE
        or "!" in LINE
        or not LINE.strip()
    ):
        raise ValueError("entry line violates the bounty rules")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
