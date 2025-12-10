
# Tuple () -> 리스트와 비슷한데 요소의 값변경/요소추가/요소삭제 모두 불가능

bbb = (10, 20, 30)
print(bbb)
print(type(bbb))

# 요소 값 사용하는 방법 - 인덱스 번호
print(bbb[0])
print(bbb[1])

# 값 변경/요소추가/삭제 모두 불가능
#bbb[0] = 100 -> error
#bbb.append(50) -> error
#bbb.clear() -> error

for value in bbb:
    print(value + 1)

# 특이하게 튜플 생성 방법 - 권장x
bbb = 10, 20, 30 # -> 파이썬은 알아서 튜플로 생성
print(type(bbb))

# 반대로 튜플의 요소값들을 여러개의 변수로 분리해서 대입하는 것이 가능(ML 작업할때 애용)
a, b, c = (10, 20, 30)
print(a, b, c)

bbb = (11, 22, 33)
a, b, c = bbb   # 요소들이 분해되서 각 변수에 대입됨
print(a, b, c)

#z, x = (10, 20, 30) -> error 개수가 다르면 error

















































































