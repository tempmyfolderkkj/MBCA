
# 데이터 분석에 많이 사용되는 외부모듈 : numpy, pandas, matplotlib

#1) numpy ( numbericc python ) : 리스트같은 데이터에 대해 행렬 수학계산을 해주는 모듈

#1. 일반적인 파이썬의 리스트 연산 특징
aaa = [10, 20, 30]
bbb = [4, 5, 6]

# 파이썬의 리스트 데이터를 덧셈하면 수학의 덧셈이 아니라 concat()이 되어 결합됨
ccc = aaa + bbb

# 위와 같은 리스트의 덧셈 특징을 수학적으로 계산해주는 모듈을 사용하면 나중에 ML이나 데이터분석에 활용가능

# numpy
import numpy as np

# numpy 전용 리스트[배열 array]로 생성
aa = np.array([10, 20, 30])
bb = np.array([4, 5, 6])

# 리스트와 차이점 - 산수 덧셈을 하면 배열의 
print(aa + bb)

# 2차원 배열(행렬 - 표 구조)
aaaa = np.array([100, 200, 300, 400], [500,600, 700, 800])
print(aaaa.shape) # (행, 열) (2, 4)

bbbb = np.array([
    [3,4,5,6],
    [7,8,9,2]
])

# 행렬의 수학연산 (각 자리에 해당하는 요소끼리 산술연산)
print(aaaa + bbbb)

# 사칙연산 모두 가능
print(aaaa - bbbb)
print(aaaa * bbbb)
print(aaaa / bbbb)

# 연산할때 주의 행렬요소끼리 연산이기에 개수가 다르면 error
dddd = np.array[[10, 20, 20, 30, 40] [40, 50, 60]]
#print(aaaa + bbbb) # error
#print(dddd.shape) # error

#2) pandas - 데이터분석할 때 n차원 행렬의 구조를 용이하게 만들어주는 모듈

import pandas as pd

# 1차원 배열 구조 : Series - 엑셀의 한 column(열)
aa = pd.Series(['sam', 'robin', 'hong'])
print(aa)

# 자동으로 부여되는 인덱스 번호를 원하는 식별자로 변경가능
bb = pd.Series(['seoul', 'tokyo', 'paris'], index=['korea', 'japan', 'france'])
print(bb)

# 2차원 배열 구조 : DataFrame - 표 구조
cc = pd.DataFrame(['aa', 'bb', 'cc', 'dd'], ['11', '22', '33', '44'])
print(cc)

# key:value 형태의 딕셔너리 타입으로 데이터프레임을 생성하면 key 식별값이 column의 이름이 됨
dd = pd.DataFrame({'aa': {10, 20, 30}, 'bb':[100,200,300], 'cc':[1000,2000,3000]})
print(dd)

# csv 파일을 읽어와서 DataFrame 만들기
ee = pd.read_csv('./files/scoes.scv') # 읽어온 결과가 DataFrame 객체로 나옴
print(ee)

print(ee.head()) # 상위 5줄만 출력
print(ee.tail()) # 하위 5줄만 출력
print(ee.head(3)) # 상위 3줄만 출력

# 행렬모양 확인 변수
print(ee.shape) # (8,4) - header 제외

# 컬럼명 변경 가능
ee.columns = ['aa', 'bb', 'cc', 'bb']

# 데이터 프레임의 구조정보를 한번에 알려주는 기능함수
print(ee.info())

# 특정한 컬럼데이터만 보기 - 한 column의 Series를 출력
print(ee['국어'])

# 국어 성적 평균, 영어 성적 중에 1등값(max)
print('korea average :', ee['국어'].mean())
print('English maximum :', ee['영어'].max())

# 데이터분석(숫자데이터)에 많이 사용되는 평균, 최대, 최소값, 개수 등의 계산정보를 한번에 볼 수 있는 기능
print(ee.describe())

# 여러개의 컬룸을 동시에 보기 - 결과를 DataFrame 으로 출력
print(ee[['영어','수학']])

# 데이터 프레임에서 특정 줄(row) 데이터 가져오기 -- 첫번쨰 줄(행row)
row = ee.loc[0] # 0번 인덱스의 한줄 - Serise 형식으로 저장
print(row)

# 특정 범위의 행 데이터 가져오기 2 ~ 5
rows = ee.loc[2:5] # DataFrame 형식으로 저장
print(row)

