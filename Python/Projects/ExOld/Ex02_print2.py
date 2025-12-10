
# 화면 출력 / 데이터 유형에 따라 출력해보기
print(10)
print(3.14)
print("Hello")
print('Nice')
print("Hello World")
print(    100)
print(    "good")
print("    good")
print(True)
print(3 + 5)
print(3 > 5)

print()
print('nice to meet you')
print()

#print 기능은 한번에 여러개의 데이터를 출력할 수 있음
print(10)
print(20)
print(1020)
#print(10 20)
print(10, 20)
print(10,    20)
print(10,  3.14,      '      Hello',   False)
print("나는", "이제", "그만 쉬고 싶어요.")
print()

print("나는 '홍길동' 입니다")
print('나는 "홍길동" 입니다')

# 만약 문자열안에 작은따옴표와 큰따옴표를 모두 사용하고 싶다면 특수문자를 사용해야함.
# 원래 규칙을 벗어나는 문자라고 해서, 이스케이프 문자 라고 부름[역슬래시 \]
print("나는 '의적'으로 활동하는 \"홍길동\" 입니다.")

# 출력데이터가 여러줄로 이루어져 있다면, 
print("안녕하세요. " \
"반가워요.")

# 이스케이프 문자의 또 다른 사용모습
# \n : new line
print("안녕하세요.    \n   반가\n워요.")
print("Hello\nNi ce\nGo  od\naaaq")

# \t [tab 간격을 가지는 문자]
print("Hello\tNice\te")
print("-" * 30)

# 여러개의 데이터를 출력상황 [ EX. 학생들의 국영수 성적 표시 ]
print("이름", "국어", "영어", "수학")
print("홍길동", 85, 90, 75)
print("sam", 100, 4, 45)
print("-" * 30)

print("이름\t", "국어\t", "영어\t", "수학")
print("홍길동", "\t", 85, "\t", 90, "\t", 75)
print("김철수", "\t", 100, "\t", 4, "\t", 72)

# \t 는 고정적인 사이즈는 아님, 다음 탭 간격으로 이동해서 [ 통상적인 1탭의 간격은 8칸 ]
print("a\tb") # a가 표시되는 1탭의 간격이 8칸, 그 후 b표시 [그러니 이 상황에서의 \t는 7칸 간격]
print("aaaaaaaa\tb")

# 여러개의 데이터 출력기법을 사용함, 이를 이용하면 특정 서식 모양을 출력형태를 만들 수는 있음.
print(3 + 5)
print(3, 5, 3 + 5)
print(3, " + ", 5," = ", 3 + 5)
print(32, " x ", 56, " = ", 32 * 56)

# 이런식으로 3단 구구단을 출력해주는 프로그램을 만들어 달라고 요청받았다
print(3, " x ", 1, " = ", 3 * 1)
print(3, " x ", 2, " = ", 3 * 2)
print(3, " x ", 3, " = ", 3 * 3)
print(3, " x ", 4, " = ", 3 * 4)
print(3, " x ", 5, " = ", 3 * 5)
print(3, " x ", 6, " = ", 3 * 6)
print(3, " x ", 7, " = ", 3 * 7)
print(3, " x ", 8, " = ", 3 * 8)
print(3, " x ", 9, " = ", 3 * 9)

# 가능은 하지만 쓰고 문자열 따옴표 쓰고 반복
# 이 특정 서식(형식format)으로 만들기 편한 기능이 문자열의 특별한 서식만들기 기능 .format()
print("나는 {} 입니다.".format("홍길동"))
print("당신의 성적은 {}점 입니다.".format(80))
print("나의 이름은 {}이고 나이는 {}살 입니다.".format("sam", 20))
print("{} x {} = {}".format( 4, 1, 4 * 1))
print("{} x {} = {}".format( 4, 2, 4 * 2))

# 주의 - {}의 개수와 format()에 전달하는 값들의 개수는 같아야 함
#print("{} - {}".format(179)) -> error
print("{} - {}".format(179, 72, 20)) # {}보다 값의 개수가 많으면 에러 아님 - 마지막 값만 소실

# PYTHON 3버전 이상부터 등장한 f-string format기술을 사용
print(f"{100 + 3}점 입니다.")
print(f"{8} x {1} = {8 * 1}")
print(f"나의 이름은 {"홍길동"}입니다.")
print(f"나의 이름은 {"손흥민"}입니다.")

print(10, end = " ")
print(20, end = "@")
print(30, end = "")
print(40, end = " - ")
print(50, end = "asfasfwas")
print(60, end = "\n")  # 기본값
print(70)
print()

# 문자열 데이터를 만들때 진짜 코드로 보이는 모습 그대로 출력해줬으면 할때, 사용하는 [따옴표3개 문자열]
print("""\
따옴표 3개를
사용하면
보이는 그대로
표시되는 문자열\
""")

# 변수의 필요성 소개
dan = 6

print(dan, "x", 1, "=", dan * 1)
print(dan, "x", 2, "=", dan * 2)
print(dan, "x", 3, "=", dan * 3)
print(dan, "x", 4, "=", dan * 4)
print(dan, "x", 5, "=", dan * 5)
print(dan, "x", 6, "=", dan * 6)
print(dan, "x", 7, "=", dan * 7)
print(dan, "x", 8, "=", dan * 8)
print(dan, "x", 9, "=", dan * 9)



