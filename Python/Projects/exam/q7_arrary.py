
#1
li = []
total = 0

for i in range(5):
    val = int(input("정수 입력 : "))
    li.append(val)
    total = total + val


print(li, "최대값 : ", max(li))
print(li, "최소값 : ", min(li))
print(li, "총 합 : ", total)

#2
st = []

num = int(input("정수 입력 : "))

for i in range(num):
    st.append(input("문자 입력 : "))

for s in st:
    print(s)

#3
score_list = []
result = ""

num = int(input("학생의 수를 입력하시오 : "))

i = 1
while True:

    if i >= 3:
        break

    std = int(input("학생 {}의 성적을 입력하세요 : ".format(i + 1)))

    if std > 100 or std < 0:
        print("잘못된 성적입니다. 다시 입력하시오")
        continue

    score_list.append(std)
    result = result + "학생 {}의 성적 : {}".format(i + 1, std) + "\n"

    i = i + 1

print("--------------------")
print(result, end="")
print("--------------------")
print("성적 평균은 {:.2f} 입니다.".format(sum(score_list) / num))

#4
list1 = [10, 20, 30, 40 ,50]
list2 = [1, 2, 3, 4, 5]
list3 = []

for i in range(len(list1)):
    list3.append(list1[i] + list2[-i -1])

for li in list3:
    print(li)

#5
scores = [85, 90, 78, 92, 68]
scores_sort = sorted(scores)
scores_80up = []
scores_p5 = []

for li in scores:
    if li >= 80 :
        scores_80up.append(li)

for li in scores:
    scores_p5.append(li + 5)

# 출력
print("평균 점수 : {}".format(sum(scores) / len(scores)))
print("가장 높은 점수 : {}, 가장 낮은 점수 : {}".format(max(scores), min(scores)))
print("오름차순 : {}".format(scores_sort))
print("80점 이상인 점수 : {}".format(scores_80up))
print("점수에 전부 5점씩 추가 : {}".format(scores_p5))

#6
point1 = (2, 3)
point2 = (5, 7)

result = (abs(point2[0] - point1[0]) ** 2 + abs(point2[1] - point1[1]) ** 2) ** (1 / 2)

print("{}, {} -> 두 점 사이의 거리 : {}".format(point1, point2, result))

#7
phone_book = {
"홍길동": "010-1234-5678",
"김철수": "010-9876-5432",
"이영희": "010-5555-6666"

}

phone_book["박민수"] = "010-1111-2222"
phone_book["김철수"] = "010-9999-0000"
del phone_book["이영희"]
print(phone_book.keys())
print(phone_book.values())
print(phone_book[input("이름 입력 : ")])

#8 - 수정(format) +
rng = 100
step = 10
list_key = []
dict_result = {}

input_num = [3,10,22,33,44,55,23,66,88,12,2]

#key 생성
for i in range(rng // step):

    s = str(i * step + 1) + " - " + str((i + 1) * step)

    list_key.append(s) 
    dict_result[s] = 0

# value 값 넣기
for num in input_num:
    location_key = (num - 1) // step

    dict_result[list_key[location_key]] = dict_result[list_key[location_key]] + 1

# 출력
for key, val in dict_result.items():
    print("{:8s} : {}".format(key, "*" * val))


#9
seat_status = {}
seet_total = 10

for i in range(seet_total):
    seat_status[str(i)] = 0


while True:

    s_chk = input("좌석을 예약하시겠습니까( 1(Y) 또는 0(N) )?")

    # 종료 조건
    if s_chk == "0" or s_chk.lower() == "n":
        break

    # 좌석 상황 출력
    print("현재의 예약 상태는 다음과 같습니다.")
    print("----------------------------------------")
    print("좌석 번호 : ", str(seat_status.keys()).replace("dict_keys([", "").replace("])", "").replace("'", "").replace(",", " "))
    print("----------------------------------------")
    print("예약 상태 : ", str(seat_status.values()).replace("dict_values([", "").replace("])", "").replace("'", "").replace(",", " "))

    s_seat = input("몇번째 좌석을 예약하시겠습니까?")

    # 예매 출력
    if seat_status[s_seat] == 0:
        print("{}번 좌석 예약되었습니다.".format(s_seat))
        seat_status[s_seat] = 1

    else:
        print("죄송합니다. 이미 예약된 좌석입니다. 다른 좌석을 선택해 주세요.")

#10
class_count = 3
class_grade = {}
grade_result = [0, 0, 0]
grade_good = ""

# 데이터 입력
for cls in range(1, class_count + 1):
    key_val = str(cls) + "반"
    class_grade[key_val] = []

    std_total = int(input("[{}] 인원 수 입력 : ".format(key_val)))

    for std in range(1, std_total + 1):
        grade = int(input("[{} {}번] : ".format(key_val, std)))
        class_grade[key_val].append(grade)

# 반 성적 출력
print("--- Python Programming 성적표 ---- ")

for key, val in class_grade.items():
    s_grade = ""

    for grade_val in val:
        s_grade = s_grade + " " + str(grade_val)

    print("[{}] {} [평균 : {}]".format(key, s_grade, sum(val) / len(val)))

    # 전체 성적, 전체 학생 수 저장 + 최우수 반 확인
    grade_result[0] = grade_result[0] + sum(val)
    grade_result[1] = grade_result[1] + len(val)

    if grade_result[2] < (sum(val) / len(val)):
        grade_result[2] = sum(val) / len(val)
        grade_good = key
    
print("-----------------------")

# 전체 평균, 최우수 반 출력
print("전체 평균 : {}".format(grade_result[0] / grade_result[1]))
print("최우수 반 : [{}]".format(grade_good))

#11
class1 = {"홍길동", "김철수", "이영희", "박민수"}
class2 = {"이영희", "김철수", "최지훈", "정은비"}

print("전체 참여자 명단(중복제거) : ", class1 | class2)
print("두 반 모두 참여한 학생 : ", class1 & class2)
print("1반만 참여한 학생 : ", class1 - class2)
print("2반만 참여한 학생 : ", class2 - class1)