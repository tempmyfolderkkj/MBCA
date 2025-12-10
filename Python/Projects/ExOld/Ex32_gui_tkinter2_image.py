
from tkinter import *

# 이미지를 보여주는 위젯은 없음. 대신, Label 위젯에 text='' 대신 image=''로 이미지를 보여줌
window = Tk()

# 이미지 파일의 경로를 써야 해서
# 이미지 파일을 읽어서 파이썬에서 사용할 수 있는 개체로 만들어주는 클래스를 이용
img1 = PhotoImage(file='image/bazzi.png')
img2 = PhotoImage(file='image/dao.png').subsample(2) # 해상도 2배 줄임 - 해상도를 줄여야 사이즈도 줄어듬

label1 = Label(window, image=img1) # jpg면 error - tkinter의 PhotoImage()는 png, gif만 가능함
label1.pack()

# jpg 이미지를 보여주고 싶다면, 외부 라이브러리 추가( pillow [ PIL 파이썬 이미지 라이브러리의 후속판])
from PIL import Image, ImageTk # Image : 이미지 객체, ImageTk : Tkinter에서 PIL Image를 사용할 수 있도록 해줌

pil_image1 = Image.open('image/koala.jpg').resize((300,200), Image.LANCZOS)
pil_image2 = Image.open('image/newyork.jpg').resize((300,200), Image.LANCZOS) # 튜플타입으로 (너비,높이) , 사이즈 조절할때 이미지품질(설정값)

# pil_image를 Label 위젯에서 인식하지 못함, 그래서 변환 - ImageTk.PhotoImage
img3 = ImageTk.PhotoImage(image=pil_image1)
img4 = ImageTk.PhotoImage(image=pil_image2)

# 이미지를 보여주는 Label 객체 생성하면 이미지를 설정
label2 = Label(window, image=img3)
label2.pack()

# 버튼클릭시에 이미지를 변경해보기
def aaa():
    if label2.cget('image') == str(img3):
        label2.config(image=img4)
        
    else:
        label2.config(image=img3)

btn = Button(window, text='change image', command=aaa)
btn.pack()







window.mainloop()
