import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
from sklearn.svm import SVC

iris = load_iris()

#訓練セット+テストセット

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)
print("size of training set: {}  size of test set: {}".format(X_train.shape[0], X_test.shape[0]))

best_score = 0

for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
    for C in [0.001, 0.01, 0.1, 1, 10, 100]:
        svm = SVC(gamma=gamma, C=C)
        svm.fit(X_train, y_train)
        score = svm.score(X_test, y_test)
        if score > best_score:
            best_score = score
            best_parameters = {'C': C, 'gamma': gamma}

print("Best score: {:.2f}".format(best_score))
print("Best parameters: {}\n".format(best_parameters))

#訓練セット+検証セット+テストセット

X_trainval, X_test, y_trainval, y_test = train_test_split(iris.data, iris.target, random_state=0)
X_train, X_valid, y_train, y_valid = train_test_split(X_trainval, y_trainval, random_state=1)
print("size of training set: {}  size of validation set: {}  size of test set: {}".format(X_train.shape[0], X_valid.shape[0], X_test.shape[0]))

best_score = 0

for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
    for C in [0.001, 0.01, 0.1, 1, 10, 100]:
        svm = SVC(gamma=gamma, C=C)
        svm.fit(X_train, y_train)
        score = svm.score(X_valid, y_valid)
        if score > best_score:
            best_score = score
            best_parameters = {'C': C, 'gamma': gamma}

svm = SVC(**best_parameters)
svm.fit(X_trainval, y_trainval)
test_score = svm.score(X_test, y_test)
print("Best score on validation set: {:.3f}".format(best_score))
print("Best parameters: {}".format(best_parameters))
print("Test score with best parameters: {:.3f}\n".format(test_score))

#交差検証を用いたグリッドサーチ
best_score = 0

for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
    for C in [0.001, 0.01, 0.1, 1, 10, 100]:
        svm = SVC(gamma=gamma, C=C)
        svm.fit(X_train, y_train)
        scores = cross_val_score(svm, X_trainval, y_trainval, cv=5)
        score = np.mean(scores)
        score
        if score > best_score:
            best_score = score
            best_parameters = {'C': C, 'gamma': gamma}

svm = SVC(**best_parameters)
svm.fit(X_trainval, y_trainval)
test_score = svm.score(X_test, y_test)
print("Best score on validation set: {:.3f}".format(best_score))
print("Best parameters: {}".format(best_parameters))
print("Test score with best parameters: {:.3f}\n".format(test_score))

#GridSearchCV使用(前の方法の簡略化)
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'gamma': [0.001, 0.01, 0.1, 1, 10, 100]}

grid_search = GridSearchCV(SVC(), param_grid, cv=5)
grid_search.fit(X_trainval, y_trainval)
print("Best score on validation set: {:.3f}".format(grid_search.best_score_))
print("Best parameters: {}".format(grid_search.best_params_))
print("Test set score: {:.3f}\n".format(grid_search.score(X_test, y_test)))
print("Best estimator:\n{}".format(grid_search.best_estimator_))

results = pd.DataFrame(grid_search.cv_results_)
scores = np.array(results.mean_test_score).reshape(-6, 6)
mglearn.tools.heatmap(scores, xlabel="gamma", xticklabels=param_grid['gamma'], ylabel="C", yticklabels=param_grid['C'], cmap='viridis')
plt.show()

#グリッドでないサーチ区間
param_grid = [{'kernel': ['rbf'], 'C': [0.001, 0.01, 0.1, 1, 10, 100], 'gamma': [0.001, 0.01, 0.1, 1, 10, 100]}, {'kernel': ['linear'], 'C': [0.001, 0.01, 0.1, 1, 10, 100]}]

grid_search = GridSearchCV(SVC(), param_grid, cv=5)
grid_search.fit(X_trainval, y_trainval)
print("Best score on validation set: {:.3f}".format(grid_search.best_score_))
print("Best parameters: {}".format(grid_search.best_params_))
print("Test set score: {:.3f}\n".format(grid_search.score(X_test, y_test)))
print("Best estimator:\n{}".format(grid_search.best_estimator_))
