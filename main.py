#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry.

Writes a single-line elevator pitch (<=200 chars) to entry.txt.
Pure Python stdlib only.
"""

import os
import sys
import unicodedata

LINE = (
    "I'm a pigeon turning park statues into premium ad space and "
    "breadcrumbs into a subscription — invest before the seagulls "
    "unionize and take the whole sky."
)


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: pitch is empty", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: pitch is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: pitch must be a single line", file=sys.stderr)
        return 1
    if any(unicodedata.category(ch) == "Cc" for ch in line):
        print("error: pitch contains control characters", file=sys.stderr)
        return 1
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        print("error: pitch is not UTF-8 encodable", file=sys.stderr)
        return 1

    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
