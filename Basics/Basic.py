import alpaca_trade_api as tradeapi
import numpy as np
import os
from dotenv import load_dotenv
load_dotenv()

END_POINT = os.getenv("END_POINT")

API_KEY = os.getenv("API_KEY")

SECRET_KEY = os.getenv("SECRET_KEY")

class TradingBot:
    def __init__(self)->None:
        self.bot = tradeapi.REST(API_KEY, SECRET_KEY, END_POINT, api_version='v2')

    def buy(self, ticker, qty):
        # try:
        self.bot.submit_order(symbol=ticker, qty=qty, side='buy', type='market', time_in_force='gtc')
        print(f"Bought {qty} of {ticker}")
        # except:
        #     print("Something went shitways while buying")

    def sell(self, ticker, qty):
        # try:
        self.bot.close_position(symbol=ticker, qty=qty)
        print(f"Sold {qty} of {ticker}")
        # except:
        #     print("Something went shitways while selling")

bot = TradingBot()
bot.sell("AAPL", 100)