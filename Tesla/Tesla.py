import alpaca_trade_api as tradeapi
import numpy as np
import sounddevice as sd 
from time import sleep
import os
from dotenv import load_dotenv
load_dotenv()

END_POINT = os.getenv("END_POINT")

API_KEY = os.getenv("API_KEY")

SECRET_KEY = os.getenv("SECRET_KEY")

BOUGHT = False

class Bot:
    def __init__(self) -> None:
        self.bot = tradeapi.REST(API_KEY, SECRET_KEY, END_POINT, api_version="v2")

    def buy(self):
        try:
            self.bot.submit_order("TSLA", 100, "buy", "market", "day")
        except:
            print("Failed to buy")

    def sell(self):
        try:
            self.bot.close_position("TSLA", qty=100)
        except:
            print("No position")

bot = Bot()

duration = 20  # seconds

def audio_callback(indata, frames, time, status):
    global BOUGHT
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm >= 12 and BOUGHT == False:
        print("Buying TSLA....")
        bot.buy()
        sleep(2)
        BOUGHT = True
        return

    if volume_norm >= 12 and BOUGHT:
        print("Selling TSLA...")
        bot.sell()
        BOUGHT = False
        sleep(2)
        return


stream = sd.InputStream(callback=audio_callback)
with stream:
    print("Starting....")
    sd.sleep(duration * 1000)
