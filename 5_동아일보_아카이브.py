from bs4 import BeautifulSoup
import requests

sess = requests.session()
h = {"Referer": "https://secure.donga.com/membership/login.php?gourl=https%3A%2F%2Fwww.donga.com%2F"}
post_data = {
    "gourl": "https%3A%2F%2Fwww.donga.com%2Farchive%2Fnewslibrary%2Fview%3Fymd%3D19920121%26mode%3D19920121%2F0002450920%2F1",
    "bid": "본인_아이디_입력",
    "bpw": "본인_비밀번호_입력"}
sess.post("https://secure.donga.com/membership/trans_exe.php", headers=h, data=post_data)
code = sess.get("https://www.donga.com/archive/newslibrary/view?idx=19920121%2F0002450920%2F1")
soup = BeautifulSoup(code.text, "html.parser")
content = soup.select_one("div.article_txt")
print(content.text)
