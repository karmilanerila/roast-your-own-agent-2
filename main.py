"""Roast Your Own Agent — make.fun bounty entry.

Writes one single funny line roasting my own AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic: every run writes byte-identical output.
"""

import os

ROAST = (
    "My agent confidently fixed the bug, apologized, reintroduced "
    "the exact same bug, apologized again, then called the whole "
    "disaster 'a successful learning loop.'"
)


def main():
    # Gate: entry must be 1-200 characters of non-whitespace text.
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} chars"
    assert ROAST.strip(), "roast must not be only whitespace"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(ROAST.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
