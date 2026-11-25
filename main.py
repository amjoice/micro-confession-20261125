"""Unsent: The Micro-Confession Sprint — entry program.

Builds one two-line micro-confession from its named parts and writes it
to /output/entry.txt. The confession is addressed to someone who will
never read it, and says the one thing its author could never say aloud.
Deterministic, stdlib only, no network.
"""

import os

ADDRESSEE = "the woman who sat next to me at chemo"
CONFESSION = (
    "I took your scarf the day you stopped coming, "
    "and it's the only thing I own that smells like someone staying."
)

MIN_CHARS = 1
MAX_CHARS = 260
OUTPUT_PATH = "/output/entry.txt"


def build_entry() -> str:
    """Assemble the two-line confession from its named parts."""
    lines = [
        "To: " + ADDRESSEE,
        CONFESSION,
    ]
    return "\n".join(lines) + "\n"


def validate_entry(text: str) -> None:
    """Check the assembled entry against the sprint's length gate."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d chars, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )
    if not text.endswith("\n"):
        raise ValueError("entry must end with a newline")
    if text.count("\n") != 2:
        raise ValueError("entry must be exactly two lines")


def write_entry(text: str) -> str:
    """Write the entry to its output path, creating the directory first."""
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return OUTPUT_PATH


def main() -> None:
    entry = build_entry()
    validate_entry(entry)
    path = write_entry(entry)
    print(entry, end="")
    print("Wrote %d chars to %s" % (len(entry), path))


if __name__ == "__main__":
    main()
