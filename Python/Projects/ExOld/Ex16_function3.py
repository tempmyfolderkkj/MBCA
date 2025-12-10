
# 람다 lambda - 간단한 함수의 정의를 조금더 단순하게 한줄로 축약해주는 문법

# 2.1 람다의 편의성을 인식하기 위해, 일반적인 아주 간단한 기능의 함수를 만들고 사용하기
def aaa(n): # 함수 기능 : 전달받은 숫자에 10을 곱한 결과를 리턴해주는 기능함수
    return n * 10

num = aaa(5)

# 2.2 람다 함수 - 위 함수와 같은 기능을 람다함수표기법으로 축약하여 정의해보기
bbb = lambda n: n * 10

bbb(4)
print(num)

# 람다함수는 다른함수의 파라미터로 함수를 전달해야 할때 많이 사용됨 (다른 함수를 파라미터로 받는 함수를 "고차함수"함수 라고 부름)
# gui 프로그램을 만들때 특정 이벤트(버튼 클릭같은)가 발생할때 실행될 함수를 등록할때 람다가 많이 사용됨
# 데이터 분석, ml 작업할때 데이터들을 정제하기 위해 특정 기능을 데이터마다 적용해야 할때 많이 사용함 

# 람다함수 활용에 대한 이해를 위해

# 변수의 값을 대입하는 상황
a = 10
b = a

# a의 값을 출력하고 싶을때 a라는 변수명을 쓰지 않아도 a값을 대입받은 b변수를 이용해서 출력도 가능
print(b)

# 파이썬의 변수는 정수, 실수, 문자열, 논리값, 객체 등 어떤 값이든 저장 가능함, 함수(코드 덩어리) 조차도 저장이 가능함
def bbb():
    print("this sis bbb function")

ccc = bbb # 함수의 이름 bbb를 쓰면 그 함수의 코드 덩어리가 전달됨
# 그래서 ccc도 bbb함수와 같은 코드를 가진것 처럼 사용이가능함
ccc()


# 함수이름 bbb, ccc 이것이  무엇인지
print(bbb) # 함수의 이름은 코드가 써있는 곳의 메모리 위치값

def eee(f):
    print("eeee")
    # 함수를 전달받은 매개변수 f를 마치 함수이름처럼 사용이 가능함
    f()

eee(bbb)

def www():
    print("www")

eee(www)

# www 함수처럼 별도로 만들어서 전달하는게 불편해서 한줄로

# 이를 실제로 사용하는 표준함수, map(), filter()
aaa = [1,2,3,4,5]

# 반복문 list.append()
bbb = []
for v in aaa:
    bbb.append(v*v)
print(bbb)

# 리스트 컴프리헨션, 리스트내포 기술 사용
ccc = [ v*v for v in aaa]
print(ccc)

# map()함수 사용
def cal_square(v):
    return v * v

ddd = map(cal_square , aaa)
print(ddd) #마치 range()처럼 리스트를 만들어주는 객체가됨 -> 한번 출력하면 날라감
# 반복문
for v in ddd:
    print(v)
# 리스트
print(list(ddd))

eee = map(lambda n:n**3, aaa)
fff = map(lambda n:n/10, aaa)
print(list(fff))

# filter(함수, 리스트) 표준함수 - 특정 조건에 해당하는 요소만 뽑아서 리스트로
aaa = [70,60,40,80,90,32,75]
# 60미만만 리스트로 뽑기
vvv = filter(lambda n:n<60, aaa)
print(list(vvv))

www = [v for v in aaa if v<60]
print(www)
























