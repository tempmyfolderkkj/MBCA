# 1
print("홍길동")
print("홍 길 동")
print("홍  길  동")

# 2
print("홍길동\n홍 길 동\n홍  길  동")

# 3
print("제 이름은", "홍길동", "입니다.")
print("제 나이는", "20", "살이고요.")
print("제가 사는 곳은", "seoul", "입니다.")

# 4
print("제 이름은 {}입니다.".format("홍길동"))
print("제 나이는 {}살이고요.".format(20))
print("제가 사는 곳은 {}입니다.".format("seoul"))

print(f"제 이름은 {"홍길동"}입니다.")
print(f"제 나이는 {20}살이고요.")
print(f"제가 사는 곳은 {"seoul"}입니다.")

#5
print(4, "+", 5, "=", 4 + 5)
print(7, "*", 9, "=", 7 * 9)

#6
print(5, "*", 1, "=", 5 * 1)
print(5, "*", 2, "=", 5 * 2)
print(5, "*", 3, "=", 5 * 3)
print(5, "*", 4, "=", 5 * 4)
print(5, "*", 5, "=", 5 * 5)
print(5, "*", 6, "=", 5 * 6)
print(5, "*", 7, "=", 5 * 7)
print(5, "*", 8, "=", 5 * 8)
print(5, "*", 9, "=", 5 * 9)

#7
print("{} * {} = {}".format(5, 1, 5 * 1))
print("{} * {} = {}".format(5, 2, 5 * 2))
print("{} * {} = {}".format(5, 3, 5 * 3))
print("{} * {} = {}".format(5, 4, 5 * 4))
print("{} * {} = {}".format(5, 5, 5 * 5))
print("{} * {} = {}".format(5, 6, 5 * 6))
print("{} * {} = {}".format(5, 7, 5 * 7))
print("{} * {} = {}".format(5, 8, 5 * 8))
print("{} * {} = {}".format(5, 9, 5 * 9))

#8
print("{}{}".format(" " * 3, "*" * 1))
print("{}{}".format(" " * 2, "*" * 3))
print("{}{}".format(" " * 1, "*" * 5))
print("{}{}".format(" " * 0, "*" * 7))

#9
print("-" * 30)
print("번호\t 이름\t 나이\t 전공\t 주소")
print("-" * 30)
print(f"{1}\t {"sam"}\t {20}\t {"web"}\t {"seoul"}")
print(f"{2}\t {"robin"}\t {25}\t {"web"}\t {"busan"}")
print(f"{3}\t {"park"}\t {30}\t {"data"}\t {"incheon"}")

#10
print("""\
파이썬은
웹 애플리케이션, 데이터 과학, 인공지능 등
다양한 분야에 사용되는 배우기 쉽고 효율적인
프로그래밍 언어입니다.\
""")