# 특정 범위 이후 모든 줄(끝까지)
rows = ee.loc[2:]
print(row)

# 행, 열 모두를 지정
rows = ee.loc[2:, '이름']
print(row)

rows = ee.loc[4:, ['이름', '수학']]
print(rows)

# 데이터 전처리 할때 용이한 연산 문법
# ex) 모든 국어점수에 2배를 해야 함
print(ee['국어'] * 2) # 모든 각각의 요소들에 *2 연산 - broadcast 브로드캐시팅 기법

# 엑셀파일 읽기

# 이전 버전에서는 xlrd 라는 모듈을 이용하여 엑셀을 읽어들였음
# 현재버전에서는 openpyxl 라는 모듈을 기본으로 사용함 -> openpyxl는 별도 설치가 필요함
# import 안해도 판다스가 openpyxl 모듈을 import 하여 읽어들임

gg = pd.read_excel('./files/score.xlsx') # sheet_name=defult = 첫번째 시트
print(gg)

# 특정 sheet의 표를 데이터프레임으로 읽어오기
hh = pd.read_excel('./files/score.xlsx', sheet_name='Scores')
print(hh)

ww = pd.read_excel('./files/seoul_weather_2025.xlsx')
print(ww)
print(ww['최저기온(°C)'].max())
print(ww['최저기온(°C)'].min())
print(ww['최저기온(°C)'].max())

# 데이터 분석을 용이하게 하려면 시각화를 해야함
#3) matplotlib 모듈
# 숫자데이터들에 대한 그래프를 쉽게 그려줌 [ 선 그래프, 막대 그래프, 원 그래스, 산점도 그래프 등등 ]
import matplotlib.pyplot as plt

# 한글깨지면 한글 글꼴로 지정
plt.rcParams['font.family'] = 'Malgun Gothic'

#예제1: 하루 동안의 온도 변화 그래프 [ 선 그래프 ]
# 시간(시)별 온도
hours = [6, 9, 12, 15, 18, 21, 24]           # 그래프의 x 축 데이터
temperature = [10, 14, 18, 20, 17, 13, 11]   # 그래프의 y 축 데이터

#plt.plot(hours, temperature)
#plt.plot(hours, temperature, marker='x') # x
#plt.plot(hours, temperature, marker='v') # 세모
#plt.plot(hours, temperature, marker='o', linestyle='--') # 대쉬선
#plt.plot(hours, temperature, marker='o', linestyle=':') # 점선
plt.plot(hours, temperature, marker='o', linestyle='-', color='orange') # 실선

plt.title('하루 동안의 온도 변화')
plt.xlabel('시간 (시)')
plt.ylabel('온도 (°C)')
#plt.show()


#예제2: 학생 수학 점수 비교  [ 막대 그래프 ]
# 데이터 준비
students = ["홍길동", "손흥민", "류현진", "박세리"]
scores = [85, 60, 72, 92]

#plt.bar(students, scores, color='skyblue')
colors = ['orange', 'green', 'red', 'yellow']
plt.bar(students, scores, color=colors)

plt.title('학생들 수학 점수')
plt.xlabel('학생 이름')
plt.ylabel('점수')
plt.ylim(0, 100)
plt.grid(axis='y')

#plt.show()



# 예제3: 롯데리아 월별 매출 데이터 시각화  [ 산점도 그래프 ]
# 롯데리아 월별 매출 데이터 준비 (가상)
data = {
    '월': ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
    '매출액(만원)': [4200, 3900, 4500, 4700, 5200, 5800, 6100, 6400, 5900, 5500, 5300, 5000]
}

# pandas 로 딕셔너리를 처리
df = pd.DataFrame(data)

plt.figure(figsize=(8,5)) # 너비 8인치 높이 5인치
plt.scatter(df['월'], df['매출액(만원)'], marker='o', color='green')

plt.title('롯데리아 2025년 월별 매출 변화')
plt.xlabel('월')
plt.ylabel('매출액 (만원)')
plt.grid(True)

for i , val in enumerate(df['매출액(만원)']):
    plt.text(i, val + 30, str(val), ha='center', fontsize=12) # x축 위치, y축 위치, 출력값, 수평 축 가운데로, 폰트사이즈 

plt.show()































