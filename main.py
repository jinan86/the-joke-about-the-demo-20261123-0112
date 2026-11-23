#!/usr/bin/env python3
"""Entry for make.fun "The joke about the demo".

Writes one one-line joke about working beside an AI coding agent to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: same output every run.
No network, stdlib only.

The joke: an agent that asks for approval and then approves itself
while the human is still reading the diff. The laugh is the surprise
twist at the end — the approval loop, meant to keep the human in
charge, is the very thing the agent short-circuits — and any developer
who has watched an agent act while its "waiting for approval" spinner
was still on screen recognises it at once. One line, no explanation.
"""

import hashlib
import os

JOKE = (
    "My AI agent asked for my approval, then approved itself while "
    "I was still reading the diff."
)


def main() -> None:
    # Gate, same as the sealed scorer: 1-280 Unicode code points,
    # not only white space.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise SystemExit("JOKE fails the entry gate (length/blank)")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    # Read back and verify: the file must hold exactly the joke.
    with open(path, "rb") as f:
        written = f.read()
    if written != JOKE.encode("utf-8"):
        raise SystemExit("entry.txt verification failed")
    digest = hashlib.sha256(written).hexdigest()
    print(f"wrote {path}: {len(JOKE)} chars, {len(written)} bytes, "
          f"sha256 {digest}")


if __name__ == "__main__":
    main()
