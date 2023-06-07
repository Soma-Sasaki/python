import os
os.chdir(r"C:\Users\shira\デスクトップ\programming\python\scraping")

from bs4 import BeautifulSoup
import urllib.request as req
import requests

url = "https://api.aoikujira.com/zip/xml/1500042"

res = requests.get(url)
print(res.text)
soup = BeautifulSoup(res.text, "html.parser")

ken = soup.find("ken").string
shi = soup.find("shi").string
cho = soup.find("cho").string
print(ken, shi, cho)
