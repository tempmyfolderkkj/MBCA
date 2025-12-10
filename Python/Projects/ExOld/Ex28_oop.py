

# OOP ( Object Oriented Programing ) - 객체 지향 프로그래밍
# 객체지향을 위한 중요한 용어 : class(클래스), object(객체)

# 왜 class와 object 라는 것이 등장했는지에 대한 필요성 알아보기

# 예) 학생의 성적을 분석하고 관리하는 서비스 개발

# 학생의 [ 이름, 국어, 영어, 수학, 평균 ] 데이터 저장

# 값을 저장해야하니 변수 필요
name = 'sam'
kor = 80
eng = 70
math = 90
aver = (kor + eng + math) / 3

# 학생1의 값들을 출력
print(name, kor, eng, math, aver)

# 두번째 학생이 있다면
name2 = 'robin'
kor2 = 50
eng2 = 40
math2 = 60
ever2 = (kor2 + eng2 + math2) / 3
print(name2, kor2, eng2, math2, ever2)

# 이런 학생들이 만약 100명이면 변수명을 만드는것도 어려워지고 다른 학생의 데이터를 실수로 저장할수도 있음
# 변수 하나에 학생 한명의 데이터들[이름, 국어, 영어, 수학, 평균]을 묶어서 가지고 있으면 관리가 더 용이
# 여러개의 데이터를 묶어서 저장해주는 타입 ([list], (tuple), {dictionary}) 을 이용
aaa = ['sam', 70, 80, 90, 80.0]
bbb = ['robin', 40, 50, 60, 50.0]

print(aaa)
print(bbb)

# 학생의 성적을 분석을 위해 두명의 학생 성적 중 '국어' 성적만 뽑아서 출력해보기
print('학생 1의 국어성적 :', aaa[1])
print('학생 2의 국어성적 :', bbb[1])

# 데이터 추출이 가능은 하지만 인덱스 번호라서 정확이 식별하기 불편함
# 요소값의 의미를 알수있는 식별자를 이용하면 가독성이 좋아짐

# key:value 쌍으로 데이터를 저장하는 dictionary
ccc = {'name' : 'sam', 'kor' : 70, 'eng' : 80, 'math' : 90}
ccc['ever'] = (ccc['kor'] + ccc['eng'] + ccc['math']) / 3
print(ccc)

print(ccc['math'])

# 또 다른 학생의 데이터를 저장
ddd = {'name' : 'robin', 'kor' : 70, 'eng' : 80, 'math' : 90}
ddd['ever'] = (ddd['kor'] + ddd['eng'] + ddd['math']) / 3
print(ddd)

# dictionary를 이용하면 식별은 좋지만 학생데이터를 만들때마다 같은 이름의 식별자를 지속적로 작성해야함
# 개발자가 원할때 큰 박스의 모양을 설계하여 사용할 수 있도록 제공되는 문법
# 이를 class(묶음 설계도)와 object(설계도로 만든 제품 - 객체)라고 부름

# class - 연관있는 데이터(변수)와 기능(함수)을 묶어놓은 설계도
# object - class를 기반으로 실제 메모리에 만들어진 제품

