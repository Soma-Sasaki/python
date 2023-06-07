import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import seaborn as sns
import os

sns.set()

#絶対パス指定
os.chdir(r"C:\Users\shira\Desktop\python\statistics\sample")

#t値の標本分布
np.random.seed(1)
norm_dist = stats.norm(loc=4, scale=0.8)
t_value_array = np.zeros(10000)
for i in range(10000):
    sample = norm_dist.rvs(size=10)
    t_value_array[i] = (np.mean(sample) - 4)/(np.std(sample, ddof=1)/np.sqrt(10))
sns.distplot(t_value_array)
x = np.arange(-8, 8.1, 0.1)
plt.plot(x, stats.norm.pdf(x=x), color='black', linestyle='dotted')
plt.show()
