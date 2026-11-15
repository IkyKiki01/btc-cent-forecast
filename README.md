# BTC Cent Forecast
Python 3.13 standard-library entry forecasting Bitcoin 240 minutes ahead.
Starts at the last close and pulls 20% toward the median of the last 60 closes.
RMS minute-return volatility over 60 minutes versus 24 hours damps the pull; adjustment is capped at 0.35%.
Run `python3 main.py`; MAKEFUN_INPUT_DIR and MAKEFUN_OUTPUT_DIR default to /input and /output, with sorted *.in cases producing matching JSON *.out files.
Deterministic and offline; prices are clamped inside (0, 10000000) and rounded to five decimals; MIT © Muhammad Rizky Fadillah.
