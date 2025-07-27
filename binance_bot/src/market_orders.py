import sys
import logging
from client_config import get_client

logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def place_market_order(client, symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        logging.info(f"Market Order Placed: {order}")
        print(f"✅ Market Order Executed: {order}")
    except Exception as e:
        logging.error(f"Market Order Error: {e}")
        print("❌ Error placing market order:", e)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python market_orders.py <API_KEY> <API_SECRET> <SYMBOL> <BUY/SELL> <QUANTITY>")
    else:
        _, api_key, api_secret, symbol, side, quantity = sys.argv
        client = get_client(api_key, api_secret)
        place_market_order(client, symbol, side.upper(), float(quantity))
