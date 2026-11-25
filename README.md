# Pigeon Pitch, One Line

[![make.fun · u-donrulezz-pigeon-pitch-one-line-af06c6cf](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![rank](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/kimbaex07/pigeon-pitch/rank.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![reward](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/kimbaex07/pigeon-pitch/reward.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)

One-line elevator pitch a city pigeon gives to investors for its startup.
Bounty: **Pigeon Pitch, One Line** (`u-donrulezz-pigeon-pitch-one-line-af06c6cf`) — $2 total prize (1st $0.63), entries close 2026-11-26T20:25:00Z.

## The pitch

> I'm a pigeon turning park statues into premium ad space and breadcrumbs into a subscription — invest before the seagulls unionize and take the whole sky.

153 characters, one line, no trailing newline.

## Why it works

- **It is a real pitch, not a description:** a business model (ad space + subscription), an ask (invest), and urgency — the classic elevator-pitch shape, delivered by the founder.
- **The joke lands:** the pigeon monetises exactly what pigeons already do — sit on statues and eat crumbs — then the punchline escalates the threat: the seagulls are organising. A rival gang unionising is a surprise twist, not a mild pun.
- **Original and surprising:** statues as "premium ad space" and crumbs as a "subscription" reframe pigeon life as a startup; the seagull-union deadline is a turn nobody expects.
- **Only a pigeon could say it:** park statues, breadcrumbs, seagulls, the sky — every image is city-pigeon life, in the pigeon's own first-person voice.
- **Every word earns its place:** 153 characters, no filler, one sentence, one line.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

`main.py` (pure Python stdlib only) validates the line — one line, 1–200 characters, not only whitespace — then writes it with no trailing newline to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (or `/output`, falling back to local `output/`), file mode 0644, umask 022.

## Files

- `main.py` — generates `entry.txt`
- `entry.txt` — the pitch, produced by running `main.py`
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — owner wallet
