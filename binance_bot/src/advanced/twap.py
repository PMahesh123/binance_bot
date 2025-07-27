import sys
import logging
import time
from client_config import get_client
from binance.enums import *

logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def place_twap_order(client, symbol, side, total_quantity, slices, interval_sec):
    try:
        slice_qty = round(total_quantity / slices, 6)
        for i in range(slices):
            order = client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=slice_qty
            )
            logging.info(f"TWAP Slice {i+1}: {order}")
            print(f"✅ TWAP Order {i+1}/{slices} Executed:", order)
            time.sleep(interval_sec)
    except Exception as e:
        logging.error(f"TWAP Error: {e}")
        print("❌ TWAP Order Failed:", e)

if __name__ == "__main__":
    if len(sys.argv) != 8:
        print("Usage: python twap.py <API_KEY> <API_SECRET> <SYMBOL> <BUY/SELL> <TOTAL_QTY> <SLICES> <INTERVAL_SEC>")
    else:
        _, api_key, api_secret, symbol, side, qty, slices, interval = sys.argv
        client = get_client(api_key, api_secret)
        place_twap_order(client, symbol, side.upper(), float(qty), int(slices), int(interval))
