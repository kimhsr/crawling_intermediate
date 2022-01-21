from bs4 import BeautifulSoup
import requests

sess = requests.session()
h = {"Referer": "https://secure.donga.com/membership/login.php?gourl=https%3A%2F%2Fwww.donga.com%2F"}
post_data = {
    "gourl": "https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19920121%26mode%3D19920121%2F0002450920%2F1",
    "bid": "본인_아이디_입력",
    "bpw": "본인_비밀번호_입력"}
sess.post("https://secure.donga.com/membership/trans_exe.php", headers=h, data=post_data)

# 뉴스 기사 제목 요소들 가져오기
code = sess.get("https://www.donga.com/archive/newslibrary/view?ymd=19920121&mode=19920121/0002450920/1")
soup = BeautifulSoup(code.text, "html.parser")
a = soup.select("ul.news_list a")
for i in a:
    article_num = i.attrs["onclick"].replace("javascript:getNewsArticle('19920121/", "").replace("/1'); return false;", "")
    url = "https://www.donga.com/archive/newslibrary/view?idx=19920121%2F{}%2F1".format(article_num)
    code = sess.get(url)
    soup = BeautifulSoup(code.text, "html.parser")
    content = soup.select_one("div.article_txt")
    print(content.text)
