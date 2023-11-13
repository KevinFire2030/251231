[231114]

```
NQ_5min

Start                                     0.0
End                                 1035421.0
Duration                            1035421.0
Exposure Time [%]                   36.600729
Equity Final [$]                    15510.575
Equity Peak [$]                       20158.1
Return [%]                         -22.447125
Buy & Hold Return [%]              591.087069
Return (Ann.) [%]                         0.0
Volatility (Ann.) [%]                     NaN
Sharpe Ratio                              NaN
Sortino Ratio                             NaN
Calmar Ratio                              0.0
Max. Drawdown [%]                  -23.199731
Avg. Drawdown [%]                   -2.427642
Max. Drawdown Duration              1033999.0
Avg. Drawdown Duration               103539.5
# Trades                              52189.0
Win Rate [%]                        34.076146
Best Trade [%]                       7.331093
Worst Trade [%]                     -4.759222
Avg. Trade [%]                      -0.003578
Max. Trade Duration                     111.0
```



[231113]

```
== on_receive_tr_data ==
선물틱차트연속조회
[선물틱연속차트조회] 1000
last_tick_count:  120
Failed login
```

[231111]
* 120틱, 10분
* 다시보자 turtle, 손익비와 승률
* fire2025 세팅
* 키움 모투, 주식, 선물
* 데이터, 전처리, 매매


□ 연장전

□ 후반전
* 251231 PRJ 목표 일정
* fire2025 세팅, 아나콘다 삭제/재설치, 파이참 재설치, 메모리 업그레이드
* 키움 코스피200 선물 120틱 받기, 터틀 백테스트, 나스닥100 선물, 

[231031]
* https://github.com/stockalgo/stolgo


[231028]
* 쿠리마쿠, 10/20/50 EMA, 눌림목 매매

(Volatility Contraction Pattern python)
https://github.com/clairetsoi1129/stock-screener


https://www.youtube.com/watch?v=WswZwmr2ebU&t=673s

https://valuefund.substack.com/p/how-does-one-trader-turn-9100-into


https://www.youtube.com/watch?v=ly5SR3um35w

