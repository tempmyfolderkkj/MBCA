
# 파이썬에서 대량의 데이터를 다루는 문법 [ List, Tuple, Dictionary, {Set} ]

# 1. List 
aaa = [70, 80 ,90]
print(aaa)
print(aaa[0])
print(aaa[1])
print(aaa[2])

# 요소의 개수가 많으면 인덱스 번호를 직접 쓰기 불편함 -> 반복문으로 인덱스번호를 자동으로 증가되도록
aaa = [10,20,30,40]
for n in range(4):
    print(aaa[n])

# for 문법의 대량의 데이터에서 요소를 반복적으로 뽑아오는 것임, aaa리스트의 요소를 뽑는 것이 더 간단함
for e in aaa:
    print(e)

# 역순으로 출력하고 싶다면
for n in range(3, -1, -1):
    print(aaa[n])

# 역순2번째 방법
for n in range(4):
    print(aaa[3 - n])

# 1 ~ 3 번 요소만 출력 [범위 출력]
for n in range(1, 4):
    print(n)

# 모든 요소값들에 1을 더한 값을 출력
for e in aaa:
    print(e + 1)

# 모든 요소의 값을 더한 총합계산
total = 0
for e in aaa:
    total = total + e

print(total)

# 리스트의 요소들 중에서 가장 큰 값 출력
m = aaa[0]
for n in range(1, 4):
    if m <= aaa[n]:
        m = aaa[n]

print(m)

m = 0
for e in aaa:
    if m <= e:
        m = e

print(m)

print(max(e))


# 요소값 변경 - 인덱스 번호 사용
aaa[0] = 100
print(aaa[0])

# 요소 추가 - append(), insert()
# aaa[4] = 50 -> 파이썬은 이런 방식으로 추가시 error 발생
aaa.append(50) # 50이라는 값을 리스트의 마지막에 추가
print(aaa)

aaa.insert(1, 600) # 1번 인덱스 위치에 600 이라는 값을 삽입
print(aaa)

# 요소 삭제 - remove(), del 연산자, clear()
aaa.remove(100) # 100이라는 값을 가진 요소를 제거
print(aaa)

del aaa[2] # aaa[2] 요소를 제거

aaa.clear() # aaa 요소들 전부 삭제
print(aaa)

# 요소의 개수를 알려주는 파이썬의 내장 기능 함수 len()
print("요소 개수 :", len(aaa))

# 요소들의 자료형이 달라도 상관 없음
aaa = [10, 3.14, False, "sam"]
print(aaa)

# 반복문으로 접근 가능
for e in aaa:
    print(e)

# 리스트가 가진 유용한 여러 기능함수들   -> reverse(), sort(), index(), in, count(), pop[], extend == +
# 1) 요소의 순서를 뒤집기
print(aaa)
aaa.reverse() # 원본 리스트가 변경됨
print(aaa)

# 2) 요소 정렬
aaa = [4, 15, 7, 2, 4, 16, 10]
aaa.sort()
print(aaa)

# 3) 요소 중 특정 값의 인덱스 번호(위치) 얻어오기
idx = aaa.index(16)  # 16이라는 숫자가 있는 위치번호
print(aaa)

# 4) 특정값이 리스트안에 있는지 여부 in 연산자
print( 7 in aaa)
print( 70 in aaa)
print(not 7 in aaa)


# 5) 특정값이 리스트안에 몇개 인지
print(aaa.count(4), "개")

# 6) 특정값을 꺼내오기 -> 원본에서 없어짐
n = aaa[2]
print(n)
print(aaa)

n = aaa.pop[2]
print(n)
print(aaa)

# 7) 다른 리스트를 한방에 추가하기
aaa = [10, 20, 30]
bbb = [4, 5, 6]

aaa.extend(bbb)
print(aaa)

# .extend() 기능 잘 사용안함. +연산을 하면 리스트 확장 기능이 발동함
ccc = [700, 800, 900]
ccc = aaa + ccc
print(ccc)

# -------------------------------------------------

# 2차원 리스트 -- 리스트의 요소가 또 다른 리스트인 것
aaa = [ [10, 20, 30], ["aa" "bb", "cc"], [3.14, 12.2, 300, 500] ]

bbb = [ [10, 20, 30], 
        ["aa" "bb", "cc"],
        [3.14, 12.2, 300, 500] ]

print(aaa)
print(aaa[0][0]) 
print(aaa[1][2]) 

# len() 기능은 리스트의 요소 개수를 알려줌
print(len(aaa)) # 3
print(len(aaa[1])) # 3 -> "aa", "bb", "cc"
print(len(aaa[1][1])) # 2 -> "aa"

for n in range(len(aaa)):
    for k in range(len(aaa[n])):
        print(aaa[n][k], end="\t")

    print()

for row in aaa:
    for col in row:
        print(col, end="\t")

    print

# 리스트를 사용하여 여러데이터를 다루는 예제 2개
# 예1) 학생 성적들의 총합과 평균
scores_list = [80, 75, 64, 90, 50]
total = 0

for score in scores_list:
    total = total + score

print("총합 : {}, 평균 : {}".format(total, total / len(scores_list)))

# 예2) 일주일의 온도 중에서 가장 더운 날의 온도와 요일 (데이터의 순서 : [월, 화, 수, 목, 금, 토, 일])
week_temparature = [15, 15, 8, 14, 9, 6, 10]
week = ["월", "화", "수", "목", "금", "토", "일"]
highest = week_temparature[0]
day = ""

for i in range(len(week_temparature)):
    
    if highest <= week_temparature[i]: 
        highest = week_temparature[i]
        day = day + week[i] + ","

print("최고 온도 :", highest)
print("가장 더운 날 :", day[:-1])















