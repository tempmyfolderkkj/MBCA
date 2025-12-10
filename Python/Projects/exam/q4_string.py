
# 1 
message = input("message= ")

print("\n문자열의 길이 :", len(message))
print("첫 번째 문자 :", message[0])
print("마지막 문자 :", message[-1])

# 2
whitespace_string = "  PYTHON  "

print(whitespace_string.strip().lower())

# 3
str = "Python is a great language"

print("great" in str)

# 4
num1 = input("첫번째 자리 입력(3자리) : ")
num2 = input("두번째 자리 입력(3 ~ 4자리) : ")
num3 = input("세번째 자리 입력(4자리) : ")

print("입력된 전화번호는 [ {} ]".format(num1 + "-" + num2 + "-" + num3))

# 5
mail_adr = input("메일 주소 입력(@포함) : ")
inx = mail_adr.rfind("@")

print("입력된 메일주소명 : {}".format(mail_adr[:inx]))
print("메일서버 이름 : {}".format(mail_adr[inx + 1:]))

# 6
message ='''
올해 신년 기자회견에서 저는 AI 연구와 AI 산업이 국가 경쟁력을 좌우할 것이라고 말씀드립니다.
정부는 공공 서비스에 ai를 적극 도입해 행정 효율성을 높일 계획입니다.
특히 의료AI 분야와 재난 대응 AI 시스템은 국민 안전을 지키는 데 중요한 역할을 할 것입니다.
교육 영역에서는 ai 기반 맞춤형 학습과 AI 튜터링 서비스를 확대하겠습니다.
중소기업의 생산성을 높이기 위해 AI 자동화와 AI 데이터 분석 지원 사업을 강화합니다.
산업 전반의 데이터·AI 생태계를 정비해 혁신 기반을 구축하겠습니다.
국방 분야에서도 ai 기술을 활용해 보다 정교한 위협 대응 체계를 마련하겠습니다.
또한 교통·에너지 관리에 AI 예측 모델을 적용해 효율성을 높이겠습니다.
정부는 AI 윤리 기준과 AI 안전 규범을 마련해 기술 발전이 책임 있게 이루어지도록 하겠습니다.
끝으로, ai 혁신이 모두에게 혜택이 될 수 있도록 포용적 성장을 이루겠습니다.
'''

print("총 글자수(앞뒤 공백 제외) : {}".format(len(message.strip())))
print("총 글자수(띄어쓰기, 줄바꿈문자 제외) : {}".format(len(message.replace(" ","").replace("\n", ""))))
print("AI 라는 글자 등장 횟수 : {}".format(message.lower().count("ai")))