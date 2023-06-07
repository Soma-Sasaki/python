import os
os.chdir(r"C:\Users\shira\Desktop\python\scraping")

from bs4 import BeautifulSoup
import requests
fp = open("fruits-vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

print(soup.select_one("#ve-list > li:nth-of-type(4)").string)
print(soup.select("#ve-list > li.black")[1].string)
cond = {"data-lo":"us", "class":"black"}
print(soup.find(id="ve-list").find("li", cond).string)
