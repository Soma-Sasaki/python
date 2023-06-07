import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd

boston = load_boston() #データ読み込み

boston_df = pd.DataFrame(boston["data"], columns = boston["feature_names"])
boston_df["MEDV"] = boston["target"]

#X = boston_df[['RM','LSTAT']].values #説明変数として平均部屋数および低所得者の割合を選択
X = boston_df.iloc[:,0:13].values #説明変数として13個全て使用
y = boston_df["MEDV"] #目的変数として住宅価格を選択

#データを訓練用とテスト用に75:25の割合で分割(常に同じ分け方になる)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

#print('coefficient = ', model.coef_[0]) # 説明変数の係数を出力
#print('intercept = ', model.intercept_) # 切片を出力

print("training score is : {:.2f}".format(model.score(X_train, y_train)))
print("test score is : {:.2f}".format(model.score(X_test, y_test)))

# #リッジ回帰
# from sklearn.linear_model import Ridge
#
# ridge =Ridge().fit(X_train, y_train)
# print("ridge training score is : {:.2f}".format(ridge.score(X_train, y_train)))
# print("ridge test score is : {:.2f}".format(ridge.score(X_test, y_test)))
#
# #ラッソ回帰
# from sklearn.linear_model import Lasso
#
# lasso = Lasso().fit(X_train, y_train)
# print("lasso training score is : {:.2f}".format(lasso.score(X_train, y_train)))
# print("lasso test score is : {:.2f}".format(lasso.score(X_test, y_test)))
# print("Number of features used: {}".format(np.sum(lasso.coef_!=0)))
