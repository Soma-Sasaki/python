import os
os.chdir(r"C:\Users\shira\デスクトップ\programming\python\scraping")

import sys
import urllib.parse as parse
import requests

#コマンドライン引数を得る
if len(sys.argv) <= 1:
    print("USAGE: hyakunin.py (keyword)")
    sys.exit()
keyword = sys.argv[1]

API = "https://api.aoikujira.com/hyakunin/get.php"
query = {"fmt": "ini", "key": keyword}
params = parse.urlencode(query)
url = API + "?" + params
print("url=", url)

data = requests.get(url)
print(data.text)
