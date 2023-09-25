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

data2 = yf.download("SPY", start="2022-05-01", end="2022-05-03")


print("25년 12월 25일 은퇴했다")