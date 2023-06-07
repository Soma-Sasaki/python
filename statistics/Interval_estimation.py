import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
from scipy import stats
import seaborn as sns
import os
sns.set()

#絶対パス指定
os.chdir(r"C:\Users\shira\Desktop\python\statistics\sample")

fish = pd.read_csv('3-7-1-fish_length.csv')['length']

#母平均・母分散の点推定
mu = np.mean(fish)
mu
sigma_2 = np.var(fish, ddof=1)
sigma_2

#母平均の区間推定
df = len(fish) - 1
se = (np.std(fish, ddof=1))/(np.sqrt(len(fish)))
interval = stats.t.interval(alpha=0.95, df=df, loc=mu, scale=se)
interval

#信頼区間の幅を決める要素
se2 = 10*(np.std(fish, ddof=1))/(np.sqrt(len(fish))) #標本標準偏差を10倍
interval = stats.t.interval(alpha=0.95, df=df, loc=mu, scale=se2)
interval #幅が広くなる
df2 = len(fish)*10 - 1 #サンプルサイズを10倍
se3 = (np.std(fish, ddof=1))/(np.sqrt(len(fish)*10)) #標本標準偏差を10倍
interval = stats.t.interval(alpha=0.95, df=df2, loc=mu, scale=se3)
interval #幅が狭くなる
df = len(fish) - 1
se = (np.std(fish, ddof=1))/(np.sqrt(len(fish)))
interval = stats.t.interval(alpha=0.99, df=df, loc=mu, scale=se) #信頼係数を大きくする
interval

#区間推定の結果の解釈
be_included_array = np.zeros(20000, dtype='bool')
np.random.seed(1)
norm_dist = stats.norm(loc=4, scale=0.8)
for i in range(0, 20000):
    sample = norm_dist.rvs(size=10)
    df = len(sample) - 1
    mu = np.mean(sample)
    se = (np.std(sample, ddof=1))/(np.sqrt(len(sample)))
    interval = stats.t.interval(0.95, df, mu, se)
    if (interval[0] <= 4 and interval[1] >= 4):
        be_included_array[i] = True
sum(be_included_array)/len(be_included_array)
