import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from sklearn.neighbors import KNeighborsClassifier as knn

X, y = mglearn.datasets.make_forge()

fig, axes = plt.subplots(1, 3, figsize=(10, 3))

for n, ax in zip([1, 3, 9], axes):
    model = knn(n_neighbors=n).fit(X, y)
    mglearn.plots.plot_2d_separator(model, X, fill=True, eps=0.5, ax=ax, alpha=.4)
    ax.scatter(X[:, 0][y==0], X[:, 1][y==0], marker='o', c='blue', label="0")
    ax.scatter(X[:, 0][y==1], X[:, 1][y==1], marker='^', c='red', label="1")
    ax.set_title("{} neighbor(s)".format(n))
    ax.set_xlabel("feature0")
    ax.set_ylabel("feature1")
plt.show()
