import pandas as pd
import numpy as np
import yfinance as yf
from backtesting import Backtest, Strategy
#from backtesting.lib import TrailingStrategy
import pandas_ta as ta
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


ohlcv = pd.read_excel('AAPL_231016v1.0.xlsx')
df = ohlcv[0:45]

df['atr'] = ta.atr(df['High'], df['Low'], df['Close'], 10)
df['hma10'] = ta.hma(df['Close'], 10)

atr = df.atr.iloc[-1]

#peaks_idx, _ = find_peaks (df.hma10, distance = 15, width = 1, prominence = atr)
#troughs_idx, _ = find_peaks (-1*df.hma10, distance = 15, width = 1, prominence = atr)

#peaks_idx, _ = find_peaks (df.hma10)
#troughs_idx, _ = find_peaks (-1*df.hma10)


#peaks_idx, _ = find_peaks (df.hma10, width = 1)
#troughs_idx, _ = find_peaks (-1*df.hma10, width = 1)


peaks_idx, _ = find_peaks (df.hma10, width = 6)
troughs_idx, _ = find_peaks (-1*df.hma10, width = 6)

fig, ax = plt.subplots()
plt.xticks(rotation=-30)
price, = ax.plot(df.index, df.Close, c='grey', alpha=0.5, zorder=5)
hma10, = ax.plot(df.index, df.hma10, c='b', alpha=0.5, zorder=5)
peaks, = ax.plot(df.index[peaks_idx], df.hma10.iloc[peaks_idx], c='r', linestyle='None', markersize=10, marker="o", zorder=10)
troughs, = ax.plot(df.index[troughs_idx], df.hma10.iloc[troughs_idx], c='g', linestyle='None', markersize=10, marker="o", zorder=10)

plt.show()


print("25년 12월 31일")
