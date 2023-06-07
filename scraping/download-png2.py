import os
os.chdir(r"C:\Users\shira\Desktop\python\scraping")


#urllibを使った方法

"""
import urllib.request
import ssl
#ssl._create_default_https_context = ssl._create_unverified_context
context = ssl.SSLContext(ssl.PROTOCOL_TLS)

url = "https://uta.pw/shodou/img/28/214.png"
savename = "test100.png"

mem = urllib.request.urlopen(url, context=context).read()
with open(savename, mode="wb") as f:
    f.write(mem)
    print("保存しました")

"""

#requestsを使った方法

import requests

url = "https://uta.pw/shodou/img/28/214.png"
savename = "test2.png"
mem = requests.get(url)
with open(savename, mode="wb") as f:
    f.write(mem.content)
    print("保存しました")
