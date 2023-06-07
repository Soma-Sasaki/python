import os
os.chdir(r"C:\Users\shira\Desktop\python\scraping")
from bs4 import BeautifulSoup
from urllib import parse
import requests, time

#リンクの抽出
html = open("eki-link.html", encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")
links = soup.select("a")
result = []
for a in links:
    href = a.attrs["href"]
    title = a.string
    result.append((title, href))
print(result)

#リンク先のダウンロード
savepath = "./out"
if not os.path.exists(savepath): os.mkdir(savepath)
for title, url in result:
    path = savepath + "/" + url + ".html"
    a_url = parse.urljoin("http://example.com", url)
    mem = requests.get(a_url)
    with open(path, mode="wb") as f:
        f.write(mem.content)
    time.sleep(1)
