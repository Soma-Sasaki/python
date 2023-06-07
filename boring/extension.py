import os
from pathlib import Path
os.chdir(r"D:\com.nttdocomo.android.sdcardbackup\manual\multimedia\20180703235258\audio")

#指定ディレクトリ内ファイルの拡張子を変更
for f in Path(".").rglob("*.sdb"):
    f.rename(f.stem + ".mp3")
