
#하나의 py파일에 모든 코드와 기능을 작성하여 사용하면 복작함, 기능별로 관리하거나 재사용하기도 어려움
# 모듈 - 여러상수값이나 기능함수들을 가지고 있는 파일의 집합체임(일종의 폴더) 

# 파이썬 모듈의 종류
# 1. 표준 모듈 - 파이썬을 설치할때 같이 내장되어 설치된 모듈들, 그래서 별도의 설치없이 그냥 import만 하면 됨(내장함수는 아님, import 없이는 사용 불가능)
# 2. 외부 모듈 - 사용하려면 별도의 다운로드 및 설치작업이 요구되는 모듈들 [이런 외부 모듈을 설치해주는 프로그램 pip(CLI로 환경으로 모듈을 설치 ex)pip install pandas )]

# 먼저 표준 모듈 중 활용이 많은 모듈들

#1. math 모듈 : 수학적인 연산기능(함수)들을 모아놓은 폴더 같은 모듈
import math as math

print(math.sin(1))
print(math.cos(1))
print(math.log(100, 10))
print(math.floor(3.3)) # 소수점 내리기
print(math.ceil(3.3)) # 소수점 올리기
print(round(3.3)) # 반올림(표준함수)
print(round(3.7)) # 반올림(표준함수)

#1.1 모듈을 사용할때 마다 모듈명. 쓰는것을 줄이는법
import math as m

print(m.pow(4, 2)) # 4 ** 2

#1.2 모듈명도 없이 필요한 함수만 뽑아서 import 가능
from math import floor, ceil

print(floor(3.3))


#2. random 모듈 - 랜덤값 새성, 관련 기능
import random

print(random.random()) # 0.00000 ~ 1
# 만약 0 ~ 9 중에 하나의 숫자를 생성하려면
num = math.floor(random.random() * 10)
print(num)
# 위 계산을 쉽게해주는 기능함수가 존재함
print(random.randrange(10)) # 0 ~ 9
print(random.randrange(5, 16)) # 5 ~ 15

# 리스트의 요소 중 랜덤하게 값을 선택하는 기능
aaa = [1, 2, 3, 4, 5]
print(random.choice(aaa)) # 랜덤 값 1개를 선택
print(random.sample(aaa, 3)) # 랜덤 값 3개 - 리스트로 리턴

# [예] 로또 번호 추천
lotto = list(range(1, 46))
print(lotto)

# 번호 45개 중에서 무작위 6개 뽑아오기
num = random.sample(lotto, 6)
print(num)

# 낮은 번호 순으로 정렬
num.sort()
print(num)


#3. os 모듈 : 운영체제와 관련된 기능 모듈
import os

print('현재 운영체제 : ', os.name)      # nt - window, posix - mac or linux
print('현재 작업폴더 : ', os.getcwd())  # current working directory - 현재 작업 폴더
print('현재 폴더안에 있는 파일과 폴더 목록들 : ', os.listdir())

# 폴더 만들기
#os.mkdir('image') # 이미 존재하는 폴더라면 error 발생
if not os.path.isdir('image'): # 폴더 존재 확인
    os.mkdir('image')

# 폴더 삭제
#os.rmdir('image') # 존재하지 않는 폴더라면 error 발생

# 파일 이름 변경
with open('nice.txt', 'w', encoding='utf-8') as file:
    file.write('hello python')

#os.rename('nice.txt', 'good.txt') # 바꿀 이름의 파일이 존재시 error 발생
if os.path.exists('good.txt'):
    os.rename('nice.txt', 'good.txt')

# 명령프롬프트(cmd)에서 실행했던 명령어를 코드로 실행할 수도 있음
os.system('dir')
#os.system('python Ex01_print') # 다른 .py 실행

# change directory 명령은 일부 안됨
os.system('cd ..') # 안됨, change directory 전용 함수를 이용해야함

print(os.getcwd())
os.chdir('..')
print(os.getcwd())

#4. datetime 모듈 : 날짜와 시간 관련 기능 모듈
import datetime

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# 원하는 날짜로 변경 가능
future = now.replace(year=(now.year+ 1 ))
print(future)

# 시간대 용어
# GMT 시간 - 그리니치 천문대 기준 시간(런던시간대) 경도0 - 한국 GMT +9
# UTC 시간 - GMT를 기반으로 지역별 시간대와 상관없이 1970/1/1,00:00:00 기준으로 밀리초마다 카운트한 원자시간 값 - 세계협정시
# UTC의 밀리초 카운트값이 가장 정확한 경과시간을 계산할 수 있어서 컴퓨터 공학 같은 곳에서 사용하는 시간

# 그 밀리초의 카운트값을 확인할 수 있음, 이를 타임스탬프
print(now.timestamp)

start_time = datetime.datetime.now()
# 특정 작업의 경과시간을 계산할때 활용
for n in range(10000):
    print(n)

elipsed_time = datetime.datetime.now() - start_time
print(elipsed_time)
      
# 날짜 계산 프로그램
a_day = datetime.datetime(2025, 11, 10)
today = datetime.datetime.now()
print('개강일로부터 :',today - a_day)

b_day = datetime.datetime(2026, 4, 9)
print('수료일까지 남은 날짜 :', b_day - today)
print('수료일까지 남은 날짜 :', (b_day - today).days, '일')


#5. time 모듈
import time

print('3초간 프로그램을 잠시 정지했다가 다음 코드가 실행되도록')
time.sleep(3)
print('Hello')





























































