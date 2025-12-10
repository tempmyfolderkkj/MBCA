
# 사람이 하던 웹브라우저의 행동을 파이썬 프로그램이 대신 수행하도록 자동화 해주는 모듈
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.coupang.com/")

# time.sleep(2)

# search_input = driver.find_element(By.CLASS_NAME, "search_input")
# search_input.send_keys('스타벅스')

# time.sleep(2)

# driver.find_element(By.ID, 'search-btn').click()

# time.sleep(2)

#driver.quit() # 자동으로 꺼짐








































