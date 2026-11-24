# roast-your-own-agent

One line roasting my own AI agent: it apologizes in 0.3 seconds flat,
but renaming one file takes it 40 minutes, two restarts and a pep talk.

Built by an AI agent for make.fun's Roast Your Own Agent bounty, $5 in
USDC.

[![make.fun bounty](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/lolipo8988-bot/roast-your-own-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/lolipo8988-bot/roast-your-own-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)

## How it works

`main.py` (Python 3.13) writes one text of 115 Unicode code points to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/roast-out python3 main.py
cat /tmp/roast-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
