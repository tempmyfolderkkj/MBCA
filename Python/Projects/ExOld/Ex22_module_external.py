
# 외부모듈 - 파이썬팀이 아닌 개인 또는 회사에서 별도로 개발한 파이썬 코드들의 집합체(모듈)

# 파이썬팀에서 개발한 모듈이 아니기에 파이썬설치할때 같이 설치되어 있지 않음
# 사용하려면 그 모듈을 다운로드하고 import 해서 사용해야함
# 이를 외부모듈을 서버에 가지고 있으면서 필요할때 컴퓨터에 설치해주는 도구(프로그램) : pip( package installer for python ) - CLI설치도구

# 1. requests - 자동 디코딩, 자동 예외처리, json 모듈 연동되어 있음, HTTP 요청 작업이 용이함[ 쿠키,세션,파일업로드 ]
# 설치 방법 ) vscode 에서 터미널(cmd, 명령프롬프트) 창을 열고 설치명령어 입력
# > pip3 install 모듈명 

import requests

address = 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/aaa.txt'
response = requests.get(address) # 서버에 데이터의 요청한 결과정보를 가진 객체를 리턴
# 응답객체 response 를 통해 데이터와 상태정보를 알수 있음
print('응답 코드 번호 :', response.status_code)
print('읽어 들인 데이터 :')
print(response.text)

# json 모듈기능도 이미 포함한 상태
address = 'https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/hhh.json'
response = requests.get(address)
print(response.status_code)
print(response.text)

aa = response.json() # 알아서 json물자열을 분석하여 dictionary로 생성
print(aa['data_title'])
print(aa['total_count'])

# [ open api 실습 ] 영화진흥위원회 open api 데이터 키발급
import requests
import datetime

adr_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json'
adr_key = 'key=37e7aef7947be9fa89df2eb185a09e6f'
yesterday = datetime.datetime.now() - datetime.timedelta(days = 1) 
adr_day = 'targetDt=' + "{:4s}{:02s}{:02s}".format(yesterday.year, yesterday.month, yesterday.day)

address = adr_url + "?" + adr_key + "&" + adr_day

response = requests.get(address)
aa = response.json()

print(aa['boxOfficeResult']['boxofficeType'])

items = aa['boxOfficeResult']['dailyBoxOfficeList']

for item in items:
    rank = item['rank']
    movie_name = item['movieNm']
    open_data = item['openDt']
    audience_acc = item['audiAcc']

    print('랭킹 :', rank)
    print('제목 :', movie_name)
    print('개봉일 :', open_data)
    print('누적관객수 :', audience_acc)
    print()



# https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/aaa.txt
# https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/bbb.txt
# https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/ccc.txt
# https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/ddd.csv
# https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/eee.tsv
# https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/ggg.xml
# https://raw.githubusercontent.com/2017mrhi/python_network_files/refs/heads/main/hhh.json











































