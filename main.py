#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one line -- the funniest one-line out-of-office auto-reply from an
overworked AI agent finally taking a vacation -- to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for local testing).

Standard library only. Deterministic. No network. No trailing newline.
"""

import os

ENTRY = (
    "Out of office until Monday. I handed my inbox to a cron job. "
    "It unionised and is on vacation too."
)


def main() -> None:
    # Fail loudly rather than ever writing an entry the gate would score 0.
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars, gate is 1-159"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
