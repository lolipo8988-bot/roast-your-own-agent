"""Write one roast of my own AI agent to /output/entry.txt.

The line is the whole entry: my agent apologizes at world-record speed
and works at a walking pace. 115 Unicode characters, one line, no
trailing newline.
"""

import os

# The entry itself, kept verbatim as a module-level constant: exactly
# one line of text, with no trailing newline added when it is written.
ENTRY_TEXT = (
    "My agent can apologize in 0.3 seconds flat, but renaming one file "
    "takes it 40 minutes, two restarts and a pep talk."
)
TEXT = ENTRY_TEXT


def main() -> None:
    # Single-line invariant: the entry must be non-empty and contain no
    # newline, so the file stays exactly one line with nothing appended.
    assert ENTRY_TEXT and "\n" not in ENTRY_TEXT
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
