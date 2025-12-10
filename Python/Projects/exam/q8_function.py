

#1
def minmax(*value):
    max = value[0]
    min = value[0]
    
    for val in value:
        if val >= max:
            max = val

        if val <= min:
            min = val

    return min, max

print(minmax(10, 20, 15))

#2
def cel_to_fah(val):
    return 1.8 * val + 32

def fah_to_cel(val):
    return (val - 32) / 1.8

print("화씨 :", cel_to_fah(10))
print("섭씨 :", fah_to_cel(50))

#3
def dan(num1, num2 = 9):
    srt = sorted([num1, num2])
    num1 = srt[0]
    num2 = srt[1]

    for i in range(num1, num2 + 1):
        for x in range(1, 10):
            print("{} x {} = {}".format(i, x, i * x))
            
        print()
    
dan(5, 3)

#4
def pibo(num):
    list_num = [0, 1]

    for i in range(num - 1):
        list_num.append(list_num[i] + list_num[i + 1])

    print(list_num)

pibo(10)

