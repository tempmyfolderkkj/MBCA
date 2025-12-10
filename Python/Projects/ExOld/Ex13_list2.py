
# 리스트를 생성하는 특별한 문법 [ 리스트 내포 - list comprehensions]
# 반복문으로 리스트의 요소를 만들때 한줄로 간결하게 만들 수 있는 문법

# 1] 기존 방식대로 반복문으로 리스트 생성
aaa = []

for n in range(1, 10):
    aaa.append(n)

bbb = [n for n in range(1, 10)]
print(bbb)

ccc = [n * 10 for n in range(1, 10)]
print(ccc)

ddd = [n **2 for n in range(1, 10)]
print(ddd)

# 60점 미만은 걸러내기
score_list = [48, 100, 85, 82, 64, 23, 5, 18]
eee = []

for score in score_list:
    if score >= 60:
        eee.append(score)
print(eee)

eee = [score for score in score_list if score> 60] # 실제 데이터분석이나 ML 작업할때 필터링을 위해 자주 활용되는 문법

# 사용자의 입력된 숫자 만큼 빈 리스트의 요소를 만들기
num = ""
ggg = [0 for n in range(num)]

# 가장 쉽게 순차적인 값을 가지는 리스트 생성하는 방법 = 리스트를 만들어 주는 함수 list()
hhh = [1, 2, 3, 4, 5]
for v in hhh:
    print(v)

kkk = list(range(1, 6))
print(kkk)




# 리스트를 다루는 특별한 문법과 기능함수들

# 1) list 나 tuple 요소들 중 최소값, 최대값, 합계를 구해주는 함수
score_list = [48, 100, 85, 82, 64, 23, 5, 18] 
print("최솟값 :", min(score_list))
print("최댓값 :", max(score_list))
print("총합 :", sum(score_list))
print("평균 :", sum(score_list) / len(score_list))

# 딕셔너리는 key를 계산함 그러니 사용 안함
aaa = {"a" : 10, "b" : 20, "c" : 30}
print(min(aaa)) # a b c


# 2) 리스트나 튜플의 for 반복할때 인덱스 번호와 값을 동시에 주는 함수
aaa = ["sam", "robin", "hong", "park"]

for value in aaa:
    print(value)

for idx, value in enumerate(aaa):
    print(idx, ":", value)


# 3) 요소의 순서를 뒤바꾸는 함수 reversed() - 원본리스트는 변경되지 않고 뒤바뀐 새로운 배열을 리턴해줌
aaa =[10, 20, 30, 40, 50]
bbb = reversed(aaa)  # aaa리스트의 요소 위치를 바꾸어 새로운 리스트를 만들어주는 객체를 줌 - range()같은

print(aaa)
for v in bbb:
    print(v)

# for문 대신 리스트로 만들기
ccc = list(reversed(aaa))
print(ccc)

# python 3버전 이상에서 완전 도입된 {Set} 자료형 - 집합
# 중복된 값이 저장되지 않음
aaa = {10, 20, 30, 40 ,50, 40, 20}
print(aaa)

bbb = [10, 50, 50, 123]
ccc= set(bbb)

# set 주요연산자 -> 합집합[union()] |, 교집함[intersection()] &
