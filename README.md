
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


(230926v1.2)
* 코드 따라 가기 run
* nan 제거하기
* enumerate
* iterrows
* print(f"{index=}, {row.age=}, {row['sex']=}")



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
