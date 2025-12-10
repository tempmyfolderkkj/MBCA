
# python desktop GUI 만들기

# 포준묘듈인 Tkinter 사용 [ TK(툴킷) interface
from tkinter import * # tkinter 모듈안에 있는 모든 클래스, 변수, 함수, 상수 들을 import

# 1] 최사위 윈도우 창 객체 생성
window = Tk()

# 화면 구성은 최상위 위젯의 mainloop() 요청 전에 추가해야함
# 3] 윈더우 상의 제목 설정
window.title('this is python gui')

# 4] 윈도우 창 크기 설정
window.geometry('400x200+100+50') # 너비x높이+x축+y축 [+왼쪽부터, +위쪽부터]
window.geometry('400x200-100-50') # 너비x높이+x축+y축 [-오른쪽부터, -아래쪽부터]

# 5] 창 크기 조절을 막을 수 있음
window.resizable(False, True) # 옆, 밑
window.resizable(0, 1) # false, true

# 6] GUI의 window창에는 print()로 출력이 안됨, 글씨를 보여주는 위젯(구성요소)을 만들어서 그 안에 글씨를 쓰고 window에 배치 - Label
label = Label(window, text='Hello. python GUI') # 이 위젯이 붙을 컨테이너위젯을 지정
# label을 적절한 위치에 배치해주는 기능 pack() - 배치관리자
label,Pack()

# 글씨를 하나더 보여주려면 또 다른 label 위젯이 필요
label2 = Label(window, 'Nice to meet you', bg='yello', fg='blue') # 배경 색상, 글씨 색장
label2.pack()

label3 = Label(window, text='안녕하세요', bg='black', fg='white', width=10, height=3) # 너비 10글자, 높이 3글자
label3.pack()

# 폰트 지정해보기
label4 = Label(window, text='have a good day. 반가워요', font='times 20 bold italic') # 글꼴, 크기, 볼드체, 이텔릭
label4.pack()

# 7] 버튼 추가하기
def aaa():
    print('click!')

btn = Button(window, text='눌러주세요', padx=10, pady=10, command=aaa) # 패딩 x, y, command=버튼클릭시 실행되는 함수
btn.pack()


# 8] 버튼 클릭할때 라벨이 보여주는 글씨 변경
label5 = Label(window, text='hello world')
label5.pack

i = 0
def bbb():
    global i

    label5.config(text='clicked button : ' + str(i))
    i = i + 1

btn2 = Button(window, text='change text', command=bbb)
btn2.pack()

# 9] Entry 사용자부터 한줄 텍스트를 입력받는 위젯
entry = Entry(window)
entry.pack()

# 버튼 클릭할때 entry에 써있는 글씨를 Label에 보여주기
def ccc():
    label6.config(text=entry.get())

btn3 = Button(window, text='입력 완료', command=ccc)
btn3.pack()

label6 = Label(window, text='')
label6.pack()


# 10] 여러줄 입력이 가능한 위젯
text = Text(window, width=30, height=3) # 너비 30칸, 높이 3줄
text.pack()

# 11] 버튼 클릭할때 경고(알림)창 보이기
from tkinter import messagebox

def ddd():
    value = text.get('1.0', END) # '1.0' 첫번째줄(1)의 첫번째 칸(0) 에서 부터 끝(END)까지
    messagebox.showinfo('메세지값', value) # 알림창의 제목, 메시지

btn4 = Button(window, text='메세지 읽기', command=ddd)
btn4.pack()


# 2] 최상위 윈도우가 화면에 보여지며, 사용자의 마우스 이동, 클릭, 버튼클릭 같은 이벤트처리를 지속적으로 수행하면서 (오차)
window.mainloop()






























































