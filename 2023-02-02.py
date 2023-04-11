# pandas
# 구조화(table)데이터 처리 지원
# 고성능 array 계산 라이브러리인 numpy와 겸하여 스프레드시트 처리
# 전처리 / 연산 / 인덱싱 함수가 포함
# sql / xml / html / csv / json 여러 포맷 데이터와 조합이 좋다 (import 가능)

# 판다스의 데이터 형태(객체) 종류
# 1. 시리즈 : Series => 하나의 열 : 위에서 아래로 늘어진 데이터 묶음 : 데이터 프레임 중 하나의 column object로 해석 가능
# 2. 데이터프레임 : DataFrame => 여러 행 + 여러 열 : 테이블 object로 해석 가능
# 시리즈의 합이 하나의 데이터프레임을 구성한다.

# 시리즈의 구성 : 인덱스와 데이터로 구성
# 데이터 외에 인덱스가 따로 존재한다.
# 인덱스는 Database의 pk와 비슷한 의미
# numpy ndarray로 시리즈 생성
# 시리즈 객체의 재료 데이터타입은 어떠한 타입도 가능

import numpy as np
import pandas as pd

print("###############################################################")
print("# 시리즈 생성")
list_data = [1,2,3,4,5]
example = pd.Series(data=list_data)
print(example)
print("###############################################################")
print("# 인덱스 지정 시리즈")
list_data = [1,2,3,4,5]
list_name = ['A','B','C','D','E']
example = pd.Series(data=list_data,index=list_name)
print(example)
print("###############################################################")
print("# Dict을 활용한 시리즈 생성")
dict_data = {'name1':'두영호','name2':'두세준','name3':'두호','name4':'두치'}
example = pd.Series(data=dict_data)
print(example)
print("# pd.Series의 여러 활용법")
example = pd.Series(dict_data,name='exam')
print(example)
print("###############################################################")
print("# Series 데이터 인덱스 활용")
print(example['name1'])
print(type(example.values)) # numpy.ndarray로 나옴
print(example.index)
print(type(example.index)) # pandas.core.indexes.base.Index로 나옴
print(type(np.array(example.index))) # ndarray로 객체 형태 변환
example.index.name = "name index"
print(example.index.name)
print(example) # index.name 지정 및 참조
print("###############################################################")
print('# 값을 딕셔너리 타입으로 주는 동시에 인덱스를 따로 지정하면?')
# 인덱스가 두 번 지정된다

# 위 상황에서 후에 주어진 인덱스 속성의 값이 갯수가 더 많다면?
dict_data_1 = {'A':1,'B':2,'C':3,'D':4}
index_1 = ['A','B','C','D','E','F']
s_obj = pd.Series(dict_data_1,index=index_1)
print(s_obj)
# 인덱스 옵션으로 주어진 인덱스 값에 따라서 시리즈의 틀이 생성
print("###############################################################")
print("# 데이터 프레임 활용")
# DataFrame은 Series의 합, Series는 곧 numpy 배열이다.
# numpy는 하나의 단일 데이터 타입을 지원한다.
# DataFrame은 하나의 Column마다 DataType이 통일된다.
# ex) 1열(순번) int / 2열(성적) float / 3열(이름) str
# DataFrame은 테이블을 의미한다.

# Dict을 넣으면 키 값이 Column의 이름 Col name이 되고,
# value는 해당 dict Key를 활용한 col 아래 데이터가 된다.
raw_data = {"name" : ['학생1','학생2','학생3','학생4'],
            "age" : [10,20,30,40]}
df = pd.DataFrame(raw_data)
print(df)

# columns 속성에는 아무값이나 넣는 것이 아니다.
print("# raw_data에 지정된 컬럼의 순서 변경")
df = pd.DataFrame(raw_data,columns=['age','name'])
print(df)

print("# 데이터프레임의 핸들링")
# 컬럼 중 일부만 선택하여 DataFrame을 생성하는 방법
df = pd.DataFrame(raw_data,columns=['age'])
print(df)

