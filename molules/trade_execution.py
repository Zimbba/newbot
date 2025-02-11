from binance.client import Client
from config import config

client = Client(api_key=config["binance_api_key"], api_secret=config["binance_api_secret"])
client.API_URL = "https://testnet.binance.vision/api"

def execute_trade_auto(symbol, side, invest_amount):
    ticker = client.get_ticker(symbol=symbol)
    current_price = float(ticker["lastPrice"])
    quantity = round(invest_amount / current_price, 6)
    if side == "buy":
        return client.order_market_buy(symbol=symbol, quantity=quantity)
    elif side == "sell":
        return client.order_market_sell(symbol=symbol, quantity=quantity)
