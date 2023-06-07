import os
os.chdir(r"C:\Users\shira\Desktop\python\scraping")

import requests
r = requests.get("https://uta.pw/shodou/img/3/3.png")

with open("test.png", "wb") as f:
    f.write(r.content)
