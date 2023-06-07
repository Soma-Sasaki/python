import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.datasets import load_iris

iris = load_iris()
X = pd.DataFrame(iris["data"], columns = iris["feature_names"]).values #説明変数
y = iris["target"] #目的変数

#訓練データとテストデータを 7:3 の割合で分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)


tree = DTC(max_depth=2, random_state=0)
tree.fit(X, y)

print("DTC training score is : {:.3f}".format(tree.score(X_train, y_train)))
print("DTC test score is : {:.3f}".format(tree.score(X_test, y_test)))


forest = RFC(max_depth=2, n_estimators=100, random_state=0)
forest.fit(X, y)

print("RFC training score is : {:.3f}".format(forest.score(X_train, y_train)))
print("RFC test score is : {:.3f}".format(forest.score(X_test, y_test)))
