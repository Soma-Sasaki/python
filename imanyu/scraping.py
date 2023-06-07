import requests, sys, webbrowser, bs4, os, chromedriver_binary, time
import pandas as pd
import os
import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
os.chdir(r"C:\Users\shira\デスクトップ\programming\python\imanyu")

#画面に表示しないヘッドレスモード
#options = Options()
#options.add_argument("--headless")

#ブラウザ起動～ログインまで
browser = webdriver.Chrome()
browser.get("https://scraping-for-beginner.herokuapp.com/login_page")
time.sleep(3)
elem_username = browser.find_element(By.ID, "username")
elem_username.send_keys("imanishi")
elem_password = browser.find_element(By.ID, "password")
elem_password.send_keys("kohei")
time.sleep(1)
elem_login_btn = browser.find_element(By.ID, "login-btn")
elem_login_btn.click()

#情報の抽出~csvファイル出力まで
keys = []
values = []
elems_th = browser.find_elements(By.TAG_NAME, "th")
elems_td = browser.find_elements(By.TAG_NAME, "td")
for elem_th, elem_td in zip(elems_th, elems_td):
    key = elem_th.text
    value = elem_td.text
    keys.append(key)
    values.append(value)

df = pd.DataFrame()
df["項目"] = keys
df["値"] = values
df.to_csv("講師情報.csv", index=False)

#beautiful_soup使用
url = "https://scraping-for-beginner.herokuapp.com/udemy"
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, "html.parser")
print(soup.prettify())
subscribers = soup.find_all("p", attrs={"class": "subscribers"})[0]
subscribers.text
n_subscribers = int(subscribers.text.split("：")[1])
n_subscribers
#CSSセレクタ利用
soup.select_one(".reviews").text.split("：")[1]

#ランキングサイト掲載情報自動取得
url = "https://scraping-for-beginner.herokuapp.com/ranking/?page=1"
res = requests.get(url)

data = []

soup = bs4.BeautifulSoup(res.text, "html.parser")

spots = soup.find_all("div", attrs={"class" : "u_areaListRankingBox"})
for spot in spots:
    spot_name = spot.find("div", attrs={"class": "u_title"})
    spot_name.find("span", attrs={"class": "badge"}).extract()
    spot_name = spot_name.text.replace("\n", "")

    eval_num = spot.find("div", attrs={"class": "u_rankBox"}).text
    eval_num = float(eval_num.replace("\n", ""))

    details = {}
    categoryItems = spot.find("div", attrs={"class" : "u_categoryTipsItem"})
    categoryItems = categoryItems.find_all("dl")
    for categoryItem in categoryItems:
        category = categoryItem.dt.text
        rank = float(categoryItem.span.text)
        details[category] = rank

    datum = details
    datum["観光地名"] = spot_name
    datum["評点"] = eval_num
    data.append(datum)

df = pd.DataFrame(data)
df = df[['観光地名', '評点', '楽しさ', '人混みの多さ', '景色', 'アクセス']]
df.to_csv("観光地情報.csv", index=False)

#画像自動取得
url = "https://scraping-for-beginner.herokuapp.com/image"
res = requests.get(url)

soup = bs4.BeautifulSoup(res.text, "html.parser")
img_tags = soup.find_all("img")
for i, img_tag in enumerate(img_tags):
    root_url = "https://scraping-for-beginner.herokuapp.com"
    img_url = root_url + img_tag["src"]

    img = Image.open(io.BytesIO(requests.get(img_url).content))
    img.save(f"img/{i}.jpg")
