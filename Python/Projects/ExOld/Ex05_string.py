
# 프로그램에서 사용하는 대부분의 데이터는 문자열인 경우가 많음
# 문자열 연산자와 기능함수들

# 문자열 연산자 3개
# 1. + 결합 연산자
print("aaa" + "bbb")

# 2. * 반복 연산자
print("nice" * 5)

# 3. [] 인덱싱/슬라이싱 연산자
s = "Hello world"
print(s[2]) # l  인덱싱
print(s[2:8]) # llo wo  슬라이싱
print(s[2:]) # 2 ~ 끝
print(s[:5]) # 시작 ~ 5번
print(s[-2]) # l 뒤에서 2번

# 문자열의 길이(length)][글자수]를 알려주는 파이썬의 내장함수
a = len(s)
print("글자수 :", a)

# 문자열 데이터가 가진 유용한 기능 함수들 알아보기
# 1) "".format() - 특정한 서식모양으로 문자열을 만들어주는 기능

# 2) upper(), lower() - 대소문자 변환 기능
print("Hello".upper())
print("Hello".lower())

# 문자열을 변수에 대입하여 저장하면 변수명으로 기능 사용 가능
word = "Machine Learning"
print(word.upper())
print(word.lower())

# 3) .strip() - 문자열의 양옆 
word = "   Hello   "
print("[" + word + "]")
print("[" + word.strip() + "]")

# 겁색어 비교 또는 아이디 비교 작업할 때 실수로 공백제거 후 비교함
print( word.strip() == "Hello")

# 4.find() : 특정 문자의 인덱스 번호 위치를 찾아주기
s = "Hello world. android. iso. aI. world"
print(s.find("world")) #찾은 글씨의 첫글자 인덱스 번호 [6]
print(s.find("ANDROID")) # 대소문자 구별 [못찾으면 -1]

# 혹시 같은 문자가  여러개면 앞에서부터 검색하기에 앞에 번호만 맞음
# 뒤에 있는 문자도 찾으려면 추가 find
idx = s.find("world") # 6
print(s.find("world", idx + 1)) # 앞에 찾은 글씨 인덱스 번호 다음부터 다시 찾기 31

# 5. in 연산자 - 특정 문자가 그 문자열 안에 있는지 여부(True / False)를 알려주는 연산자
print("world" in s) # s변수가 가진 문자열안에 "world" 라는 글씨가 있는지
print("WORLD" in s) # False

# 대소문자 구분없이 특정 문자의 존재 여부를 알고싶다면
print("WORLD" in s.upper())

# 6. replace - 글자 바꾸기
s = "Hello world. nice world. good world"

# world 글씨들을 python 이라는 글씨로 변경해서 출력
print(s.replace("world", "python"))
print(s.replace("WorLD", "coding")) # 바꿀 글씨가 없으면 그대로

# 대소문자 상관없이 찾아서 바꾸기
print(s.replace("WorLD".lower(), "coding"))

# replace를 이용하면 글씨 사이의 공백문자(띄어쓰기) 제거 가능
aa = s.replace(" ", "")
print(aa)
aa = s.replace("\n", "")
print(aa)

# 7) .split() : 특정 문자를 기준으로 글씨를 나누어서 [리스트]로 만들어주는 기능함수
csv = "sam,20,seoul"
aaa = csv.split(",")

print(aaa[0])
print(aaa[1])
print(aaa[2])

# 8) isXXX() 기능함수들
# 8.1] 알파벳으로만 이루어 졌는가
print("Hello".isalpha()) # True
print("Hello123".isalpha()) # False
print("Hello안녕하세여".isalpha()) # True

# 8.2] 숫자로 이루어 졌는가 (숫자 + 로마숫자 + 윗첨자) -> int() 형변환이 가능한지 확인 가능
print("1234".isnumeric()) # True
print("1234abc".isnumeric()) # False
print("Ⅳ".isnumeric()) # True
print("4²".isnumeric()) # True

# 8.3] 숫자만 허용 [아라비아숫자 + 윗첨자]
print("1234".isdigit()) # True
print("Ⅳ".isdigit()) # False
print("4²".isdigit()) # True

# 8.4] 오직 아라비아 숫자만 허용
print("1234".isdecimal()) # True
print("Ⅳ".isdecimal()) # False
print("4²".isdecimal()) # False

# 8.5] 알파벳 + 숫자로만 이루어 졌는가 (특수문자 제외)
print("Hello123".isalnum) # True
print("Hello 123".isalnum) # False

# 8.6] 소문자만 [띄어쓰기 가능]
print("Hello world".islower()) # False
print("hello world".islower()) # True

# 9) count() - 문자열안에 특정 단어가 몇개인지 알려주는 기능함수
message = """EDA(Exploratory Data Analysis) : 탐색적 데이터 분석.
data를 다양한 각도에서 관찰하고 이해하는 첫번째 단계. 
시각화와 통계적 기법을 사용하여 Data를 분석합니다 """

print("data 라는 문자의 개수 :", message.count("data")) # 1개
print("data 라는 문자의 개수 :", message.lower().count("data")) # 3개

# 위 9개 말고도 문자열에는 많은 기능함수들이 존재함
# 나머지는 필요할때 검색해서 사용함

