import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_score, cross_val_predict, GridSearchCV, train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import log_loss, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier as RFC

os.chdir(r"C:\Users\shira\Desktop\python\machine_learning")

df_ks = pd.read_csv("df_ks_int.csv", index_col="ID")

X = df_ks.iloc[:, 1:].values
y = df_ks["state"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
len(X_train)
len(y_train)

param_grid = {'max_depth': [2, 4, 8], 'n_estimators': [2, 4, 8]} #グリッドサーチ用のハイパーパラメータ

grid = GridSearchCV(RFC(), param_grid, cv=5)
grid.fit(X_train, y_train)
results = pd.DataFrame(grid.cv_results_)

print("\nBest cross-validation accuracy: {:.3f}".format(grid.best_score_))
print("Best parameters: {}".format(grid.best_params_))
