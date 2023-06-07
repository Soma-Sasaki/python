import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.ensemble import RandomForestClassifier as RFC
import os

#絶対パス指定
os.chdir(r"C:\Users\shira\デスクトップ\E資格\スキルアップAI\Day8_vr1_4_0")

train = pd.read_pickle("titanic/titanic_train.pkl")
test = pd.read_pickle("titanic/titanic_test.pkl")
data = [train, test]

tr_train, tr_test = train_test_split(train, test_size=0.3, random_state=1234)

tr_train_X = tr_train[train.columns[1:]]
tr_train_Y = tr_train[train.columns[0]]
tr_test_X = tr_test[train.columns[1:]]
tr_test_Y = tr_test[train.columns[0]]


model_dtc = DTC()
model_dtc.fit(tr_train_X, tr_train_Y)
score = model_dtc.score(tr_test_X, tr_test_Y)
score

model_rfc = RFC(n_estimators=100)
model_rfc.fit(tr_train_X, tr_train_Y)
score = model_rfc.score(tr_test_X, tr_test_Y)
score

#グリッドサーチ交差検証とか追加

k = 5
kfold = KFold(n_splits=k, shuffle=False)
param = {"n_estimators": range(100, 1000, 100)}
GS_rf = GridSearchCV(RFC(random_state=0), param_grid=param, cv=kfold)
GS_rf.fit(tr_train_X, tr_train_Y)
results = pd.DataFrame(GS_rf.cv_results_)
print("Best parameters: {}".format(GS_rf.best_params_))
GS_rf.score(tr_test_X, tr_test_Y)
GS_rf_re = RFC(**GS_rf.best_params_)
GS_rf_re.fit(tr_train_X, tr_train_Y)
feature_importances = pd.DataFrame({"feature_importances": GS_rf_re.feature_importances_})
sns.barplot(tr_train_X.columns, feature_importances["feature_importances"])
