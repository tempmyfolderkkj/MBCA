
# 3. Dictionary {} - 리스트처럼 요소의 추가/삭제/변경 모두 가능 [단, 인덱스 번호 대신에 원하는 "식별자"로 요소를 구별함]

# {"key" : "value", "key" : "value"}
ccc = {"name":"sam", "age": 20, "address" : "seoul"}
print(ccc)
print(type(ccc))

# 요소 개별값 사용 - "식별자" key 사용
print(ccc["name"])
print(ccc["age"])
print(ccc["address"])

# 요소값 변경
ccc["age"] = 25
print(ccc["age"])

# 요소 추가
ccc["email"] = "aaa@aaa.com"
print(ccc)

# 요소 제거
del ccc["email"]
print(ccc)

# 요소 모두 삭제
ccc.clear()
print(ccc)

# in 연산자 - 값을 찾는게 아니라 식별자를 찾아서 그 안의 값에 접근해야함
ccc = {"name":"robin", "age": 25, "address" : "busan"}

if "name" in ccc:  # 식별자만 확인 가능
    print("name :", ccc["name"])

# 만약 존재하지 않은 식별자를 사용하면 error
#print(ccc["tel"]) - error

# 에러가 걱정이라면 in 연산자로 검사해야 하지면 번거로움
# 그래서 특정 식별자의 값을 []로 접근하지 않고 값을 얻어주는 기능함수 get()를 활용

value = ccc.get("adrress")
print(value)

value = ccc.get("tel") # 없는 key를 사용하면 None 값을 줌
print(value)


for key in ccc:
    print(ccc[key])


# 딕셔너리의 (key, value) 쌍을 가지고 있는 Item이라는 녀석으로 for 사용
items = ccc.items()
print(items)

for item in items:
    print(item)
    key, value = item
    print(key, value)








































































































