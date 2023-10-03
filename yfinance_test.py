import yfinance as yf
import pandas_datareader.data as web

"""
ticker = 'AY'
net = yf.Ticker(ticker)

start_date, end_date = '2020-11-06', '2020-11-07'
daily_signals_df = net.history(start=start_date, end=end_date, interval='1d', back_adjust=True, auto_adjust=True, prepost=False)
hourly_signals_df = net.history(start=start_date, end=end_date, interval='1h', back_adjust=True, auto_adjust=True, prepost=True)

print(daily_signals_df)

print(hourly_signals_df)
"""

#data = yf.download("AAPL", start="2022-05-01", end="2022-05-03",  interval = "1m")

#data2 = yf.download("SPY", start="2022-05-01", end="2022-05-03")

#주식
"""
tickers = ["AAPL", "MSFT", "AMZN"]

yfObj = yf.Tickers(tickers)
#df = yfObj.history(start=self.start, end=self.end, interval='1h', back_adjust=True, auto_adjust=True, prepost=True)
df = yfObj.history(start="2023-09-01", end="2023-09-25")
df.drop(['Open', 'Dividends', 'Stock Splits', 'Volume'], inplace=True, axis=1)
df.ffill(inplace=True)
df = df.swaplevel(axis=1)

df.to_excel('data2.xlsx')

"""
#ETF
"""
tickers = ["SPY", "QQQ"]

yfObj = yf.Tickers(tickers)
#df = yfObj.history(start=self.start, end=self.end, interval='1h', back_adjust=True, auto_adjust=True, prepost=True)
df = yfObj.history(start="2023-09-01", end="2023-09-25")
df.drop(['Capital Gains', 'Open', 'Dividends', 'Stock Splits', 'Volume'], inplace=True, axis=1)
df.ffill(inplace=True)
df = df.swaplevel(axis=1)

df.to_excel('data4.xlsx')
"""

#선물
"""
tickers = ["NQ=F", "ES=F"]

yfObj = yf.Tickers(tickers)
#df = yfObj.history(start=self.start, end=self.end, interval='1h', back_adjust=True, auto_adjust=True, prepost=True)
df = yfObj.history(start="2023-09-01", end="2023-09-25")
#df.drop(['Capital Gains', 'Open', 'Dividends', 'Stock Splits', 'Volume'], inplace=True, axis=1)
df.drop(['Open', 'Dividends', 'Stock Splits', 'Volume'], inplace=True, axis=1)
df.ffill(inplace=True)
df = df.swaplevel(axis=1)

df.to_excel('data5.xlsx')
"""
"""
tickers = ["NQ=F", "ES=F"]

yfObj = yf.Tickers(tickers)
#df = yfObj.history(start=self.start, end=self.end, interval='1h', back_adjust=True, auto_adjust=True, prepost=True)
df = yfObj.history(start="2023-09-01", end="2023-09-25", interval='1h')
#df.drop(['Capital Gains', 'Open', 'Dividends', 'Stock Splits', 'Volume'], inplace=True, axis=1)
df.drop(['Open', 'Dividends', 'Stock Splits', 'Volume'], inplace=True, axis=1)
df.ffill(inplace=True)
df = df.swaplevel(axis=1)

#df.to_excel('data6.xlsx')
"""

"""
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


#df = yfObj.history(start="2023-09-01", end="2023-09-25", interval='5m')
#df.drop(['Capital Gains', 'Open', 'Dividends', 'Stock Splits', 'Volume'], inplace=True, axis=1)
#df.drop(['Open', 'Dividends', 'Stock Splits', 'Volume'], inplace=True, axis=1)
#df.ffill(inplace=True)
#df = df.swaplevel(axis=1)

#df.to_excel('data6.xlsx')

"""

tickers = ["NQ=F",""]


yfObj = yf.Tickers(tickers)

df_1d = yfObj.history(start="2023-09-20", end="2023-09-25", interval='1d')

print("나는 25년 12월 31일 은퇴했다")