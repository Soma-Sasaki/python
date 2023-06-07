import traceback, os, shutil, logging

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
os.chdir(r"C:\Users\shira\Desktop\python\boring")
#例外を起こす
def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("symbolは1文字の文字列でなければならない。")
    if width <= 2:
        raise Exception("widthは2より大きくなければならない。")
    if height <= 2:
        raise Exception("heightは2より大きくなければならない。")
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (("*", 4, 4), ("x", 1, 3), ("ZZ", 3, 3), ("O", 20, 5)):
    try:
        box_print(sym, w, h)
    except Exception as err:
        print("例外が起こりました!!: " + str(err))

#トレースバックを文字列として受け取る
try:
    raise Exception("これはエラーメッセージです。")
except:
    error_file = open("errorInfo.txt", "w")
    error_file.write(traceback.format_exc())
    error_file.close()
    print("トレースバック情報をerrorInfo.txtに書きました")

#アサート(python -O debug.py で無効化)
market_2nd = {"ns": "green", "ew": "red"}
mission_16th = {"ns": "red", "ew": "green"}

def switch_lights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == "green":
            stoplight[key] = "yellow"
        elif stoplight[key] == "yellow":
            stoplight[key] = "red"
        elif stoplight[key] == "red":
            stoplight[key] = "green"
    assert "red" in stoplight.values(), "赤信号がない！ " + str(stoplight)

switch_lights(market_2nd)

logging.debug("プログラミング開始")
def factorial(n):
    logging.debug("factorial({})開始".format(n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug(f"i = {i}, total = {total}")
    logging.debug("factorial({})終了".format(n))
    return total

print(factorial(5))
logging.debug("プログラミング終了")
