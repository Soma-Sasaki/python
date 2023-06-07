import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from sklearn.datasets import load_iris
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import GroupKFold

iris = load_iris()
logreg = LogisticRegression()

#3分割すると、個々の分割が個々のクラスに対応しているので、結果がひどいことになる例
kfold = KFold(n_splits=3, shuffle=False)
len(iris.data)
splitter = kfold.split(iris.data, iris.target)
for a, b in splitter:
    print(a)
    print(b)
scores = cross_val_score(logreg, iris.data, iris.target, cv=kfold)
print("Cross-validation scores: {}".format(scores))
print("Average cross-validation score: {:.2f}".format(scores.mean()))

#3分割シャッフル
kfold = KFold(n_splits=3, shuffle=True, random_state=0)
scores = cross_val_score(logreg, iris.data, iris.target, cv=kfold)
print("Cross-validation scores: {}".format(scores))
print("Average cross-validation score: {:.2f}".format(scores.mean()))

#1つ抜き交差検証
loo = LeaveOneOut()
scores = cross_val_score(logreg, iris.data, iris.target, cv=loo)
print("Number of cv iterations: {}".format(len(scores)))
print("Average cross-validation score: {:.2f}".format(scores.mean()))

#シャッフル分割交差検証
shufful_split = ShuffleSplit(test_size=.5, train_size=.5, n_splits=10)
scores = cross_val_score(logreg, iris.data, iris.target, cv=shufful_split)
print("Cross-validation score:\n{}".format(scores))

#グループ付き交差検証
X, y = make_blobs(n_samples=12, random_state=0)
groups = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3]
scores = cross_val_score(logreg, X, y, groups, cv=GroupKFold(n_splits=3))
print("Cross-validation score:\n{}".format(scores))
