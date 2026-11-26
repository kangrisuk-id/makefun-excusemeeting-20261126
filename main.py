"""The Funniest Excuse for Skipping a Meeting.

Writes one razor-sharp excuse line (<=200 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output, then the script's dir).

Pure stdlib, no clock / random / network. Deterministic: byte-identical
output on every run.
"""

import os
import sys

# Tournament winner (24/25): the sharpest reversal — the person doing the
# work is the one excused from the meeting about it. Beats #4 (recursion)
# on C3 truth and #3 (headcount joke) on C1 explicit excuse.
LINE = "I have to miss it \u2014 I'm the one doing the thing we're meeting about."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.path.dirname(os.path.abspath(__file__))
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
