import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from sklearn.model_selection import train_test_split

from sample import make_forge
from sklearn.linear_model import LogisticRegression as LR
from sklearn.svm import SVC

X, y = make_forge()

fig, axes = plt.subplots(1, 2, figsize=(10, 3))

for model, ax in zip([SVC(), LR()], axes):
    clf = model.fit(X, y)
    mglearn.plots.plot_2d_separator(clf, X, fill=False, eps=0.5, ax=ax, alpha=.7)
    ax.scatter(X[:, 0][y==0], X[:, 1][y==0], marker='o', c='blue', label="0")
    ax.scatter(X[:, 0][y==1], X[:, 1][y==1], marker='^', c='red', label="1")
    ax.set_title("{}".format(clf.__class__.__name__))
    ax.set_xlabel("Feature 0")
    ax.set_ylabel("Feature 1")
plt.show()
