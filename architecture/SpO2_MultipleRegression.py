import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import make_scorer
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

print("Multiple Regression")

#RMSEを求める関数定義
def rmse(y_true, y_pred):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    return rmse

os.chdir(r"C:\Users\shira\Desktop\python\architecture")
data = pd.read_csv('window10overlap9_R.csv')

X = data.iloc[:,0:-1].values #説明変数
y = data['SpO2'].values #目的変数

k = 5 #交差検証の分割数
kfold = KFold(n_splits=k, shuffle=False) #5分割交差検証(シャッフルなし)

#ノーマル重回帰
lr = LinearRegression() #モデル作成
splitter = kfold.split(X)
fig, axes = plt.subplots(2,3, figsize=(14, 8))
axes[1,2].axis('off')
MAE, RMSE = [], []
#結果の図示
for i, (ax, (train, test)) in enumerate(zip(axes.ravel(), splitter)):
    X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
    lr.fit(X_train, y_train)
    predict_lr = lr.predict(X_test)
    MAE.append(mean_absolute_error(y_test, predict_lr))
    RMSE.append(rmse(y_test, predict_lr))
    ax.set_title("Split {}".format(i))
    ax.plot(y_test, label="True")
    ax.plot(predict_lr, label="predicted")
    ax.set_xlabel("time[s]")
    ax.set_ylabel("SpO2[%]")
    ax.legend(loc='lower left')
fig.tight_layout()
plt.show()

# print("MAE : {}".format(sum(MAE)/len(MAE)))
print("RMSE : {}\n".format(sum(RMSE)/len(RMSE)))
