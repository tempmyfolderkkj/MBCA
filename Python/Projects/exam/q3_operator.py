

#1
num1 = int(input("정수 1 :"))
num2 = int(input("정수 2 :"))

print("{} / {} 결과 -> 몫 : {}, 나머지 : {}".format(num1, num2, num1 // num2, num1 % num2))

#2
pi = float(input("반지름 입력 : "))
result = 3.14 * (pi ** 2)

print("원의 면적 : {}".format(result))

#3
won = 1458.13
doller = int(input("달러 입력 : "))

print("{} 달러 -> 원화 : {}".format(doller, won * doller))

#4
num1 = int(input("정수 1 : "))
num2 = int(input("정수 2 : "))
num3 = int(input("정수 3 : "))
sum = num1 + num2 + num3

print("{}, {}, {} -> 합 : {} , 평균 : {}".format(num1, num2, num3, sum, sum / 3))

#5
hour = int(input("시 : "))
min = int(input("분 : "))
sec = int(input("초 : "))

print("00:00:00 기준 {}초가 흐름".format(hour * 60 * 60 + min * 60 + sec))

#6
pay = int(input("받은 돈 : "))
price = int(input("상품 가격 : "))

print("\n부가세 : {}".format(price // 10))
print("잔돈 : {}".format(pay - price))

#7
val_x1 = int(input("점1 x 좌표 : "))
val_y1 = int(input("점1 y 좌표 : "))
val_x2 = int(input("점2 x 좌표 : "))
val_y2 = int(input("점2 y 좌표 : "))

val_result = (val_x2 - val_x1) * (val_y2 - val_y1)

print("좌 상단의 x 좌표 : {}".format(val_x1))
print("좌 상단의 y 좌표 : {}".format(val_y1))
print("우 하단의 x 좌표 : {}".format(val_x2))
print("우 하단의 y 좌표 : {}".format(val_y2))

print("두 점이 이루는 직사각형의 넓이는 {}입니다".format(val_result))

# 1
s1 = input("s1 = ")
s2 = input("s2 = ") 

print(s1 + " " + s2)
print(s2 * 3)

# 2
sentence = "I love Python programming"

print(sentence[7:13])