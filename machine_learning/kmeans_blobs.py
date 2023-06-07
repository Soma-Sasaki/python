import numpy as np
import matplotlib.pyplot as plt
import mglearn

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X, y = make_blobs(random_state=1)
fig, axes = plt.subplots(1, 3, figsize=(10,3))

for i, ax in zip(range(2,5,1), axes.ravel()):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(X)
    mglearn.discrete_scatter(X[:, 0], X[:, 1], kmeans.labels_, ax=axes[i-2])
    ax.set_title("k = {}".format(i))
    ax.legend(loc='best')

plt.show()
