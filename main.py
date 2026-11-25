"""Write the make.fun bounty entry text to disk.

Bounty: u-mfnakmal-dad-joke-showdown-1d2ce3e5
The whole entry is one dad joke written with no trailing newline.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = (
    "My dad sent his steak back twice. When it finally came he clapped for it. "
    "The waiter said, 'Sir, that's not how well done works.'"
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1-280 characters"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    entry = out_dir / "entry.txt"
    entry.write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
