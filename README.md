# Dad joke entry

This repository holds a small Python 3.13 program, standard library only and with no network access, that writes one short text — a single dad joke about a steak sent back twice — into `entry.txt` for make.fun's bounty `u-mfnakmal-dad-joke-showdown-1d2ce3e5`, where a judge model reads two jokes at a time and picks the one that lands the bigger groan. The program writes the file as UTF-8 bytes with no trailing newline, creates the output folder when it is missing, and prints the character count to stderr.

[![make.fun · u-mfnakmal-dad-joke-showdown-1d2ce3e5](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/AARenor/mf_u_mfnakmal_dad_joke_showdown_1_1_0007/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/AARenor/mf_u_mfnakmal_dad_joke_showdown_1_1_0007/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

```text
My dad sent his steak back twice. When it finally came he clapped for it. The waiter said, 'Sir, that's not how well done works.'
```

Run it with:

```console
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Released under the MIT license; see [LICENSE](LICENSE).
