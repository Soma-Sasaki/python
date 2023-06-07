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

fish = pd.read_csv("3-4-1-fish_length_100000.csv")['length']
sampling_result = np.random.choice(fish, size=10, replace=False)
np.var(sampling_result, ddof=0)

#確率密度作成
x = np.arange(1, 7.1, 0.1)
y = stats.norm.pdf(x=x, loc=np.mean(fish), scale=np.std(fish))
sns.distplot(fish, kde=False, norm_hist=True)
plt.plot(x, y, color='black')
plt.show()

#母集団を「平均4, 標準現作0.8の正規分布」とする

population = stats.norm(loc=np.mean(fish), scale=np.std(fish))

sample_mean = []
np.random.seed(1)
for i in range(10000):
    sample = population.rvs(size=10)
    sample_mean.append(np.mean(sample))

np.mean(sample_mean) #洋本平均の平均値
np.std(sample_mean, ddof=1) #標本平均の標準偏差

#サンプルサイズと標本平均
size_array = np.arange(10, 100100, 100)
sample_mean_array = np.zeros(len(size_array))
np.random.seed(1)
for i in range(len(size_array)):
    sample = population.rvs(size=size_array[i])
    sample_mean_array[i] = np.mean(sample)

plt.plot(size_array, sample_mean_array)
plt.xlabel("sample size")
plt.ylabel("sample mean")
plt.show()

#標本平均を計算する関数作成
def calc_sample_mean(size, n_trial, loc, scale):
    population = stats.norm(loc=loc, scale=scale)
    sample_mean_array = np.zeros(n_trial)
    for i in range(n_trial):
        sample = population.rvs(size=size)
        sample_mean_array[i] = np.mean(sample)
    return(sample_mean_array)


np.random.seed(1)
np.mean(calc_sample_mean(10, 10000, np.mean(fish), np.std(fish)))

#標本分散の平均値
sample_var_array = np.zeros(10000)
np.random.seed(1)
for i in range(10000):
    sample = population.rvs(size=10)
    sample_var_array[i] = np.var(sample, ddof=0)
np.mean(sample_var_array) #分散を過小評価している

#不偏分散使ってみる
sample_var_array = np.zeros(10000)
np.random.seed(1)
for i in range(10000):
    sample = population.rvs(size=10)
    sample_var_array[i] = np.var(sample, ddof=1)
np.mean(sample_var_array) #母分散0.64に近い値を取る

#ってことで標本分散(不偏分散使ったほう)を計算する関数作成
def calc_sample_var(size, n_trial, loc, scale):
    population = stats.norm(loc=loc, scale=scale)
    sample_var_array = np.zeros(n_trial)
    for i in range(n_trial):
        sample = population.rvs(size=size)
        sample_var_array[i] = np.var(sample, ddof=1)
    return(sample_var_array)

#サンプルサイズと標本分散
size_array = np.arange(10, 100100, 100)
sample_var_array = np.zeros(len(size_array))
np.random.seed(1)
for i in range(len(size_array)):
    sample_var_array[i] = calc_sample_var(size_array[i], 1, 4, 0.8)
plt. plot(size_array, sample_var_array)
plt.xlabel("sample size")
plt.ylabel("unvias var")
plt.show()

#中心極限定理
n_size = 10000
n_trial = 50000
coin = [0, 1]
count_coin = np.zeros(n_trial)
np.random.seed(1)
for i in range(n_trial):
    count_coin[i] = np.sum(np.random.choice(coin, size=n_size, replace=True))
sns.distplot(count_coin)
