#! python3
# regex.py クリップボードから電話番号とメアドの検索

import pyperclip, re
import mojimoji

phone_regex = re.compile(r"""(
    (\d{1,4}|\(\d{1,4}\))? # 市外局番
    (\s|-)? # 区切り
    (\d{1,4}) # 市内局番
    (\s|-) # 区切り
    (\d{3,4}) # 加入者番号
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # 内線番号
    )""", re.VERBOSE)

email_regex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+ # ユーザー名
    @ # アットマーク
    [a-zA-Z0-9.-]+ # ドメイン名
    (\.[a-zA-Z]{2,4}) # ドットなんとか
    )""", re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phone_regex.findall(text):
    phone_num = "-".join([mojimoji.zen_to_han(groups[1]), mojimoji.zen_to_han(groups[3]), mojimoji.zen_to_han(groups[5])])
    if groups[8] != "":
        phone_num += " x" + groups[8]
    matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])

print(matches)

if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("クリップボードにコピーしました: ")
    print("\n".join(matches))

else:
    print("電話番号やメアドは見つかりませんでした")
