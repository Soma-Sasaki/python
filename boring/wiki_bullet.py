#! python3
# wiki_bullet.py クリップボードのテキストの各行に点を打つやつ

import pyperclip

text = pyperclip.paste()
text
lines = text.split("\r\n")
lines
for i in range(len(lines)):
    lines[i] = "* " + lines[i]
lines
text = "\r\n".join(lines)
text
pyperclip.copy(text)
