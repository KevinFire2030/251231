import pandas as pd
import numpy as np
import yfinance as yf
from backtesting import Backtest, Strategy
#from backtesting.lib import TrailingStrategy
import pandas_ta as ta


def HMA10(df):
    return df['hma10']
def HMA20(df):
    return df['hma20']

def HMA60(df):
    return df['hma60']



class TrailingStrategy(Strategy):
    """
    A strategy with automatic trailing stop-loss, trailing the current
    price at distance of some multiple of average true range (ATR). Call
    `TrailingStrategy.set_trailing_sl()` to set said multiple
    (`6` by default). See [tutorials] for usage examples.

    [tutorials]: index.html#tutorials

    Remember to call `super().init()` and `super().next()` in your
    overridden methods.
    """
    __n_atr = 6.
    __atr = None

    def init(self):
        super().init()
        self.set_atr_periods()

    def set_atr_periods(self, periods: int = 20):
        """
        Set the lookback period for computing ATR. The default value
        of 100 ensures a _stable_ ATR.
        """
        h, l, c_prev = self.data.High, self.data.Low, pd.Series(self.data.Close).shift(1)
        tr = np.max([h - l, (c_prev - h).abs(), (c_prev - l).abs()], axis=0)
        atr = pd.Series(tr).rolling(periods).mean().bfill().values
        self.__atr = atr

    def set_trailing_sl(self, n_atr: float = 2):
        """
        Sets the future trailing stop-loss as some multiple (`n_atr`)
        average true bar ranges away from the current price.
        """
        self.__n_atr = n_atr

    def next(self):
        super().next()
        # Can't use index=-1 because self.__atr is not an Indicator type
        index = len(self.data)-1
        for trade in self.trades:
            if trade.is_long:
                trade.sl = max(trade.sl or -np.inf,
                               self.data.Close[index] - self.__atr[index] * self.__n_atr)

            else:
                trade.sl = min(trade.sl or np.inf,
                               self.data.Close[index] + self.__atr[index] * self.__n_atr)

        if self.position:
            if self.trades[-1].is_long:
                if (self.data.Close[index] >= self.trades[-1].entry_price + self.__atr[index]) and (len(self.trades) < 6):
                    self.buy(size=0.2)
                    print("Long Pyramiding")
                else:
                    if (self.data.Close[index] <= self.trades[-1].entry_price - self.__atr[index]) and (
                            len(self.trades) < 6):
                        self.sell(size=0.2)
                        print("Short Pyramiding")

            pass

class Turtle(TrailingStrategy):

    def init(self):
        super().init()
        super().set_trailing_sl(2)

        self.hma10 = self.I(HMA10, self.data)
        self.hma20 = self.I(HMA20, self.data)
        self.hma60 = self.I(HMA60, self.data)

        pass

    def next(self):
        super().next()

        if self.position:
            pass
        else:
            self.buy(size = 0.2)


ticker = yf.Ticker("TSLA")


ohlcv = ticker.history(start="2023-01-01", end="2023-10-20")
ohlcv.index = ohlcv.index.tz_localize(None)


ohlcv['hma10'] = ta.hma(ohlcv['Close'], 10)
ohlcv['hma20'] = ta.hma(ohlcv['Close'], 20)
ohlcv['hma60'] = ta.hma(ohlcv['Close'], 60)


bt = Backtest(ohlcv, Turtle, cash=10000, commission=.000, trade_on_close=True)
stats = bt.run()
print(stats)

print(stats['_trades'].to_string())

bt.plot()

print("나는 2025년 12월 31일 10억 자산과 월500만원 버는 시스템을 갖추고 은퇴했다")