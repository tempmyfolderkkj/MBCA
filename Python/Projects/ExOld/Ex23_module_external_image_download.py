
# 네트워크 상의 이미지파일을 다운로드 하는 프로그램

# requests [외부모듈 - 별도 설치 필요(터미널 > pip install requests)]

import requests

address = 'https://cdn.pixabay.com/photo/2019/12/17/14/43/christmas-4701783_640.png' # 이미지파일의 인터넷경로(URL)
response = requests.get(address)
print("응답코드 :", response.status_code)
# data = response.text # 이미지는 글씨가 아님, 알수없는 글씨들이 표시됨

# 이미지는 2진수의 픽셀정보를 가지고 있는 데이터 파일
# response 응답객체는 본이이 읽어온 바이너리데이터를 16진수로 보여줄수있음
print(response.content)

# 읽어온 이미지 파일데이터 덩어리를 내 컴퓨터에 파일 저장하기
import datetime
now = datetime.datetime.now()

file_name = 'IMG_' + str(now)
file_name = file_name.replace(' ', '')
file_name = file_name.replace('-', '')
file_name = file_name.replace(':', '').replace('.', '')
file_name = file_name + '.png'

# 날짜를 이용한 트정 서식모양(format) 으로 만들어주는 기능이 now 시간객체에 존재함
file_name = 'IMG_' + now.strftime('%Y%m%d%H%M%s') + '.pmg'

file = open('download/' + file_name, 'wb')  # wb - write binary
file.write(response.content)
file.close()
















