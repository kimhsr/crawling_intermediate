from selenium import webdriver
import time

# 크롬 창 안뜨게 하기
option = webdriver.ChromeOptions()
option.add_argument("headless")
browser = webdriver.Chrome("./chromedriver", options=option)
browser.implicitly_wait(5)
browser.get("https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net")

# 로그인 하기
id = browser.find_element_by_css_selector("input#id")
id.send_keys("본인_아이디_입력")
pw = browser.find_element_by_css_selector("input#inputPwd")
pw.send_keys("본인_비밀번호_입력")
button = browser.find_element_by_css_selector("button#loginBtn")
button.click()
time.sleep(3)  # 로그인될 때까지 3초

# 이메일함으로 이동
browser.get("https://mail.daum.net/")
time.sleep(2)  # 로그인될 때까지 2초 기다리기

# 이메일 제목 크롤링
# browser.find_element_by_css_selector() # select_one()
title = browser.find_elements_by_css_selector("strong.tit_subject")  # select()
for i in title:
    print(i.text)
browser.close()
