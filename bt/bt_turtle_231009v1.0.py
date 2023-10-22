import pandas as pd
import numpy as np
import yfinance as yf
from backtesting import Backtest, Strategy


sys1_entry = 20
sys1_exit = 10
atr_periods = 20
r_max = 0.02

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

class Turtle(Strategy):

    def init(self):

        super().init()

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

        #size = (self.equity * r_max) // N
        unit = np.floor((self.equity * r_max) // (5 * N) )

        unit = self._check_cash_balance(unit, price)

        #unit = 70


        if len(self.trades) > 0:

            """
            #Exit
            if self.trades[-1].is_long and (price == S1_ExL or price <= self.trades[-1].sl):
                self.trades[-1].close()

            elif self.trades[-1].is_short and (price == S1_ExS or price >= self.trades[-1].sl):
                self.trades[-1].close()
            """

            # Pyramid
            #if self.trades[-1].is_long and (price == self.trades[-1].

            pass

        """
        if len(self.trades) > 0:

            if self.trades[-1].is_long:
                self.trades[-1].tp = S1_ExL

            elif self.trades[-1].is_short:
                self.trades[-1].tp = S1_ExL

            pass
        """

        if len(self.trades) == 0:

            # Buy on breakout
            if price == S1_EL:

                tp = price + 4 * N
                sl = price - 2 * N

                #self.buy(sl=sl,size=size)
                self.buy(sl=sl, tp=tp, size=unit)
                #self.buy(sl=sl, size=unit)

            # Sell short
            elif price == S1_ES:

                tp = price - 4 * N
                sl = price + 2 * N

                self.sell(sl=sl,tp=tp, size=unit)
                #self.sell(sl=sl, size=unit)



ticker = yf.Ticker("AAPL")
start_date = "2020-01-01"
end_date = "2023-10-09"
ohlcv = ticker.history(start=start_date, end=end_date)

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