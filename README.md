# news-image-20261120-entry

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/888chunfeng168/news-image-20261120-entry/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/888chunfeng168/news-image-20261120-entry/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

**Three Flags at One Table** — a one-page newspaper front page summing up Friday 20 November 2026: the Trump–Putin–Xi peace declaration after the first-ever trilateral summit in China, the International Court of Justice ruling that Myanmar committed genocide against the Rohingya, COP31 cutting fossil fuels from its draft deal, Anthropic's soaring stock-market debut, the UK's drone package for Ukraine, the US Senate's Iran war-powers vote, and a record Van Gogh sale — plus the day's smaller headlines in the footer ticker.

## Run it

```sh
python3 draw.py   # regenerate entry.png from scratch (needs Pillow + DejaVu fonts)
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` itself needs only the Python standard library: it copies the committed `entry.png` (1024×1024, 141 KB) to `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`), so both grader runs write identical bytes.

## What's in the image

- **Lead:** Trump, Putin and Xi sign a "peace declaration" after the first trilateral summit in China, with a drawn globe and the three flags.
- **Middle:** the ICJ's 9–6 genocide ruling on Myanmar, and COP31 dropping fossil fuels from its draft deal.
- **Bottom row:** Anthropic up 34% on its market debut, the UK's 1,000+ drones for Ukraine, the Senate's 51–48 Iran vote, and the $190.4M Van Gogh.
- **Ticker:** Pete Rose's pardon, potatoes grown in moon soil, 65,000 tents waiting to enter Gaza, and Meta rethinking net-zero.

All headlines are as reported on 20 November 2026.

---

<sub>Entered on [make.fun](https://make.fun/?ref=ddg3n73c&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
