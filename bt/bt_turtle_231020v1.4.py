import pandas as pd
import numpy as np
import yfinance as yf
from backtesting import Backtest, Strategy
import pandas_ta as ta

sys1_entry = 20
sys1_exit = 10
atr_periods = 20
r_max = 0.02
u_max = 5

def calcTR(high, low, close):
  '''Calculate True Range'''
  return np.max(np.abs([high-low, close-low, low-close]))


def calc_breakouts(data, sys1_entry, sys1_exit):
    # Gets breakouts for all tickers

    # Breakouts for enter long position (EL), exit long (ExL)
    # enter short (ES), exit short (ExS)
    data['S1_EL'] = data['Close'].rolling(sys1_entry).max()
    data['S1_ExL'] = data['Close'].rolling(sys1_exit).min()
    data['S1_ES'] = data['Close'].rolling(sys1_entry).min()
    data['S1_ExS'] = data['Close'].rolling(sys1_exit).max()

    return data

def calc_N(data, atr_periods):
    # Calculates N for all tickers

    tr = data.apply(
        lambda x: calcTR(x['High'], x['Low'], x['Close']), axis=1)
    data['N'] = tr.rolling(atr_periods).mean()

    return data

def SUPERTl(df):
    return df['SUPERTl_20_2.0']
def SUPERTs(df):
    return df['SUPERTs_20_2.0']

class Turtle(Strategy):

    def init(self):

        super().init()

        df = pd.DataFrame()
        df['high'] = pd.Series(self.data.High)
        df['low'] = pd.Series(self.data.Low)
        df['close'] = pd.Series(self.data.Close)
        st = ta.supertrend(df['high'], df['low'], df['close'], 20, 2)

        df['hma10_c'] = ta.hma(df['close'], 10)
        df['hma10_h'] = ta.hma(df['high'], 10)
        df['hma10_l'] = ta.hma(df['low'], 10)
        df['hma10_diff'] = df['hma10_c'].diff()
        df['hma_atr'] = ta.atr(df['hma10_h'], df['hma10_l'], df['hma10_c'], 10)

        #self.sma5 = self.I(ta.sma, pd.Series(self.data.Close), 5)
        self.sma10 = self.I(ta.sma, pd.Series(self.data.Close), 10)
        #self.hma10 = self.I(ta.hma, pd.Series(self.data.Close), 10)
        #self.hma20 = self.I(ta.hma, pd.Series(self.data.Close), 20)
        self.st_short = self.I(SUPERTs, st)
        self.st_long = self.I(SUPERTl, st)

        #self.st = self.I(ta.supertrend, pd.Series(self.data.High),pd.Series(self.data.Low), pd.Series(self.data.Close), 10, 2)


        pass

    def _check_cash_balance(self, shares, price):
        # Checks to see if we have enough cash to make purchase.
        # If not, resizes position to lowest feasible level
        if self.equity <= shares * price:
            shares = np.floor(self.equity / price)
        return shares

    def next(self):
        super().next()

        price = self.data.Close[-1]
        S1_EL = self.data.S1_EL[-1]
        S1_ES = self.data.S1_ES[-1]

        S1_ExL = self.data.S1_ExL[-1]
        S1_ExS = self.data.S1_ExS[-1]

        N = self.data.N[-1]




        if len(self.trades) > 0:

            self.trades[0].sl = self.trades[0].entry_price * 0.9
            self.trades[0].tp = self.trades[0].entry_price * 1.1

            self.trades[-1].sl = self.trades[-1].entry_price * 0.9
            self.trades[-1].tp = self.trades[-1].entry_price * 1.1

            # Exit
            if self.trades[-1].is_long and (price == S1_ExL or price <= self.trades[-1].sl):

                """
                for i in reversed(range(0, len(self.trades))):
                    self.trades[i].close()
                """

                self.position.close()

            elif self.trades[-1].is_short and (price == S1_ExS or price >= self.trades[-1].sl):

                """
                for i in reversed(range(0, len(self.trades))):
                    self.trades[i].close()
                """

                self.position.close()

            # Pyramid
            if self.trades[-1].is_long and (price >= self.trades[-1].entry_price + N) and (len(self.trades) < 6):

                sl = price - 2 * N
                self.buy(sl=sl, size=0.2)

                print("Long Pyramiding")

            elif self.trades[-1].is_short and (price <= self.trades[-1].entry_price - N) and (len(self.trades) < 6):

                sl = price + 2 * N
                self.sell(sl=sl, size=0.2)

                print("Short Pyramiding")


        if len(self.trades) == 0:

            # Buy on breakout
            if price == S1_EL:
                sl = price - 2 * N
                self.buy(sl=sl, size=0.2)

            # Sell short
            elif price == S1_ES:
                sl = price + 2 * N
                self.sell(sl=sl, size=0.2)



#ticker = yf.Ticker("ES=F")
#ticker = yf.Ticker("MSFT")
#ticker = yf.Ticker("AAPL")
#ticker = yf.Ticker("AMZN")
ticker = yf.Ticker("TSLA")
#ohlcv = ticker.history(interval='1d')

ohlcv = ticker.history(start="2023-01-01", end="2023-10-20")

ohlcv = calc_breakouts(ohlcv, sys1_entry, sys1_exit)

ohlcv = calc_N(ohlcv, atr_periods)

ohlcv.dropna(inplace=True)
ohlcv.reset_index(inplace=True)

bt = Backtest(ohlcv, Turtle, cash=10000, commission=.000)
stats = bt.run()
print(stats)

print(stats['_trades'].to_string())

bt.plot()

print("나는 2025년 12월 31일 10억 자산과 월500만원 버는 시스템을 갖추고 은퇴했다")