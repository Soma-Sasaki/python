from urllib.parse import urljoin

base = "http://example.com/html/a.html"

URL = lambda q : print(urljoin(base, q))

print(urljoin(base, "b.html"))
URL("b.html")
URL("sub/c.html")
URL("../css/hoge.png")
URL("http://kujirahand.com/wiki")
