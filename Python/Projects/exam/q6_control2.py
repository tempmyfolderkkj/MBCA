#234

# 5.11
visited = "오늘 방문자 수는 350명이었고, 어제는 280명이었다."
num_today = ""
num_yester = ""

location = visited.find(",")
for str in visited[:location]:
    if str.isdigit():
        num_today = num_today + str

for str in visited[location:]:
    if str.isdigit():
        num_yester = num_yester + str

if int(num_today) >= int(num_yester):
    print(int(num_today) - int(num_yester), "증가")

else:
    print(int(num_yester) - int(num_today), "감소")

# 5.12
content = input("입력 : ")
s = ""
location = 0
location_end = 0
result = ""

if len(content) >= 30:
    result = "긴 문장, "

for i in range(content.count(" ") + 1):
    location = location_end
    location_end = content.find(" ", location_end + 1)
    s = content[location:location_end]

    if location_end == -1:
        s = content[location:]

    if s[-1] == "!":
        result =  "감탄 문장, " + result

    if s[-1] == "?":
        result = "의문 문장, " + result

for i in range(1, 10):
    if str(i) in content:
        result = result + "숫자 포함 문장, "
        break

print("출력 : "+ result[:-2])

# 1
num = int(input("정수 입력 : "))

for i in range(num):
    print("Hello World!")

# 2
num = int(input("정수 입력 : "))
result = ""

for i in range(1, num + 1):
    result = result + " " + str(i * 3)

print(result)

# 3
total = 0

while True:
    num = int(input("정수 입력 : "))

    if( num == 0):
        break

    total = total + num

print(total)

# 4
num = int(input("정수 입력 : "))

for i in range(9, 0, -1):
    print("{} x {} = {}".format(num, i, num * i))

# 5
num = int(input("입력 값 갯수 : "))
total = 0

for i in range(num):
    total = total + int(input("정수 입력 : "))

print("평균 :", total / num)

# 6
total = 0
i = 0

while i < 5:
    num = int(input("정수 입력 : "))

    if num >= 1:
        i = i + 1
        total = total + num
    
print(total)

# 7
for i in range(5):
    print(("o" * i) + "*")


# 8
for i in range(1, 100):
    
    if i % 7 == 0:
        print(i)

    elif i % 9 == 0:
        print(i)

# 9
val = input("단어 입력 : ")
location_str = 0
location_end = 0

for i in range(val.count(",") + 1):
    location_str = location_end
    location_end = val.find(",", location_str + 1)

    if location_end == -1:
        location_end = len(val)

    s = val[location_str + 1:location_end]

    if len(s) >= 5:
        print(s)

# 10
for i in range(2, 10):

    if i % 2 == 1:
        continue

    for i2 in range(1, 10):
        print("{} x {} = {}".format(i, i2, i * i2))

        if i2 == i:
            break

