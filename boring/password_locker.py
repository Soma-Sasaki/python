#! python3
# password_locker.py パスワード管理システム(脆弱性あり)

import sys
import pyperclip

PASSWORDS = {"email": "soma.sasaki.q3@dc.tohoku.ac.jp", "PIP100031": "rRmFpkUw"}

if len(sys.argv) < 2:
    print("使い方: python ファイル名 アカウント名")
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("パスワードをクリップボードにコピーします")
else:
    print(account + "というアカウント名はありません")
