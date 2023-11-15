

    def _get_data(self):
        """
        # Gets data for all tickers from YFinance
        yfObj = yf.Tickers(self.tickers)
        #df = yfObj.history(start=self.start, end=self.end, interval='1h', back_adjust=True, auto_adjust=True, prepost=True)
        df = yfObj.history(start=self.start, end=self.end)
        df.drop(['Open', 'Dividends', 'Stock Splits', 'Volume'], inplace=True, axis=1)
        df.ffill(inplace=True)
        return df.swaplevel(axis=1)
        """

        # 튜플 컬럼 리스트 생성
        tuple_columns_list = [("KOSPI200", "date_time"),
                              ("KOSPI200", "Open"),
                              ("KOSPI200", "High"),
                              ("KOSPI200", "Low"),
                              ("KOSPI200", "Close"),
                              ("KOSPI200", "Volume"),
                              ]
        print(tuple_columns_list)
        # 멀티 인덱스 컬럼 생성
        multi_index_columns = pd.MultiIndex.from_tuples(tuple_columns_list)

        # 판다스 데이터 프레임 생성
        df = pd.DataFrame(columns=multi_index_columns)


        df['KOSPI200'] = pd.read_csv("kospi200_120tick_231110.csv")




        return df

