
#1
num = int(input("정수 입력 : "))

if num >= 0:
    print("입력한 값의 절대값 :", num)
else:
    print("입력한 값의 절대값 :", -num)

print("입력한 값의 절대값 :", abs(num))

#2
num1 = int(input("정수 입력 : "))
num2 = int(input("정수 입력 : "))

if num1 >= num2 : 
    print("{}, {} 중에 작은 값 : {}".format(num1, num2, num2))
else:
    print("{}, {} 중에 작은 값 : {}".format(num1, num2, num1))

#3
a = int(input("정수 입력 : "))
b = int(input("정수 입력 : "))
c = int(input("정수 입력 : "))
max = 0

if a > b and a > c:
    max = a
    
elif b >= c:
    max = b

else:
    max = c

print("{}, {}, {} 중에서 가장 큰 값은 {}".format(a, b, c, max))

#4
num1 = int(input("정수1 입력 : "))
num2 = int(input("정수2 입력 : "))

if num1 >= num2:
    print("{}, {} 차이 값 : {}".format(num1, num2, (num1 - num2)))
else:
    print("{}, {} 차이 값 : {}".format(num1, num2, (num2 - num1)))

print("{}, {} 차이 값 : {}".format(num1, num2, abs(num1 - num2)))

#5
num1 = int(input("정수1 입력 : "))
num2 = int(input("정수2 입력 : "))

print("{}, {} 차이 값 : {}".format(num1, num2, (num1 - num2))) if num1 >= num2 else print("{}, {} 차이 값 : {}".format(num1, num2, (num2 - num1)))

#6
saved_id = "python"
saved_pw = "1234"

in_id = input("saved_id = ")
in_pw = input("saved_pw = ")

if in_id == saved_id and in_pw == saved_pw:
    print("로그인 성공")

else:
    print("로그인 실패")

#7
num = int(input("정수 입력 : "))

if num >= 80 and num <= 100:
    print("높음")
    
elif num >= 50 and num < 80:
    print("보통")

elif num >= 0 and num < 50:
    print("낮음")

else:
    print("범위를 벗어남")

#8
str = input("문장 입력 : ")

if "error" in str.lower():
    print("오류 포함")

else:
    print("정상")

#9
num1 = int(input("정수1 입력 : "))
num2 = int(input("정수2 입력 : "))
num3 = int(input("정수3 입력 : "))

print("입력 받은 정수 : {}, {}, {}".format(num1, num2, num3))

if num1 > num2 and num1 > num3:
    print("세 수 중 가장 큰 값 :", num1)

elif num2 >= num3:
    print("세 수 중 가장 큰 값 :", num2)

else:
    print("세 수 중 가장 큰 값 :", num3)

print("세 수의 평균 : ", ((num1 + num2 + num3) / 3))

if (num1 + num2 + num3) / 3 > 70:
    print("통과")

else:
    print("불합격")

if isinstance((num1 + num2 + num3) / 3, int):
    print("정수 평균")

else:
    print("실수 평균")

#10


#10 ?
file_name = input("파일명 입력 : ")
out_val = ""

if "2025" in file_name:
    out_val = out_val + "올해 파일, "

if "report" == file_name[:6]:
    out_val = out_val + "보고서 유형, "

if ".csv" == file_name[-4:]:
    out_val = out_val + "csv 데이터 파일"

print(out_val)

#11
visited = "오늘 방문자 수는 350명이었고, 어제는 280명이었다."
cnt_today = 0
cnt_yester = 0
result = ""


location1 = 0
location2 = visited.find("명") + 1
location1_end = visited.find("명")
location2_end = visited.find("명", start:=visited.find("명") + 1)

# today 찾기
if visited.find(" ", start:=location1 + 1) < location1_end:
    location1 = visited.find(" ", start:=location1 + 1)

    if visited.find(" ", start:=location1 + 1) < location1_end:
        location1 = visited.find(" ", start:=location1 + 1)

        if visited.find(" ", start:=location1 + 1) < location1_end:
            location1 = visited.find(" ", start:=location1 + 1)

            if visited.find(" ", start:=location1 + 1) < location1_end:
                pass

    cnt_today = int(visited[location1:location1_end])

if visited.find(" ", start:=location2 + 1) < location2_end:
    location2 = visited.find(" ", start:=location2 + 1)

    if visited.find(" ", start:=location2 + 1) < location2_end and not visited.find(" ", start:=location2 + 1) == -1:
        location2 = visited.find(" ", start:=location2 + 1)
    
        if visited.find(" ", start:=location2 + 1) < location2_end and not visited.find(" ", start:=location2 + 1) == -1:
            location2 = visited.find(" ", start:=location2 + 1)

            if visited.find(" ", start:=location2 + 1) < location2_end and not visited.find(" ", start:=location2 + 1) == -1:
                pass

    cnt_yester = int(visited[location2:location2_end])


if cnt_today >= cnt_yester:
    result = str(cnt_today - cnt_yester) + " 증가"

else:
    result = result = str(cnt_yester - cnt_today) + " 감소"

print("오늘 : {}, 전날 : {}, 차이 {}".format(cnt_today, cnt_yester, result))

#12

#str = input()
str = "Python is amazing! 123"
location = 0
result = ""

if str.find(" ", start:=location + 1) < len(str) and not str.find(" ", start:=location + 1) == -1:
    location = str.find(" ", start:=location + 1)
    
    if "!" in str[location - 1]:
        result = result + "감탄 문장, "

    if "!" in str[location - 1]:
        result = result + "의문 문장, "
    
    elif str.find(" ", start:=location + 1) < len(str) and not str.find(" ", start:=location + 1) == -1:
        location = str.find(" ", start:=location + 1)

        if "!" in str[location - 1]:
            result = result + "감탄 문장, "

        if "!" in str[location - 1]:
            result = result + "의문 문장, "

        elif str.find(" ", start:=location + 1) < len(str) and not str.find(" ", start:=location + 1) == -1:
            location = str.find(" ", start:=location + 1)

            if "!" in str[location - 1]:
                result = result + "감탄 문장, "

            if "!" in str[location - 1]:
                result = result + "의문 문장, "

if len(str) >= 30:
    result = result + "긴 문장, "

# if "%d" in str:
#     result = result + "숫자 포함 문장, "

print(result[:len(result)-2])

