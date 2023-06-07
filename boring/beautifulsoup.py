import requests, bs4, os

os.chdir(r"C:\Users\shira\デスクトップ\programming\python\boring")

res = requests.get("http://nostarch.com")
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text)
type(no_starch_soup)

example_file = open("example.html")
example_soup = bs4.BeautifulSoup(example_file)
elems = example_soup.select("#author")
elems
p_elems = example_soup.select("p")
p_elems
