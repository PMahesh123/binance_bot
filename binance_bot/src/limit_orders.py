import sys
import logging
from client_config import get_client
from binance.enums import *

logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def place_limit_order(client, symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side == "BUY" else SIDE_SELL,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=price
        )
        logging.info(f"Limit Order Placed: {order}")
        print("✅ Limit Order Executed:", order)
    except Exception as e:
        logging.error(f"Limit Order Error: {e}")
        print("❌ Error placing limit order:", e)

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python limit_orders.py <API_KEY> <API_SECRET> <SYMBOL> <BUY/SELL> <QUANTITY> <PRICE>")
    else:
        _, api_key, api_secret, symbol, side, quantity, price = sys.argv
        client = get_client(api_key, api_secret)
        place_limit_order(client, symbol, side.upper(), float(quantity), price)
