
# 웹스크래핑 : 웹 페이지에서 특정 정보를 추출하는 작업

# 외부 모듈 : requests, beautifulspip4 [별도 설치 필요]

# 웹 페이지를 분석 - 웹 페이지를 만드는 문법

# 아주 간단한 웹페이지 만들어보기. [ HTML, CSS, JavaScript]

import requests
response = requests.get('https://2017mrhi.github.io/web-test/')

# html 웹문서를 분석, 요소들을 찾아서 안에 있는 값 뽑아오기 [외부 모듈 Beautifulsoup]
from bs4 import BeautifulSoup

# HTML 분석가 객체 생성
soup = BeautifulSoup(response.text, "html.parser")

# p요소 모두 찾아보기
p_list = soup.select('p')
print(p_list[0].string)
print(p_list[1].string)

# 아이디로 찾기 - 이미지 경로 찾기
img = soup.select_one('#kk')
print(img.get('src'))

# 클래스로 찾기
es = soup.select('.aa')
print(es[1].string)

# [실습] 네이버 금융 페이지의 '코스피 지수' 스크래핑 해보기 (막 실행 x)
import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com/sise/')
soup = BeautifulSoup(response.text, 'html.parser')

#웹 문서에서 요소 찾기
span_element = soup.select_one('#KOSPI_now')
print(span_element.string)










