import sys

import pandas as pd
import numpy as np

import time as t

import telegram
import asyncio

import platform
if platform.system()=='Windows':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

token = "5896631247:AAFY3galrUXBRnIjgzkKnknn7FBk16gFkGI"
chat_id = 5440299023

from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from window import Window
from datetime import datetime

import pandas_ta as ta
#import ta_py as ta2
import finta as ta2

import matplotlib.pyplot as plt
from mplfinance.original_flavor import candlestick_ohlc

from backtesting import Strategy
from backtesting import Backtest

import warnings

warnings.filterwarnings(action='ignore')
#warnings.filterwarnings(action='default')






class Kiwoom(QAxWidget, QMainWindow):

    def __init__(self):
        super().__init__()
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")
        self.OnEventConnect.connect(self.on_event_connect)
        self.OnReceiveTrData.connect(self.on_receive_tr_data)
        self.OnReceiveRealData.connect(self.on_receive_real_data)
        self.OnReceiveMsg.connect(self.on_receive_msg)
        self.OnReceiveChejanData.connect(self.on_receive_chejan_data)

        self.screen_number = 1000
        self.account_numbers = []
        self.tick_unit = {}
        self.tick_count = 0
        self.code_symbol = "101TC000"

        self.cnt = 0
        self.basis_tick_unit = 120
        self.basis_time_unit = 0


        self.current_minute_dt = 0
        self.current_minute_close = 0
        self.current_minute_high = 0
        self.current_minute_low = 0
        self.current_minute_open = 0
        self.current_minute_volume = 0

        self.current_tick_dt = 0
        self.current_tick_close = 0
        self.current_tick_high = 0
        self.current_tick_low = 0
        self.current_tick_open = 0
        self.current_tick_volume = 0

        self.target_minute_index = -1
        self.target_minutes = [1, 3, 5, 15, 30]
        self.minute_1_range = [str(minute).zfill(2) for minute in range(0, 60)]
        self.minute_3_range = [str(minute).zfill(2) for minute in range(0, 60, 3)]
        self.minute_5_range = [str(minute).zfill(2) for minute in range(0, 60, 5)]
        self.minute_15_range = [str(minute).zfill(2) for minute in range(0, 60, 15)]
        self.minute_30_range = [str(minute).zfill(2) for minute in range(0, 60, 30)]
        self.current_minute = None


        self.current_position = 0
        self.quantity = 1
        self.sl_points = 0
        self.tp_points = 0
        self.sl_price = 0
        self.tp_price = 0
        self.entry_price = 0

        self.min_bars = pd.DataFrame(columns=['date_time', 'Open', 'High', 'Low', 'Close', 'Volume'])
        self.tick_bars = pd.DataFrame(columns=['date_time', 'Open', 'High', 'Low', 'Close', 'Volume'])

        self.login()

    # login
    def login(self):
        self.dynamicCall('CommConnect()')

    def get_login_info(self):
        self.account_numbers = self.dynamicCall('GetLoginInfo(QString)', 'ACCNO').split(';')


    # Event Handler
    def on_event_connect(self, err_code):
        if err_code == 0:
            print('Successfully login')
            # self.get_global_future_code_list()
            self.get_login_info()
        else:
            print('Failed login')

    def on_receive_tr_data(self, sScrNo, sRQName, sTrCode, sRecordName, sPrevNext):

        print('== on_receive_tr_data ==')

        if sRQName == '선물분차트조회':
            print('선물분차트조회')

            current_time = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName,
                                                         0, "체결시간").strip()
            self.current_minute = current_time[10:12]

            self.current_minute_dt = pd.to_datetime(current_time)

            self.current_minute_close = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName,
                                                         0, "현재가").strip()
            self.current_minute_close = abs(round(float(self.current_minute_close), 2))

            self.current_minute_open = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName,
                                                        0, "시가").strip()
            self.current_minute_open = abs(round(float(self.current_minute_open), 2))

            self.current_minute_low = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName,
                                                       0,
                                                       "저가").strip()
            self.current_minute_low = abs(round(float(self.current_minute_low), 2))

            self.current_minute_high = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName,
                                                        0, "고가").strip()
            self.current_minute_high = abs(round(float(self.current_minute_high), 2))

            self.current_minute_volume = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName,
                                                          0, "거래량").strip()
            self.current_minute_volume = abs(int(self.current_minute_volume))

            rows = self.dynamicCall("GetRepeatCnt(QString, QString)", sTrCode, sRQName)

            for i in range(1, rows):
                dt = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i,
                                      "체결시간").strip()
                date_time = pd.to_datetime(dt)

                open = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i,
                                        "시가").strip()
                open = abs(round(float(open), 2))

                high = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i,
                                        "고가").strip()
                high = abs(round(float(high), 2))

                low = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i,
                                       "저가").strip()
                low = abs(round(float(low), 2))

                close = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i,
                                         "현재가").strip()
                close = abs(round(float(close), 2))

                volume = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i,
                                          "거래량").strip()
                volume = abs(int(volume))

                new_bar = pd.DataFrame(
                    {'date_time': date_time, 'Open': open, 'High': high, 'Low': low, 'Close': close,
                     'Volume': volume}, index=[0])

                self.min_bars = pd.concat([new_bar, self.min_bars], ignore_index=True)


            self.min_bars.to_csv('utils\분차트_900_kr.csv', index=None)

            print("선물분차트조회 끝!")


        if sRQName == '선물틱차트조회':

            print('선물틱차트조회')


            tick_count = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, 0, "마지막틱갯수").strip()
            #code_name = sPrevNext.split(' ')[0][2:] # code_name에서 F0은 제거한다.
            self.tick_count = int(tick_count)

            print("last_tick_count: ", self.tick_count)

            current_time = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, 0, "체결시간").strip()

            self.current_tick_dt = pd.to_datetime(current_time)

            self.current_tick_close = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, 0, "현재가").strip()
            self.current_tick_close = abs(round(float(self.current_tick_close), 2))

            self.current_tick_open = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, 0, "시가").strip()
            self.current_tick_open = abs(round(float(self.current_tick_open), 2))

            self.current_tick_low = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, 0, "저가").strip()
            self.current_tick_low = abs(round(float(self.current_tick_low), 2))

            self.current_tick_high = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, 0, "고가").strip()
            self.current_tick_high = abs(round(float(self.current_tick_high), 2))

            self.current_tick_volume = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, 0, "거래량").strip()
            self.current_tick_volume = abs(round(float(self.current_tick_volume), 2))

            if self.tick_count == 0:

                new_tick = pd.DataFrame(
                    {'date_time': current_time, 'Open': self.current_tick_open,
                     'High': self.current_tick_high,
                     'Low': self.current_tick_low, 'Close': self.current_tick_close,
                     'Volume': self.current_tick_volume}, index=[0])

                self.tick_bars = pd.concat([self.tick_bars, new_tick], ignore_index=True)

                #print("tick_count==0")
                #print(self.tick_bars.tail(1))
                #print('== on_receive_tr_data == end')

                # 초기화
                self.current_tick_open = 0
                self.current_tick_high = 0
                self.current_tick_low = 10000000
                self.current_tick_close = 0
                self.current_tick_volume = 0



            rows = self.dynamicCall("GetRepeatCnt(QString, QString)", sTrCode, sRQName)

            for i in range(1, rows):

                current_time = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i,
                                                "체결시간").strip()

                tick_dt = pd.to_datetime(current_time)

                close_price = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i, "현재가").strip()
                close_price = abs(round(float(close_price), 2))

                open_price = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i, "시가").strip()
                open_price = abs(round(float(open_price), 2))

                low_price = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i, "저가").strip()
                low_price = abs(round(float(low_price), 2))

                high_price = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i, "고가").strip()
                high_price = abs(round(float(high_price), 2))

                volume = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode,
                                                            sRQName, i, "거래량").strip()
                volume = abs(int(volume))

                new_tick = pd.DataFrame(
                    {'date_time': tick_dt, 'Open': open_price, 'High': high_price, 'Low': low_price, 'Close': close_price, \
                     'Volume': volume}, index=[0])

                self.tick_bars = pd.concat([new_tick, self.tick_bars], ignore_index=True)

            self.tick_bars.to_csv('utils\틱차트_900_kr.csv', index=None)

            print("선물틱차트조회 끝!")

        if sRQName == '선물틱차트연속조회':

            print('선물틱차트연속조회')

            self.cnt = self.cnt + 1

            print("[선물틱차트연속조회] %d" % (self.cnt))

            if self.cnt == 1000:

                print("선물틱차트연속조회 1000회!")
                self.tick_bars.to_csv('ticks.csv', index=None)
                return

            tick_count = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, 0, "마지막틱갯수").strip()
            print("last_tick_count: ", tick_count)

            rows = self.dynamicCall("GetRepeatCnt(QString, QString)", sTrCode, sRQName)

            print(rows)

            for i in range (rows):


                current_time = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i, "체결시간").strip()

                dt = pd.to_datetime(current_time)

                open = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i,
                                        "시가").strip()
                open = abs(round(float(open), 3))

                high = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i,
                                        "고가").strip()
                high = abs(round(float(high), 3))

                low = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i, "저가").strip()
                low = abs(round(float(low), 3))

                close = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i, "현재가").strip()
                close = abs(round(float(close), 3))

                volume = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i, "거래량").strip()
                volume = abs(round(float(volume), 3))


                new_tick = pd.DataFrame(
                    {'date_time': dt, 'Open': open, 'High': high, 'Low': low, 'Close': close, 'Volume': volume}, index=[0])

                self.tick_bars = pd.concat([self.tick_bars, new_tick], ignore_index=True)

            if sPrevNext == 0:
                print("선물틱차트연속조회 끝!")

                self.ticks.to_csv('ticks.csv', index = None)

            else:
                # 틱데이터 받기
                self.dynamicCall("SetInputValue(QString, QString)", "종목코드", self.code_symbol)
                self.dynamicCall("SetInputValue(QString, QString)", "시간단위", self.basis_tick_unit)
                self.dynamicCall("CommRqData(QString, QString, QString, QString)", "선물틱차트연속조회", "OPT50028", 2, "2004")




        if sRQName == '미결제잔고내역조회':
            print(sRQName)
            rows = self.dynamicCall("GetRepeatCnt(QString, QString)", sTrCode, sRQName)

            if rows == 0:
                self.current_position = 0

            for i in range(rows):
                code = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i,"종목코드").strip()
                buy_or_sell = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i, "매매구분").strip()  # buy:2 , sell: 1
                quantity = self.dynamicCall("GetCommData(QString, QString, int, QString)", sTrCode, sRQName, i, "잔고수량").strip()

                if buy_or_sell == '매수':
                    self.set_position(2)
                elif buy_or_sell == '매도':
                    self.set_position(1)
            #print('current position: ' + str(self.current_position))



    def on_receive_real_data(self, sCode, sRealType, sRealData):

        #if sRealType == '선물시세':

        #print(sRealData)
        #print(sRealData)
        if sRealType == '선물시세':
            if self.basis_tick_unit > 0:
                self.get_tick_data(sCode, sRealType, sRealData)
            elif self.basis_time_unit > 0:
                self.get_time_data(sCode, sRealType, sRealData)


    def on_receive_msg(self, screen_number, rq_name, tr_code, msg):
        #pass
        print('== on_receive_msg ==')
        #print(screen_number)
        #print(rq_name)
        #print(tr_code)
        print(msg)

    def on_receive_chejan_data(self, sGubun, nItemCnt, sFidList):
        #pass
        # self.get_current_position()
        print('== on_receive_chejan_data ==')
        print(sGubun)
        print(nItemCnt)
        print(sFidList)

    # functions
    def get_tick_data(self, sCode, sRealType, sRealData):

        trade_time = self.dynamicCall("GetCommRealData(QString, int)", sCode, 20)  # 체결 시간
        #trade_date = self.dynamicCall("GetCommRealData(QString, int)", sCode, 22)  # 체결 일자
        trade_date = t.strftime('%Y%m%d')
        time = trade_date + trade_time

        current_price = self.dynamicCall("GetCommRealData(QString, int)", sCode, 10)  # 현재가(체결가)
        current_price = abs(float(current_price))

        current_volume = self.dynamicCall("GetCommRealData(QString, int)", sCode, 15)  # 체결량
        current_volume = abs(int(current_volume))

        # 새로운 틱켄들이 시작되면 기존 틱켄들 추가

        self.tick_count = self.tick_count + 1

        # 틱 데이터 저장, 체결 일시, 현재가, 체결량

        # 기존 틱켄들 업데이트

        if self.tick_count == 1:
            self.current_tick_open = current_price
            self.current_tick_dt = pd.to_datetime(time)

        if self.current_tick_high < current_price:
            self.current_tick_high = current_price

        if self.current_tick_low > current_price:
            self.current_tick_low = current_price

        self.current_tick_close = current_price

        self.current_tick_volume = self.current_tick_volume + current_volume

        if self.tick_count == self.basis_tick_unit:

            new_tick = pd.DataFrame(
                {'date_time': self.current_tick_dt, 'Open': self.current_tick_open,
                 'High': self.current_tick_high,
                 'Low': self.current_tick_low, 'Close': self.current_tick_close,
                 'Volume': self.current_tick_volume}, index=[0])

            self.tick_bars = pd.concat([self.tick_bars, new_tick], ignore_index=True)

            #print(self.tick_bars.tail(1))

            # trade
            self.trade(sCode, current_price)

            # 초기화
            self.current_tick_open = 0
            self.current_tick_high = 0
            self.current_tick_low = 10000000
            self.current_tick_close = 0
            self.current_tick_volume = 0
            self.tick_count = 0

    def get_time_data(self, sCode, sRealType, sRealData):

        trade_time = self.dynamicCall("GetCommRealData(QString, int)", sCode, 20)  # 체결 시간
        # trade_date = self.dynamicCall("GetCommRealData(QString, int)", sCode, 22)  # 체결 일자
        trade_date = t.strftime('%Y%m%d')
        dt = trade_date + trade_time

        date_time = pd.to_datetime(dt)

        current_price = self.dynamicCall("GetCommRealData(QString, int)", sCode, 10)  # 현재가(체결가)
        current_price = abs(float(current_price))

        current_volume = self.dynamicCall("GetCommRealData(QString, int)", sCode, 15)  # 체결량
        current_volume = abs(int(current_volume))

        # 틱 데이터 저장, 체결 일시, 현재가, 체결량

        # 새로운 분이 시작되면 기존 분봉 추가
        if self.is_minute_candle_close(self.basis_time_unit, trade_time):
            # 현재의 켄들을 min_bar에 추가
            new_bar = pd.DataFrame(
                {'date_time': self.current_minute_dt, 'Open': self.current_minute_open,
                 'High': self.current_minute_high,
                 'Low': self.current_minute_low, 'Close': self.current_minute_close,
                 'Volume': self.current_minute_volume}, index=[0])

            self.min_bars = pd.concat([self.min_bars, new_bar], ignore_index=True)

            #print(self.min_bars.tail(1))

            # trade
            self.trade(sCode, current_price)

            # 초기화
            # 2023-02-02 12:31:00
            trade_time = trade_time[0:4] + '00'
            dt = trade_date + trade_time
            self.current_minute_dt = pd.to_datetime(dt)
            self.current_minute_open = 0
            self.current_minute_high = 0
            self.current_minute_low = 10000000
            self.current_minute_close = 0
            self.current_minute_volume = 0

        # 기존 분이면 업데이트
        if self.current_minute_open == 0:
            self.current_minute_open = current_price

        if self.current_minute_high < current_price:
            self.current_minute_high = current_price

        if self.current_minute_low > current_price:
            self.current_minute_low = current_price

        self.current_minute_close = current_price

        self.current_minute_volume = self.current_minute_volume + current_volume

    def is_minute_candle_close(self, basis_minute_unit, current_time):
        current_hour = current_time[:2]
        current_minute = current_time[2:4]

        if basis_minute_unit in self.target_minutes:
            if basis_minute_unit == 1:
                if self.current_minute is not None and self.current_minute != current_minute and current_minute in self.minute_1_range:
                    self.current_minute = current_minute
                    return True
                self.current_minute = current_minute

            elif basis_minute_unit == 3:
                if self.current_minute is not None and self.current_minute != current_minute and current_minute in self.minute_3_range:
                    self.current_minute = current_minute
                    return True
                self.current_minute = current_minute

            elif basis_minute_unit == 5:
                if self.current_minute is not None and self.current_minute != current_minute and current_minute in self.minute_5_range:
                    self.current_minute = current_minute
                    return True
                self.current_minute = current_minute

            elif basis_minute_unit == 15:
                if self.current_minute is not None and self.current_minute != current_minute and current_minute in self.minute_15_range:
                    self.current_minute = current_minute
                    return True
                self.current_minute = current_minute

            elif basis_minute_unit == 30:
                if self.current_minute is not None and self.current_minute != current_minute and current_minute in self.minute_3_range:
                    self.current_minute = current_minute
                    return True
                self.current_minute = current_minute
            return False

        elif basis_minute_unit in self.target_hours:
            if basis_minute_unit == 60:
                if self.current_hour is not None and self.current_hour != current_hour and current_hour in self.hour_1_range:
                    self.current_hour = current_hour
                    return True
                self.current_hour = current_hour

            elif basis_minute_unit == 120:
                if self.current_hour is not None and self.current_hour != current_hour and current_hour in self.hour_2_range:
                    self.current_hour = current_hour
                    return True
                self.current_hour = current_hour

            elif basis_minute_unit == 180:
                if self.current_hour is not None and self.current_hour != current_hour and current_hour in self.hour_3_range:
                    self.current_hour = current_hour
                    return True
                self.current_hour = current_hour

            elif basis_minute_unit == 240:
                if self.current_hour is not None and self.current_hour != current_hour and current_hour in self.hour_4_range:
                    self.current_hour = current_hour
                    return True
                self.current_hour = current_hour

            elif basis_minute_unit == 360:
                if self.current_hour is not None and self.current_hour != current_hour and current_hour in self.hour_6_range:
                    self.current_hour = current_hour
                    return True
                self.current_hour = current_hour

            elif basis_minute_unit == 720:
                if self.current_hour is not None and self.current_hour != current_hour and current_hour in self.hour_12_range:
                    self.current_hour = current_hour
                    return True
                self.current_hour = current_hour

            return False

    def trade(self, code, current_price):

        signallength = 200

        # signal dataframe

        if self.basis_tick_unit > 0:

            self.sl_points = 5
            self.tp_points = 10

            endid = len(self.tick_bars)
            startid = endid - signallength

            df = self.tick_bars[startid:endid]
            df.reset_index(drop=True, inplace=True)

        elif self.basis_time_unit > 0:

            self.sl_points = 10
            self.tp_points = 20

            endid = len(self.min_bars)
            startid = endid - signallength

            df = self.min_bars[startid:endid]
            df.reset_index(drop=True, inplace=True)

            # signal #1
            df['HMA'] = ta.hma(df.Close, length=120)
            # df['HMA'] = round(float(df['HMA']), 2)
            df['HMAt'] = 0  # HMA trend, 1 = up trend, 0 = down trend
            df.loc[df['HMA'] > df['HMA'].shift(), 'HMAt'] = 1
            df['signal1'] = df['HMAt'].diff()  # HMA signal

            msg = '[200] [%d] %s %.2f %.2f %.2f %.2f %d' % \
                  (df.index.values[-1], df.date_time.values[-1], df.Open.values[-1], df.High.values[-1],
                   df.Low.values[-1], df.Close.values[-1], df.Volume.values[-1])

            # telegram_bot
            # asyncio.run(self.telegram_bot(msg))

            # print(df.tail(1))
            print(msg)

            # signal#2  macd
            # MACDh_12_26_9
            macd_info = ta.macd(df.Close)
            df = pd.concat([df, macd_info], axis=1, ignore_index=False)

            # signal#3  Chandelier Exit
            atr_period = 22
            df['atr'] = ta.atr(df.High, df.Low, df.Close, length=atr_period)
            chandelier_info = ta2.TA.CHANDELIER(df, short_period=atr_period, long_period=atr_period, k=3)
            df = pd.concat([df, chandelier_info], axis=1, ignore_index=False)

            #  Long position
            df['enter_long'] = np.where((df['Close'] > df['Short.']) & (df['Close'].shift(1) <= df['Short.'].shift(1)),
                                        1,
                                        0)
            df['exit_long'] = np.where((df['Close'] < df['Long.']) & (df['Close'].shift(1) >= df['Long.'].shift(1)), 1,
                                       0)

            #  Short position
            df['enter_short'] = np.where((df['Close'] < df['Long.']) & (df['Close'].shift(1) >= df['Long.'].shift(1)),
                                         1, 0)
            df['exit_short'] = np.where((df['Close'] > df['Short.']) & (df['Close'].shift(1) <= df['Short.'].shift(1)),
                                        1, 0)

            self.get_current_position()
            position = self.get_position()
            # print('current_position:' + str(position)) # buy:2 , sell: 1

            msg = '[%d] %d %d %.2f %.2f %d %d' % \
                  (position, df.HMAt.values[-1], df.signal1.values[-1], df.MACDh_12_26_9.values[-1], df.atr.values[-1],
                   df.enter_long.values[-1], df.enter_short.values[-1])

            # telegram_bot
            asyncio.run(self.telegram_bot(msg))

            # print(df.tail(1))
            print(msg)

            if position == 0:
                if df.HMAt.values[-1] == 1 and df.MACDh_12_26_9.values[-1] > df.MACDh_12_26_9.values[-2] and \
                        df.enter_long.values[-1] == 1:

                    # 신규매수 (롱포지션 진입)
                    self.send_order("send_order_fo_req", "0101", self.account_numbers[0], self.code_symbol, 1, "2", "3", 1, "0", "")


                    # 진입가/손절/익절 설정
                    self.entry_price = current_price
                    self.sl_price = current_price - df.atr.values[-1] * 1
                    self.tp_price = current_price + df.atr.values[-1] * 2

                    # self.set_position(2)
                    self.get_current_position()

                    print('롱포지션 진입')
                    asyncio.run(self.telegram_bot('롱포지션 진입'))

                elif df.HMAt.values[-1] == 0 and df.MACDh_12_26_9.values[-1] < df.MACDh_12_26_9.values[-2] and \
                        df.enter_short.values[-1] == 1:

                    # 신규매도 (숏포지션 진입)
                    self.send_order("send_order_fo_req", "0101", self.account_numbers[0], self.code_symbol, 1, "1", "3", 1,
                                   "0", "")



                    # 진입가/손절/익절 설정
                    self.entry_price = current_price
                    self.sl_price = current_price + df.atr.values[-1] * 2
                    self.tp_price = current_price - df.atr.values[-1] * 3
                    # self.set_position(1)
                    self.get_current_position()

                    print('숏포지션 진입')
                    asyncio.run(self.telegram_bot('숏포지션 진입'))

            elif position == 2:

                # 신규매도 (롱포지션 청산)

                if current_price < self.sl_price:

                    self.send_order("send_order_fo_req", "0101", self.account_numbers[0], self.code_symbol, 1, "1", "3", 1, "0", "")


                    # 진입가/손절/익절 초기화
                    self.entry_price = 0
                    self.sl_price = 0
                    self.tp_price = 1000000

                    # self.set_position(0)
                    self.get_current_position()

                    print('롱포지션 손절')
                    asyncio.run(self.telegram_bot('롱포지션 손절'))

                # 손절 포인트 이동
                # elif current_price > self.entry_price + 10 and current_price < self.tp_price:
                #    self.sl_price = current_price

                #    print('롱포지션 손절 이동')
                #    asyncio.run(self.telegram_bot('롱포지션 손절 이동'))

                elif current_price > self.tp_price:

                    self.send_order("send_order_fo_req", "0101", self.account_numbers[0], self.code_symbol, 1, "1", "3", 1, "0", "")

                    # 진입가/손절/익절 초기화
                    self.entry_price = 0
                    self.sl_price = 0
                    self.tp_price = 1000000

                    # self.set_position(0)
                    self.get_current_position()

                    print('롱포지션 익절')
                    asyncio.run(self.telegram_bot('롱포지션 익절'))

            elif position == 1:

                # 신규매수 (숏포지션 청산)
                if current_price > self.sl_price:

                    self.send_order("send_order_fo_req", "0101", self.account_numbers[0], self.code_symbol, 1, "2", "3", 1, "0", "")

                    # 손절/익절 초기화
                    self.sl_price = 1000000
                    self.tp_price = 0

                    # self.set_position(0)
                    self.get_current_position()

                    print('숏포지션 손절')
                    asyncio.run(self.telegram_bot('솟포지션 손절'))


                # 손절 포인트 이동
                # elif current_price < self.entry_price - 10 and current_price < self.tp_price:
                #    self.sl_price = current_price

                #    print('숏포지션 손절 이동')
                #    asyncio.run(self.telegram_bot('숏포지션 손절 이동'))

                elif current_price < self.tp_price:

                    self.send_order("send_order_fo_req", "0101", self.account_numbers[0], self.code_symbol, 1, "2", "3", 1,
                                    "0", "")

                    # 손절/익절 초기화
                    self.sl_price = 1000000
                    self.tp_price = 0

                    # self.set_position(0)
                    self.get_current_position()

                    print('숏포지션 익절')
                    asyncio.run(self.telegram_bot('숏포지션 익절'))

        # 선옵잔고 요청
    def get_current_position(self):
        # print('request get current position')

        trade_date = t.strftime('%Y%m%d')

        self.dynamicCall("SetInputValue(QString, QString)", "계좌번호", self.account_numbers[0])
        self.dynamicCall("SetInputValue(QString, QString)", "비밀번호", '0000')
        self.dynamicCall("SetInputValue(QString, QString)", "조회일자", trade_date)
        self.dynamicCall("SetInputValue(QString, QString)", "비밀번호입력매체", '00')
        self.dynamicCall("CommRqData(QString, QString, QString, QString)", "미결제잔고내역조회", "opw20006", '0', "2001")

    def send_order(self, rqname, screen_no, acc_no, code, order_type, slbytp, hoga, quantity, price, order_no):
        self.dynamicCall(
            "SendOrderFO(QString, QString, QString, QString, int, QString, QString, int, QString, QString)",
            [rqname, screen_no, acc_no, code, order_type, slbytp, hoga, quantity, price, order_no])

    def get_position(self):
        return self.current_position

    def set_position(self, position):
        self.current_position = position

    def get_screen_number(self):
        if self.screen_number > 9999:
            self.screen_number = 1000
        self.screen_number = self.screen_number + 1
        return str(self.screen_number)

    def get_order_type(self, order_type):
        if order_type == '신규매매':
            return 1
        elif order_type == '정정':
            return 2
        elif order_type == '취소':
            return 3

    def get_order_type2(self, order_type):

        if order_type == '매도':
            return "1"
        elif order_type == '매수':
            return "2"


    def get_trade_type(self, trade_type):
        if trade_type == '지정가':
            return "1"
        elif trade_type == '시장가':
            return "3"

    # test 버튼
    def test(self):
        print('test')

        self.get_current_position()

        #self.login()
        #self.actionbt()

        #self.get_current_position()


        #message = "TelegramBot"

        #asyncio.run(self.telegram_bot(message))


    def actionStart_mCandle(self):
        #QMessageBox.about(self, "message", "실시간 1분 캔들")

        # 분봉 데이터 900개 받기
        self.dynamicCall("SetInputValue(QString, QString)", "종목코드", self.code_symbol)
        self.dynamicCall("SetInputValue(QString, QString)", "시간단위", self.basis_time_unit)
        self.dynamicCall("CommRqData(QString, QString, QString, QString)", "선물분차트조회", "OPT50029", 0, "2004")

    def actionStart_tCandle(self, code):

        self.dynamicCall("SetInputValue(QString, QString)", "종목코드", self.code_symbol)
        self.dynamicCall("SetInputValue(QString, QString)", "시간단위", self.basis_tick_unit)
        self.dynamicCall("CommRqData(QString, QString, QString, QString)", "선물틱차트조회", "OPT50028", '0', "2000")



    def actionBuy(self):
        print('actionBuy')

        self.send_order("send_order_fo_req", "0101", self.account_numbers[0], self.code_symbol, 1, "2", "3", 1, "0", "")

        #self.send_order("시장가주문", self.get_screen_number(), self.account_numbers[0], self.code_symbol,
        #                self.get_order_type('신규매매'), self.get_order_type('매수'), self.get_trade_type('시장가'),
        #                self.quantity, '0', '')

    def actionSell(self):
        print('actionSell')

        self.send_order("send_order_fo_req", "0101", self.account_numbers[0], self.code_symbol, 1, "1", "3", 1, "0", "")

        #self.send_order("시장가주문", self.get_screen_number(), self.account_numbers[0], self.code_symbol,
        #                self.get_order_type('신규매매'), self.get_order_type('매도'), self.get_trade_type('시장가'),
        #                self.quantity, "0", "")



    def actionGetData(self):
        QMessageBox.about(self, "message", "선물틱차트연속조회")


        # 분봉 데이터 900개 받기
        self.dynamicCall("SetInputValue(QString, QString)", "종목코드", self.code_symbol)
        self.dynamicCall("SetInputValue(QString, QString)", "시간단위", self.basis_tick_unit)
        self.dynamicCall("CommRqData(QString, QString, QString, QString)", "선물틱차트연속조회", "OPT50028", 0, "2004")


    def actionbt(self):
        #QMessageBox.about(self, "message", "BackTrader (MACD)")
        print("backtest")

        df = pd.read_csv("min3_600_2302024.csv")

        df['HMA120'] = ta.hma(df.Close, length=120)

        # HalfTrend
        htdf = ta.halftrend(df)
        df = df.join(htdf)

        df = df.dropna()
        df.reset_index(drop=True, inplace=True)

        self.show_chart(df)


        df['signal'] = 0

        # Generate the signals
        df.loc[df['HMA120'] > df['HMA120'].shift(), 'signal'] = 1

        # Generate the holding signals
        df['positions'] = df['signal'].diff()

        bt = Backtest(df, MyStrat, cash=20000)
        stat = bt.run()

        print(stat)
        print(stat['_trades'].to_string())

        bt.plot()

        print('ok')

    def show_chart(self, df):

        x = np.arange(len(df.index))
        ohlc = df[['Open', 'High', 'Low', 'Close']]
        dohlc = np.hstack((np.reshape(x, (-1, 1)), ohlc))

        p1 = plt.subplot(2, 1, 1)
        plt.grid(True)
        candlestick_ohlc(p1, dohlc, width=.6, colorup='red', colordown='blue')  # ⑦
        plt.plot(df.index, df['HMA120'], color='red', label='HMA120')
        plt.plot(df.index, df['atrhigh'], color='green', label='ATRh')
        plt.plot(df.index, df['atrlow'], color='orange', label='ATRl')
        plt.plot(df.index, df['halftrend'], color='blue', label='HalfT')
        for i in range(len(df)):
            if df.buy.values[i] == 1:  # ①
                plt.plot(df.index.values[i], df.atrlow.values[i], 'r^')  # ②
            elif df.sell.values[i] == 1:  # ③
                plt.plot(df.index.values[i], df.atrhigh.values[i], 'bv')  # ④

        plt.legend(loc='best')

        p4 = plt.subplot(2, 1, 2)
        plt.grid(True)
        plt.bar(df.index, df['Volume'], color='m', label='volume')

        plt.show()

    async def telegram_bot(self, msg):  # 실행시킬 함수명 임의지정

        bot = telegram.Bot(token=token)

        await bot.send_message(chat_id, msg)


class MyStrat(Strategy):

    def init(self):
        super().init()

    def next(self):
        super().next()

        if len(self.trades) > 0:
            if self.trades[-1].is_long and self.data.sell == 1:
                self.trades[-1].close()
            elif self.trades[-1].is_short and self.data.buy == 1:
                self.trades[-1].close()

        if self.data.buy == 1 and len(self.trades) == 0:

            self.buy()

        elif self.data.sell == 1 and len(self.trades) == 0:

            self.sell()





if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        hts = Kiwoom()
        window = Window(hts)
        window.show()
        sys.exit( app.exec_() )
    except Exception as e:
        print(e)
