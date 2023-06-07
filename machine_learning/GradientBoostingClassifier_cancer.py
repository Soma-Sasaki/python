import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import GradientBoostingClassifier as GBC

breast_cancer = load_breast_cancer()

breast_cancer_df = pd.DataFrame(breast_cancer["data"], columns = breast_cancer["feature_names"])
breast_cancer_df["label"] = breast_cancer["target"]

X = breast_cancer_df.iloc[:,:-1]
y = breast_cancer_df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

forest = GBC(max_depth=1, learning_rate=0.1, random_state=0)
forest.fit(X, y)

print("training score is : {:.3f}".format(forest.score(X_train, y_train)))
print("test score is : {:.3f}".format(forest.score(X_test, y_test)))

#特徴量重要度
fig, ax = plt.subplots()
fig.subplots_adjust(left=0.3)
ax.barh(breast_cancer.feature_names, forest.feature_importances_)
plt.show()
