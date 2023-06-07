import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

#絶対パス指定
os.chdir(r"C:\Users\shira\デスクトップ\E資格\スキルアップAI\Day6_vr1_5_0")

tips = pd.read_csv("tips/tips.csv")
tips

#棒グラフ
sns.countplot(tips.day)

#ヒストグラム
sns.displot(tips.total_bill, bins=20, kde=True)

#散布図
sns.regplot(tips.total_bill, tips.tip, fit_reg=True)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
sns.countplot(tips.day, ax=axes[0])
sns.regplot(tips.total_bill, tips.tip, ax=axes[1])

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
sns.countplot(tips.smoker, ax=axes[0])
sns.distplot(tips.tip, bins=20, kde=False, ax=axes[1])
sns.regplot(tips.total_bill, tips.tip, fit_reg=False, ax=axes[2])

sns.pairplot(tips)

tips.corr().style.background_gradient("summer_r")
sns.heatmap(tips.corr(), cmap="summer_r")

#カテゴリごとにデータの分布を表示
sns.swarmplot("day", "total_bill", data=tips, hue="sex", dodge=True)

sns.boxplot(tips.day, tips.tip, hue=tips.sex)


house = pd.read_csv("house/house_data.csv")
house

plt.scatter(house.price*100, house.sqft_living, s=1, color="green")
plt.xlabel("price[yen]")
plt.ylabel("size of livingroom")

house["good/bad"] = "good"
house.loc[(house.condition >= 0) & (house.condition <= 2), "good/bad"] = "bad"
house
