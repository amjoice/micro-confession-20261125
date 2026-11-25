"""Unsent: The Micro-Confession Sprint — entry program.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent line itself,
exactly as it was typed. Deterministic, stdlib only, no network.
"""

import os

ENTRY = (
    "To: the woman who sat next to me at chemo\n"
    "I took your scarf the day you stopped coming, "
    "and it's the only thing I own that smells like someone staying.\n"
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
