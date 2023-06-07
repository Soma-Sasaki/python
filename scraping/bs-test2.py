from bs4 import BeautifulSoup

html = """
<html><body>
    <h1 id="title">スクレイピングとは？</h1>
    <p id="body1">Webページを解析すること。</p>
    <p id="body2">任意の箇所を抽出すること。</p>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')

h1 = soup.find(id="title")
p1 = soup.find(id="body1")
p2 = soup.find(id="body2")

print(h1.string)
print(p1.string)
print(p2.string)
