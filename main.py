"""Entry point for the news-image-20261122 bounty.

Copies the pre-rendered front page, entry.png, into the output
directory named by MAKEFUN_OUTPUT_DIR (or /output when unset).

Standard library only, no network, deterministic: the same input
bytes always produce the same output bytes.
"""

import os
import shutil
import sys


def main() -> int:
    """Copy entry.png into the output directory and report success."""
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
