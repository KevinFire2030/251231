
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
