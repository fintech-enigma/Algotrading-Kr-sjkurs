import pandas_ta as ta
import alpaca_trade_api as tradeapi
import pandas as pd
import os
from dotenv import load_dotenv
from alpaca_trade_api.rest import TimeFrame
import datetime as dt
import pytz

load_dotenv()

API_KEY = os.getenv('API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
END_POINT = os.getenv('END_POINT')

# Create the Alpaca API client
api = tradeapi.REST(API_KEY, SECRET_KEY, END_POINT, api_version='v2')

GMT = pytz.timezone('GMT')

time_now = dt.datetime.now(tz=GMT)
time_15_min_ago = time_now - dt.timedelta(minutes=15)
time_1_hr_ago = time_now - dt.timedelta(hours=20)

bars = api.get_bars('AAPL', TimeFrame.Minute, 
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


data['ema_180'] = ta.ema(data['close'], length=180)
data['rsi'] = ta.rsi(data['close'], length=14)
data['sma_50'] = ta.sma(data['close'], length=50)

print(data)
