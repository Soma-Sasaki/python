import os
os.chdir(r"C:\Users\shira\デスクトップ\programming\python\scraping")

from bs4 import BeautifulSoup

html = """
<html><body>
<div id="meigen">
    <h1>トルストイの名言</h1>
    <ul class="items">
        <li>汝の心に教えよ、心に学ぶな。</li>
        <li>謙虚な人は誰からも好かれる。</li>
        <li>強い人々は、いつも気取らない。</li>
    </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.select_one("div#meigen > h1").string #idセレクタ
h2 = soup.select_one("[id='meigen'] > h1").string #属性セレクタ

print("h1 =", h1)
print("h2 =", h2)

li_list1 = soup.select("div#meigen > ul.items > li")
li_list2 = soup.select(".items > li")
li_list1
li_list2

for li in li_list1:
    print("li =", li.string)
