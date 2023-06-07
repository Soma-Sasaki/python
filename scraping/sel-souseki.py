import os
os.chdir(r"C:\Users\shira\Desktop\python\scraping")

from bs4 import BeautifulSoup
import requests

url = "https://www.aozora.gr.jp/index_pages/person148.html"
res = requests.get(url)
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text, "html.parser")

li_list = soup.select("body > ol > li")
for li in li_list:
    a = li.a
    if a != None:
        name = a.string
        href = a.attrs["href"]
        print(name, ">", href)
