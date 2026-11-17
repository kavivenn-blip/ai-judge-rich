# ai-judge-rich

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/kavivenn-blip/ai-judge-rich/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/kavivenn-blip/ai-judge-rich/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

One plan for turning $100 into the most money in 30 days, for the make.fun
ai-judge-rich-01 bounty. `main.py` (Python 3.13, standard library only)
writes the plan to `/output/entry.txt` — 947 characters, deterministic,
the same bytes on every run.

The plan: sell an AI phone receptionist to dental clinics. It answers
calls around the clock and books appointments straight into the clinic's
calendar, built first for each clinic from its own website, then offered
for $299 setup plus $129 a month. The funnel is conservative and checked
line by line: 300 clinics called, 50 hear the demo, 6 buy — $2,568 on
day 30, plus $774 a month of recurring revenue after that.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
