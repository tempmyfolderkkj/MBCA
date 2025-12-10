# 기능 요구
#1. '파일 선택' 버튼을 누르면 엑셀파일을 선택할 수 있어야 함
#2. 선택한 파일경로는 Entry 요소에 보여야 함
#3. '파일 읽기' 버튼을 누르면 해당경로의 엑셀을 pandas로 읽어야 함
#4. '그래프보기'버튼을 누르면 숫자 데이터들이 선그래프로 보여야 함
#5. '엑셀데이터보기' 버튼을 누르면 다시 표 형태의 데이터가 보여야 함

from tkinter import *
from tkinter import filedialog, messagebox, ttk
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#7.1 전역변수 선언 - 이 .py파일 어디서든 인식이 가능한 변수
df = None # 엑셀파일을 판다스로 읽어서 표 형태로 데이터를 가지고 있는 객체 참조변수
plt.rcParams['font.family'] = 'Malgun Gothic'
figure_canvas = None

# 버튼 클릭시 실행될 코드가 작성된 영역(함수 function 기능) 정의

#6. 파일 선택버튼 클릭시 동작할 기능코드(함수)
def clicked_file_chooser():
    # 윈도우 탐색기처럼 사용자가 마우스로 파일을 선택할 수 있도록 하는 [파일선택기]를 띄우기 - tkinter모듈안에 하위모듈로 filedialog를 이용
    file_path = filedialog.askopenfilename(title='엑셀 파일 선택', filetypes=[('엑셀 파일', '*.xlsx *.xls')]) # return - 파일 경로
    #filedialog.askopenfilename(title='엑셀 파일 선택', filetypes=[('엑셀 파일', '*.xlsx *.xls'), ('모든 파일', '*.*'), ('이미지 파일', '*.png *.jpg')])

    if file_path:
        # 기존 Entry에 이미 이전 경로명이 써 있을 수도 있기에 먼저 제거
        entry.delete(0, END)
        # 사용자가 선택한 새로운 파일경로를 첫번째 자리부터 작성하기
        entry.insert(0, file_path)



def clicked_file_read():
    global df

    # 선택한 파일의 경로를 Entry로 부터 얻어오기
    file_path = entry.get()

    # 선택된 경로가 없는 데 읽으라고 하면 file_path 경로에 실제 파일이 이는지 확인하기 위해 os 모듈 사용
    if not os.path.exists(file_path):
        messagebox.showerror('파일읽기 오류', '파일을 찾을 수가 없습니다')
        # 에러가 났으니 더이상 파일읽기 기능을 수행할 필요가 없으므로 이 함수의 동작을 멈춤
        return
    
    
    # 파일이 존재하는 상태이므로 pandas를 이용하여 file_path의 엑셀파일을 읽어서 DataFrame으로 만들기
    df = pd.read_excel(file_path)
    
    # 데이터가 확인 되었으니 GUI 위젯으로 데이터를 보여주기 이 작업이 좀 복잡할 것임
    # 그래서 이 위치에 작성하면 지저분해 질 듯
    # 또한 [엑셀데이터 보기] 버튼이 클릭되었을때도 이 df를 보여주는 작업을 해야함, 즉. 같은 기능을 다시 수행
    # 그래서 이 작업을 별도의 함수에서 수행
    show_data()

#8. show_data 함수를 정의 - 데이터 프레임(df)의 데이터를 TreeView에 표 형태로 보여주기
def show_data():
    global df
    global figure_canvas

    if df is None:
        return
    
    # 그래프가 그려진 FigureCanvasTkAgg를 지워야함
    if figure_canvas is not None:
        figure_canvas.get_tk_widget().destroy()
        figure_canvas = None

    treeview.delete(*treeview.get_children()) # 리스트로 한번에 지정 할수 밖에 없음, 그래서 * 언패킹 연산자 사용

    treeview['columns'] = list(df.columns) # 표의 칸수를 지정
    treeview['show'] = 'headings' # 컬럼 제목이 표시되어야 함을 설정

    for col in df.columns:
        treeview.heading(col, text=col) # 첫번째 파라미터인 col에게 보여질 글씨 지정
        treeview.column(col, width=120)

    for idx, row in df.iterrows():
        treeview.insert('', 'end', values=list(row))
        # '' - 최상위 레벨(parent) , 'end' - 기존 데이터가 추가된 다음 줄에 추가, values - 컬럼별 데이터 값 지정

