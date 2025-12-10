#import datetime
#a = datetime.datetime.now().replace(month=4,day=1)
#day_end = (datetime.datetime.now() - datetime.timedelta(days= 1)).day
#print(a.strftime('%Y%m%d'))

# lambda s:s+'\n'
# [v for v in aaa if v<60]
# [ v*v for v in aaa]'
# from math import sin,cos

# from urllib import request
# address = 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/ddd.csv'
# url = request.urlopen(address)
# data = url.read()

# import requests
# address = 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/hhh.json'
# response = requests.get(address) # 서버에 데이터의 요청한 결과정보를 가진 객체를 리턴
# # 응답객체 response 를 통해 데이터와 상태정보를 알수 있음
# print('응답 코드 번호 :', response.status_code)
# print('읽어들인 데이터',response.text)
# aa = response.json() # 알아서 json물자열을 분석하여 dictionary로 생성
# print(aa['data_title'])
# print(aa['total_count'])

# html 웹문서를 분석, 요소들을 찾아서 안에 있는 값 뽑아오기 [외부 모듈 Beautifulsoup]
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(response.text, "html.parser") # HTML 분석가 객체 생성 , html.parser - 기본 형식
# p_list = soup.select('p') # p요소 모두 찾아보기
# print(p_list[0].string)
# img = soup.select_one('#kk') # 아이디로 찾기 [ # ]
# print(img.get('src'))
# es = soup.select('.aa') # 클래스로 찾기 [ . ]
# print(es[1].string)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Chrome()
# driver.get("https://www.naver.com/")
# time.sleep(2)
# search_input = driver.find_element(By.CLASS_NAME, "search_input")
# search_input.send_keys('스타벅스')
# time.sleep(2)
# driver.find_element(By.ID, 'search-btn').click()
# time.sleep(2)

# import numpy as np
# aa = np.array([10, 20, 30])
# bb = np.array([4, 5, 6])
# print(aa + bb) # 리스트와 차이점 - 사칙연산 가능, 행렬요소끼리 연산이기에 개수가 다르면 error
# aaaa = np.array([100, 200, 300, 400], [500,600, 700, 800])
# print(aaaa.shape) # (행, 열) (2, 4)

# import pandas as pd
# aa = pd.Series(['sam', 'robin', 'hong']) # 1차원 배열 구조 : Series - 엑셀의 한 column(열)
# bb = pd.Series(['seoul', 'tokyo', 'paris'], index=['korea', 'japan', 'france']) # 자동으로 부여되는 인덱스 번호를 원하는 식별자로 변경가능
# cc = pd.DataFrame(['aa', 'bb', 'cc', 'dd'], ['11', '22', '33', '44']) # 2차원 배열 구조 : DataFrame - 표 구조
# # key:value 형태의 딕셔너리 타입으로 데이터프레임을 생성하면 key 식별값이 column의 이름이 됨
# dd = pd.DataFrame({'aa': {10, 20, 30}, 'bb':[100,200,300], 'cc':[1000,2000,3000]})

