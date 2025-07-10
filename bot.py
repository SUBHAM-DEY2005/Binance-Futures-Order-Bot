from binance.client import Client
from binance.enums import *
import logging

# Setup logging
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        if testnet:
            self.client = Client(api_key, api_secret, testnet=True)
            self.client.API_URL = 'https://testnet.binancefuture.com/fapi'
        else:
            self.client = Client(api_key, api_secret)
        logging.info("Client initialized with testnet: %s", testnet)

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info("Market order placed: %s", order)
            return order
        except Exception as e:
            logging.error("Market order failed: %s", e)
            return {"error": str(e)}

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce=TIME_IN_FORCE_GTC
            )
            logging.info("Limit order placed: %s", order)
            return order
        except Exception as e:
            logging.error("Limit order failed: %s", e)
            return {"error": str(e)}

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                type=ORDER_TYPE_STOP_MARKET,
                quantity=quantity,
                stopPrice=stop_price,
                timeInForce=TIME_IN_FORCE_GTC
            )
            logging.info("Stop-Limit order placed: %s", order)
            return order
        except Exception as e:
            logging.error("Stop-Limit order failed: %s", e)
            return {"error": str(e)}
