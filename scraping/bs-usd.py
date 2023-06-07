import os
os.chdir(r"C:\Users\shira\デスクトップ\programming\python\scraping")

from bs4 import BeautifulSoup
import requests

url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=usdjpy"

res = requests.get(url)
print(res.text)
soup = BeautifulSoup(res.text, "html.parser")
price1 = soup.select_one(".stoksPrice")
print("usd/jpy =", price1)
