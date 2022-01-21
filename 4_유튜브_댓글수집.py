from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("./chromedriver")
browser.get("https://www.youtube.com/watch?v=cNKpSlZ5-_4")
time.sleep(5)

# 스크롤 내려서 댓글 생성시키기
# PAGE_DOWN : 스크롤 살짝 / END : 스크롤 끝까지
browser.find_element_by_css_selector("html").send_keys(Keys.END)
time.sleep(4)
comments = browser.find_elements_by_css_selector("#content-text")
idx = 0
while True:
    try:
        print(comments[idx].text)
    except:
        print("======== 크롤링 완료! ========")
        break

    idx += 1
    if idx % 20 == 0: # idx 가 20의 배수라면?
        browser.find_element_by_css_selector("html").send_keys(Keys.END)
        time.sleep(4)
        comments = browser.find_elements_by_css_selector("#content-text")