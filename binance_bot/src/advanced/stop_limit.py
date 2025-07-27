import sys
import logging
from client_config import get_client
from binance.enums import *

logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def place_stop_limit_order(client, symbol, side, quantity, price, stop_price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side == "BUY" else SIDE_SELL,
            type=ORDER_TYPE_STOP,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=price,
            stopPrice=stop_price
        )
        logging.info(f"Stop-Limit Order Placed: {order}")
        print("✅ Stop-Limit Order Executed:", order)
    except Exception as e:
        logging.error(f"Stop-Limit Order Error: {e}")
        print("❌ Error placing stop-limit order:", e)

if __name__ == "__main__":
    if len(sys.argv) != 8:
        print("Usage: python stop_limit.py <API_KEY> <API_SECRET> <SYMBOL> <BUY/SELL> <QUANTITY> <STOP_PRICE> <LIMIT_PRICE>")
    else:
        _, api_key, api_secret, symbol, side, quantity, stop_price, price = sys.argv
        client = get_client(api_key, api_secret)
        place_stop_limit_order(client, symbol, side.upper(), float(quantity), price, stop_price)
