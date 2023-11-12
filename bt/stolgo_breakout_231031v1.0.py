
import pandas as pd
import numpy as np
import yfinance as yf
from backtesting import Backtest, Strategy
#from backtesting.lib import TrailingStrategy
import pandas_ta as ta
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

from stolgo.breakout import Breakout


ticker = yf.Ticker("TSLA")
ohlcv = ticker.history(start="2023-01-01", end="2023-10-26")

#df = ohlcv[0:45]

df = ohlcv

breakout_test = Breakout()

is_be = breakout_test.is_breaking_out(df,periods=None,percentage=None) #periods:Number of candles,percentage: range of consolidation in percentage

print("25년 12월 31일")

