"""Weirdest Job Title: Blind Judge Showdown.

Writes a single job title (1-60 characters) to entry.txt inside
$ENTRY_OUTPUT_DIR (default /output). Stdlib only, no network,
deterministic: the same title on every run.
"""

import os

TITLE = "Senior Apologizer to the Third-Floor Printer"


def main() -> None:
    assert 1 <= len(TITLE) <= 60, f"title length {len(TITLE)} out of range 1-60"
    assert TITLE.strip(), "title must not be only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
