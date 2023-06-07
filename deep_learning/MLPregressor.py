import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPRegressor

#RMSEを求める関数定義
def rmse(y_true, y_pred):
    rmse = np.sqrt(metrics.mean_squared_error(y_true, y_pred))
    return rmse

os.chdir(r"C:\Users\shira\Desktop\python\architecture")
data = pd.read_csv('window10overlap9.csv')
X, y = data.iloc[:,0:-1].values, data['SpO2'].values #説明変数と目的変数

#グリッドサーチ用のハイパーパラメータ
param_grid = {'hidden_layer_sizes': [(100,), (100,100), (100,100,100)], \
              'max_iter': [100, 500, 1000], 'solver': ['sgd', 'adam']}

#5分割交差検証を用いたグリッドサーチを行い, 最も精度が高いパラメータセット表示
kfold = KFold(n_splits=5, shuffle=False)
splitter = kfold.split(X)
grid_search = GridSearchCV(MLPRegressor(), param_grid, cv=kfold, \
              scoring=metrics.make_scorer(rmse, greater_is_better=False)).fit(X, y)
print("Best parameters: {}".format(grid_search.best_params_))

#最も精度が高いパラメータセットにおけるモデルの再作成
mlp_re = MLPRegressor(**grid_search.best_params_)

#結果の表示
fig, axes = plt.subplots(2,3, figsize=(14, 8))
axes[1,2].axis('off')
RMSE = []
for i, (ax, (train, test)) in enumerate(zip(axes.ravel(), splitter)):
    X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
    mlp_re.fit(X_train, y_train)
    predict_mlp = mlp_re.predict(X_test)
    RMSE.append(rmse(y_test, predict_mlp))
    ax.set_title("Split {}".format(i))
    ax.plot(y_test, label="True")
    ax.plot(predict_mlp, label="predicted")
    ax.set_xlabel("time[s]")
    ax.set_ylabel("SpO2[%]")
    ax.legend(loc='lower left')
fig.tight_layout()
plt.show()
print("RMSE : {}\n".format(sum(RMSE)/len(RMSE)))