#9. show_graph함수를 정의 - 데이터프레임(df)의 데이터를 TreeView에 그래프로 보여주기
def show_graph():
    global df
    global figure_canvas

    if df is None:
        return
    
    # 그래프가 TreeView에 그려져야 하기에 기존에 추가되어 있던 컬룸들을 모두 제거
    treeview.delete(*treeview.get_children())

    # 시각화를 위한 그래프용 모듈 추가 matplotlib
    #1. x축에 보여줄 데이터와 라벨들 준비 - 일반적으로는 첫번째 컬룸에 있는 경우가 많음
    xs = df.iloc[:, 0] # 모든 row 첫번째(0번) 칸 ex) [0, 0:2] - 0번째 row 데이터 col 3개
    xs_label = df.columns[0]

    # Y축에 그려질 데이터들을 준비 - 그래프이기에 숫자 데이터들만 그려짐
    # 데이터프레임(df)에서 숫자 타입의 데이터를 가진 컬룸들만 뽑아서 다시 데이터프레임 만들기
    numeric_df = df.select_dtypes(include=['int64', 'float64'])

    # 혹시 숫자데이터 컬룸이 없으면 그래프는 못보여줌
    if numeric_df.empty:
        messagebox.showwarning('경고', '그래프를 그릴 수 있는 숫자 컬룸이 없습니다.')
        return
    
    # 숫자데이터들을 선 그래프에 표시하기
    figure = plt.figure(figsize=(10, 6))

    for col in numeric_df: # col 순서
        if col == xs_label:
            continue

        # x축 값, y축 값들로 선 그래프 그리기
        plt.plot(xs, numeric_df[col], label=col, marker='o')

    plt.xlabel(xs_label)
    plt.ylabel('값들')
    plt.title('엑셀 데이터 그래프')
    plt.legend() # 범례 표시
    plt.grid(True) #격자 눈금(가로,세로 모두)
    
    # 그래프를 tkinter의 TreeView안에 넣기위해 그래프 그리는 전용 위젯 필요 - FigureCanvasTkAgg
    if figure_canvas is not None:
        figure_canvas = FigureCanvasTkAgg(figure=figure, master=treeview)
        figure_canvas.get_tk_widget().pack()



window = Tk()
window.title('엑셀 파일 뷰어')
window.geometry('800x600+50+50')

#2. 파일 선택 영역 Frame
frame_top = Frame(window)
frame_top.pack(fill='x', padx=10, pady=5)

#3. 파일경로를 직접 입력하거나 선택된 파일경로가 보여지는 entry 위젯
entry = Entry(frame_top, width=60)
entry.pack(side='left', padx=10, pady=10)

btn_file_chooser = Button(frame_top, text='파일 선택', command=clicked_file_chooser)
btn_file_chooser.pack(side='left', padx=5)

btn_file_read = Button(frame_top, text='파일 읽기', command=clicked_file_read)
btn_file_read.pack(side='left', padx=5)

#8.1 [엑셀데이터 보기] [그래프 보기] 버튼으로 데이터를 보여주는 위젯들

# 위 파일선택영역과 시각적으로 구분하기 위해 '구분선' 위젯(Separator) 사용 - 이 위젯은 tkinter 안에 ttk 하위모듈에 존재함
separator = ttk.Separator(window, orient='horizontal')
separator.pack(fill='x', pady=10)

# 버튼 2개 배치
frame_buttons = Frame(window)
frame_buttons.pack(anchor='center')

btn_show_data = Button(frame_buttons, text='엑셀데이터 보기', command=show_data)
btn_show_data.pack(side='left', padx=10)

btn_show_graph = Button(frame_buttons, text='그래프 보기', command=show_graph)
btn_show_data.pack(side='left', padx=10)

# 8.2 표 형태와 그래프를 번갈아 보여줄 수 있어야 하기에 ttk.Treeview이용 - 자식 요소들을 제거했다가 추가했다가 할수 있도록
treeview = ttk.Treeview(window)
treeview.pack(expand=True, fill='both')















window.mainloop()