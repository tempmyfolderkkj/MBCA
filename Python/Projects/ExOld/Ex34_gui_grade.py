

# 1. 사용자로부터 [이름, 국어, 영어, 수학] 점수를 입력 받아야함
# 2. [입력완료]버튼을 클릭하면 [총점, 평균]을 자동 계산하여, 데이터들을 리스트박스에 추가해야 함
# 3. [입력취소]버튼을 클릭하면 입력된 모든 글씨 일괄 삭제
# 4. 리스트박스의 항목을 건택하여 삭제하는 기능 [버튼으로 실행]
# 5. 리스트박스에 등록된 성적 데이터를 csv 파일로 저장하는 버튼

from tkinter import *

#[5]. 각 버튼들이 클릭되었을때 수행할 작업코드 들을 별도의 함수들로 만들어서 버튼에 적용하기

def clicked_complete():
    # 각 Entry 위젯에 써있는 글씨를 얻어오기
    name = entry_name.get()
    korea = entry_korea.get()
    eng = entry_eng.get()
    math = entry_math.get()
    total = int(korea) + int(eng) + int(math)
    everage = total / 3

    # 리스트박스에 입력데이터들 + 총점 + 평균
    listbox_result.insert(END, f'{name},{korea},{eng},{math},{total},{everage}') # 마지막위치(END) - tkinter 기능
    clicked_delete()


def clicked_reset():
    # Entry 요소에 써있는 글씨 모두 삭제
    entry_name.delete(0,END) # 0번 위치 글씨부터 끝까지
    entry_eng.delete(0,END)
    entry_korea.delete(0,END)
    entry_math.delete(0,END)

def clicked_delete():
    # 리스트 박스에서 선택한 항목위치(index)를 알아야 삭제 가능
    index = listbox_result.curselection()  # current selection - 현재 선택된 항목의 인덱스 번호를 튜플로 줌
    listbox_result.delete(index[0])

import csv
def clicked_save():
    all_items = listbox_result.get(0, END) # 0번부터 끝까지
    
    # 튜플로 되어있는 각 줄의 데이터를 csv파일로 저장하기
    with open('filse/grades.csv', 'w', encoding='UTF-8') as file:
        writer = csv.writer(file)

        for row in all_items:
            writer.writerow(row.split(',')) # 한줄문자열을 , 단위로 분리하여 리스트[]로 만들어 csv파일에 저장


#[1]. 화면부터 구성
window = Tk()
window.title('성적처리 프로그램')
window.resizable(False, True)
window.geometry('400x400-200+50')

#[2]. [이름, 국어, 영어, 수학] 성적을 입력하기 위한 위젯만들기
frame1 = Frame(window, padx=30, pady=10) # 여백
frame1.pack(fill='x')

label_name = Label(frame1, text='이름', font=('',14)) # 글꼴, 글자 크기
label_name.grid(row=0, column=0, padx=10, pady=10,)

entry_name = Entry(frame1, font=('', 12), width=15) # 15칸 정도 사이즈
entry_name.grid(row=0, column=1)

label_korea = Label(frame1, text='국어', font=('',14))
label_korea.grid(row=1, column=0, padx=10, pady=10,)

entry_korea = Entry(frame1, font=('', 12), width=15)
entry_korea.grid(row=1, column=1)

label_eng = Label(frame1, text='영어', font=('',14))
label_eng.grid(row=2, column=0, padx=10, pady=10,)

entry_eng = Entry(frame1, font=('', 12), width=15) 
entry_eng.grid(row=2, column=1)

label_math = Label(frame1, text='수학', font=('',14))
label_math.grid(row=3, column=0, padx=10, pady=10,)

entry_math = Entry(frame1, font=('', 12), width=15)
entry_math.grid(row=3, column=1)


#[3]. 입력완료, 취소 버튼이 놓여지는 영역 만들기
frame2 = Frame(window, padx=10)
frame2.pack(fill='x')

btn_complete = Button(frame2, text='입력완료', font=('Gungsuh', 12), command=clicked_complete)
btn_complete.pack(side='left', padx=20, pady=5)

btn_esc = Button(frame2, text='입력취소', font=('Gungsuh', 12), command=clicked_reset)
btn_esc.pack(side='right', padx=20, pady=5)


