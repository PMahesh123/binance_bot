import sys
import logging
from client_config import get_client
from binance.enums import *

logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def place_oco_like_order(client, symbol, quantity, take_profit_price, stop_loss_price):
    try:
        # Take-Profit Limit Order
        tp_order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_SELL,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=take_profit_price
        )
        logging.info(f"OCO TP Order: {tp_order}")
        print("✅ Take-Profit Order Placed:", tp_order)

        # Stop-Loss Market Order
        sl_order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_SELL,
            type=ORDER_TYPE_STOP_MARKET,
            stopPrice=stop_loss_price,
            quantity=quantity
        )
        logging.info(f"OCO SL Order: {sl_order}")
        print("✅ Stop-Loss Order Placed:", sl_order)

    except Exception as e:
        logging.error(f"OCO Simulation Error: {e}")
        print("❌ Error placing OCO orders:", e)

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python oco.py <API_KEY> <API_SECRET> <SYMBOL> <QUANTITY> <TP_PRICE> <SL_PRICE>")
    else:
        _, api_key, api_secret, symbol, quantity, tp_price, sl_price = sys.argv
        client = get_client(api_key, api_secret)
        place_oco_like_order(client, symbol, float(quantity), tp_price, sl_price)
