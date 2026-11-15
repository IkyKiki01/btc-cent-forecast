import json
import math
import os
from pathlib import Path
from statistics import median


def volatility(prices, minutes):
    window = prices[-(minutes + 1):]
    squared_returns = ((b / a - 1.0) ** 2
                       for a, b in zip(window, window[1:]))
    return math.sqrt(math.fsum(squared_returns) / (len(window) - 1))


def forecast(prices):
    base = prices[-1]
    recent = volatility(prices, 60)
    daily = volatility(prices, 1440)
    scale = min(1.0, daily / recent) if recent > 0.0 else 1.0
    pull = 0.2 * (median(prices[-60:]) - base) * scale
    limit = base * 0.0035
    adjustment = max(-limit, min(limit, pull))
    return round(max(0.00001, min(9999999.99999, base + adjustment)), 5)


def main():
    input_dir = Path(os.environ.get("MAKEFUN_INPUT_DIR", "/input"))
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    for path in sorted(input_dir.glob("*.in")):
        case = json.loads(path.read_text(encoding="utf-8"))
        result = {"forecasts": [{"case": path.stem,
                                 "price": forecast(case["markets"][0]["prices"])}]}
        (output_dir / (path.stem + ".out")).write_text(
            json.dumps(result, separators=(",", ":"), allow_nan=False) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
