
from tkinter import *

# 파이썬 만의 특정 폴더 영역으로 리소스(이미지, 동영상, 음성 파일)

window = Tk()
img = PhotoImage(file='../../image/ms/ms21.png')
label = Label(window, image=img)
label.pack()


window.mainloop()