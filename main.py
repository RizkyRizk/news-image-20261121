#!/usr/bin/env python3
"""Deliver the competition entry image.

Copies the finished entry.png sitting beside this file in the
repository root, byte for byte, to /output/entry.png.

Standard library only, no arguments, no network.
"""

import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
DEST = Path("/output/entry.png")


def main() -> int:
    if not SOURCE.is_file():
        print(f"error: source image not found: {SOURCE}", file=sys.stderr)
        return 1

    try:
        DEST.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(SOURCE, DEST)
    except OSError as exc:
        print(f"error: failed to write {DEST}: {exc}", file=sys.stderr)
        return 1

    print(f"entry image written: {DEST} ({DEST.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