![image](https://github.com/KevinFire2030/251231/assets/109524169/93a7846e-497e-434d-ad7d-da5ac55d6e81)

```
[진입 조건]
*이동평균선 EMA 3개, 손익비와 승률
*자금과 리스크 관리(중요)로 스윙 트레이딩

1. 리스크 관리!
– 투자금은 전체 자산의 10 ~ 20%
– 손절폭은 전체 자산의 0.5% ~ 1.5%

2. 진입 시점!
– 상승 혹은 하락 후 이평선 눌림 후 발산 시점
– 이동평균선 10 / 20 / 50일선이 완전 정배열 혹은 완전 역배열을 이룰 때
– 눌림목 조정의 박스권을 돌파하는 시점

 

[손절 조건]
1. 진입 후 반대 캔들 발생시, 1/2 손절
(Ex. 상승 추세일 경우, 첫 음봉 발생시 1/2 손절 혹은 익절)

2. 진입 캔들 돌파시 전량 손절

 

[익절 조건]
1. 진입 후 반대 캔들 발생시, 1/2 익절

2. 10일선이 20일선 돌파시 전량 익절

 

참조 : https://www.youtube.com/watch?v=hHA8_aa55mY

```

![image](https://github.com/KevinFire2030/251231/assets/109524169/10295968-e0f9-4364-97e6-ba8e2a774351)

![image](https://github.com/KevinFire2030/251231/assets/109524169/4e0bb9d2-8683-4851-be3a-6f143d627a45)


![image](https://github.com/KevinFire2030/251231/assets/109524169/72104b88-74a4-4775-bdad-036254003b68)

![image](https://github.com/KevinFire2030/251231/assets/109524169/0f0817f5-0879-43d9-a6eb-b53ead1423e3)

![image](https://github.com/KevinFire2030/251231/assets/109524169/a76f14cd-6d79-415f-aea0-fcbb69ce3bb6)

![image](https://github.com/KevinFire2030/251231/assets/109524169/e2b9eeea-cd26-4ddc-8171-62f933f74bad)

![image](https://github.com/KevinFire2030/251231/assets/109524169/80057d60-5ef3-4475-acd1-66c446be6118)

![image](https://github.com/KevinFire2030/251231/assets/109524169/25bc5d6d-32c6-4fc8-9073-a964c92232df)

![image](https://github.com/KevinFire2030/251231/assets/109524169/0bcfb2b6-286f-4ea0-94fd-88a76a26a203)

![image](https://github.com/KevinFire2030/251231/assets/109524169/d44a138f-5944-451e-a826-3a0d88c09044)


[231026]
* 퓨쳐셀프, 25년 12월 31일 나는 자산10억과 월500 버는 시스템을 갖추고 은퇴(Fire)했다
* 다시보자 터틀 트래이딩
* find_peaks()와 횡보구간 피하기

(find_peaks와 breakouts, 그리고 ATR)

```
df['atr'] = ta.atr(df['High'], df['Low'], df['Close'], 20)
df['hma10'] = ta.hma(df['Close'], 20)

df['S1_EL'] = df['Close'].rolling(20).max()
df['S1_ES'] = df['Close'].rolling(20).min()


```


![image](https://github.com/KevinFire2030/251231/assets/109524169/21fa51e0-6ca3-4d33-ac11-e7fba32fd574)



```
ax.vlines(df.index[peaks_idx], ymin=df.hma10.iloc[peaks_idx]-df.atr.iloc[peaks_idx], ymax=df.hma10.iloc[peaks_idx], color="C1")
ax.vlines(df.index[troughs_idx], ymax=df.hma10.iloc[troughs_idx]+df.atr.iloc[troughs_idx], ymin=df.hma10.iloc[troughs_idx], color="C1")
```

![image](https://github.com/KevinFire2030/251231/assets/109524169/aee266a5-5052-42d7-9579-00932315ef48)


(find_peaks와 breakouts)

![image](https://github.com/KevinFire2030/251231/assets/109524169/16545958-a631-48e1-b295-be7c9806e25e)


(find_peaks)

ticker = yf.Ticker("TSLA")
ohlcv = ticker.history(start="2023-01-01", end="2023-10-26")

peaks_idx, _ = find_peaks (df.hma10)
troughs_idx, _ = find_peaks (-1*df.hma10)

![image](https://github.com/KevinFire2030/251231/assets/109524169/55a15984-8c35-437a-abac-f6493a8ab655)


![image](https://github.com/KevinFire2030/251231/assets/109524169/43c5f1b3-2a17-46cf-97fd-d837406de77f)


![image](https://github.com/KevinFire2030/251231/assets/109524169/4daa956d-5660-4f60-83db-4027829185e7)



[231023]
* 본전컷
* hma, 변곡점 매매, 10일 vs 20일
* 키움 브로커


( hma, 변곡점 매매)
* 변곡점에 점찍기
* hma20 vs hma10
* 횡보구간 피하기, 5개 이상 유지, 고점대비 1atr 변동
* 피라미딩, 10번, 1/2atr
* 피라미딩, 역피라미딩, 조던의 방식

[231021]
* sl 변경하기
* 거래량
* 횡보구간
* 손실은 작게 이익은 크게
* 지표 추가, 승률과 손익비 그리고 비중조절

(롱숏)
* SUPERTd

```
Start                     2023-01-03 00:00:00
End                       2023-10-19 00:00:00
Duration                    289 days 00:00:00
Exposure Time [%]                   93.532338
Equity Final [$]                 11813.134885
Equity Peak [$]                  13583.359467
Return [%]                          18.131349
Buy & Hold Return [%]              103.617025
Return (Ann.) [%]                   23.232844
Volatility (Ann.) [%]               25.005783
Sharpe Ratio                         0.929099
Sortino Ratio                        1.807234
Calmar Ratio                         1.640832
Max. Drawdown [%]                  -14.159183
Avg. Drawdown [%]                   -7.245193
Max. Drawdown Duration      121 days 00:00:00
Avg. Drawdown Duration       51 days 00:00:00
# Trades                                   33
Win Rate [%]                        42.424242
Best Trade [%]                      42.986063
Worst Trade [%]                    -13.014114
Avg. Trade [%]                       4.403809
Max. Trade Duration          41 days 00:00:00
Avg. Trade Duration          18 days 00:00:00
Profit Factor                        2.629905
Expectancy [%]                        5.49794
SQN                                  1.226756
_strategy                              Turtle
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
    Size  EntryBar  ExitBar  EntryPrice   ExitPrice         PnL  ReturnPct  EntryTime   ExitTime Duration
0      5        12       18  133.419998  166.660004  166.200027   0.249138 2023-01-20 2023-01-30  10 days
1      4        25       40  201.289993  190.772003  -42.071960  -0.052253 2023-02-08 2023-03-02  22 days
2      5        22       40  189.979996  190.772003    3.960037   0.004169 2023-02-03 2023-03-02  27 days
3      5        17       40  177.899994  190.772003   64.360046   0.072355 2023-01-27 2023-03-02  34 days
4      8        16       40  160.270004  190.772003  244.015991   0.190316 2023-01-26 2023-03-02  35 days
5     11        13       40  143.750000  190.772003  517.242035   0.327110 2023-01-23 2023-03-02  38 days
6      9        12       40  133.419998  190.772003  516.168045   0.429861 2023-01-20 2023-03-02  41 days
7     12        40       45  190.899994  174.977991 -191.064038  -0.083405 2023-03-02 2023-03-09   7 days
8    -13        45       53  172.919998  195.424004 -292.552071  -0.130141 2023-03-09 2023-03-21  12 days
9      7        53       62  197.580002  194.770004  -19.669983  -0.014222 2023-03-21 2023-04-03  13 days
10     4        53       64  197.580002  189.727007  -31.411981  -0.039746 2023-03-21 2023-04-05  15 days
11     8        61       63  207.460007  192.580002 -119.040039  -0.071725 2023-03-31 2023-04-04   4 days
12    -1        63       85  192.580002  169.565001   23.015001   0.119509 2023-04-04 2023-05-05  31 days
13   -12        85       95  170.059998  180.381006 -123.852100  -0.060690 2023-05-05 2023-05-19  14 days
14     3       108      117  234.860001  254.235007   58.125018   0.082496 2023-06-08 2023-06-22  14 days
15     4       107      117  224.570007  254.235007  118.659998   0.132097 2023-06-07 2023-06-22  15 days
16     5       104      117  213.970001  254.235007  201.325027   0.188181 2023-06-02 2023-06-22  20 days
17     6       101      117  201.160004  254.235007  318.450018   0.263845 2023-05-30 2023-06-22  23 days
18     9        96      117  188.869995  254.235007  588.285104   0.346085 2023-05-22 2023-06-22  31 days
19    11        95      117  180.139999  254.235007  815.045081   0.411319 2023-05-19 2023-06-22  34 days
20     8       117      119  264.609985  241.050003 -188.479858  -0.089037 2023-06-22 2023-06-26   4 days
21     1       117      120  264.609985  250.210007  -14.399979  -0.054420 2023-06-22 2023-06-27   5 days
22    -8       120      124  250.210007  279.441991 -233.855872  -0.116830 2023-06-27 2023-07-03   6 days
23     6       134      136  293.339996  269.582011 -142.547910  -0.080991 2023-07-18 2023-07-20   2 days
24     8       124      136  279.820007  271.218001  -68.816052  -0.030741 2023-07-03 2023-07-20  17 days
25    -9       136      159  262.899994  233.722003  262.601917   0.110985 2023-07-20 2023-08-22  33 days
26   -10       159      164  233.190002  248.730991 -155.409882  -0.066645 2023-08-22 2023-08-29   7 days
27     8       164      167  257.179993  245.009995  -97.359985  -0.047321 2023-08-29 2023-09-01   3 days
28     8       172      181  273.579987  253.058009 -164.175818  -0.075013 2023-09-11 2023-09-22  11 days
29     1       164      181  257.179993  253.058009   -4.121983  -0.016028 2023-08-29 2023-09-22  24 days
30    -9       180      190  255.699997  261.985999  -56.574014  -0.024584 2023-09-21 2023-10-05  14 days
31     9       190      199  260.049988  244.614995 -138.914937  -0.059354 2023-10-05 2023-10-18  13 days
32    -9       199      199  242.679993  242.679993   -0.000000  -0.000000 2023-10-18 2023-10-18   0 days

```

![image](https://github.com/KevinFire2030/251231/assets/109524169/8da4051a-4227-4160-ae0e-da8f55cd774e)



(trailing stop)
* 본전컷
* breakeven cut
* 다음에 하자

(Pyramiding)
* Pyramiding
```
Start                     2023-01-03 00:00:00
End                       2023-10-19 00:00:00
Duration                    289 days 00:00:00
Exposure Time [%]                   99.004975
Equity Final [$]                 15593.137956
Equity Peak [$]                  17008.005756
Return [%]                           55.93138
Buy & Hold Return [%]              103.617025
Return (Ann.) [%]                   74.536717
Volatility (Ann.) [%]               45.905176
Sharpe Ratio                         1.623711
Sortino Ratio                        4.849016
Calmar Ratio                          6.13003
Max. Drawdown [%]                  -12.159275
Avg. Drawdown [%]                   -3.860145
Max. Drawdown Duration      121 days 00:00:00
Avg. Drawdown Duration       29 days 00:00:00
# Trades                                   30
Win Rate [%]                        56.666667
Best Trade [%]                      67.873992
Worst Trade [%]                    -15.096405
Avg. Trade [%]                         9.8758
Max. Trade Duration          63 days 00:00:00
Avg. Trade Duration          26 days 00:00:00
Profit Factor                        5.580942
Expectancy [%]                      11.807113
SQN                                  2.407418
_strategy                              Turtle
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object
    Size  EntryBar  ExitBar  EntryPrice   ExitPrice          PnL  ReturnPct  EntryTime   ExitTime Duration
0      3        22       40  189.979996  190.772003     2.376022   0.004169 2023-02-03 2023-03-02  27 days
1      4        17       40  177.899994  190.772003    51.488037   0.072355 2023-01-27 2023-03-02  34 days
2      6        16       40  160.270004  190.772003   183.011993   0.190316 2023-01-26 2023-03-02  35 days
3      9        13       40  143.750000  190.772003   423.198029   0.327110 2023-01-23 2023-03-02  38 days
4     12         9       40  131.490005  190.772003   711.383972   0.450848 2023-01-17 2023-03-02  44 days
5     17         1       40  113.639999  190.772003  1311.244064   0.678740 2023-01-04 2023-03-02  57 days
6     13        40       45  190.899994  174.977991  -206.986041  -0.083405 2023-03-02 2023-03-09   7 days
7      8        53       64  197.580002  189.727007   -62.823962  -0.039746 2023-03-21 2023-04-05  15 days
8     10        50       64  184.130005  189.727007    55.970016   0.030397 2023-03-16 2023-04-05  20 days
9     14        45       64  172.919998  189.727007   235.298117   0.097195 2023-03-09 2023-04-05  27 days
10     6        61       66  207.460007  176.141003  -187.914020  -0.150964 2023-03-31 2023-04-10  10 days
11    13        66       74  184.509995  170.222989  -185.731073  -0.077432 2023-04-10 2023-04-20  10 days
12     4       104      117  213.970001  254.235007   161.060022   0.188181 2023-06-02 2023-06-22  20 days
13     5       101      117  201.160004  254.235007   265.375015   0.263845 2023-05-30 2023-06-22  23 days
14     6        96      117  188.869995  254.235007   392.190070   0.346085 2023-05-22 2023-06-22  31 days
15     8        95      117  180.139999  254.235007   592.760059   0.411319 2023-05-19 2023-06-22  34 days
16    11        86      117  171.789993  254.235007   906.895148   0.479917 2023-05-08 2023-06-22  45 days
17    15        74      117  162.990005  254.235007  1368.675018   0.559820 2023-04-20 2023-06-22  63 days
18     7       134      136  293.339996  269.582011  -166.305894  -0.080991 2023-07-18 2023-07-20   2 days
19     9       124      136  279.820007  271.218001   -77.418059  -0.030741 2023-07-03 2023-07-20  17 days
20    12       117      136  264.609985  271.218001    79.296185   0.024973 2023-06-22 2023-07-20  28 days
21    12       136      148  262.899994  246.359996  -198.479974  -0.062914 2023-07-20 2023-08-07  18 days
22    12       148      155  251.449997  228.425999  -276.287970  -0.091565 2023-08-07 2023-08-16   9 days
23     6       172      181  273.579987  253.058009  -123.131863  -0.075013 2023-09-11 2023-09-22  11 days
24     7       164      181  257.179993  253.058009   -28.853883  -0.016028 2023-08-29 2023-09-22  24 days
25    10       160      181  236.860001  253.058009   161.980087   0.068386 2023-08-23 2023-09-22  30 days
26    13       155      181  225.600006  253.058009   356.954042   0.121711 2023-08-16 2023-09-22  37 days
27     9       189      199  261.160004  244.614995  -148.905080  -0.063352 2023-10-04 2023-10-18  14 days
28    12       181      199  244.880005  244.614995    -3.180121  -0.001082 2023-09-22 2023-10-18  26 days
29    12       199      199  242.679993  242.679993     0.000000   0.000000 2023-10-18 2023-10-18   0 days
```

![image](https://github.com/KevinFire2030/251231/assets/109524169/821c24c5-66ed-4e41-9b22-8433e7014b2c)



(trailing stop)


(Detecting Price Trends in python - Higher Highs, Higher Lows)

https://www.youtube.com/watch?v=v3z3FuxLzjU

![image](https://github.com/KevinFire2030/251231/assets/109524169/9eb5a5fc-16a4-4315-abc3-26023269d1f0)



![image](https://github.com/KevinFire2030/251231/assets/109524169/2fcf3890-5ee5-48b7-b63b-aea63bc949a0)


(Live trading support )

https://github.com/kernc/backtesting.py/issues/81

(Stop Losses in Backtesting.py)
* 참 대단한 사람들이 많구나 ㅠㅠ
https://greyhoundanalytics.com/blog/stop-losses-in-backtestingpy/

```
from backtesting import Backtest
from backtesting import Strategy
from backtesting.test import GOOG
from backtesting.lib import crossover

class TrailingStrategy(Strategy):

    __sl_amount = 6.

    def init(self):
        super().init()

    def set_trailing_sl(self, sl_amount: float = 6):
        """
    Set the trailing stop loss as $n below the current price (for long positions)
        Works for future bars only
        """
        self.__sl_amount = sl_amount

    def next(self):
        super().next()
        # Can't use index=-1 because self.__atr is not an Indicator type
        index = len(self.data)-1

        for trade in self.trades:
            if trade.is_long:
                trade.sl = max(trade.sl or -np.inf,
                               self.data.Close[index] -  self.__sl_amount)
            else:
                trade.sl = min(trade.sl or np.inf,
                               self.data.Close[index] +  self.__sl_amount)

```


(adjusting SL/TP)
https://github.com/kernc/backtesting.py/discussions/1015

```

       if len(self.trades) > 0:

            self.trades[0].sl = self.trades[0].entry_price * 0.9
            self.trades[0].tp = self.trades[0].entry_price * 1.1

            self.trades[-1].sl = self.trades[-1].entry_price * 0.9
            self.trades[-1].tp = self.trades[-1].entry_price * 1.1

```



```

class MACDStrategy(Strategy):
    
    # Define the two EMA lags as *class variables*
    # for later optimization
    fast = 12
    slow = 26
    signal = 9
    
    def init(self):                
        self.fast_macd      = self.I(MACD_Backtesting_FAST, self.data.Close, self.fast, overlay=True, name='FAST')
        self.slow_macd      = self.I(MACD_Backtesting_SLOW, self.data.Close, self.slow, overlay=True, name='SLOW')        
        self.macd_macd_      = MACD_Backtesting_MACD(self.fast_macd, self.slow_macd)        
        self.signal_macd_    = MACD_Backtesting_SIGNAL(self.macd_macd_, self.signal)
        self.histogram_macd_ = MACD_Backtesting_HISTOGRAMM(self.macd_macd_, self.signal_macd_)
        
        self.macd_macd, self.signal_macd, self.histogram_macd = self.I(
            lambda: (self.macd_macd_, self.signal_macd_, self.histogram_macd_)                                    
                , overlay=False,legends=['MACD', 'signal', 'histogramm'], histogramms=[False, False, True], scatter=False, name='MACD',)
 ```       

(SL First)
When SL and TP are hit within the same bar, backtesting.py acts pessimistically, that is considering SL as hit first.
SL과 TP가 동일한 막대 내에 도달하면 backtesting.py는 비관적으로 작동합니다. 즉, SL을 먼저 적중한 것으로 간주합니다.

(timezone 제거)
You can remove the time zone information of DatetimeIndex using DatetimeIndex.tz_localize() , as follows:

hist.index = hist.index.tz_localize(None)


bt = Backtest(df, Scalp_buy, cash=10000, commission=.0014, trade_on_close=True)

![image](https://github.com/KevinFire2030/251231/assets/109524169/39cdc5e5-edff-43bd-ae7c-433f4b82e1b6)

```
Methods
def I
(
self, func, *args, name=None, plot=True, overlay=None, color=None, scatter=False, **kwargs)
Declare indicator. An indicator is just an array of values, but one that is revealed gradually in Strategy.next() much like Strategy.data is. Returns np.ndarray of indicator values.

func is a function that returns the indicator array(s) of same length as Strategy.data.

In the plot legend, the indicator is labeled with function name, unless name overrides it.

If plot is True, the indicator is plotted on the resulting Backtest.plot().

If overlay is True, the indicator is plotted overlaying the price candlestick chart (suitable e.g. for moving averages). If False, the indicator is plotted standalone below the candlestick chart. By default, a heuristic is used which decides correctly most of the time.

color can be string hex RGB triplet or X11 color name. By default, the next available color is assigned.

If scatter is True, the plotted indicator marker will be a circle instead of a connected line segment (default).

Additional *args and **kwargs are passed to func and can be used for parameters.

For example, using simple moving average function from TA-Lib:

```


[231020]
* 날짜
* position close
* 10일선 sl 표시, 
* sl 변경하기
* supertrend
* 거래량
* 횡보구간


Close portion of position by closing portion of each active trade. See Trade.close().

[231016]


(bt_turtle_231016v1.3.py)
* 머징
* 날짜, 표준시 처리

(피라미딩 적용후)

```

AAPL 1시간봉
ticker = yf.Ticker("AAPL")
ohlcv = ticker.history(interval='1h')
size = 0.2

                for i in reversed(range(0, len(self.trades))):
                    self.trades[i].close()

Start                                     0.0
End                                     121.0
Duration                                121.0
Exposure Time [%]                   66.393443
Equity Final [$]                  10077.44046
Equity Peak [$]                  10182.589462
Return [%]                           0.774405
Buy & Hold Return [%]                 0.48518
Return (Ann.) [%]                         0.0
Volatility (Ann.) [%]                     NaN
Sharpe Ratio                              NaN
Sortino Ratio                             NaN
Calmar Ratio                              0.0
Max. Drawdown [%]                   -1.315668
Avg. Drawdown [%]                   -0.579292
Max. Drawdown Duration                   54.0
Avg. Drawdown Duration              18.333333
# Trades                                 13.0
Win Rate [%]                        53.846154
Best Trade [%]                       3.006381
Worst Trade [%]                      -1.25181
Avg. Trade [%]                       0.302979
Max. Trade Duration                      41.0
Avg. Trade Duration                 17.384615
Profit Factor                        1.783875
Expectancy [%]                       0.311594
SQN                                  0.935513
_strategy                              Turtle
_equity_curve                        Equit...
_trades                       Size  EntryB...
dtype: object
    Size  EntryBar  ExitBar  EntryPrice   ExitPrice        PnL  ReturnPct  EntryTime  ExitTime  Duration
0    -11         2       11  174.550003  176.380005 -20.130020  -0.010484          2        11         9
1    -11        24       40  173.089996  171.889999  13.199966   0.006933         24        40        16
2     -9        29       40  171.740005  171.889999  -1.349945  -0.000873         29        40        11
3     -7        33       40  169.850006  171.889999 -14.279953  -0.012011         33        40         7
4     11        52       59  173.350006  171.179993 -23.870148  -0.012518         52        59         7
5      5        85       86  177.934998  175.995081  -9.699585  -0.010902         85        86         1
6     11        75      116  173.960098  179.190002  57.528946   0.030064         75       116        41
7      9        78      116  175.119995  179.190002  36.630066   0.023241         78       116        38
8      7        82      116  176.679993  179.190002  17.570068   0.014207         82       116        34
9      5        90      116  177.960007  179.190002   6.149979   0.006912         90       116        26
10     4        92      116  178.899994  179.190002   1.160034   0.001621         92       116        24
11     4       107      116  180.070007  179.190002  -3.520020  -0.004887        107       116         9
12   -11       118      121  178.261002  176.619995  18.051071   0.009206        118       121         3

AAPL 1시간봉
ticker = yf.Ticker("AAPL")
ohlcv = ticker.history(interval='1h')
size = 0.2


Start                                     0.0
End                                     134.0
Duration                                134.0
Exposure Time [%]                   62.962963
Equity Final [$]                 10042.930283
Equity Peak [$]                  10173.599365
Return [%]                           0.429303
Buy & Hold Return [%]                0.241515
Return (Ann.) [%]                         0.0
Volatility (Ann.) [%]                     NaN
Sharpe Ratio                              NaN
Sortino Ratio                             NaN
Calmar Ratio                              0.0
Max. Drawdown [%]                   -1.316831
Avg. Drawdown [%]                   -0.550538
Max. Drawdown Duration                   54.0
Avg. Drawdown Duration              16.857143
# Trades                                 15.0
Win Rate [%]                        46.666667
Best Trade [%]                       3.006381
Worst Trade [%]                      -1.25181
Avg. Trade [%]                       0.132871
Max. Trade Duration                      41.0
Avg. Trade Duration                 15.866667
Profit Factor                        1.329292
Expectancy [%]                       0.140677
SQN                                  0.511876
_strategy                              Turtle
_equity_curve                        Equit...
_trades                       Size  EntryB...
dtype: object
    Size  EntryBar  ExitBar  EntryPrice   ExitPrice        PnL  ReturnPct  EntryTime  ExitTime  Duration
0     11         7       10  179.130005  177.589996 -16.940094  -0.008597          7        10         3
1     -9        16       25  174.550003  176.380005 -16.470016  -0.010484         16        25         9
2    -11        15       25  176.770004  176.380005   4.289993   0.002206         15        25        10
3     -7        47       54  169.850006  171.889999 -14.279953  -0.012011         47        54         7
4     -9        43       54  171.740005  171.889999  -1.349945  -0.000873         43        54        11
5    -11        38       54  173.089996  171.889999  13.199966   0.006933         38        54        16
6     11        66       73  173.350006  171.179993 -23.870148  -0.012518         66        73         7
7      5        99      100  177.934998  175.995081  -9.699585  -0.010902         99       100         1
8      4       121      130  180.070007  179.190002  -3.520020  -0.004887        121       130         9
9      4       106      130  178.899994  179.190002   1.160034   0.001621        106       130        24
10     5       104      130  177.960007  179.190002   6.149979   0.006912        104       130        26
11     7        96      130  176.679993  179.190002  17.570068   0.014207         96       130        34
12     9        92      130  175.119995  179.190002  36.630066   0.023241         92       130        38
13    11        89      130  173.960098  179.190002  57.528946   0.030064         89       130        41
14   -11       132      134  178.261002  178.940002  -7.469009  -0.003809        132       134         2


AAPL 1시간봉
ticker = yf.Ticker("AAPL")
ohlcv = ticker.history(interval='1h')
size = 0.1

Start                                     0.0
End                                     134.0
Duration                                134.0
Exposure Time [%]                   62.962963
Equity Final [$]                 10019.874838
Equity Peak [$]                  10097.189886
Return [%]                           0.198748
Buy & Hold Return [%]                0.241515
Return (Ann.) [%]                         0.0
Volatility (Ann.) [%]                     NaN
Sharpe Ratio                              NaN
Sortino Ratio                             NaN
Calmar Ratio                              0.0
Max. Drawdown [%]                   -0.780564
Avg. Drawdown [%]                   -0.342732
Max. Drawdown Duration                   55.0
Avg. Drawdown Duration              19.833333
# Trades                                 15.0
Win Rate [%]                        46.666667
Best Trade [%]                       3.006381
Worst Trade [%]                      -1.25181
Avg. Trade [%]                       0.132871
Max. Trade Duration                      41.0
Avg. Trade Duration                 15.866667
Profit Factor                        1.329292
Expectancy [%]                       0.140677
SQN                                  0.473592
_strategy                              Turtle
_equity_curve                        Equit...
_trades                       Size  EntryB...
dtype: object
    Size  EntryBar  ExitBar  EntryPrice   ExitPrice        PnL  ReturnPct  EntryTime  ExitTime  Duration
0      5         7       10  179.130005  177.589996  -7.700043  -0.008597          7        10         3
1     -5        16       25  174.550003  176.380005  -9.150009  -0.010484         16        25         9
2     -5        15       25  176.770004  176.380005   1.949997   0.002206         15        25        10
3     -4        47       54  169.850006  171.889999  -8.159973  -0.012011         47        54         7
4     -5        43       54  171.740005  171.889999  -0.749969  -0.000873         43        54        11
5     -5        38       54  173.089996  171.889999   5.999985   0.006933         38        54        16
6      5        66       73  173.350006  171.179993 -10.850067  -0.012518         66        73         7
7      4        99      100  177.934998  175.995081  -7.759668  -0.010902         99       100         1
8      3       121      130  180.070007  179.190002  -2.640015  -0.004887        121       130         9
9      3       106      130  178.899994  179.190002   0.870026   0.001621        106       130        24
10     4       104      130  177.960007  179.190002   4.919983   0.006912        104       130        26
11     4        96      130  176.679993  179.190002  10.040039   0.014207         96       130        34
12     5        92      130  175.119995  179.190002  20.350037   0.023241         92       130        38
13     5        89      130  173.960098  179.190002  26.149521   0.030064         89       130        41
14    -5       132      134  178.261002  178.940002  -3.395004  -0.003809        132       134         2

```

![image](https://github.com/KevinFire2030/251231/assets/109524169/253fd82d-664c-4ed2-8d48-5fb80b5114f9)


(피라미딩 적용전)

```
AAPL 1시간봉
ticker = yf.Ticker("AAPL")
ohlcv = ticker.history(interval='1h')


Start                                     0.0
End                                     134.0
Duration                                134.0
Exposure Time [%]                   62.962963
Equity Final [$]                 10012.154388
Equity Peak [$]                  10030.949402
Return [%]                           0.121544
Buy & Hold Return [%]                0.241515
Return (Ann.) [%]                         0.0
Volatility (Ann.) [%]                     NaN
Sharpe Ratio                              NaN
Sortino Ratio                             NaN
Calmar Ratio                              0.0
Max. Drawdown [%]                   -0.246564
Avg. Drawdown [%]                   -0.113801
Max. Drawdown Duration                   54.0
Avg. Drawdown Duration              16.857143
# Trades                                  6.0
Win Rate [%]                             50.0
Best Trade [%]                       3.006381
Worst Trade [%]                      -1.25181
Avg. Trade [%]                       0.228356
Max. Trade Duration                      41.0
Avg. Trade Duration                 13.166667
Profit Factor                        1.572878
Expectancy [%]                       0.237976
SQN                                  0.372438
_strategy                              Turtle
_equity_curve                        Equit...
_trades                      Size  EntryBa...
dtype: object
   Size  EntryBar  ExitBar  EntryPrice   ExitPrice        PnL  ReturnPct  EntryTime  ExitTime  Duration
0     5         7       10  179.130005  177.589996  -7.700043  -0.008597          7        10         3
1    -5        15       25  176.770004  176.380005   1.949997   0.002206         15        25        10
2    -5        38       54  173.089996  171.889999   5.999985   0.006933         38        54        16
3     5        66       73  173.350006  171.179993 -10.850067  -0.012518         66        73         7
4     5        89      130  173.960098  179.190002  26.149521   0.030064         89       130        41
5    -5       132      134  178.261002  178.940002  -3.395004  -0.003809        132       134         2
```

![image](https://github.com/KevinFire2030/251231/assets/109524169/a83d4b8e-dac5-402b-929d-1b80187f8404)


* 피라미딩 구현
```
Start                                     0.0
End                                    5949.0
Duration                               5949.0
Exposure Time [%]                   72.672269
Equity Final [$]                 16596.875874
Equity Peak [$]                  17326.389727
Return [%]                          65.968759
Buy & Hold Return [%]            22130.181273
Return (Ann.) [%]                         0.0
Volatility (Ann.) [%]                     NaN
Sharpe Ratio                              NaN
Sortino Ratio                             NaN
Calmar Ratio                              0.0
Max. Drawdown [%]                  -20.772209
Avg. Drawdown [%]                   -3.300172
Max. Drawdown Duration                 1689.0
Avg. Drawdown Duration             128.478261
# Trades                                711.0
Win Rate [%]                        39.803094
Best Trade [%]                      59.952609
Worst Trade [%]                    -26.424501
Avg. Trade [%]                       0.543516
Max. Trade Duration                      79.0
Avg. Trade Duration                 14.566807
Profit Factor                        1.357373
Expectancy [%]                        0.92328
SQN                                   2.55557
_strategy                              Turtle
_equity_curve                         Equi...
_trades                        Size  Entry...
dtype: object

```


```
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
        #unit = np.floor((self.equity * r_max) // (5 * N) )

        #unit = self._check_cash_balance(unit, price)

        #unit = 70


        if len(self.trades) > 0 :

            #self.trades[-1].entry_price = 10


            #Exit
            if self.trades[-1].is_long and (price == S1_ExL or price <= self.trades[-1].sl):

                for i in range(0, len(self.trades)):
                    self.trades[i].close()

                return

            elif self.trades[-1].is_short and (price == S1_ExS or price >= self.trades[-1].sl):
                for i in range(0, len(self.trades)):
                    self.trades[i].close()

                return


            # Pyramid
            if self.trades[-1].is_long and (price >= self.trades[-1].entry_price + N) and (len(self.trades) < 6):

                sl = price - 2 * N
                self.buy(sl=sl, size=0.1)

                print("롱 불타기")

            elif self.trades[-1].is_short and (price <= self.trades[-1].entry_price - N) and (len(self.trades) < 6):

                sl = price + 2 * N
                self.sell(sl=sl, size=0.1)

                print("숏 불타기")



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

                #tp = price + 4 * N
                sl = price - 2 * N


                #self.buy(sl=sl,size=size)

                #self.buy(sl=sl, tp=tp, size=unit)
                self.buy(sl=sl, size=0.1)
                #self.buy(sl=sl, size=0.1)
                #self.buy(sl=sl, size=unit)

            # Sell short
            elif price == S1_ES:

                #tp = price - 4 * N
                sl = price + 2 * N


                #self.sell(sl=sl,tp=tp, size=unit)
                #self.sell(sl=sl, size=unit)
                self.sell(sl=sl, size=0.1)


```



[231015]
* 통계를 내보니 신뢰도가 확떨어지는데 ㅋ
* 일단 저장

(turtle_231014v1.9)

![image](https://github.com/KevinFire2030/251231/assets/109524169/6b2d23e5-c699-4c07-a59a-328e8f56d70a)



![image](https://github.com/KevinFire2030/251231/assets/109524169/13d8afbd-67da-41f0-b703-9cc392dd02b7)



[231014]
* 승률과 손익비 그리고 비중조절
* 터틀 백테스팅, 시간, 분단위, 결과 보기

(turtle_231014v1.9)
* 데이터 읽기, 시간/분 단위
* 거래수, 승률, 손익비, 평균 이익, 평균 손실, 최대/최소 이익, 최대/최소 손실, 평균 거래일수, 최대 거래일수

![image](https://github.com/KevinFire2030/251231/assets/109524169/7eeaa9b1-9287-4f2f-a681-b3aa99ec9a27)


tickers = ["AAPL", "MSFT", "AMZN"]

sys = TurtleSystem(tickers, init_account_size=1E4, start='2000-01-01')


        tot_returns  annual_returns  ...  max_drawdown  max_drawdown_duration
Turtle      44.0638          0.1744  ...        0.6616                   2625
SPY          3.5854          0.0664  ...        0.5519                   2406



![image](https://github.com/KevinFire2030/251231/assets/109524169/dd971ff5-c055-4974-a0e1-826c8d741820)


(승률과 손익비 그리고 비중조절)

https://www.youtube.com/watch?v=Ey_czmqP1Xs


[231011]
* 피라미딩
* 횡보구간 피하기


[231010]
* 포트폴리오 vs 타이밍
* backtesing.py 좀더 파보자, 파이미팅 position size 변경, size에서 주식수로 하면 안되는 이유, position에서 tp 조정, close 동작, 1시간 봉
* position class 이해하기
* codetrading 참고, stackoverflow 사이트 참고
* 시간
* 키움 연동, next() 호출

(pyramid)
* 총알이 있냐
* trade와 position 바꾸기

(tl 동적 변경)

```
        if len(self.trades) > 0:

            if self.trades[-1].is_long and (price == S1_ExL or price <= self.trades[-1].sl):
                self.trades[-1].close()

            elif self.trades[-1].is_short and (price == S1_ExS or price >= self.trades[-1].sl):
                self.trades[-1].close()
```

(size 주식 수로 주문이 안되는 이유)

```
 def _check_cash_balance(self, shares, price):
        # Checks to see if we have enough cash to make purchase.
        # If not, resizes position to lowest feasible level
        if self.equity <= shares * price:
            shares = np.floor(self.equity / price)
        return shares


```


[231009]
* 백테스트
* 오리지널 터틀 (2% 리스크)
* transaction 분석 vs BT 구현 (code trading, 이헌열)
* 삼중창 구현
* 1시간/5분 백테스트
* 터틀처럼, 한걸음 한걸음, 내 걸음으로


(turtle_orginal_231009v2.1.py)
* transaction 분석, np.where() 함수 활용
* 주요 지표 계산식 검증, 강환국의 할수 있다 퀀트 투자, 보고 싶은 지표
* 월별 수익율 구현, bt
* 즐기기
* 수익률 계산 변경, pct_change(1)
* 기간 줄이기
* 파일 혹은 DB에서 읽기
* 총 테스트 기간(데이터 갯수), 테스트 횟수, 롱숏, 승율, 평균 이익율, 엑셀로 분석
* MDD 이해하기
* 나스닥 1분봉/1시간봉 열추가하기 혹은 1개 종목만 
* 타이밍 bt, run에서 ticker 1개만 돌리기, 혹은 ticker 없이
* 있는거 완벽하게 이해하기, 이것 저것 전선 넓히지 않기, 선택과 집중
* getStratStats -> get_transactions(self) -> 시간단위 변경(1h/1m) 기간 최대 설정 변수 -> 횡보구간 제외시
* backtesting.py 보니까 욕심이 생기네, 하지만 필요한 것만 참조


◇ 다시!! backtesting.py
* 해보자


◇ 다시!! get_transactions()
* show_trades
* # Trades
* Win Rate[%]
* 

◇ 도전!! backtesting.py
* 된다!! 하면된다
* 해보자
* CodeTrading 참고
* 쉬운게 없구나 ㅠㅠ


◇ get_transactions()
* 엑셀로 저장해서 분석, 총거래

trades = sys.get_transactions()

![image](https://github.com/KevinFire2030/251231/assets/109524169/5af6370c-3284-4d82-a88b-f1cfbfdd1f89)


◇ getStratStats
* 있는거 이해하기
* 추가하기, 강환국, 시그널메이커
* 월별 수익율, bt_monthly
* exp
* pandas cumprod() 함수, 누적곱

```py

tats = {}  # Total Returns
    stats['tot_returns'] = np.exp(log_returns.sum()) - 1

    # Mean Annual Returns
    stats['annual_returns'] = np.exp(log_returns.mean() * 252) - 1

    # Annual Volatility
    stats['annual_volatility'] = log_returns.std() * np.sqrt(252)

```



◇ get_portfolio_values(self)
* 포트폴리오 자료 구조 이해하기

![image](https://github.com/KevinFire2030/251231/assets/109524169/dcd7b1a5-ec01-4e6d-974f-99304ae31e51)


![image](https://github.com/KevinFire2030/251231/assets/109524169/e020e4b4-f2ba-4177-829f-ad6438719bde)


![image](https://github.com/KevinFire2030/251231/assets/109524169/bb2dcb7d-a5d4-4558-8b22-e3df9d662158)



```py

    def get_portfolio_values(self):
        vals = []
        for v in self.portfolio.values():
            pv = sum([v1['value'] for v0 in v.values() if type(v0) is dict
                      for k1, v1 in v0.items() if v1 is not None])
            pv += v['cash']
            vals.append(pv)
        return pd.Series(vals, index=self.data.index)
```

◇ 수익률 계산 변경, pct_change(1)
```
# Compare to SPY baseline
    sp500 = yf.Ticker('SPY').history(start=sys.start, end=sys.end)
    sp500['returns'] = sp500['Close'] / sp500['Close'].shift(1)
    sp500['log_returns'] = np.log(sp500['returns'])
    sp500['cum_rets'] = sp500['log_returns'].cumsum()

    sp500['pct_change'] = sp500['Close'].pct_change(1).dropna()
```

![image](https://github.com/KevinFire2030/251231/assets/109524169/60707c4d-5339-46c3-b056-4fea117afffe)




(Trading Indicator Analysis: CHOCH Indicator Python Implementation)


(turtle_orginal_231008v2.0.py)
* 랜덤 5종목, 2000.01.01 - 2023.09.26, 100회

![image](https://github.com/KevinFire2030/251231/assets/109524169/85e9ecfe-c97a-4aa0-924c-a30067b05d44)

[resutl.xlsx](https://github.com/KevinFire2030/251231/files/12842079/resutl.xlsx)



[231008]
* https://covely.tistory.com/20, 코딩 놀이터, 터틀 전략 BackTrader로 백테스팅
* https://raposa.trade/blog/testing-turtle-trading-the-system-that-made-newbie-traders-millions/


(100회 테스트 결과)

행 레이블	평균 : tot_returns
SPY	3.5854
Turtle	11.496062
![image](https://github.com/KevinFire2030/251231/assets/109524169/803c1abc-25d7-478e-b224-17f77ed4330a)


(toutle.py, price 제외)

Ticker Symbols:
	SNA
	REGN
	PEG
	ARE
	NTAP

        tot_returns  annual_returns  ...  max_drawdown  max_drawdown_duration
Turtle       7.9963          0.0972  ...        0.5096                    989
SPY          3.5854          0.0664  ...        0.5519                   2406

Ticker Symbols:
	DHR
	HOLX
	PH
	OGN
	AEP

        tot_returns  annual_returns  ...  max_drawdown  max_drawdown_duration
Turtle      14.7340          0.1234  ...        0.4088                    952
SPY          3.5854          0.0664  ...        0.5519                   2406

Ticker Symbols:
	TMO
	TPR
	EMR
	TEL
	TRV

         tot_returns  annual_returns  ...  max_drawdown  max_drawdown_duration
Turtle       9.1459          0.1028  ...        0.6249                   1756
SPY          3.5854          0.0664  ...        0.5519                   2406


Ticker Symbols:
	BX
	STLD
	MTD
	KR
	SYF

         tot_returns  annual_returns  ...  max_drawdown  max_drawdown_duration
Turtle      25.3087          0.1480  ...        0.4523                   1727
SPY          3.5854          0.0664  ...        0.5519                   2406


![image](https://github.com/KevinFire2030/251231/assets/109524169/4d4542f9-8e0c-4a60-b62d-abe9732d1561)


Ticker Symbols:
	TGT
	HIG
	CMA
	J
	CRM

         tot_returns  annual_returns  ...  max_drawdown  max_drawdown_duration
Turtle      14.4227          0.1224  ...        0.5819                   1114
SPY          3.5854          0.0664  ...        0.5519                   2406

![image](https://github.com/KevinFire2030/251231/assets/109524169/e76b2af3-fd4e-4d69-b0ae-b0d442b55a58)


[231007]
* 듀얼 모멘텀 전략, 소나기 피하기, 횡보시 거래 중지 (혹은 평균회귀 전략)
* 일정 속도 이상일때만


[231003]
* yfinance data 엑셀 파일로 저장, 읽고 쓰기, 파일 이름 규칙 정하기
* 파이썬으로 데이터 가공이 어렵다면 엑셀로 데이터 가공, 예) ticker 하나만 읽어오기
* 강환국, 할수 있다! 퀀트 투자, 생각에 관한 생각
* 제시리버모어의 회상
* tutle vs turtle_231002v1.6 성과 비교
* trend 컬럼 추가, 1,0,-1, 삼중창 시스템 응용
* SPY vs SPY 터틀, ticker =1, 엑셀 vs 코딩
* unit_limit, 선물의 경우, 증거금으로 계산
* MDD 기간도 같이 표시, 초기인지 판단하기 위해


(SPY vs SPY 터틀, ticker =1, 엑셀 vs 코딩)
* turtle_231004v1.7
* 1d, 1m, max

* SPY 컬럼 추가

* yfObj = yf.Tickers(tickers), QQQ 삭제 

![image](https://github.com/KevinFire2030/251231/assets/109524169/717d1ed2-eb1f-44d3-90d6-cc247672314f)


![image](https://github.com/KevinFire2030/251231/assets/109524169/5af04196-4e63-4040-8d11-85650ea9b606)



(tutle vs turtle_231002v1.6 성과 비교)  
* 리스크 크기__turtle_231002v1.5 vs 투자금액_turtle_231002v1.6

```py

    def _size_position(self, data, dollar_units):

        #self.dollars_per_point
        shares = np.floor(dollar_units / (
                self.risk_level * data['N'] * data['Close']))

        #shares = np.floor(dollar_units / (
        #        self.risk_level * data['N'] * self.dollars_per_point))

        return shares
```

![image](https://github.com/KevinFire2030/251231/assets/109524169/35b8f2f1-93ee-410d-99e7-f7bfd584aab6)

        tot_returns  annual_returns  ...  max_drawdown  max_drawdown_duration
Turtle       2.8189          0.0587  ...        0.6895                   1790
SPY          3.5854          0.0664  ...        0.5519                   2406


[231002]
* 포지션 크기 결정
* 마크다운 다시 보기
* 유닛 크기, 1회당 투자금액이 아닌 1회당 손실 크기 결과 정리
* 통계, F, 승률, 손실대비이익 비율, 총 거래횟수, 이익거래 횟수, 손실거래 횟수
* 월별 수익률, 연간 수익률, 피벗
* 티커 하나일때 get_data, 시간봉, 분봉
* 시스템 vs Buy&Hold 비교
* 변동성 이해하기, TQQQ/SQQQ vs QQQ vs NQ vs NQ=F, 변동성 x 포인트당 달러가치
* 변동성 이해하기, 시초가 갭상승, 갭하락, 특히 코스피200, 나스닥100 비는 1시간
* 코스닥200 선물 데이터 읽기
* unit_limit=5, 자동으로 계산하기, 선물 증거금, 나스닥100, 코스피200
* self.sys_list = ['S1', 'S2'] , S2에 다른 전략(삼중창) 구현하기, 시스템수 늘리기 S3 = 볼린저 벤드
* backtesting.py로 돌리기
* backtesting.py 통계자료 포멧



(turtle_231002v1.6)  
* 승률, 총 거래 횟수, 손실 횟수, 이익 횟수
* 수익/손실률, 캘리의 법칙 VS 2n 손절
* 액셀 피벗으로 월별 손익률 구하기
* * backtesting.py 통계자료 포멧
 
(backtesting.py)
https://kernc.github.io/backtesting.py/

![image](https://github.com/KevinFire2030/251231/assets/109524169/f44c4b4f-0753-4608-ba71-4aedd5fac065)

![image](https://github.com/KevinFire2030/251231/assets/109524169/4119d7d3-294a-4ac0-b54b-c4886fc6f550)

  
(turtle_231002v1.5)  

* 백테스팅 결과
1. 시장 선택: 주식, 3종목 (APPL, MSFT, AMZN)
2. 기간: 2000.01.01 ~ 2023.09.26
3. 유닛 크기를 투자금에서 리스크로 변경 (계정의 1%, 투자금 VS 리스크)

![image](https://github.com/KevinFire2030/251231/assets/109524169/9875f6a6-a98e-480d-98c3-24f5b6c48309)


![image](https://github.com/KevinFire2030/251231/assets/109524169/6983a667-2533-4b00-a8a0-e9b57ff0dcf1)


![image](https://github.com/KevinFire2030/251231/assets/109524169/1f3030f4-bd7c-439c-980f-d0528e515bda)
 
![image](https://github.com/KevinFire2030/251231/assets/109524169/702db17e-bb03-4114-9eb4-f11178d21f3d)



[230927]
* 리스크 관리 규칙과 코드 점검

(turtle_230927v1.4)
* 리스크 관리
* 단위, 수량 점검
* 포인트당 달러 가치 (틱벨류) 변수만 추가, 레버리지, 일단 추가만, 단위 크기 동작 이해하고 활용
* 초기 cash 에 따라 결과가 달라지는 이유 (1E4, 1E5, 1E6)
* breakout은 == 아니고 >= 혹은 <=
* 가격이 왜 소수 4자리? 표시는 소주 2자리네 어쨌든
* 변동성만 보면 가격이 비싼 놈의 변동성(ATR)과 싼 놈의 변동성이 같다고 볼수 없다
* 따라서, 가격당 변동성, 다시말해 변동률이 필요하다
* ATR_R = ART / Price
* 피라미딩 단위 0.5(=1/2) * N

* 선물

  ![image](https://github.com/KevinFire2030/251231/assets/109524169/421e8d11-8dd8-4199-9385-a96dd18f2fb3)


 ![image](https://github.com/KevinFire2030/251231/assets/109524169/50076e3d-2cb1-4332-b324-ff8b93420e5e)


* 포트폴리오 수
![image](https://github.com/KevinFire2030/251231/assets/109524169/c0a91f13-61fb-4a5a-864f-c1fb70263625)


* 켈리의 공식

https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=bryankim1225&logNo=220550843446

![image](https://github.com/KevinFire2030/251231/assets/109524169/83ce64b5-d816-4e65-9c6a-e1e0587cd61d)


![image](https://github.com/KevinFire2030/251231/assets/109524169/66e14ca9-430e-4252-a60a-e32acc24bd88)

켈리 공식 계산기
https://fical.net/ko/%EC%BC%88%EB%A6%AC-%EA%B3%B5%EC%8B%9D-%EA%B3%84%EC%82%B0%EA%B8%B0



```

np.floor

https://wikidocs.net/193711

np.floor(), np.round(), np.ceil()
np.floor() 함수는 주어진 숫자를 내림하여 정수로 반환하는 함수입니다. 즉, 소수점 이하를 버리고 정수 부분만 남깁니다.

import numpy as np

x = np.array([1.23, 4.56, 7.89])
y = np.floor(x).astype(int)  # y = [1, 4, 7]
반올림하는 함수는 np.round() 함수이며, 이 함수는 주어진 숫자를 반올림하여 정수 또는 소수점 이하 n자리까지 반올림하여 반환합니다. 예를 들어, np.round(3.141592, 2)는 소수점 이하 두 자리까지 반올림하여 3.14를 반환합니다.

주어진 숫자를 무조건 올림하는 함수는 np.ceil() 함수입니다. np.ceil() 함수는 인수로 받은 숫자를 올림하여 반환합니다. 예를 들어, np.ceil(3.141592)는 4.0을 반환합니다.

```



* breakout은 == 아니고 >= 혹은 <=, 다시 보니 == 이거네
![image](https://github.com/KevinFire2030/251231/assets/109524169/6b3968b9-12a1-4333-9a96-e73ba167fe88)


 ![image](https://github.com/KevinFire2030/251231/assets/109524169/4b9fa383-6832-428c-a5f6-390052450491)


![image](https://github.com/KevinFire2030/251231/assets/109524169/17e2aff8-eccb-4186-9d0d-2fefd81425c3)


![image](https://github.com/KevinFire2030/251231/assets/109524169/cb30209a-1b3b-4d61-bfb9-0ded0f4eb461)

![image](https://github.com/KevinFire2030/251231/assets/109524169/3b57ce4e-ff51-45bc-85cc-3c79f68138cd)


deepcopy
![image](https://github.com/KevinFire2030/251231/assets/109524169/5da4639e-04fd-44d4-90ba-9f7083346f12)


마소
![image](https://github.com/KevinFire2030/251231/assets/109524169/fe882e95-f297-4f04-91fb-74d1ef69bfe5)


![image](https://github.com/KevinFire2030/251231/assets/109524169/daed6513-d561-45f6-9a62-ae5eea9e43d8)

![image](https://github.com/KevinFire2030/251231/assets/109524169/dfc5cec0-5360-4f07-b7dc-45abeeb4297d)


```py

    def _run_system(self, ticker, data, position, system=1):
        S = system  # System number
        price = data['Close']
        if np.isnan(price):
            # Return current position in case of missing data
            return position
        N = data['N']
        dollar_units = self._get_units(S)
        shares = 0
        if position is None:
            if price >= data[f'S{S}_EL']:  # Buy on breakout
                if S == 1 and self.last_s1_win[ticker]:
                    self.last_s1_win[ticker] = False
                    return None
                shares = self._size_position(data, dollar_units)
                stop_price = price - self.risk_level * N
                long = True
            elif self.shorts:
                if price <= data[f'S{S}_ES']:  # Sell short
                    if S == 1 and self.last_s1_win[ticker]:
                        self.last_s1_win[ticker] = False
                        return None
                    shares = self._size_position(data, dollar_units)
                    stop_price = price + self.risk_level * N
                    long = False
            else:
                return None
            if shares == 0:
                return None
            # Ensure we have enough cash to trade
            shares = self._check_cash_balance(shares, price)
            value = price * shares

            self.cash -= value
            position = {'units': 1,
                        'shares': shares,
                        'entry_price': price,
                        'stop_price': stop_price,
                        'entry_N': N,
                        'value': value,
                        'long': long}
            if np.isnan(self.cash) or self.cash < 0:
                raise ValueError(f"Cash Error\n{S}-{ticker}\n{data}\n{position}")

        else:
            if position['long']:
                # Check to exit existing long position
                if price <= data[f'S{S}_ExL'] or price <= position['stop_price']:
                    self.cash += position['shares'] * price
                    if price >= position['entry_price']:
                        self.last_s1_win[ticker] = True
                    else:
                        self.last_s1_win[ticker] = False
                    position = None
                # Check to pyramid existing position
                elif position['units'] < self.unit_limit:
                    if price >= position['entry_price'] + position['entry_N']:
                        shares = self._size_position(data, dollar_units)
                        shares = self._check_cash_balance(shares, price)
                        self.cash -= shares * price
                        stop_price = price - self.risk_level * N
                        avg_price = (position['entry_price'] * position['shares'] +
                                     shares * price) / (position['shares'] + shares)
                        position['entry_price'] = avg_price
                        position['shares'] += shares
                        position['stop_price'] = stop_price
                        position['units'] += 1
            else:
                # Check to exit existing short position
                if price >= data[f'S{S}_ExS'] or price >= position['stop_price']:
                    self.cash += position['shares'] * price
                    if S == 1:
                        if price <= position['entry_price']:
                            self.last_s1_win[ticker] = True
                        else:
                            self.last_s1_win[ticker] = False
                    position = None
                # Check to pyramid existing position
                elif position['units'] < self.unit_limit:
                    if price <= position['entry_price'] - position['entry_N']:
                        shares = self._size_position(data, dollar_units)
                        shares = self._check_cash_balance(shares, price)
                        self.cash -= shares * price
                        stop_price = price + self.risk_level * N
                        avg_price = (position['entry_price'] * position['shares'] +
                                     shares * price) / (position['shares'] + shares)
                        position['entry_price'] = avg_price
                        position['shares'] += shares
                        position['stop_price'] = stop_price
                        position['units'] += 1

            if position is not None:
                # Update value at each time step
                position['value'] = position['shares'] * price

        return position


```



```
f-string 포맷팅
if price == data[f'S{S}_ES']:  # Sell short
```

[230926]
* 다양성, 단순성, 일관성, 겸손
* 다양성, 시장 선택시 일정 조건을 만족하는 것 중에서 랜덤하게 선택하기
* 단순성, 진입시 상위 단위로 추세판단, 횡보일때는 미진입 (예 주봉에서 12중 평균선, 쩐의 흐름을 타라)
* Tickers 에서 하나만 선택
* 전체적인 흐름 이해, 디버깅 모드로 한 스탭씩 따라 가면서, 자료 구조와 흐름(논리) 따라가기
* 모투 전에, 충분한 검증, 시간단위 별
* 코드가 터틀의 규칙을 잘 반영하고 있는지 검증 (예 dollar_unit 계산, 주식과 선물 모두 적용 가능한가)
* README 가 개발 일지가 될수 있도록 자세히? 기록하기
* 마크다운 문법 공부
* 10000$에서 거래가 일어나지 않는 이유 알아내기 (APPL, MSFT)
* 24년 경영계획, 수입/지출/저축, 월별/항목별, 원하는 수준 결정하기, 네비게이션 현재위치 파악
* 나는 25년 12월 31일 은퇴했다, 선우와 선우 동생과 더 많은 시간을 보내기 위해
* 이모 청소 부탁, 1-3회, 선우 하원전
* 개인연금, 퇴직연금, 퇴직금, 터틀 규칙으로 메뉴얼 투자하기, 진입/청산/손절 표 만들기
* APPL/Close/High/Low 접근 (읽고/쓰기) 방법

(turtle_230927v1.4)
* 리스크 관리
* 단위, 수량 점검

  


(230926v1.2)
* 코드 따라 가기 run
* nan 제거하기
* enumerate
* iterrows
* print(f"{index=}, {row.age=}, {row['sex']=}")
* deepcopy
* np.log





```
3. f-string 포맷팅 _ 직관적으로 알 수 있다
something = '볼펜'
EA = 2
one_length = 5.343
scale = 'cm'

print(f'{something} {EA}개의 길이는 {one_length*EA}{scale} 입니다.')
print(f'{something} {EA}개의 길이는 {one_length*EA:.1f}{scale} 입니다.')


for i, (index, row) in enumerate(df.iterrows()):
    print(f"{i}, {index}, {row.age}, {row['sex']}")    
    
0, 315, adults, women
1, 1304, child, women
2, 318, adults, women
3, 342, adults, man
4, 1260, child, man


```


```

for i, (index, row) in df.iterrows():
    print(f"{i=}, {index=}, {row.age=}, {row['sex']=}")
    
Traceback (most recent call last):
  File "C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.2\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
ValueError: too many values to unpack (expected 2)


for i, (index, row) in enumerate(df.iterrows()):
    print(f"{i=}, {index=}, {row.age=}, {row['sex']=}")  
  
    
i=0, index=315, row.age='adults', row['sex']='women'
i=1, index=1304, row.age='child', row['sex']='women'
i=2, index=318, row.age='adults', row['sex']='women'
i=3, index=342, row.age='adults', row['sex']='man'
i=4, index=1260, row.age='child', row['sex']='man'


```
  

```
https://bio-info.tistory.com/149

2) iterrows 행 반복
for index, row in df.iterrows():
    print(f"{index=}, {row.age=}, {row['sex']=}")
* 코드 설명

df.iterrows()를 사용하면 각 행별로 index와 row(시리즈 형태)를 반복합니다. index는 데이터프레임의 index값이고, row는 시리즈기 때문에 row.age처럼 점(.)을 통해 age 열에 접근할 수 있고, row['sex']처럼 리스트 형태로 sex 열에 접근할 수도 있습니다.
```


```
https://www.daleseo.com/python-enumerate/
[팁] 2차원 리스트 루프
이제 enumerate() 함수의 작동 원리까지 배웠으니 좀 더 고급 응용 사례를 살펴볼까요?

아래와 같은 2차원 리스트나 튜플이 담고 있는 데이터를 루프를 돌면서 접근해야한다고 가정해봅시다.

>>> matrix = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
이 때 일반적으로 다음과 같이 중첩 for 문 내에서 행과 열의 인덱스로 데이터를 읽도록 작성을 많이 하실 거에요.

>>> for r in range(len(matrix)):
...     for c in range(len(matrix[r])):
...             print(r, c, matrix[r][c])
...
0 0 A
0 1 B
0 2 C
1 0 D
1 1 E
1 2 F
2 0 G
2 1 H
2 2 I
동일한 작업을 하는 코드를 enumerate() 함수를 이용해서 재작성하면 어떨까요?

>>> for r, row in enumerate(matrix):
...     for c, letter in enumerate(row):
...             print(r, c, letter)
...
0 0 A
0 1 B
0 2 C
1 0 D
1 1 E
1 2 F
2 0 G
2 1 H
2 2 I

```
  
  

(230926v1.1)
* Tickers 에서 하나만 선택
* 하나 이상, 아니면 KeyError

  ```
  
tickers = ["NQ=F",""]


yfObj = yf.Tickers(tickers)

df_1d = yfObj.history(start="2023-09-20", end="2023-09-25", interval='1d')

```


[230926]
* 코드 이해 하기
* turtle_230926v1.3



* position

![image](https://github.com/KevinFire2030/251231/assets/109524169/6a67f669-bbff-413c-894a-c8dd60721c2f)
  
```python

    def run(self):
        # Runs backtest on the turtle strategy
        self.portfolio = {}
        position = {s:
                        {t: None for t in self.tickers}
                    for s in self.sys_list}

```


* N

  ![image](https://github.com/KevinFire2030/251231/assets/109524169/6bf34929-b44c-4a39-b931-85afb0f4db82)


*   data_2309260125.xlsx
![image](https://github.com/KevinFire2030/251231/assets/109524169/2f040d74-f344-4379-8f0e-66b4cfd298ff)






[230925]




* turtle w/ SPY vs SPY
* 일/시간/분 데이터 읽기

https://www.qmr.ai/yfinance-library-the-definitive-guide/

![image](https://github.com/KevinFire2030/251231/assets/109524169/95ca6e74-3c50-4cdd-96dd-19e5b5d90e13)


```

tickers = ["NQ=F", "ES=F"]

#appl = yf.Ticker("APPL")
#hist = appl.history(start="2023-09-01", end="2023-09-25", interval='1h')

yfObj = yf.Tickers(tickers)
#df = yfObj.history(start=self.start, end=self.end, interval='1h', back_adjust=True, auto_adjust=True, prepost=True)
df_1m = yfObj.history(start="2023-09-20", end="2023-09-25", interval='1m')
df_2m = yfObj.history(start="2023-09-20", end="2023-09-25", interval='2m')
df_5m = yfObj.history(start="2023-09-20", end="2023-09-25", interval='5m')
df_15m = yfObj.history(start="2023-09-20", end="2023-09-25", interval='15m')
df_30m = yfObj.history(start="2023-09-20", end="2023-09-25", interval='30m')
df_60m = yfObj.history(start="2023-09-20", end="2023-09-25", interval='60m')
df_90m = yfObj.history(start="2023-09-20", end="2023-09-25", interval='90m')
df_1h = yfObj.history(start="2023-09-20", end="2023-09-25", interval='1h')
df_1d = yfObj.history(start="2023-09-20", end="2023-09-25", interval='1d')
df_5d = yfObj.history(start="2023-09-20", end="2023-09-25", interval='5d')
df_1wk = yfObj.history(start="2023-01-20", end="2023-09-25", interval='1wk')
df_1mo = yfObj.history(start="2023-01-20", end="2023-09-25", interval='1mo')
df_3mo = yfObj.history(start="2023-01-20", end="2023-09-25", interval='3mo')
#df_1y = yfObj.history(start="2020-09-20", end="2023-09-25", interval='1y')

```



* (v1.3)
* yfince_test_230925v1.3
* 흐름도
* SPY, QQQ
* 선물
* 
* ValueError: Excel does not support datetimes with timezones. Please ensure that datetimes are timezone unaware before writing to Excel.


https://pypi.org/project/yfinance/

일/주/월/분기 봉 등과  1분/2분/5분/15분/30분/60분/90분 봉, 생략하면 '1d'가 default

1/2/5/15/30m 1h 1d 1w 1mo 1y



[230924]
230923v1.1
100회 테스트, 100회 평균
총거래회수, 수익거래횟수, 손실거래 횟수

230924v1.2
turtle w/ SPY vs SPY
