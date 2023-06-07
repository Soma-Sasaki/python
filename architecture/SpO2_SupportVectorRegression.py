import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import make_scorer
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline

print("Support Vector Regression (SVR)")
#RMSEを求める関数定義
def rmse(y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    return rmse

os.chdir(r"C:\Users\shira\デスクトップ\programming\python\architecture")
data = pd.read_csv('window10overlap9_R.csv')

X = data.iloc[:,0:-1].values #説明変数
y = data['SpO2'].values #目的変数

pipe = Pipeline([("scaler", MinMaxScaler()), ("svr", SVR())])

param_grid = {'svr__C': [0.01, 0.1, 1, 10, 100], 'svr__epsilon': [0.0001, 0.001, 0.01, 0.1, 1], 'svr__kernel': ['rbf'], 'svr__gamma': ['auto']} #グリッドサーチ用のハイパーパラメータ
k = 5 #交差検証の分割数
kfold = KFold(n_splits=k, shuffle=False) #5分割交差検証(シャッフルなし)

#RMSEを基準としてグリッドサーチ
grid_search = GridSearchCV(pipe, param_grid, cv=kfold, scoring=make_scorer(rmse, greater_is_better=False))
grid_search.fit(X, y)
results = pd.DataFrame(grid_search.cv_results_)
print("Best parameters: {}".format(grid_search.best_params_)) #最も精度が高いパラメータセット表示

#svr_re = SVR(**grid_search.best_params_) #最も精度が高いパラメータセットにおけるモデル作成
splitter = kfold.split(X)
fig, axes = plt.subplots(2,3, figsize=(14, 8))
axes[1,2].axis('off')
MAE, RMSE = [], []

#結果の図示
for i, (ax, (train, test)) in enumerate(zip(axes.ravel(), splitter)):
    X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
    scaler = MinMaxScaler().fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    svr_re = SVR(C=1, epsilon=0.001, gamma='auto', kernel='rbf')
    svr_re.fit(X_train_scaled, y_train)
    X_test_scaled = scaler.transform(X_test)
    predict_svr = svr_re.predict(X_test_scaled)
    MAE.append(mean_absolute_error(y_test, predict_svr))
    RMSE.append(rmse(y_test, predict_svr))
    ax.set_title("Split {}".format(i))
    ax.plot(y_test, label="True")
    ax.plot(predict_svr, label="predicted")
    ax.set_xlabel("time[s]")
    ax.set_ylabel("SpO2[%]")
    ax.legend(loc='lower left')

fig.tight_layout()
plt.show()

# print("MAE : {}".format(sum(MAE)/len(MAE)))
print("RMSE : {}".format(sum(RMSE)/len(RMSE)))
