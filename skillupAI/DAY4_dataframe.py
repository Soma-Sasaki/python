import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

#絶対パス指定
os.chdir(r"C:\Users\shira\Desktop\就活\スキルアップAI\Day4_vr1_6_0")

df_titanic = pd.read_csv("titanic_train.csv")
df_titanic

df_titanic.sort_values("Age", ascending=False)
df_titanic.loc[(df_titanic["Age"]<40) & (df_titanic["Sex"]=="male")]
df_titanic.loc[df_titanic["Survived"]==1, "Name"].count()

df_titanic.isnull().sum(axis=0)
df_titanic_drop = df_titanic.dropna()
df_titanic_drop.isnull().sum()
df_titanic.info()
df_titanic.describe()
