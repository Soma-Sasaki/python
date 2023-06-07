#ボストン住宅価格の単回帰

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

boston = load_boston() #データ読み込み

boston_df = pd.DataFrame(boston["data"], columns = boston["feature_names"])
boston_df['MEDV'] = boston["target"]

X = boston_df[['RM']].values #説明変数として平均部屋数を選択
y = boston_df[['MEDV']].values #目的変数として住宅価格を選択

#データを訓練用とテスト用に7:3の割合で分割(常に同じ分け方になる)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

#print('coefficient = ', model.coef_[0]) # 説明変数の係数を出力
#print('intercept = ', model.intercept_) # 切片を出力

#プロット
plt.scatter(X, y) #散布図のプロット
plt.plot(X, model.predict(X), color = 'blue') #回帰直線のプロット

plt.title('Single Regression of Boston Home Prices')
plt.xlabel('Average number of rooms')
plt.ylabel('Prices in $1000\'s')
plt.grid()

plt.show()

score = model.score(X_test, y_test)

print('score is', score)
