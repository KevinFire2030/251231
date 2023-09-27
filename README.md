
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
