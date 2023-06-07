import os
os.chdir(r"C:\Users\shira\デスクトップ\programming\python\scraping")
import urllib.parse
import requests

context = ssl.SSLContext(ssl.PROTOCOL_TLS)

API = "https://api.aoikujira.com/zip/xml/get.php"

values = {'fmt' : 'xml', 'zn' : '1500042'}
params = urllib.parse.urlencode(values)
url = API + "?" + params
print(url)
data = requests.get(url)
print(data.text)
