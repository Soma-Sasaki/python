import os
os.chdir(r"C:\Users\shira\Desktop\python\scraping")

from bs4 import BeautifulSoup
import requests
fp = open("books.html", encoding="utf-8").read()
soup = BeautifulSoup(fp, "html.parser")

sel = lambda q : print(soup.select_one(q).string)
sel("#nu")
sel("ul > li#nu")
sel("ul#bible > li#nu")
sel("li[id='nu']")
sel("li:nth-of-type(4)")

print(soup.select("li")[3].string)
print(soup.find_all("li")[3].string)
