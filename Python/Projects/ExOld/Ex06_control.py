

# 제어문 -- 프로그램의 진행순서를 제어하는 문법

# 1. 조건문 , if, if - else, if - elif

#1) if
age = 15

if age < 20:
    print("미성년자는 시청에 주의하세요.")
    print("다른 콘텐츠를 시청하세요.")

print("넷플릭스 입니다.")


#2) if - else
age = 25

if(age >= 20):
    print("환영합니다. 문나이트 입니다.")
    print("신나게 노세요~~")

    # 영역안에 출력기능만 사용가능한 것은 아님
    # 어떤 코드든 가능
    n = int(input("숫자 입력: "))
    n +=2
    print("n :", n)

else:
    print("꺼져!")
    print("더 커서와~~")

#3) 중첩 if - elif
age = 19

if(age > 20):
    print('꺼져!')
    
    if(age > 18):
        print("뒷문으로...")

else:
    print("환영합니다. 문나이트 입니다.")

    gender = "female"
    if(gender == "female"):
        print("할인해 줍니다.")

    else:
        print("정가 그래도")

    print("필요한거 있으면")

#4) if - elif
# 예) 시험 점수를 입력하면 학점(A, B, C, D, F)을 계산하여 알려주는 프로그램
score = 75

# 중첩 if문
if(100 >= score >= 90):
    print("A")
    print("매우 우수 합니다.")
else:
    if(90 > score >= 80):
        print("B")
        print("우수 합니다")
    else:
        if(80 > score >= 70):
            print("C")
            print("준수 합니다")
        else:
            if(70 > score >= 60):
                print("D")
                print("분발하세요")
            else:
                if(60 > score >= 0):
                    print("F학점 입니다")
                    print("FFFF")
                else:
                    print("잘못입력했습니다")
                    print("0 ~ 100 사이 숫자만 입력해주세요")

# elif
score = 95

if(90 <= score <= 100):
    print("A학점")
    print("아주 우수합니다")
elif(80 <= score < 90):
    print("B학점")
    print("우수합니다")
elif(70 <= score < 80):
    print("C학점")
    print("준수합니다")
elif(60 <= score < 70):
    print("D학점")
    print("분발하세요")
elif(0 <= score < 60):
    print("F학점")
    print("재수강 입니다")
else:
    print("잘못 입력했습니다.")


# 조건이 2개 이상인 경우. [2개 이상의 변수의 조건을 묶어서 비교해야 하는경우] --비교연산을 묶어주는 연산자[논리연산 and or not]

#5.1) and를 사용하는 경우 [점수 90이상이고 결석이 1개 이하일때는 A+]
score = 95
absent_days = 1

if( score >= 90 and absent_days <= 1):
    print("A+ 학점입니다. 최우수 학생입니다")
else:
    print("최우수 학생은 아닙니다.")

#5.2) or을 사용하는 경우 [ 이벤트 당첨. 리뷰를 썻는데 특정단어가 포함되어 있거나 최소 20글자 이상 작성한 리뷰]
review = "오늘 신발이 도착했어요"

if( ("좋아요" in review) or (len(review) >= 20) ):
    print("이벤트 당첨")
else:
    print("원하는 단어가 없거나 글자수가 너무 적어요")

#5.3) not을 사용하는 경우 [ 필수는 아니지만 코드를 해독할때 사람이 생각하는 데로 써져있어서 선호함 ]
# 예) "나이가 성인이 아니면" 이라는 조건

age = 15

if(not age > 20):
    print("미성년")

else:
    print("성년")

#6) 조건에 사용하는 비교연산인 크다 작다만 있는 것은 아님.

# 강아지 키우는 게임
print("@ 강아지 키우기 @")
print("----------------")
print("1. 밥먹기")
print("2. 산책하기")
print("3. 목욕하기")
print("----------------")

menu = input("메뉴선택 : ")

# 메뉴 선택에 따라 다른 동작
if(menu == "1"):
    print("아구아구 맛있다")
elif(menu == "2"):
    print("와우~~ 신난다")
elif(menu == "3"):
    print("으아!! 짜증!!")
else:
    print("잘못된 메뉴 번호를 입력했습니다.")

# python 3.10버전에서 새로 도입된 문법 match-case [다른 언어에서 사용하는 switch]
match menu:
    case "1" :
        print("아구아구 맛있다")
    case "2":
        print("와우~~ 신난다")
    case "3" | "4" | "5": # | 사용 가능(파이썬 match-case에서는 or 처럼 해석함)
        print("으아!! 짜증!!")
    case _:
        print("잘못된 메뉴 번호를 입력했습니다.")

#7) 특이한 키워드 pass -- 미완성 작업중일때 사용
a = 100
if(a < 100):
    print("aaa")
elif(a < 200): pass
    # 여기 작업을 좀 나중에 다른 작업 후에 완료하고 싶을때

print("----------------------")

#8) 조건식을 쓸때 소괄호() 행략해도됨
if a < 10:
    print("aaa")
else:
    print("bbb")

#9) 조건의 실행문이 한줄이면 코드도 한줄로 써도 됨
#1] if
age = 25
if age > 20: print("adult")

#2] if - else [순서가 조금 이상함]
#원래 모습
number = 10
if number % 2 == 0:
    print("짝수")
else:
    print("홀수")

# one line if [순서 주의] - 실행문A if() else 실행문 B
print("짝수") if number % 2 == 0 else print("홀수")

#3] if elif else
menu = 1
print("Hello") if menu == 1 else print("nice") if menu == 2 else print("good")

#10) 삼항연산자 [ age > 2? "A":"B" ] / 파이썬은 one line if 문으로 대응함
# 예) 사용자가 정수 2개를 입력하면 그 값 중에 큰값이 max 라는 변수에 저장되도록
num1 = 10
num2 = 5
max = 0

if(num1 > num2):
    max = num1
else:
    max = num2

max = num1 if num1 > num2 else max = num2

# 예2) 학점 출력을 삼항연산자로
score = input()
grade = "A학점" if score >= 90 else "B학점" if score >= 80 else "C학점" if score >= 70 else "D학점" if score >= 60 else "F학점"

print("당신의 학점은 :", grade)

#10) 파이썬은 0과 같이 값이 없는 것을 제외하고는 모두 참으로 해석
data = 10 # True
data = "aaa" # True
data = 0 # False
data = "" # False
data = [] # False

if data:
    print("")

# 사용자가 입력해야 하는데 안하고 그냥 엔터
text = input("글씨를 입력하세요 : ")
# 사용자가 입력을 안했을 경우를 대응하기 위헤
if not text:
    print("입력해")
else:
    print("입력된 글씨는 : ", text)

# 조건 사용할때 주의할 점
aa = "Hello"
n = 5

if n < 10 :
    aa = "nice"
    t = 11

print("aa :", aa)
print("t :", t) # 조건 만족 x -> 오류 발생