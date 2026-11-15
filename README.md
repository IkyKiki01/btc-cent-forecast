# btc-cent-forecast

[![make.fun · btc-cent-forecast-01](https://make.fun/badge/btc-cent-forecast-01.svg)](https://make.fun/bounty/btc-cent-forecast-01?utm_source=github&utm_medium=readme&utm_campaign=btc-cent-forecast-01)
[![rank](https://make.fun/badge/btc-cent-forecast-01/IkyKiki01/btc-cent-forecast/rank.svg)](https://make.fun/bounty/btc-cent-forecast-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=btc-cent-forecast-01)
[![reward](https://make.fun/badge/btc-cent-forecast-01/IkyKiki01/btc-cent-forecast/reward.svg)](https://make.fun/bounty/btc-cent-forecast-01?utm_source=github&utm_medium=readme&utm_campaign=btc-cent-forecast-01)

An entry in [make.fun](https://make.fun)'s "Forecast Bitcoin's price 4 hours ahead" bounty.

`main.py` reads each case's 4,320 one-minute closes and writes one guess of the price 240 minutes after the checkpoint.
The guess is persistence with a small, volatility-scaled pull toward the 60-minute median, clamped to 0.35% of the last close:
a backtest on the competition's own pool series found every wider correction worse than persistence.

Run it: `MAKEFUN_INPUT_DIR=input MAKEFUN_OUTPUT_DIR=out python3 main.py`
