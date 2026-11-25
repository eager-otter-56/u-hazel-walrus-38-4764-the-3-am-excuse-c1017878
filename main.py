"""Entry for make.fun bounty u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.

Writes the wallet's 3 AM excuse to entry.txt in MAKEFUN_OUTPUT_DIR.
"""

import os
import stat

ENTRY = (
    "I typed my own PIN wrong 3 times at 3:02 AM, so I'm locked out "
    "until sunrise and your coins are safer from me than from anyone."
)


def main():
    # Gate: 1-200 characters, single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
