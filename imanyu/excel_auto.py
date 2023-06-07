import os
import pandas as pd
from glob import glob
import tensorflow


os.chdir(r"C:\users\shira\Desktop\python\imanyu")

filepaths = glob("*.xlsx")

def extract(filepath):
    _df = pd.read_excel(filepath)
    columns = _df.iloc[10, [1, 2, 4, 10, 11, 14]]
    df = _df.iloc[11:23, [1, 2, 4, 10, 11, 14]]
    df.columns = columns
    df["企業名"] = _df.iloc[2, 0]
    df["企業コード"] = _df.iloc[3, 4]
    df["請求書No"] = _df.iloc[2, 12]
    df["発行日"] = _df.iloc[3, 12]
    df["発行者"] = _df.iloc[4, 12]
    df["発行者コード"] = _df.iloc[4, 13]
    return df

df = pd.DataFrame()

for filepath in filepaths:
    _df = extract(filepath)
    df = pd.concat([df, _df])
df = df.dropna()
df = df.iloc[:, [6, 7, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5]]
df.to_excel("./all_data.xlsx", index=False)
