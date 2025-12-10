import random

def sbgame():
    digits = list(range(10))
    random.shuffle(digits)
        
    num_rnd = digits[:4]

    input_val = ""
    while(True):
        s = 0
        b = 0

        input_num = input("")

        for i in range(len(input_num)):
        
            if str(num_rnd[i]) == input_num[i]:
                s = s + 1

            elif input_num[i] in str(num_rnd):
                b = b + 1
            

        input_val = input_val + "\n" + input_num + " {}s {}b".format(s, b)
        print("------------------------------\n" + input_val)

        if s == 4:
            break

    print("--정답--")


def boomgame():

    digits = list(range(10))

    numbers = list(range(1, 9999))
    a = random.sample(numbers, 5)
    print(a)









    pass


if __name__ == "__main__":
    print("----시작----")
    #sbgame()
    boomgame()