#[4]. 리스트박스, 항목삭제버튼, csv 파일저장 버튼 구성
frame3 = Frame(window, padx=10, pady=10)
frame3.pack(fill='x')

listbox_result = Listbox(frame3, font=('',12), height=5) # 5줄 높이
listbox_result.pack(fill='x')

btn_delete = Button(frame3, text='항목 삭제', font=('Batang', 12), command=clicked_delete)
btn_delete.pack(side='left', pady=10)

btn_save = Button(frame3, text='csv 파일 저장', font=('Batang', 12), command=clicked_save)
btn_save.pack(side='right', pady=10)


window.mainloop()


#줄임
# from tkinter import *

# #[5]. 각 버튼들이 클릭되었을때 수행할 작업코드 들을 별도의 함수들로 만들어서 버튼에 적용하기

# def clicked_complete():
#     # 각 Entry 위젯에 써있는 글씨를 얻어오기
#     input_data = [input_entry[i].get() for i in range(len(input_entry))]
#     total = sum(int(x) for x in input_data if x.isdigit())
#     everage = total / 3
    
#     # 리스트박스에 입력데이터들 + 총점 + 평균
#     listbox_result.insert(END, '{},{},{},{},{},{}'.format(*input_data, total, everage))
#     clicked_reset()


# def clicked_reset():
#     # Entry 요소에 써있는 글씨 모두 삭제
#     for v in input_entry:
#         v.delete(0, END)

# def clicked_delete():
#     # 리스트 박스에서 선택한 항목위치(index)를 알아야 삭제 가능
#     index = listbox_result.curselection()  # current selection - 현재 선택된 항목의 인덱스 번호를 튜플로 줌
#     listbox_result.delete(index[0])

# import csv
# def clicked_save():
#     all_items = listbox_result.get(0, END) # 0번부터 끝까지
    
#     # 튜플로 되어있는 각 줄의 데이터를 csv파일로 저장하기
#     with open('filse/grades.csv', 'w', encoding='UTF-8') as file:
#         writer = csv.writer(file)

#         for row in all_items:
#             writer.writerow(row.split(',')) # 한줄문자열을 , 단위로 분리하여 리스트[]로 만들어 csv파일에 저장


# #[1]. 화면부터 구성
# window = Tk()
# window.title('성적처리 프로그램')
# window.resizable(False, True)
# window.geometry('400x400-200+50')

# #[2]. [이름, 국어, 영어, 수학] 성적을 입력하기 위한 위젯만들기
# frame1 = Frame(window, padx=30, pady=10) # 여백
# frame1.pack(fill='x')

# input_label = []
# input_entry = []
# input_label_nm = ['이름', '국어', '영어', '수학']
    
# for i in range(len(input_label_nm)):

#     input_label.append(Label(frame1, text=input_label_nm[i], font=('',14)))
#     input_label[i].grid(row=i, column=0, padx=10, pady=10,)

#     input_entry.append(Entry(frame1, font=('', 12), width=15))
#     input_entry[i].grid(row=i, column=1)


# #[3]. 입력완료, 취소 버튼이 놓여지는 영역 만들기
# frame2 = Frame(window, padx=10)
# frame2.pack(fill='x')

# btn_complete = Button(frame2, text='입력완료', font=('Gungsuh', 12), command=clicked_complete)
# btn_complete.pack(side='left', padx=20, pady=5)

# btn_esc = Button(frame2, text='입력취소', font=('Gungsuh', 12), command=clicked_reset)
# btn_esc.pack(side='right', padx=20, pady=5)


# #[4]. 리스트박스, 항목삭제버튼, csv 파일저장 버튼 구성
# frame3 = Frame(window, padx=10, pady=10)
# frame3.pack(fill='x')

# listbox_result = Listbox(frame3, font=('',12), height=5) # 5줄 높이
# listbox_result.pack(fill='x')

# btn_delete = Button(frame3, text='항목 삭제', font=('Batang', 12), command=clicked_delete)
# btn_delete.pack(side='left', pady=10)

# btn_save = Button(frame3, text='csv 파일 저장', font=('Batang', 12), command=clicked_save)
# btn_save.pack(side='right', pady=10)


# window.mainloop()