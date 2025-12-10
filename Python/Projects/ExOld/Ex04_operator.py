
# 연산자 : 산술, 비교, 논리, 비트, 복합대입, 형변환
# 산술 -> + - * / % // (-)
# 비교 -> > < >= <= == !=  [0 < a < 10]가능
# 논리 -> and or not 
# 비트 -> & | ^ >> <<  ~
# 복합대입 -> += -= *= /= %= //=
# 1. 산술
a = 10
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a % b)
print(a // b)

# 나눗셈의 몫, 나머지값을 한번에 연산하여 결과를 주는 기능함수를 제공함 divmod()
x, y = divmod(a, b)
print("몫 : {}, 나머지 : {}".format(x, y))

# 부호 변경 연산자 - [단항 연산자]
c = 10
print(-c)
c = -10
print(-c)

# 제곱 연산자
a = 4
print(a ** 2)
print(a ** 3)
print(a ** (1 / 2)) # 4의 제곱근 [루트]

# 2. 비교 연산자
a = 10
b = 4

print(a > b) # True
print(a < b) # False
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

# a 변수가 특정 범위 안에 있는지 여부
# a 가 0 ~ 100 사이 숫자인가
print(0 < a < 100)
# 나이가 20대 인지
age = 35
print(20 < age < 30)

# 3. 논리연산자 : and, or, not
# 하나의 변수에 대한 범위조건이 아니라 2개 변수의 조건을 동시에 체크하는 경우도 많음
# [예] (놀이기구 탈때) 나이가 10살 이상, 키가 150이상 조건 확인
age = 15
height = 160
print(age >= 10 and height >= 150) # 두 비교연산의 결과가 모두 True인 경우만 True가 되는 논리연산

# 나이가 10살 미만이거나 키가 150보다 작다면
print(age < 10 or height < 150) # 두 비교연산의 결과 중 하나라도 True면 True결과를 주는 논리연산

# 미성년자가 아닌지 확인 조건
age = 15
print(age >= 20) # 성인인지 조건
print(not age < 20) # 미성년자인지 조건

# 4. 비트연산자(거의 사용 안함)
print(7 & 4) # and 비트 연산
print(7 | 4) # or 비트 연산
print(7 ^ 4) # exclusive or(exor) 비트 연산
print(8 >> 2) # shift 연산 비트를 오른쪽으로 2칸밀기
print(8 << 2)
print(~10) # 0 -> 1, 1 -> 0 (숫자의 부호도 바뀌어버림)

# 복합대입 연산자 ( 산술 + 대입 )
a = 10
a = a + 1
print("a :", a + 1)

# a 변수가 가진 값을 증가
a = 20
a = a + 1
print("a :", a + 1) # 21

a = a + 2
print("a :", a + 1) # 23

a = a + 10
print("a :", a + 1) # 33

# 만약 변수의 이름이 길면
charater_age = 20
charater_age = charater_age + 1
print("age :", charater_age)

# 변수명이 길면 변수명을 2번 쓰는게 불편함
charater_age = 20
charater_age += 1
print("age :", charater_age) # 21

charater_age += 5
print("age :", charater_age) # 26

charater_age -= 3
print("age :", charater_age) # 23

charater_age *= 10
print("age :", charater_age) # 230

charater_age /= 2
print("age :", charater_age) # 115.0

# 순서는 바꿀 수 없음
charater_age =+ 2 # -> charater_age = +2
print("age :", charater_age) # 2

# 6. 형변환 연산자(기능) [type casting]
a = "10"
print(type(a))
#print(a + 3) # error : str + int
# "10" -> 10 변환
a = int(a)
print(type(a))
print(a + 3)

a = "3.14"
#print(int(a) + 5.12) #error 
a = float(a)
print(a + 5.12)

# str() 형변환 기능, 문자열로 변환
print(5 + 3) # 숫자 + 숫자, 산술 더하기
print(str(5) + str(3)) # 문자 + 문자, 문자열 결합 -> "5" + "3" => "53"

# bool() : 단순히 "True" 문자열을 True 논리값으로 변환하는 것은 아님
# 파이썬은 값이 없는것(0, "", [], None, False)을 제외하고 모두 참(True)
a = "True"
print(type(a))

a = bool(a)
print(type(a))

a = 10
print(bool(a)) # True

a = 0
print(bool(a)) # False

a = -5
print(bool(a)) # True

a = "hello"
print(bool(a)) # True

a = ""
print(bool(a)) # False

a = " "
print(bool(a)) # True

# 나중에 조건문 if 문법을 사용할때 조건에 대해 확인할때 이 개념을 사용함
# 예) 엑셀파일을 읽어들여서 그 데이터를 출력할때

# 일반 산수에도 연산자 우선순위가 있듯이 파이썬에도 존재
print(3 + 5 * 6) # 3 + 30 -> 33
print((3 + 5) * 6) # 우선순위 변경은 소괄호

num = 3 + 6 # num = 9

#--------------------------------------------------------------------------------

# 프로그램에서 사용하는 대부분의 데이터는 문자열이 많음 [ 이름, 제목, 메모글, 리뷰, 아이디]
# 문자열 데이터를 다루기 위한 연산자와 기능함수들 소개

# 1) 문자열 연산자 3개 + * []
# 1] + 결합 연산자
print("aa" + "bb")

# 2] * 반복 연산자
print("aa" * 3)

# 3] 문자엘에 인덱싱 슬라이싱
s = "Hello world"
print(s)
# 문자열(문자가 여러개인것)의 특성 위치 글자를 추출할 수 있음
print(s[1]) # 인덱스 번호(0 ~) 1번째 위치의 값 => e
print(s[1:7]) # 1번부터 ~ 7번 전까지(6번까지)의 글씨 뽑아오기 => ello w
print(s[1:]) # 1번부터 ~ 끝까지
print(s[:7]) # 처음부터 ~ 7번 전까지(6번까지)
print(s[-1]) # 뒤에서 첫번째 요소의 글씨
print(s[-5:]) # 뒤에서 5번째 요소의 글씨부터 ~ 끝까지

# 2) 문자열이 가진 유용한 기능함수()들

# 1] 문자열의 길이(글자수)를 알려주는 내장함수 len() : length
s = "Hello"
print(len(s))

# 2] .format() 기능 -- 특정서식모양을 만들어 사용하는 기능
money = 500
print(money, "만원")
print("{}만원".format(money))

name = "sam"
age = 20
print("이름: {}  나이 : {}".format(name, age))
aaa = "{}s님 반가워요".format(name)
print("만들어진 문자열 :", aaa)
print("글자수는 :", len(aaa))

# format()의 {}에 들어갈 데이터의 종류를 미리 고정할 숫 있음. 코드 실수 방지
print("{:d}   {:d}".format(10, 20)) # d -> decimal 10진수
print("{:f}    {:s}".format(3.14, "asd")) # f -> float, s -> string

# 데이터를 출력할때 표시되는 칸수를 지정할 수 있음
hour = 1
min = 12
sec = 7
print("{:02d}:{:02d}:{:02d}".format(hour,min,sec))

# 정수일때 칸수 지정
print("[{:5d}]".format(100))
print("[{:05d}]".format(100))
print("[{:15d}]".format(100))

# 부호가 표시되고 싶다면
print("[{:+d}]".format(30))
print("[{:+d}]".format(-30))

# 부호가 표시되는 영역을 비워놓고 싶다면
print("[{: d}]".format(30))
print("[{: d}]".format(-30))

# 부호를 칸의 왼쪽끝으로 배치하기
print("[{:=+8d}]".format(30))
print("[{:=+8d}]".format(-30))

# 실수일때 칸수 지정
print("[{}]".format(3.14))
print("[{:f}]".format(3.14)) # float을 쓰면 무조건 소수점 아래 6자리까지 출력됨
print("[{:10f}]".format(3.14))

# 소수점 아래의 칸수를 지정
print("[{:10.2f}]".format(3.14))
print("[{:.2f}]".format(3.14))

#정수를 소수점으로 표시하기
print("[{:.1f}]".format(100))

# 소수점이 존재할때만 소수점 출력
print("{:g}".format(100)) # 알아서 구분해서 출력
print("{:g}".format(3.14))

# 문자열일때 칸수 지정
print("이것은 [{}]입니다".format("aaa"))
print("이것은 [{:s}]입니다".format("aaa"))
print("이것은 [{:10s}]입니다".format("aaa"))

# 문자열 남은 공간의 오른쪽으로 배치
print("이것은 [{:>10s}]입니다".format("aaa"))

# 진법 표시
print(" {:d} ".format(10)) # 10진수 - decimal
print(" {:o} ".format(10)) # 8진수 - octal
print(" {:x} ".format(10)) # 16진수 - hexadecimal
print(" {:b} ".format(10)) # 2진수 - binary

# 파이썬 코드로 2진수, 8진수, 16진수를 표기
print(" {} ".format(0o10)) # 8진수 표기법 0o
print(" {} ".format(0x10)) # 16진수 표기법 0x
print(" {} ".format(0b10)) # 2진수 표기법 0b




