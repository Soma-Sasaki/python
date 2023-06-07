#! python3
# map_address.py コマンドラインやクリップボードに指定した住所の地図を開く
import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)
