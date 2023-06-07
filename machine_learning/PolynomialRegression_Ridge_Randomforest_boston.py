import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import MinMaxScaler

boston = load_boston()
boston_df = pd.DataFrame(boston["data"], columns = boston["feature_names"])
boston_df["MEDV"] = boston["target"]
X = boston_df.iloc[:,0:13].values #説明変数として13個全て使用
y = boston_df["MEDV"] #目的変数

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

#0から1の間になるようにデータのスケール変換
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#2次までの多項式特徴量と交互作用の抽出
poly = PolynomialFeatures(degree=2).fit(X_train_scaled)
X_train_poly = poly.transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

#交互作用特徴量を入れない場合(Ridge回帰)
print("Ridge Regression")
ridge = Ridge().fit(X_train_scaled, y_train)
print("Score without interactions: {:.3f}".format(ridge.score(X_test_scaled, y_test)))

#交互作用特徴量を入れる場合(Ridge回帰)
ridge = Ridge().fit(X_train_poly, y_train)
print("Score with interactions: {:.3f}".format(ridge.score(X_test_poly, y_test)))

#交互作用特徴量を入れない場合(RandomForest回帰)
print("\n Random Forest Regression")
rf = RFR().fit(X_train_scaled, y_train)
print("Score without interactions: {:.3f}".format(rf.score(X_test_scaled, y_test)))

#交互作用特徴量を入れる場合(Random Forest回帰)
rf = RFR().fit(X_train_poly, y_train)
print("Score with interactions: {:3f}".format(rf.score(X_test_poly, y_test)))
