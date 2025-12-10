
# 파이썬의 표준(내장) 함수 중 활용이 많은 15개 정도 소개

#1. print() - 데이터를 화면에 출력

#2. input() - 키보드로부터 문자열로 데이터를 입력

#3. type() : 데이터 또는 변수의 타입을 리턴

#4. len() : 문자열이나 리스트등의 길이를 알려주는 기능함수

#5. sum() - 반복 가능한 데이터의 모든 요소 합을 리턴

#6. min(), max() - 최솟값, 최대값 리턴

#7. abs() - 절대값 리턴

#8. range() - 지정된 범위의 숫자 시퀀스를 만들어 줌

#9. list() - 다른 형태의 iterable(반복할수있는) 객체들을 모두 list 타입으로 변환
aa = list('hello')
print(aa) # [h, e, l, l, o]
bb = list({'name':'sam','age':20})
print(bb) # [name,age]

#10. map() - 반복 가능한 객체의 각 요소애 특정 함수를 적용한 결과 리스트를 리턴
aaa = [10, 20, 30]
bbb = map(lambda n:n * 2, aaa)
print(list(bbb))

#11. filter() - 반복 가능한 객체의 각 요소에 특정 함수의 조건값이 True인 결과 요소만 뽑아서 리스트를 리턴
aaa = [100, 50, 40, 85, 60]
bbb = filter(lambda n:n >= 50, aaa)
print(list(bbb))

#12. sorted() - 반복 가능한 객체의 정렬된 새로운 리스트를 반환
aaa = [40, 23, 79, 5, 1500, 72]
bbb = sorted(aaa)
ccc = sorted(aaa, reverse=True)
print(bbb)

#13. enumerate() - 순서가 있는 자료형(리스트, 튜플)에 인덱스 값을 포함하는 튜플(index, value)로 리턴해주는 기능
aaa = ['sam', 'robin', 'hong']
for t in enumerate(aaa):
    a, b = t
    print(a, b)

for idx, value in enumerate(aaa):
    print(idx, value)

#14. zip() - 여러개의 리스트의 요소들을 병렬로 묶어서 튜플의 반복자를 만들어냄
name_list = ['sam', 'robin', 'hong', 'park']
age_list = [20, 23, 28, 15]
people = zip(name_list, age_list)
print(list(people))

# 튜플데이터를 사전(dictionary) 타입으로 바꿀 수 있음
people = zip(name_list, age_list)
vvv = dict(people)

#15. any(), all()
# any() = 요소 중에 하나라도 조건에 맞으면 True
limit = 3
ccc = [1, 2, 3, 6, 5, 8]
# 요소들 중에 하나라도 limit 보다 작은 값이 있는가
print(any( n < limit for n in ccc))

# all - 모든 요소가 조건에 맞아야 True
print(all( n < limit for n in ccc))

#16. 형변환 연산자들 - int(), float(), str(), bool(), list(), tuple(), dict(), set()

# 파이썬의 타입 2종류
# 1. 기초 타입 : int, float, str, bool                          [데이터를 저장하는 변수]
# 2. 참조 타입 : list, tuple, dict, set, object 등 나머지 모두    [객체의 주소를 저장하는 변수]

# 기초 타입 상황
a = 10
b = a
print(a)
print(b)

b = 50
print(a)
print(b)

# 참조 타입 상황

aaa = [100, 200, 300]
bbb = aaa  # list(aaa) 안바뀜

print('aaa =',aaa)
print('bbb =', bbb)

bbb[1] = 5000
print('aaa =', aaa)

