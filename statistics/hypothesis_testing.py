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

junk_food = pd.read_csv("3-8-1-junk-food-weight.csv")["weight"]
junk_food

#t検定
mu = np.mean(junk_food)
df = len(junk_food) - 1
se = (np.std(junk_food, ddof=1)) / (np.sqrt(len(junk_food)))
t_value = (mu - 50) / (se)
t_value

alpha = stats.t.cdf(t_value, df=df) #母平均を50としたとき, t値が標本のt値を下回る確率(累積分布関数から求まる)
p = 2 * (1 - alpha)
p

stats.ttest_1samp(junk_food, 50) #もっとかんたん

#シミュレーションによるp値の計算
#p値は「帰無仮説が正しいと仮定し, 何度も標本抽出～t値計算を繰り返した時, t標本以上のt値が得られる割合」
t_value_array = np.zeros(50000)
sigma = np.std(junk_food, ddof=1)
np.random.seed(1)
norm_dist = stats.norm(loc=50, scale=sigma) #帰無仮説は「母集団が平均50の正規分布に従う」
for i in range(50000):
    sample = norm_dist.rvs(size=len(junk_food))
    t_value_array[i] = (np.mean(sample) - 50) / (np.std(sample, ddof=1) / np.sqrt(len(junk_food)))
(sum(t_value_array >= t_value) / 50000) * 2




#平均値の差の検定

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

paired_test_data = pd.read_csv('3-9-1-paired-t-test.csv')
paired_test_data

#対応のあるt検定
before = np.array(paired_test_data.query('medicine == "before"')["body_temperature"])
before
after = np.array(paired_test_data.query('medicine == "after"')["body_temperature"])
after
diff = after - before
diff
stats.ttest_1samp(diff, 0)
stats.ttest_rel(after, before) #もっとかんたん

#対応のないt検定
mean_bef = np.mean(before)
mean_aft = np.mean(after)
sigma_bef = np.var(before, ddof=1)
sigma_aft = np.var(after, ddof=1)
m = len(before)
n = len(after)
t_value = (mean_aft - mean_bef) / (np.sqrt((sigma_bef / m) + (sigma_aft / n)))
t_value
stats.ttest_ind(after, before, equal_var=False)

#分割表を用いた検定

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

#カイ二乗検定

1 - sp.stats.chi2.cdf(x=6.667, df=1)
click_data = pd.read_csv('3-10-1-click_data.csv')
cross = pd.pivot_table(data = click_data, index='color', columns='click')
np.set_printoptions(precision=3)
sp.stats.chi2_contingency(cross, correction=False)
