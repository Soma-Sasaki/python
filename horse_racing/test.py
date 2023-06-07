import os
os.chdir(r"C:\Users\shira\デスクトップ\programming\python\horse_racing")
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs

#画面に表示しないヘッドレスモード
#options = Options()
#options.add_argument("--headless")

chrome_service = fs.Service(executable_path=r"..\chromedriver.exe")
browser = webdriver.Chrome(service=chrome_service)
browser.get("https://db.netkeiba.com/race/202003010302")

html = browser.page_source.encode('utf-8')
soup = BeautifulSoup(html, 'html.parser')


#馬情報の抽出
soup_span = soup.find_all("span")
N = int((len(soup_span)-9)/3) + 1 #馬の数

soup_txt_l = soup.find_all(class_="txt_l")
soup_txt_r=soup.find_all(class_="txt_r")
soup_nowrap = soup.find_all("td",nowrap="nowrap",class_=None)
soup_txt_c = soup.find_all("td",nowrap="nowrap",class_="txt_c")
name, jockey, horse_num, runtime, odds, pas, weight, sex_and_old, handicap, last, popular= [], [], [], [], [], [], [], [], [], [], []

for i in range(N):
    name.append(soup_txt_l[4*i].contents[1].contents[0])
    jockey.append(soup_txt_l[4*i + 1].contents[1].contents[0])
    horse_num.append(soup_txt_r[5*i + 1].contents[0])
    runtime.append(soup_txt_r[5*i + 2].contents[0])    
    odds.append(soup_txt_r[5*i + 3].contents[0])
    pas.append(soup_nowrap[3*i].contents[0])
    weight.append(soup_nowrap[3*i + 1].contents[0])
    sex_and_old.append(soup_txt_c[5*i].contents[0])
    handicap.append(soup_txt_c[5*i + 1].contents[0])
    last.append(soup_txt_c[5*i + 3].contents[0])
    popular.append(soup_span[3*i + 7].contents[0])



horse_info = [name, jockey, horse_num, runtime, odds, pas, weight, sex_and_old, handicap, last, popular]
df = pd.DataFrame(horse_info, index=["馬名", "騎手", "馬番", "タイム", "オッズ", "通過", "体重", "性齢", "斤量", "上がり", "人気"])
#display(df)

#払い戻し情報の抽出
payback = soup.find_all("table", summary='払い戻し')
payback_info=[] #単勝、複勝、枠連、馬連、ワイド、馬単、三連複、三連単の順番で格納

def append_payback1(input_soup): #複勝とワイド以外
    tmp_list = []
    tmp_list.append(input_soup.contents[3].contents[0])
    tmp_list.append(input_soup.contents[5].contents[0])
    payback_info.append(tmp_list)


def append_payback2(input_soup): #複勝とワイド
    tmp_list = []
    for i in range(3):
        tmp_list.append(input_soup.contents[3].contents[2*i])
        tmp_list.append(input_soup.contents[5].contents[2*i])
    payback_info.append(tmp_list)


for i in range(2):
    for j in range(4):
        if ((i==0) and (j==1)) or ((i==1) and (j==0)):
            append_payback2(payback[i].contents[1].contents[2*j])
        else:
            append_payback1(payback[i].contents[1].contents[2*j])  

print(payback_info)