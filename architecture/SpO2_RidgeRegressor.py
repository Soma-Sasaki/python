import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.metrics import make_scorer
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

print("Ridge Regression")

#RMSEを求める関数定義
def rmse(y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    return rmse

os.chdir(r"C:\Users\shira\Desktop\python\architecture")
data = pd.read_csv('window10overlap9_R.csv')

X = data.iloc[:,0:-1].values #説明変数
y = data['SpO2'].values #目的変数

param_grid = {'alpha': [0.01, 0.05, 0.1, 0.5, 1]} #グリッドサーチ用のハイパーパラメータ
k = 5 #交差検証の分割数
kfold = KFold(n_splits=k, shuffle=False) #5分割交差検証(シャッフルなし)

#RMSEを基準としてグリッドサーチ
grid_search = GridSearchCV(Ridge(), param_grid, cv=kfold, scoring=make_scorer(rmse, greater_is_better=False))
grid_search.fit(X, y)
results = pd.DataFrame(grid_search.cv_results_)
print("Best parameters: {}".format(grid_search.best_params_)) #最も精度が高いパラメータセット表示

ridge_re = Ridge(**grid_search.best_params_) #最も精度が高いパラメータセットにおけるモデル作成
splitter = kfold.split(X)

#結果の図示
fig, axes = plt.subplots(2,3, figsize=(14, 8))
axes[1,2].axis('off')
MAE, RMSE = [], []
for i, (ax, (train, test)) in enumerate(zip(axes.ravel(), splitter)):
    X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
    ridge_re.fit(X_train, y_train)
    predict_ridge = ridge_re.predict(X_test)
    MAE.append(mean_squared_error(y_test, predict_ridge))
    RMSE.append(np.sqrt(mean_squared_error(y_test, predict_ridge)))
    ax.set_title("Split {}".format(i))
    ax.plot(y_test, label="True")
    ax.plot(predict_ridge, label="predicted")
    ax.set_xlabel("time[s]")
    ax.set_ylabel("SpO2[%]")
    ax.legend(loc='lower left')

fig.tight_layout()
plt.show()

# print("MAE : {}".format(sum(MAE)/len(MAE)))
print("RMSE : {}\n".format(sum(RMSE)/len(RMSE)))
