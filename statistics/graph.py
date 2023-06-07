import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()
x = [0, 1, 2, 3, 4]
y = [5, 6, 7, 8, 9]

plt.plot(x, y)
plt.show()
fish_data = [2, 3, 3, 4, 4, 4, 4, 5, 5, 6]
#カーネル密度推定によるヒストグラム平滑化
sns.distplot(fish_data)
#2変量データに対するヒストグラム
fish = pd.DataFrame({'species' : ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'], 'length' : [2, 3, 3, 4, 4, 4, 4, 5, 6, 7, 8, 9, 9, 9, 9, 10, 10, 11]})
fish.groupby('species').describe()
length_a = fish.query('species == "A"')['length']
length_b = fish.query('species == "B"')['length']
sns.distplot(length_a, bins=5, color='black', kde=False)
sns.distplot(length_b, bins=5, color='gray', kde=False)
#箱ひげ図
sns.boxplot(x='species', y='length', data=fish, color='gray')
#バイオリンプロット
sns.violinplot(x='species', y='length', data=fish, color='gray')
