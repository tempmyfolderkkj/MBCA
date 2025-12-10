

#1
name = input("이름 > ")
food = input("음식 > ")

print("안녕하세요! 저는 {}입니다.".format(name))
print("좋아하는 음식은 {}입니다.".format(food))

#2
name = input("이름 > ")
age = input("나이 > ")
hobby = input("취미 > ")

print("제 이름은 {}이고, 나이는 {}살입니다. ".format(name, age))
print("제 취미는 {}입니다.".format(hobby))

#3
name = "철수"
age = 15
height = 165.3
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

#4
num1 = 10
num2 = 3 

print("덧셈 결과:", num1 + num2)
print("뺄셈 결과:", num1 - num2)
print("곱셈 결과:", num1 * num2)
print("나눗셈 결과:", num1 / num2)

#5
country = "한국"
city = "서울"
year = 2025

print(f"{year}년에 저는 {country} {city}에 살고 있습니다.")

#6
num1 = int(input("숫자1 : "))
num2 = int(input("숫자2 : "))

print("{} - {} = {}".format(num1, num2, num1 - num2))
print("{} * {} = {}".format(num1, num2, num1 * num2))

#7
num1 = int(input("숫자1 : "))
num2 = int(input("숫자2 : "))
num3 = int(input("숫자3 : "))

print(f"{num1} * {num2} + {num3} = {num1 * num2 + num3}")

#8
num1 = int(input("숫자 : "))
print(f"{num1} 제곱 : {num1 * num1}")

#9
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

#10
num = int(input("마일을 입력하시오: "))

print(f"{num}마일은 {num * 1.609}킬로미터입니다.")
