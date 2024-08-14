import os
import time
import numpy as np
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi

# Load environment variables from .env file
load_dotenv()

# Get Alpaca API credentials
API_KEY = os.getenv('API_KEY')
SECRET_KEY = os.getenv('APCA_API_SECRET_KEY')
END_POINT = os.getenv('END_POINT')

# Create the Alpaca API client
api = tradeapi.REST(API_KEY, SECRET_KEY, END_POINT, api_version='v2')

# Define the stock symbol and EMA period
symbol = 'AAPL'
ema_period = 180
qty = 1  # Number of shares to trade

# Function to calculate the 180 EMA
def calculate_ema(prices, period):
    return prices.ewm(span=period, adjust=False).mean()

# Function to get historical data and calculate 180 EMA
def get_historical_data_and_ema(symbol, ema_period):
    # Get historical data (e.g., past 200 days)
    barset = api.get_barset(symbol, 'day', limit=200)
    bars = barset[symbol]

    # Convert to DataFrame
    data = pd.DataFrame({
        'time': [bar.t for bar in bars],
        'close': [bar.c for bar in bars]
    })
    data.set_index('time', inplace=True)

    # Calculate the 180 EMA
    data['180_ema'] = calculate_ema(data['close'], ema_period)

    return data

# Function to check the current price against 180 EMA and make trades
def trade_logic(symbol, qty, ema_period):
    data = get_historical_data_and_ema(symbol, ema_period)
    current_price = api.get_last_trade(symbol).price
    current_ema = data['180_ema'].iloc[-1]

    print(f"Current price: {current_price}")
    print(f"180 EMA: {current_ema}")

    # Check if price is above EMA (buy condition)
    if current_price > current_ema:
        print("Price is above the 180 EMA, buying...")
        try:
            api.submit_order(
                symbol=symbol,
                qty=qty,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
            print(f"Bought {qty} share(s) of {symbol}.")
        except Exception as e:
            print(f"Error placing buy order: {e}")

    # Check if price is below EMA (sell condition)
    elif current_price < current_ema:
        print("Price is below the 180 EMA, selling...")
        try:
            api.submit_order(
                symbol=symbol,
                qty=qty,
                side='sell',
                type='market',
                time_in_force='gtc'
            )
            print(f"Sold {qty} share(s) of {symbol}.")
        except Exception as e:
            print(f"Error placing sell order: {e}")

# Main loop to continuously check and trade based on conditions
def main():
    while True:
        trade_logic(symbol, qty, ema_period)
        time.sleep(60)  # Wait 1 minute before checking again

if __name__ == "__main__":
    main()
