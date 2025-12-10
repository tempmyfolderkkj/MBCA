#327p

# 파일 처리(입출력)를 위한 파이썬의 표준 내장 함수

#1. 파일에 데이터를 저장하기 - 파일명을 경로없이 쓰면 이 .py파일이 있는 곳과 같은 위치에 만들어짐
file = open("aaa.txt", "w", encoding="UTF-8") #  mode : "w" write, "a" append, "r" read

file.write("This is python programming 한글")

#파일쓰기 작업이 종료되면 반드시 스트림을 닫아야함
file.close()

# 2. 파일에서 텍스트 데이터 읽어오기
file = open("aaa.txt", "r", encoding="UTF-8") # 파일명이 없으면 안읽어짐

contents = file.read()
print("파일에서 읽은 텍스트 : ", contents)

file.close()

# 3. 파일 이어쓰기 append mode
file = open("bbb.txt", 'a', encoding='UTF-8')
file.write('apple')
file.write('banana')
file.write('orange')
file.close()


file = open("ccc.txt", 'a', encoding='UTF-8')
file.write('apple\n')
file.write('banana\n')
file.write('orange')
file.close()

# 사용자로부터 한줄 리뷰를 계속 입력받기, 'quit'를 입력시 종료 하도록
file = open('ddd.txt', 'a', encoding='UTF-8')

while True:
    message = input('리뷰 입력 : ')

    if message.lower() == 'quit':
        break

    file.write(message + '\n')
    
# 4. 파일경로에 폴더명
file = open('files/aaa.txt', 'w') #files 폴더 안에

# 5. 문자열 중에 여러 문자열
file = open('eee.txt', 'a')
a = ('''
asd
asf
asd
'''
)
file.write(a)
    

# 6. 리스트 데이터 저장
names = ['강종구', '김종경', '유자희', '최준영']

file = open('files/902호 학생들.txt', 'w', encoding='UTF-8')
file.writelines(names) # 줄바꿈을 자동으로 해주지 않음 [해결은 원본 데이터들에 줄바꿈 문자를 추가해서 저장]
file.writelines(list(map(lambda s:s+'\n', names))) # 줄바꿈
file.close()

# 7. with 키워드 -> 파일을 다룰때 주의할점 close()를 잊지 않아야하는데 이를 보완하는 특별한 키워드

with open('ggg.txt', 'w') as file:
    file.write('hello python')

# close()를 안해도 자동으로 with 영역이 종료되면 file객체에게 close()를 요청해줌

# 8. 아주 긴 파일을 읽어와서 출력해보기

with open('files/long story.txt', 'r', encoding='UTF-8') as file: # encoding - 'utf-8', 'utf-16,'cp949'(ANSI), 'ecu-kr
    contents = file.read()
    print(contents)

# 9. 대량의 데이터를 파일로 부터 읽어서 분석하려면 일단 대두분의 경우 한철철아
with open('files/short story.txt', 'r', encoding='UTF-8') as file: # encoding - 'utf-8', 'utf-16,'cp949'(ANSI), 'ecu-kr
    line = file.readline()
    print(line)

# 1o
# 데이터셋 파일들은 엑셀형태가 많음 -> 엑셀파일을 읽어서 데이터를 분석
# 파이썬 표준함수에는 excel 파일을 읽을수 있는 기능함수가 없음

# 대부분의 분석할 데이터들을 표형태(행 row, 열 colum 구조)를 가지고 만들어짐
# 이를 위해 등장한 데이터표기형식(csv, xml, json)
with open('files/member.scv', 'r', encoding='utf-8') as file:
    # contents = file.read() 
    # 보통의 표 형태의 데이터 구조는 한줄에 한 아이템의 정보들이 존재함
    # 그래서 한줄 단위로 읽어서 처리
    is_header=True
    for line in file: # 자동으로 readline()을 하면서 반복수행함
        print(line)

        if is_header:
            is_header = False
            continue

        # 한줄 안에 있는 여러개의 데이터를 분리해서 취득하기 - csv 분석(parse)
        data_list = line.split(',')
        print('이름 :', data_list[0])
        print('나이 :', data_list[1])
        print('주소 :', data_list[2])

        #인덱스 번호로 칸의 의미를 해석하기 불편 - 리스트의 요소를 분해하여 변수에 대입
        name, age, address = data_list
        print('이름 :', name)
        if age.isdigit():
            print('나이 :', int(age) + 1)
        else:
            print('나이 :', age)
        print('주소 :', address)


#[추가] mode 지정할 때 '+' 기호

#1) w+ (읽기 + 쓰기 모두 가능)
with open('files/ggg.txt', 'w+', encoding='utf-8') as file:
    file.write('next data')
    # 파일커서의 위치가 글씨의 마지막에 있어서 그냥 읽으면 이후 데이터 없음
    file.seek(0)
    contents = file.read()
    print(contents)


#2) a+ (읽기 + 쓰기)
#3) r+




















































