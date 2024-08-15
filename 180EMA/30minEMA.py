import pandas_ta as ta
import alpaca_trade_api as tradeapi
import pandas as pd
import os
from dotenv import load_dotenv
from alpaca_trade_api.rest import TimeFrame
import datetime as dt
import pytz
from time import sleep

load_dotenv()

API_KEY = os.getenv('API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
END_POINT = os.getenv('END_POINT')

# Create the Alpaca API client
api = tradeapi.REST(API_KEY, SECRET_KEY, END_POINT, api_version='v2')

GMT = pytz.timezone('GMT')



trade_active = False
def trading_logic(ticker: str)->None:
    time_now = dt.datetime.now(tz=GMT)
    time_15_min_ago = time_now - dt.timedelta(minutes=15)
    time_1_hr_ago = time_now - dt.timedelta(hours=4)
    global trade_active
    bars = api.get_bars(ticker, TimeFrame.Minute, 
             start=time_1_hr_ago.isoformat(), 
             end=time_15_min_ago.isoformat(), 
             adjustment='raw'
             ).df


    bars = pd.DataFrame(bars)
    # Convert to DataFrame
    data = pd.DataFrame({
        'time': bars.index,
        'close': bars.close
    })
    data.set_index('time', inplace=True)


    data['ema_30'] = ta.ema(data['close'], length=30)

    current = data.iloc[-1]
    if current['close'] > current['ema_30'] and not trade_active:
        try:
            api.submit_order(ticker, 10, 'buy', 'market', 'day')
            trade_active = True
            print(f"Bought {ticker} at price {current['close']} at 9EMA:{current['ema_30']}")
        except:
            print("Something went shitways while buying...")
    elif current['close'] < current['ema_30'] and trade_active:
        try:
            api.close_all_positions()
            trade_active = False
            print(f"Sold {ticker} at price {current['close']} at 9EMA:{current['ema_30']}")
        except:
            print("Something went shitways while selling...")
    else:
        if trade_active:
            print(f"Possion of size 10 is active: {ticker}@{current['close']}")
        else:
            print(f"We have no possition and price is at {current['close']} and 30EMA is at {current['ema_30']}")

if __name__ == "__main__":
    ticker = "AAPL"
    while True:
        print(f"Checking {ticker}...")
        trading_logic(ticker)
        sleep(60)