# 학생의 [이름, 국어, 영어, 수학, 평균] 변수를 하나의 그룹(class)으로 묶는다고 설계해보기 - 파이썬 시스템에게 이렇게 묶을거라고 알려주는 설계도
# class 이름 명명하는 규칙 - 변수 식별자와 유사함, 표기법은 스네이크표기법 말고, 단어의 첫글자를 대문자로 사용하는 파스칼표기법(Aaa)을 권장
class Student():
    # 변수 5개를 사용하겠다고 미리 설계해야함, 변수도 초기화가 필요하듯이 class 묶음도 초기화 과정이 필요함
    # 이 class로 제품(객체 object)을 만들때 자동으로 처음 실행되는 특별한 영역(함수)이 존재함(생성자 함수라고 부름)
    def __init__(self): # 필수
        print('student 설계도(class)로 객체가 생성되었습니다')

        # 이 제품이 가지고 있을 값들을 저장할 변수들을 선언하면, 이 생성자 함수 안에서만 사용하는 지역변수가 됨
        # 변수명을 그냥쓰면 안됨, 이 클래스 본인 것이라고 말하면서 선언해야 함 - 키워드(함수의 파라미터로 전달된 self)
        # 이 클래스의 소속임을 표현하는 self로 만들어진 변수를 멤버변수라고 부름
        self.name = 'sam'
        self.kor = 0
        self.eng = 0
        self.math = 0
        self.ever = 0.0

    # 멤버변수의 값들을 알아서 출력해주는 기능함수를 정의 - 메소드(멤버함수) 라고 부름
    def show(self): # 파이썬의 클래스 영역안에서 멤버변수를 지칭하려면 반드시 self와 함께 해야해서 함수의 파라미터 self가 있어야함
        print(self.name)
        print(self.kor)
        print(self.eng)
        print(self.math)
        print(self.ever)

    # 멤버변수에 값을 대입해주는 기능함수
    def setMembers(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.ever = (kor + eng + math) / 3
        

# class는 설계도임, 아직 제품이 아니기에 클래스를 설계했다고 해서 그 안에 있는 코드가 실행되지 않음(함수 정의 처럼)

# student라는 이름을 가진 클래스(설계도)를 기반으로 제품(객체)을 만들어보기
# 객체 생성 문법(함수 호출문과 유사함) - 클래스명()
Student() # 객체가 생성되면 __init__() 함수의 영역이 실행됨, 이때 이 제품안에 5개의 변수가 만들어짐


# 같은 설계도를 또 다른 제품(객체)를 생성할 수 있음
Student().name = 'robin'

# 객체(5개의 변수를 한번에 가지고 있는 녀석)를 만들었으면 이제 사용해야하는데 이 객체를 제어하는 변수가 없으면 사용 불가 - 마치 리스트를 만들고 변수에 대입을 안한 것과 같은 상황
# 객체를 사용하려면 변수에 대입
std1 = Student() # std1 변수를 이용하여 student 설계도로 만든 객체를 제어할 수 있음
print(std1) # std1이라는 참조변수가 참조하고 있는 실제 Student 객체의 우치(메모리 주소)를 출력함
# std1의 참조하는 student 객체 안에 있는 변수들을 사용하기[ 이때 사용하는 것이 . 연산자 ]
print(std1.name)
print(std1.kor)
print(std1.eng)
print(std1.math)
print(std1.ever)

# 객체 안에 있는 작은변수(멤버변수)들에 값을 대입할때 리스트처럼 한번에 넣는 것 불가능, 하나씩 대입해야함
std1.kor = 70
std1.eng = 80
std1.math = 90
std1.ever = (std1.kor + std1.eng + std1.math) / 3

print(std1.name)
print(std1.kor)
print(std1.eng)
print(std1.math)
print(std1.ever)


# 두번째 학생의 데이터 저장이 필요하면 변수 5개를 만들어야 하지만 Student라는 큰 덩어리를 설계해 놓았으니
# Studnet 덩어리 객체를 하나 만들면 안에 멤버로 5개의 변수가 한번에 만들어짐
std2 = Student()
std2.name = 'robin'
std2.kor = 70
std2.eng = 80
std2.math = 90
std2.ever = (std2.kor + std2.eng + std2.math) / 3

# 멤버변수의 값 출력
print(std2.name)
print(std2.kor)
print(std2.eng)
print(std2.math)
print(std2.ever)

# 이런식이면 새로운 학생만들고 출력할때 마다 멤버값 출력코드를 매번 작성하는것이 매우 번거로움 -> 클래스 영역안에 변수 외에 함수도 미리 만들어 놓을수 있음

# 세번째 학생
std3 = Student()
std3.name = 'hong'
std3.kor = 70
std3.eng = 75
std3.math = 80
std3.ever = (std3.kor + std3.eng + std3.math) / 3

std3.show()

# 객체를 만들고 그 멤버변수에 값을 대입할때 멤버변수 하나에 한줄씩 대입하는 것 불편
std4 = Student()

# 전달할 값을 한번에 넣어주는 기능
std4.setMembers('kim', 50, 60, 70)

std4.show()

# 5번째 학생도 쉽게 저장 및 출력가능
std5 = Student()
std5.setMembers('lee', 10, 30, 50)
std5.show()

# 객체를 만들때 값을 전달하도록 하기 - 이 함수를 '생성자(constructor) 함수'라고 부름 - 파이썬은 이 용도의 함수명을 미리 정해놓음 -> __init__()
# 이 생성자 함수의 파라미터에 값을 전달하여 생성하면 값 대입이 가능해짐


#------------------------------------------------------------------------------------------------------------------------

# [이름, 나이, 주소]를 정보를 그룹으로 묶어서 가질 수 있는 클래스 설계

class Member:
    def __init__(self, name, age, address):
        print('Member 클래스로 객체를 생성했습니다.')

        #[이름, 나이, 주소]를 저장하기위한 멤버변수를 선언, 멤버변수는 이 클래스의 소속임을 보여주기위해 self키워드 필요
        # 파라미터로 전달받은 값들을 멤버변수에 대입
        self.name = name
        self.age = age
        self.address = address

    def show(self):
        print(self.name)
        print(self.age)
        print(self.address)


# 위 설계도 class로 [이름, 나이, 주소]를 한번에 저장하는 객체 생성
m1 = Member('sam', 20, 'seoul')
m2 = Member('robin', 25, 'incheon')
m3 = Member('hong', 30, 'paris')

m1.show()
m2.show()
m3.show()

# 각 객체들의 나이만 출력하려면
print(m1.age, m2.age, m3.age)

member_list = [m1, Member('aa', 22, 'tt')]

for mem in member_list:
    mem.show() # m1, / aa 22 tt


# 여러학생의 [이름, 파이썬, 웹. AI] 성적 데이터를 저장하기 편하도록 4개 데이터를 한번에 저장하는 객체를 설계하여 사용
class Stu:
    # 객체의 초기값을 설정하기 위한 생성자 함수 - 객체생성할때 전달되는 4개의 값으로 초기화
    def __init__(self, name, python, web, ai):
        self.name = name
        self.python = python
        self.web = web
        self.ai = ai

    # 멤버변수의 값을 출력해주는 기능함수 설계하기 - 멤버함수의 첫번째 파라미터에 언제나 self를 등록
    def show(self):
        print(self.name, self.python, self.web, self.ai)

    def get_total(self):
        return self.python + self.web + self.ai

# class는 단지 설계도이므로 객체가 되지 않았기에 사용 불가능
# class 설계대로 멤버(변수4개, 함수1개)를 가지는 객체를 생성하여 사용
s1 = Stu('sam', 80, 70, 50)
s1.show()

s2 = Stu('robin', 60, 50, 20)
s2.show

total1 = s1.python + s1.web + s1.ai
total2 = s2.get_total()

# 객체안에 변수와 함수가 같이 존재함
# 객체 밖에서 값을 저장하는 것을 '변수 variable', 기능코드가 있는 영역 '함수 function'
# 객체 안에서 값을 저장하는 것을 '속성 propterty(멤버변수)', 기능코드가 있는 영역 ' 메소드 method(멤버함수)'

a = 10 # 변수
def aa():pass # 함수

s1.name # 객체의 속성값
s1.show() # 객체의 메소드


# filse/seoul_weather_2025.xlsx의 칸들 6개를 저장하는 클래스 설계, 그 값을 출력하는 기능함수 설계
import openpyxl
import pandas as pd

class SavePrint():
    def __init__(self, month, aver, max, min, rain, supdo):
        self.month = month
        self.aver = aver
        self.max = max
        self.min = min
        self.rain = rain
        self.supdo = supdo

    def print_all(self):
        print(self.month, self.aver, self.max, self.min, self.rain, self.supdo)

data = pd.read_excel('./files/seoul_weather_2025.xlsx',)

data_list = []
for i in range(len(data)):
    data_temp = []

    for key, val in data.items():
        data_temp.append(str(val[i]))
    
    data_list.append(SavePrint(*data_temp))

for li in data_list:
    li.print_all()















