import os
os.chdir(r"C:\Users\shira\Desktop\python\scraping")
import urllib.request
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS)

url = "https://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url, context=context)
data = res.read()

print(data.decode("utf-8"))