print("# 데이터프레임 추가적인 Column")
# 추가적인 column을 대입하는 경우 : NaN값이 배치된다.
df = pd.DataFrame(raw_data,columns=['age','hello'])
print(df)
print("###############################################################")
print("# Column Name(컬럼명)의 활용 방법")
# Column Name = 속성명
print(df.age)
print(type(df.age)) # <class 'pandas.core.series.Series'> / 속성 방식으로 추출하는 경우 반환 타입
print("# Column Name(컬럼명) 인덱싱")
print(df['age'][0])
print(type(df['age'][0])) # <class 'numpy.int64'>
print("###############################################################")
print("# Raw 추출")
# loc : index location => 지정한 값
# iloc : index position => 지정한 갯수를 뜻함
raw_data = {'name' : ['김','이','박','유'],
            'age' : [10,20,30,40]}
df = pd.DataFrame(raw_data,index=[1,3,5,7])
print(df)
print('--loc-----------')
print(df.loc[5]) # 1번째가 아닌 인덱스의 실제 값의 위치 (사용자가 메긴 인덱스값)
print(type(df.loc[5]))
print('--iloc----------')
print(df.iloc[0]) # 실제 인덱스 번호 1 : 2번째 행 (기존의 인덱싱 방법과 비슷)
print(type(df.iloc[0]))
# loc , iloc 사용 -> df col명이 series의 index화
print('----------------')
print(df.name)
print(df.age > 20)
print('--transpose-----')
print(df.T) # transpose
print("###############################################################")
print("# CSV 활용")
print('--csv----------')
df_csv = df.to_csv()
print(df_csv)
print('--삭제----------')
del df['name']
print(df)
print("# CSV파일 업로드")
print('--csv upload----')
# 공공데이터 포털 파일 다운로드
path = 'C:\\Users\\202-25\\Desktop\\대전.csv'
df = pd.read_csv(path,encoding='cp949')
# euc-kr / cp949
print(df['사업장명'])
print(df[['사업장명','데이터기준일']])
print('--머리-----------')
print(df[['사업장명','데이터기준일']].head(3))
print('--꼬리-----------')
print(df[['사업장명','데이터기준일']].tail(3))
print('--슬라이싱-------')
print(df[:3])
print(df['사업장명'][:3])
print(type(df['사업장명'][:3]))
print('--raw 삭제-------')
df_1 = df.drop(3)
print(df_1)
df_2 = df.drop([0,1]) # 0행, 1행을 삭제, 여러 인덱스 줄 때는 대괄호로 묶어준다.
print(df_2)
df_3 = df.drop('번호',axis=1)
print(df_3)
print("###############################################################")
print("# 시리즈의 연산 활용")
s1 = pd.Series(range(1,6),index=list('abcde'))
print(s1)
s2 = pd.Series(range(5,11),index=list('bcedef'))
print(s2)
print('--연산자 활용--------')
# index를 기준으로 pk처럼 작동
# 겹치는 index가 없으면 NaN값으로 배치 된다.
# 겹치지 않는 index를 NaN값으로 보지않으려면 fill_value = num (대체값 지정)을 설정해준다.
print(s1.add(s2))
print(s1+s2)
print(s1.add(s2,fill_value=100))
print("###############################################################")
print("# DataFrame 연산 활용")
df1 = pd.DataFrame(np.arange(9).reshape(3,3),columns=list('ABC'))
print(df1)
df2 = pd.DataFrame(np.arange(16).reshape(4,4),columns=list('ABCD'))
print(df2)
# df1, df2 매트릭스 사이즈가 다름, 큰 매트릭스 기준으로 틀 생성
# 빈 부분은 NaN으로 채워지나, fill_value로 빈 값에 대응할 값 지정함
print(df1.add(df2,fill_value=10))
df3 = pd.DataFrame(np.arange(16).reshape(4,4),columns=list('ABCD'))
print(df3)
S = pd.Series(np.arange(10,14),index=list('ABCD'))
print(S)
print(df3+S)
# 위 연산에서 시리즈의 인덱스 ABCD가
# DataFrame의 abcd 열을 기준으로 브로드캐스팅이 된다.
# 시리즈의 인덱스 : DataFrame의 Column과 매칭
# 그 과정에서 T가 작동 (transpose)
print("###############################################################")
print("# DataFrame 여러가지 조회방법")
print(df3.describe())
print(df3.D.unique())
print(df3.sum(axis=0))
print(df3.isnull()) # bool타입 형태로 나옴 NaN = True / esle = False
print(df3.sort_values(["B",'C']))