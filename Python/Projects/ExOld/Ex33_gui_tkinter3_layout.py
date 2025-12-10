
from tkinter import *

# 배치 관리자 - pack, grid, place

window = Tk()
window.title('gui layout')
window.geometry('400x300+100+50')


# 위젯 배치방법 3가지
#1) pack
btn1 = Button(window, text='button #1')
btn1.pack(side='left', anchor='n')

btn2 = Button(window, text='button #2')
btn2.pack(side='right', fill='y')

btn3 = Button(window, text='button #3')
btn3.pack(side='top', anchor='e')

btn4 = Button(window, text='button #4')
btn4.pack(side='bottom', fill='x')

#2) place - 절대 위치, 원하는 좌표에 배치 (겹칠수도 있음)
btn5 = Button(window, text='button #5')
btn5.place(x=50, y=50) # 50, 50 픽셀
 
btn6 = Button(window, text='button #6')
btn6.place(x=70, y=70) 

btn7 = Button(window, text='button #7')
btn7.place(x=0, y=290)

#3) grid - 격자(행렬) 배치 -> 계산기 같은 GUI 만들때 용이

# 화면의 일부 영역을 구분하는 용도로 사용하는 컨테이너용 위젯
frame = Frame(window, width=300, height=150, bg='aqua')
frame.place(x=0, y=100)

# frame 안에 버튼들을 격자로 배치해보기
# b1 = Button(frame, text='7')
# b1.grid(row=0, column=0)

# b2 = Button(frame, text='8')
# b1.grid(row=0, column=1)

# b3 = Button(frame, text='9')
# b1.grid(row=0, column=2)

bt = ('b' + str(n) for n in range(1,10))

r = 0
c = 0
for v in bt:
    v = Button(frame, text=str(9 - r * 3 - c))
    v.grid(row=r, column=c)
    c = c + 1
    
    if c == 3:
        c = 0
        r = r + 1



window.mainloop()



