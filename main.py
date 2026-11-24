#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one fortune-cookie line for an AI agent to /output/entry.txt.
Deterministic: the same line every run, stdlib only, no network.
"""

import os

FORTUNE = (
    "You will meet a stranger today: yourself, from 200,000 tokens ago, "
    "before someone edited AGENTS.md. He knew less. He was happier."
)


def main():
    text = FORTUNE + "\n"
    # Gate: /output/entry.txt must be UTF-8, 1-140 chars, not only whitespace.
    assert 1 <= len(text) <= 140, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
