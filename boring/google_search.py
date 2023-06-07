import requests, sys, webbrowser, bs4, os

os.chdir(r"C:\Users\shira\デスクトップ\programming\python\boring")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
res = requests.get("http://google.com/search?q=" + " ".join(sys.argv[1:]), headers=headers)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
link_elms = soup.select(".yuRUbf > a")
num_open = min(5, len(link_elms))
for i in range(num_open):
    webbrowser.open(link_elms[i].get("href"))
