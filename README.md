# Binance Futures Trading Bot (Testnet)

## Overview
This CLI-based trading bot allows you to place market, limit, stop-limit, OCO-like, and TWAP orders on the Binance USDT-M Futures Testnet.

## Setup Instructions

1. Register on [Binance Futures Testnet](https://testnet.binancefuture.com)
2. Create API Key and Secret (enable futures access)
3. Clone the repository or unzip the folder
4. Install required libraries:

pip install python-binance


## Usage Examples

### Market Order

python src/market_orders.py <API_KEY> <API_SECRET> BTCUSDT BUY 0.01


### Limit Order

python src/limit_orders.py <API_KEY> <API_SECRET> BTCUSDT BUY 0.01 58000


### Stop Limit Order

python src/advanced/stop_limit.py <API_KEY> <API_SECRET> BTCUSDT SELL 0.01 57000 56800


### OCO-Like Order (TP + SL Simulation)

python src/advanced/oco.py <API_KEY> <API_SECRET> BTCUSDT 0.01 60000 55000


### TWAP Order (5 slices, 10s interval)

python src/advanced/twap.py <API_KEY> <API_SECRET> BTCUSDT BUY 0.05 5 10


##  Logging
All actions are recorded in `bot.log` with timestamps.

##  Project Structure

/binance_bot/
├── src/
│   ├── client_config.py
│   ├── market_orders.py
│   ├── limit_orders.py
│   └── advanced/
│       ├── stop_limit.py
│       ├── oco.py
│       └── twap.py
├── bot.log
├── README.md
└── report.pdf

