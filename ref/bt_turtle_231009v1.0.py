# turtle trading
from datetime import datetime
import math
import backtrader as bt
import yfinance as yf

class Turtle(bt.Strategy):

    def __init__(self):
        self.atr = bt.ind.ATR(self.data, period=20)
        self.highest = 0  # 고가
        self.add_unit = 1  # unit 단위 수
        self.origin_cost = 0  # 가장 최근에 매수한 날짜의 종가
        self.total_cost = 0  # 총자산

    # 시스템 1 단기 전략
    def next(self):
        high_point = self.datas[0].close.get(ago=-1, size=20)  # 20일
        low_point = self.datas[0].close.get(ago=-1, size=10)  # 10일

        highest = max(high_point)
        lowest = min(low_point)

        # TR 값 구하기
        TR1 = self.datas[0].high[0] - self.datas[0].low[0]  # 당일 고가 - 저가
        TR2 = self.datas[0].high[0] - self.datas[0].close[-1]  # 당일 고가 - 전일 종가
        TR3 = self.datas[0].low[0] - self.datas[0].close[-1]  # 당일 저가 - 전일 종가

        # 위의 3가지 중 절댓값이 가장 큰 값이 TR
        tr = abs(TR1)
        if (tr < abs(TR2)):
            tr = abs(TR2)
        if (tr < abs(TR3)):
            tr = abs(TR3)

        # ATR = (전날 ATR*19 + 당일 TR*2) / 21
        self.atr = (self.atr * 19 + tr * 2) / 21

        unit = (self.broker.get_cash() * 0.01) / self.atr

        if not self.position:  # 아직 주식을 사지 않았을 때

            if self.datas[0].close[0] > highest:  # 20일 고점 상향 돌파 시 매수
                self.buy(self.datas[0], size=unit)
                self.origin_cost = self.datas[0].close[0]
                self.total_cost = self.broker.getvalue()

        else:
            # 1ATR 만큼 가격이 올랐을 때마다 1단위씩 추가 매수 (5단위까지만 매수 가능)
            if self.datas[0].close[0] > self.origin_cost + self.atr and self.add_unit < 6:
                self.buy(self.datas[0], size=unit)
                self.origin_cost = self.datas[0].close[0]
                self.add_unit += 1
                self.total_cost = self.broker.getvalue()

            # 2 ATR 손실 발생 시 손절
            # 총 자산에서 2% 손실 시 손절
            # 10일 저점 하향 돌파 시 매도
            elif self.datas[0].close[0] < lowest or self.broker.getvalue() < self.total_cost * 0.98 or self.datas[
                0].close < self.origin_cost - 2 * self.atr:
                self.close(self.datas[0])
                self.add_unit = 1



# cerebro 가져오기
cerebro = bt.Cerebro()

# 야후 금융 데이터 불러오기
"""
data = bt.feeds.YahooFinanceData(dataname='AAPL',
                                 fromdate=datetime(2023, 1, 1),
                                 todate=datetime(2023, 10, 9))
"""

data = bt.feeds.PandasData(dataname=yf.download('TSLA', '2018-01-01', '2019-01-01'))

# 데이터 추가
cerebro.adddata(data)

# 전략 추가
cerebro.addstrategy(Turtle)
cerebro.broker.setcash(10000000)  # 브로거 설정

# 초기 투자금
init_cash = cerebro.broker.getvalue()

# cerebro 실행
cerebro.run()

# 최종 금액
final_cash = cerebro.broker.getvalue()

print("최종 금액 : ", final_cash, "\\")
print("수익률 : ", float(final_cash - init_cash) / float(init_cash) *100.0, "%")

# 차트 출력
cerebro.plot()