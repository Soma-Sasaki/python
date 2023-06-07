import requests, os

os.chdir(r"C:\Users\shira\Desktop\python\boring")

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
try:
    res.raise_for_status()
    len(res.text)
    play_file = open("RomeoAndJuliet.txt", "wb")
    for chunk in res.iter_content(100000):
        play_file.write(chunk)
    play_file.close()
except Exception as exc:
    print("ダウンロードに問題あり: {}".format(exc))



res = requests.get("https://inventwithpython.com/page_that_does_not_exist")
try:
    res.raise_for_status()
    print("うまくいったー")
except Exception as exc:
    print("ダウンロードに問題あり: {}".format(exc))
