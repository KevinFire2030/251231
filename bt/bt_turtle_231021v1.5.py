import pandas as pd
import numpy as np
import yfinance as yf
from backtesting import Backtest, Strategy
import pandas_ta as ta
from scipy.signal import savgol_filter
from scipy.signal import find_peaks

def SUPERTl(df):
    return df['SUPERTl_20_2.0']
def SUPERTs(df):
    return df['SUPERTs_20_2.0']

def HMA10(df):
    return df['hma10']

def Close_smooth(df):
    return df['Close_smooth']

class Turtle(Strategy):

    def init(self):

        super().init()

        self.hma10 = self.I(HMA10, self.data)
        self.close_smooth = self.I(Close_smooth, self.data)


        #self.sma5 = self.I(ta.sma, pd.Series(self.data.Close), 5)
        #self.sma10 = self.I(ta.sma, pd.Series(self.data.Close), 10)
        #self.hma10 = self.I(ta.hma, pd.Series(self.data.Close), 10)
        #self.hma20 = self.I(ta.hma, pd.Series(self.data.Close), 20)
        #self.st_short = self.I(SUPERTs, st)
        #self.st_long = self.I(SUPERTl, st)

        #self.st = self.I(ta.supertrend, pd.Series(self.data.High),pd.Series(self.data.Low), pd.Series(self.data.Close), 10, 2)




        pass

    def next(self):
        super().next()



        pass

#ticker = yf.Ticker("ES=F")
#ticker = yf.Ticker("MSFT")
#ticker = yf.Ticker("AAPL")
#ticker = yf.Ticker("AMZN")
ticker = yf.Ticker("TSLA")
#ohlcv = ticker.history(interval='1d')

ohlcv = ticker.history(start="2023-01-01", end="2023-10-20")
ohlcv.index = ohlcv.index.tz_localize(None)


#st = ta.supertrend(ohlcv['High'], ohlcv['Low'], ohlcv['Close'], 20, 2)

ohlcv['hma10'] = ta.hma(ohlcv['Close'], 10)
ohlcv['Close_smooth'] = savgol_filter(ohlcv['Close'], 49, 5)
#ohlcv['hma10_diff'] = ohlcv['hma10'].diff()

peaks_idx = find_peaks(ohlcv['hma10'], distance=15, width=3, prominence=atr)

bt = Backtest(ohlcv, Turtle, cash=10000, commission=.000)
stats = bt.run()
print(stats)

print(stats['_trades'].to_string())

bt.plot()

print("나는 2025년 12월 31일 10억 자산과 월500만원 버는 시스템을 갖추고 은퇴했다")