import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)

# #愚直な方法
# scaler = MinMaxScaler().fit(X_train)
# X_train_scaled = scaler.transform(X_train)
# svm = SVC()
# svm.fit(X_train_scaled, y_train)
# X_test_scaled = scaler.transform(X_test)
# print("Test score: {:.3f}".format(svm.score(X_test_scaled, y_test)))

#スケール変換→SVM訓練のパイプライン構築(上の結果と一致)
pipe = Pipeline([("scaler", MinMaxScaler()), ("svm", SVC())])
pipe.fit(X_train, y_train)
print("Default test score: {:.3f}".format(pipe.score(X_test, y_test)))

#パイプラインを用いたグリッドサーチ
param_grid = {'svm__C': [0.001, 0.01, 0.1, 1, 10, 100], 'svm__gamma': [0.001, 0.01, 0.1, 1, 10, 100]}
grid = GridSearchCV(pipe, param_grid=param_grid, cv=5)
grid.fit(X_train, y_train)
print("\nBest cross-validation accuracy: {:.3f}".format(grid.best_score_))
print("Grid test score: {:.3f}".format(grid.score(X_test, y_test)))
print("Best parameters: {}".format(grid.best_params_))
