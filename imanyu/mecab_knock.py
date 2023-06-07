import MeCab, os
from glob import glob
import matplotlib.pyplot as plt
import japanize_matplotlib
from collections import defaultdict
os.chdir(r"C:\Users\shira\Desktop\python\imanyu")

txt = '''はじめまして、こちらはいまにゅチャンネルです。
Pythonを使いこなして色んなことができるように、一緒に学んでいきましょう。
本講義では特に自然言語処理について学びます。
様々なライブラリを活用することで手軽に分析ができます。
では早速進めていきましょう。'''

with open("output.txt", "x") as f:
    f.write(txt)

filepaths = glob("*.txt")
filepath = filepaths[0]
with open(filepath, "r") as f:
    txt = f.read()
txt

#MeCab形式の形態素解析
tagger = MeCab.Tagger()
print(tagger.parse(txt))

#chasen形式の形態素解析
tagger = MeCab.Tagger("-Ochasen")
print(tagger.parse(txt))

#分かち書き
tagger = MeCab.Tagger("-Owakati")
print(tagger.parse(txt))

#カタカナ変換
tagger = MeCab.Tagger("-Oyomi")
print(tagger.parse(txt))

#品詞ごとの分類
tagger = MeCab.Tagger()
parsed_txt = tagger.parse(txt)
elements = parsed_txt.split("\n")[:-2]
elements
results = []
for element in elements:
    parts = element.split(",")
    surface_pos, pos1, base = parts[0], parts[1], parts[-3]
    surface, pos = surface_pos.split("\t")
    results.append(dict(表層形=surface, 基本形=base, 品詞=pos, 品詞1=pos1))
results

#動詞の抽出
surface_verbs = set()
for result in results:
    if result["品詞"] == "動詞":
        surface_verbs.add(result["表層形"])
surface_verbs

base_verbs = set()
for result in results:
    if result["品詞"] == "動詞":
        base_verbs.add(result["基本形"])
base_verbs

#頻度(デフォルトデクトはキーがなければ新たに作ってくれる)
word_freq = defaultdict(int)
for result in results:
    if result["品詞"] != "記号":
        word_freq[result["基本形"]] += 1
word_freq

#頻度順に並び替え
sorted_word_freq = sorted(word_freq.items(), key=lambda x:x[1], reverse=True)
sorted_word_freq

keys = [_[0] for _ in sorted_word_freq[:10]]
values = [_[1] for _ in sorted_word_freq[:10]]
plt.figure(figsize=(8, 4))
plt.bar(keys, values)
plt.show()

#バイグラムとトライグラム
txt = "Pythonを一緒に学びましょう"
tagger = MeCab.Tagger("-Owakati")
words = tagger.parse(txt).split(" ")[:-1]
words
for i in range(len(words)-1):
    print("".join(words[i:i+2]))

for i in range(len(words)-2):
    print("".join(words[i:i+3]))
