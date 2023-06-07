import os
os.chdir(r"C:\Users\shira\デスクトップ\programming\python\scraping")
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary


#画面に表示しないヘッドレスモード
#options = Options()
#options.add_argument("--headless")

USER = "山田太郎"
PASS = "password"

browser = webdriver.Chrome(executable_path=r"..\chromedriver.exe")
browser.get("http://uta.pw/sakusibbs/users.php?action=login")
print("ログインページにアクセスしました")

#テキストボックスに文字を入力
e = browser.find_element(By.ID, "user")
e.clear()
e.send_keys(USER)
e = browser.find_element(By.ID, "pass")
e.clear()
e.send_keys(PASS)

#1秒まってログイン
time.sleep(1)
elem_login_btn = browser.find_element(By.CSS_SELECTOR, "#loginForm > form > table > tbody > tr:nth-child(3) > td:nth-child(2) > input[type=submit]")
elem_login_btn.click()

#ページのロードまで待機
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".islogin")))

#マイページに移動
a = browser.find_element(By.CSS_SELECTOR, "#header_menu > span > a")
url_mypage = a.get_attribute("href")
print("マイページのURL=", url_mypage)
browser.get(url_mypage)
#お気に入りのタイトルを列挙
links = browser.find_elements(By.CSS_SELECTOR, "#favlist > li > a")

for a in links:
    href = a.get_attribute("href")
    title = a.text
    print("-", title, ">", href)
