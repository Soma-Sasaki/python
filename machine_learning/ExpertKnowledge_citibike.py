import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.linear_model import LinearRegression as LR
from sklearn.linear_model import Ridge
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import PolynomialFeatures

citibike = mglearn.datasets.load_citibike()

plt.figure(figsize=(10, 3))
xticks = pd.date_range(start=citibike.index.min(), end=citibike.index.max(), freq='D')
plt.xticks(xticks, xticks.strftime("%a %m-%d"), rotation=90, ha='left')
plt.plot(citibike, linewidth=1)
plt.xlabel("Data")
plt.ylabel("Rentals")
plt.show()

n_train = 184

#与えられた特徴量から回帰機を評価し、プロットする関数
def eval_on_features(features, target, regressor):
    X_train, X_test = features[:n_train], features[n_train:]
    y_train, y_test = target[:n_train], target[n_train:]
    regressor.fit(X_train, y_train)
    print("Test-set R^2: {:.2f}".format(regressor.score(X_test, y_test)))
    y_pred = regressor.predict(X_test)
    y_pred_train = regressor.predict(X_train)
    plt.figure(figsize=(10, 3))
    plt.xticks(range(0, len(X), 8), xticks.strftime("%a %m-%d"), rotation=90, ha='left')
    plt.plot(range(n_train), y_train, label="train")
    plt.plot(range(n_train, len(y_test) + n_train), y_test, '-', label="test")
    plt.plot(range(n_train), y_pred_train, '--', label="prediction train")
    plt.plot(range(n_train, len(y_test) + n_train), y_pred, '--', label="prediction test")
    plt.legend(loc=(1.01, 0))
    plt.xlabel("Date")
    plt.ylabel("Rentals")
    plt.show()


#モデル : ランダムフォレスト
regressor = RFR(n_estimators=100, random_state=0)
#特徴量 : POSIX時刻
X = citibike.index.astype('int64').to_numpy().reshape(-1, 1) // 10**9
y = citibike.values
eval_on_features(X, y, regressor)
#特徴量 : 1日の中の時刻
X_hour = citibike.index.hour.to_numpy().reshape(-1, 1)
eval_on_features(X_hour, y, regressor)
#特徴量 : 1日の中の時刻 + 曜日
X_hour_week = np.hstack([citibike.index.dayofweek.to_numpy().reshape(-1, 1), citibike.index.hour.to_numpy().reshape(-1, 1)])
eval_on_features(X_hour_week, y, regressor)

#モデル : 線形回帰
regressor = LR()
#特徴量 : 1日の中の時刻 + 曜日
eval_on_features(X_hour_week, y, regressor)

#モデル : リッジ回帰
regressor = Ridge()
#OneHotEncoder
enc = OneHotEncoder()
X_hour_week_onehot = enc.fit_transform(X_hour_week).toarray()
eval_on_features(X_hour_week_onehot, y, regressor)
#交互作用特徴量
poly_transformer = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
X_hour_week_onehot_poly = poly_transformer.fit_transform(X_hour_week_onehot)
eval_on_features(X_hour_week_onehot_poly, y, regressor)
