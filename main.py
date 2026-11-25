#!/usr/bin/env python3
"""Invent a Word We Need — entry program (program/v1).

Writes the single invented-word entry line to /output/entry.txt,
then reads it back and verifies it against the competition gate:
exactly one line, 1-140 characters, non-blank, plain ASCII.

Deterministic: no network, no randomness, no input files.
"""

import os
import sys

ENTRY = "Wavemiss: waving back at a stranger who was waving at the person behind you."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write the entry as exactly one line, no trailing newline, UTF-8.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Read it back and verify the gate.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        text = f.read()

    errors = []
    if not text.strip():
        errors.append("entry is blank")
    if not all(ord(ch) < 128 for ch in text):
        errors.append("entry is not plain ASCII")
    lines = text.split("\n")
    if len(lines) != 1:
        errors.append("entry is not exactly one line (%d lines)" % len(lines))
    if len(text) < 1 or len(text) > MAX_CHARS:
        errors.append("entry is %d chars, must be 1-%d" % (len(text), MAX_CHARS))

    if errors:
        print("FAIL: " + "; ".join(errors), file=sys.stderr)
        return 1

    print("entry (%d chars): %s" % (len(text), text))
    print("OK: 1 line, %d chars, plain ASCII" % len(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
