

# 함수(function 기능)  : 특정 기능을 수행하는 코드를 모아놓은 코드영역
# 예) 로그인함수(==로그인 기능 코드를), 회원가입수(==회원가입 코드들 영역), max함수(==최대값을 구하는 기능 코드들)

# [ 특정 기능을작성한 코드 영역을 필요할때 마다 언제든 호출(call) 그 코드영역을 실행되도록]

# 파이썬 함수의 종류
# 1. 표준(내장) 함수 : 이미 파이썬에서 만들어서 내장해 놓은 함수들 print(), input(), len(), ....
# 2. 외부 함수 : 기존 개발자 또는 업체들에서 만들어 라이브러리로 재공하는 함수, 내장되어 있지 않아서 그냥 사용 불가능
#               대신 그 모듈(함수들을 가진 폴더)을 파일에 삽입(import)하여 불러 사용함
# 3. 개발자 정의 함수


# 코드가 써있는 영역을 구분하기 위해 보통 함수의 임을 영어로 작성(동사o)
# 함수 이름(식별자) 옆애 소괄호가 반드시 있오여험, 이를 통해 변수와 구별함

#1 함수 정의 문법 def [define]
def show():
    print("show funcion")
    print("good")
# 함수를 정의했다고해서 코드가 실행하는 것은 아님, 함수를 사용하겠다고 호출해야 그 영역의 코드들이 실행됨

# 함수 호출 function call
show("함수 호출 연습")
show()


def show_name(name):
    print("wel come", name)

show_name("sam")
show_name("robin")


# 매개변수는 여러개 일수도 있음
def output(a, b):
    print("a :", a)
    print("b :", b)

# 함수 호출하면서 값 전달
output(10, 20)
#사용할때 주의할점, 함수 호출할때 매개변수의 개수만큼 값을 줘야함
# output(1000) # error
# output(1000, 2000, 3000)


# 결국 파라미터 개수만큼 반드시 값을 전달해야만 함
# 경우에 따라서 매개변수 미입력시 기본값 지정

# 3. 함수 파라미터의 default value 지정
def display(a = 1, b = 2):
    print("a의 값 :", a)
    print("b의 값 :", b)

display(100, 200)
display(10, a = 20)


# 기능을 만들다 보면 전달값이 몇개인지 특정하기 어려운 경워 존재
# 예) 전달받은 모든 값출력, 모든 값 덧셈 (총합)구하기

def cal_total(number_list):
    print("전달 받은 값의 총합 :", sum(number_list))

cal_total([10, 20, 30, 40])
#cal_total(10, 20, 30) #error

# 4. 매개변수의 길이가 가변적인 파라미터 variable length aragments [가변 파라미터]
def nice(*values):  # 변수 1개로 보이지만 내부에서는 리스트로 만들어줌
    print("전달 받은 값의 개수 :", len(values))

nice()
nice(10)
nice(10,20)

# 함수를 정의할때 유의할 점, 같은 이름의 함수를 또 정의하면 덮어쓰기 됨
def aaa():
    print("aaa function")

aaa()

def aaa():
    print("다시만든 aaa function")

aaa()

def aaa(num):
    print("aaa num:", num)

aaa(10)
#aaa() # error

# 내장함수와 같은 이름의 함수를 만드는 경우 내장함수가 날라감

print(min(1,2,3,4,5,6,2))
#min = 10
#min(1,2,3,4,5,6,2) # error

# 함수의 호출문이 함수 정의보다 먼저되면 안됨
#gg() #error

def gg():
    print("gg")


# 5. 리턴을 해주는 함수 - 함수안에 print()로 출력만 하는게 아니라 연산 결과를 함수를 호출하는 쪽으로 되돌려 주는 문법 return
def aaa():
    return 10

aa = aaa()

def bbb():
    return "Hello"

bb = bbb()

# 매번 같은 값만 리턴되면 효용가치가 떨어지는 기능임
# 2개의 정수를 전달하면 덧셈의 결과를 계산해서 리턴해주는 기능(함수)
def add(a, b):
    x = a + b
    return(x)

num = add(3, 5)
print(num)

num = add(8, 6)
print(num)

# return 을 할때 값이 없이 사용하는 것도 가능함
def ccc():
    print("ccc function")
    return # 이 글자를 만나면 이 함수의 코드 영역이 종료되는 것을 의미함

ccc()

def ddd(n):
    if n < 0:
        print("음수 출력 금지")
        return
    
    print(n)

ddd(10)
ddd(-10)

def eee():
    print("eee!!")

x = eee() # error는 안뜸
print(x) #  none

# 리턴값은 원래 1개만 가능, 파이썬은 여러개 가능
def fff():
    print("fff~~~~")
    return 10, 20, 30

a, b, c =fff()
print(a, b, c)

# 일반변수 대입도 한번에 여러개 대입 되어있음
#n1, n2 = 100, 200, 300 # error
#n1, n2, n3 = 100, 200 # error

a = 1000, 2000
print(a)

def ggg():
    print("ggg")
    return 100, 200, 300

a = ggg()
print(a)

def hhh():
    return ["sam", "robin", "hong"]

name_list = hhh()
print(name_list)

# 리턴된 리스트1개를 분해하여 요소별로 변수에 바로 대입

name1, name2, name3 = hhh()

# [별외.] 지역변수(local variable)와 전역변수(global variable)에 대한 이해
def mmm():
    age = 20 # 지역변수 - 함수 안에서 처음 만들어진 변수 : 이 지역안에서만 인식 가능
    print("나이 :", age)

mmm()
# 함수의 지역변수 밖에서 사용 불가능
#print("밖 :", age) # error

# 함수 밖에 만든 변수는 전역변수
name = "park"

def nnn():
    # 함수안에서 변수값을 변경하려는 코드를 쓰면 새로운 지역변수 생성문법으로 인식함
    name = "kim" 
    print("함수 안 :", name) # 밖에서 만들어진 변수를 사용할 수 있음

nnn()

print("함수 밖 :", name)

# 그래서 함수안에서 전역변수의 값을 변경하고 싶다면, 사용하는 변수가 전역변수임을 명시적으로 알려줘야함
def ttt():
    global name # 이 함수안에서 name 변수는 밖에 있는 전역변수를 사용할 것이라고 명시
    name = "lee"
    print("in", name)

print("out", name)



















































