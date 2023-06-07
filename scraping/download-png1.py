import os
os.chdir(r"C:\Users\shira\デスクトップ\programming\python\scraping")

#urllibを使った方法

import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://uta.pw/shodou/img/28/214.png"
savename = "test.png"
urllib.request.urlretrieve(url, savename)
print("保存しました")
