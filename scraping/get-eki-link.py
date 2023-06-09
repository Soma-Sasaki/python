from bs4 import BeautifulSoup

html = open("eki-link.html", encoding="utf-8").read()
soup = BeautifulSoup(html, "html.parser")
links = soup.select("a")
result = []
for a in links:
    href = a.attrs["href"]
    title = a.string
    result.append((title, href))
print(result)
