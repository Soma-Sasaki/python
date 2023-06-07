import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

#絶対パス指定
os.chdir(r"C:\Users\shira\デスクトップ\E資格\スキルアップAI\Day5_vr1_4_0")

x = np.linspace(0, 10, 20)
y = x**2
z = (x - 1)**3
w = ((x - 2)*(x - 4))**2
v = x + 1
plt.plot(x, y, label="y = x^2", linestyle="dashed")
plt.plot(x, z, label="z = (x-1)^3")
plt.plot(x, w, label="w = {(x-2)(x-4)}^2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

Fx = [y, z, w, v]
Fxname = ["y = x^2", "z = (x-1)^3", "w = {(x-2)(x-4)}^2", "v = x+1"]

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes.ravel()
for i, ax in enumerate(axes.ravel()):
    ax.plot(x, Fx[i])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(Fxname[i])
plt.tight_layout()
plt.show()

x = np.linspace(-np.pi, np.pi, 100)
y = [np.sin(x), np.cos(x), np.tan(x)]

fig, axes = plt.subplots(3, 1, figsize=(8, 6))
for i, ax in enumerate(axes.ravel()):
    ax.plot(x, y[i])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
plt.tight_layout()
plt.show()


tips = pd.read_csv("tips/tips.csv")
tips

left = range(4)
height = tips.day.value_counts().values
day = tips.day.value_counts().keys()

#棒グラフ
plt.bar(left, height, tick_label = day)

#円グラフ
plt.pie(tips.day.value_counts(), autopct="%.1f%%", labels=day)

#ヒストグラム
plt.hist(tips.total_bill, bins=20, color="green")
plt.xlabel("total_bill")
plt.ylabel("counts")
plt.title("hisogram of total_bill")


#散布図
plt.scatter("total_bill", "tip", data=tips)
plt.xlabel("total_bill")
plt.ylabel("tip")


tips_male = tips.loc[tips["sex"]=="Male"]
tips_female = tips.loc[tips["sex"]=="Female"]
fig, axes = plt.subplots(2, 1, figsize=(8, 6))
axes[0].scatter(tips_male["total_bill"], tips_male["tip"], color="blue")
axes[0].set_title("Male")
axes[1].scatter(tips_female["total_bill"], tips_female["tip"], color="red")
axes[1].set_title("Female")
for ax in axes:
    ax.set_xlabel("total_bill")
    ax.set_ylabel("tip")
plt.tight_layout()
plt.show()
