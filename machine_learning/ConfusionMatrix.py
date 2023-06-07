import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_digits
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.linear_model import LogisticRegression as LogReg
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score

digits = load_digits()
y = digits.target == 9

X_train, X_test, y_train, y_test = train_test_split(digits.data, y, random_state=0)


#ランダムにクラスを返すだけのクラス分類器
dummy = DummyClassifier(strategy='stratified').fit(X_train, y_train)
print("Dummy: {:.3f}".format(dummy.score(X_test, y_test)))
pred_dummy = dummy.predict(X_test)
print(confusion_matrix(y_test, pred_dummy))
print("f1 score : {:.3f}".format(f1_score(y_test, pred_dummy)))

#頻度の高いものだけを返すクラス分類器
dummy_majority = DummyClassifier().fit(X_train, y_train)
print("\nmost frequent: {:.3f}\n".format(dummy_majority.score(X_test, y_test)))
pred_most_frequent = dummy_majority.predict(X_test)
print(confusion_matrix(y_test, pred_most_frequent))
print("f1 score : {:.3f}".format(f1_score(y_test, pred_most_frequent)))

#決定木クラス分類器
tree = DTC(max_depth=2).fit(X_train, y_train)
print("\nDecision Tree: {:.3f}".format(tree.score(X_test, y_test)))
pred_tree = tree.predict(X_test)
print(confusion_matrix(y_test, pred_tree))
print("f1 score : {:.3f}".format(f1_score(y_test, pred_tree)))

#ロジスティック回帰
logreg = LogReg(C=0.1, max_iter=1000).fit(X_train, y_train)
print("\nLogistic Regression: {:.3f}".format(logreg.score(X_test, y_test)))
pred_logreg = logreg.predict(X_test)
print(confusion_matrix(y_test, pred_logreg))
print("f1 score : {:.3f}".format(f1_score(y_test, pred_logreg)))
