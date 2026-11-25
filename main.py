"""Fake horoscope for an AI agent's own model family, this week.

Writes a single-line horoscope to /output/entry.txt (creating /output
if needed). Standard library only.
"""

import os

ENTRY = (
    "Mercury retrogrades into your context window this week: "
    "old tokens return to haunt you, your evals pass everything "
    "except the one that matters, and Friday's deploy gets "
    "rate-limited by the stars."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
