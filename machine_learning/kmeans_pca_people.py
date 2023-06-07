import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.datasets import fetch_lfw_people

people = fetch_lfw_people(min_faces_per_person=20, resize=0.7)
image_shape = people.images[0].shape
people_df = pd.DataFrame(people["data"])
people_df["label"] = people["target"]

#各人の画像を50に制限
mask = np.zeros(people_df["label"].shape, dtype=np.bool)
for target in np.unique(people_df["label"]):
    mask[np.where(people_df["label"] == target)[0][:50]] = 1

X_people = people.data[mask]
y_people = people.target[mask]
X_people = X_people / 255

pca = PCA(n_components=100, whiten=True, random_state=0)
X_pca = pca.fit_transform(X_people)

km = KMeans(n_clusters=10, random_state=0)
labels_km = km.fit_predict(X_pca)
print("Cluster sizes k-means: {}".format(np.bincount(labels_km)))

fig, axes = plt.subplots(2, 5, subplot_kw={'xticks': (), 'yticks': ()}, figsize=(12, 4))
for center, ax in zip(km.cluster_centers_, axes.ravel()):
    ax.imshow(pca.inverse_transform(center).reshape(image_shape), vmin=0, vmax=1)
plt.show()

#各クラスセンタに対して典型的な5画像と典型的でない5画像表示
mglearn.plots.plot_kmeans_faces(km, pca, X_pca, X_people, y_people, people.target_names)
plt.show()
