import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
from scipy import stats
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm
import os
sns.set()

#絶対パス指定
os.chdir(r"C:\Users\shira\Desktop\python\statistics\sample")

weather_beer = pd.DataFrame({"beer" : [6, 8, 2, 4, 10, 12], "weather" : ["cloudy", "cloudy", "rainy", "rainy", "sunny", "sunny"]})
weather_beer
sns.boxplot(x="weather", y="beer", data=weather_beer, color='gray')
#天気による影響のみを考えた場合の売上
effect = [7, 7, 3, 3, 11, 11]
#群間分散
mu_effect = np.mean(effect)
squares_model = np.sum((effect - mu_effect)**2) #群間の偏差平方和
squares_model
df_model = 3 - 1 #水準の種類数(曇り・雨・晴れ) - 1
variance_model = squares_model / df_model
variance_model
#群内分散
resid = weather_beer.beer - effect
squares_resid = np.sum(resid**2) #群内のの偏差平方和
squares_resid
df_resid = 6 - 3 #サンプルサイズ - 水準の種類数
variance_resid = squares_resid / df_resid
variance_resid

#F比, p値の計算
f_ratio = variance_model / variance_resid
f_ratio
p = 1 - sp.stats.f.cdf(x=f_ratio, dfn=df_model, dfd=df_resid)
p

anova_model = smf.ols("beer~weather", data=weather_beer).fit()
sm.stats.anova_lm(anova_model, typ=2)


#回帰モデルにおける分散分析

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
from scipy import stats
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api as sm
import os
sns.set()

#絶対パス指定
os.chdir(r"C:\Users\shira\Desktop\python\statistics\sample")

beer = pd.read_csv('5-1-1-beer.csv')
lm_model = smf.ols(formula='beer~temperature', data=beer).fit()
df_lm_model = 2 - 1 #推定されるパラメタの数 - 1
df_lm_resid = 30 - 2 #サンプルサイズ - パラメタの数
sm.stats.anova_lm(lm_model, typ=2)

#複数の説明変数を持つモデル
sales = pd.read_csv('5-3-1-lm-model.csv')
sales
lm_sales = smf.ols('sales ~ weather + humidity + temperature + price', data=sales).fit()
lm_sales.params