# # csv 파일을 읽어와서 DataFrame 만들기
# ee = pd.read_csv('./files/scoes.scv') # 읽어온 결과가 DataFrame 객체로 나옴
# print(ee.head()) # 상위 5줄만 출력
# print(ee.tail()) # 하위 5줄만 출력
# print(ee.head(3)) # 상위 3줄만 출력
# print(ee.shape) # 행렬모양 확인 변수 (8,4) - header 제외
# ee.columns = ['aa', 'bb', 'cc', 'bb'] # 컬럼명 변경 가능
# print(ee.info()) # 데이터 프레임의 구조정보를 한번에 알려주는 기능함수
# print(ee['국어']) # 특정한 컬럼데이터만 보기 - 한 column의 Series를 출력
# # 국어 성적 평균, 영어 성적 중에 1등값(max)
# print('korea average :', ee['국어'].mean())
# print('English maximum :', ee['영어'].max())
# # 데이터분석(숫자데이터)에 많이 사용되는 평균, 최대, 최소값, 개수 등의 계산정보를 한번에 볼 수 있는 기능
# print(ee.describe())
# # 여러개의 컬룸을 동시에 보기 - 결과를 DataFrame 으로 출력
# print(ee[['영어','수학']])
# # 데이터 프레임에서 특정 줄(row) 데이터 가져오기 -- 첫번쨰 줄(행row)
# row = ee.loc[0] # 0번 인덱스의 한줄 - Serise 형식으로 저장
# rows = ee.loc[2:5] # 특정 범위의 행 데이터 가져오기 2 ~ 5 - DataFrame 형식으로 저장
# rows = ee.loc[2:] # 특정 범위 이후 모든 줄(끝까지)
# rows = ee.loc[2:, '이름'] # 행, 열 모두를 지정
# rows = ee.loc[4:, ['이름', '수학']]
# gg = pd.read_excel('./files/score.xlsx') # sheet_name=defult = 첫번째 시트
# hh = pd.read_excel('./files/score.xlsx', sheet_name='Scores') # 특정 sheet의 표를 데이터프레임으로 읽어오기
# ww = pd.read_excel('./files/seoul_weather_2025.xlsx')
# print(ww['최저기온(°C)'].max())
# print(ww['최저기온(°C)'].min())
# print(ww['최저기온(°C)'].max())

# from tkinter import * # tkinter 모듈안에 있는 모든 클래스, 변수, 함수, 상수 들을 import
# window = Tk() # 1] 최상위 윈도우 창 객체 생성
# window.title('this is python gui')
# window.geometry('400x200+100+50') # 너비x높이+x축+y축 [+왼쪽부터, +위쪽부터]
# window.resizable(False, True) # 옆, 밑
# window.resizable(0, 1) # false, true
# window.mainloop()

# label = Label(window, text='Hello. python GUI') # 이 위젯이 붙을 컨테이너위젯을 지정
# label3 = Label(window, text='안녕하세요', bg='black', fg='white', width=10, height=3) # 너비 10글자, 높이 3글자
# label4 = Label(window, text='have a good day. 반가워요', font='times 20 bold italic') # 글꼴, 크기, 볼드체, 이텔릭
# label4.config(text='clicked button : ')

# btn = Button(window, text='눌러주세요', padx=10, pady=10, command=aaa) # 패딩 x, y, command=버튼클릭시 실행되는 함수

# entry = Entry(window) #Entry 사용자부터 한줄 텍스트를 입력받는 위젯
# text=entry.get()
# value = text.get('1.0', END) # '1.0' 첫번째줄(1)의 첫번째 칸(0) 에서 부터 끝(END)까지

# from tkinter import messagebox
# messagebox.showinfo('메세지값', value) # 알림창의 제목, 메시지

# img1 = PhotoImage(file='image/bazzi.png')
# img2 = PhotoImage(file='image/dao.png').subsample(2) # 해상도 2배 줄임 - 해상도를 줄여야 사이즈도 줄어듬
# label1 = Label(window, image=img1)

# from PIL import Image, ImageTk # Image : 이미지 객체, ImageTk : Tkinter에서 PIL Image를 사용할 수 있도록 해줌
# pil_image1 = Image.open('image/koala.jpg').resize((300,200), Image.LANCZOS)
# pil_image2 = Image.open('image/newyork.jpg').resize((300,200), Image.LANCZOS) # 튜플타입으로 (너비,높이) , 사이즈 조절할때 이미지품질(설정값)
# img3 = ImageTk.PhotoImage(image=pil_image1) # pil_image를 Label 위젯에서 인식하지 못함, 그래서 변환 - ImageTk.PhotoImage
# img4 = ImageTk.PhotoImage(image=pil_image2)
# if label2.cget('image') == str(img3):
#         label2.config(image=img4)

# btn1 = Button(window, text='button #1')
# btn1.pack(side='left', anchor='n')
# btn1.pack(side='right', fill='y')
# btn5.place(x=50, y=50) # place - 절대 위치, 원하는 좌표에 배치 (겹칠수도 있음) / 50, 50 픽셀
# b1.grid(row=0, column=0)
# b1.grid(row=0, column=1)
# b1.grid(row=0, column=2)