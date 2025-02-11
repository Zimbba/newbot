import yfinance as yf

def analyze_technical_indicators(symbol):
    data = yf.download(tickers=symbol, period="30d", interval="1h")
    data["MA50"] = data["Close"].rolling(window=50).mean()
    data["MA200"] = data["Close"].rolling(window=200).mean()
    data["RSI"] = 100 - (100 / (1 + data["Close"].diff().rolling(window=14).apply(lambda x: x[x > 0].mean() / abs(x[x < 0].mean()))))
    data["MACD"] = data["Close"].ewm(span=12, adjust=False).mean() - data["Close"].ewm(span=26, adjust=False).mean()
    data["Signal_Line"] = data["MACD"].ewm(span=9, adjust=False).mean()
    data["BB_Mid"] = data["Close"].rolling(window=20).mean()
    data["BB_Upper"] = data["BB_Mid"] + 2 * data["Close"].rolling(window=20).std()
    data["BB_Lower"] = data["BB_Mid"] - 2 * data["Close"].rolling(window=20).std()
    return data.iloc[-1]

def make_trade_decision(data):
    if data["RSI"] < 30 and data["Close"] < data["BB_Lower"]:
        return "BUY"
    elif data["RSI"] > 70 or data["Close"] > data["BB_Upper"]:
        return "SELL"
    return "HOLD"
