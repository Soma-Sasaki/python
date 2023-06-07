import requests
r = requests.get("https://api.aoikujira.com/time/get.php")

text = r.text
print(text)

bin = r.content
print(bin)
