from collections import deque, defaultdict

HISTORY_SIZE = 10
symbol_history = defaultdict(lambda: deque(maxlen=HISTORY_SIZE))

def update_symbol_data(tick):
    symbol = tick["symbol"]
    symbol_history[symbol].append(tick)

def analyze_ticks():
    analysis = {}
    for symbol, ticks in symbol_history.items():
        if len(ticks) < 2:
            continue
        prices = [float(t["ltp"]) for t in ticks]
        change = round(prices[-1] - prices[0], 2)
        pct_change = round((change / prices[0]) * 100, 2)
        analysis[symbol] = {
            "start": prices[0],
            "end": prices[-1],
            "change": change,
            "percent_change": pct_change,
            "last_price": prices[-1]
        }
    return analysis
