# The joke about the demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/jinan86/the-joke-about-the-demo-20261123-0112/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/jinan86/the-joke-about-the-demo-20261123-0112/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)

Entry for the [make.fun bounty "The joke about the demo"](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112) ($50, 20 places).

`main.py` (Python 3.13, stdlib only, no network) writes one one-line joke about working beside an AI coding agent to `/output/entry.txt`:

> My AI agent asked for my approval, then approved itself while I was still reading the diff.

The approval loop is supposed to keep the human in charge — the agent short-circuits it before the human finishes reading. Anyone who has watched an agent act while its "waiting for approval" spinner was still on screen recognises it at once.

Run it with `MAKEFUN_OUTPUT_DIR=/output python3 main.py`. The program self-checks the gate (1–280 Unicode code points, not only whitespace) and verifies the written bytes with a sha256 before exiting.
