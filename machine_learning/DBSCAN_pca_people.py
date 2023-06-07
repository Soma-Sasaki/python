import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn

from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
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

# ノイズ画像の表示
# dbscan = DBSCAN(min_samples=3, eps=15)
# labels = dbscan.fit_predict(X_pca)
#
# noise = X_people[labels==-1]
# fig, axes = plt.subplots(3, 9, subplot_kw={'xticks': (), 'yticks': ()}, figsize=(12, 4))
# for image, ax in zip(noise, axes.ravel()):
#     ax.imshow(image.reshape(image_shape), vmin=0, vmax=1)
# plt.show()

for eps in [1, 3, 5, 7, 9, 11, 13]:
    print("\n eps={}".format(eps))
    dbscan = DBSCAN(eps=eps, min_samples=3)
    labels = dbscan.fit_predict(X_pca)
    print("Clusters present: {}".format(np.unique(labels)))
    print("Cluster sizes: {}".format(np.bincount(labels + 1)))

# #eps=7のときのクラスタリング結果の可視化
# dbscan = DBSCAN(min_samples=3, eps=7)
# labels = dbscan.fit_predict(X_pca)
# for cluster in range(max(labels) + 1):
#     mask = labels == cluster
#     n_images = np.sum(mask)
#     fig, axes = plt.subplots(1, n_images, figsize=(n_images * 1.5, 4), subplot_kw={'xticks': (), 'yticks': ()})
#     for image, label, ax in zip(X_people[mask], y_people[mask], axes.ravel()):
#         ax.imshow(image.reshape(image_shape), vmin=0, vmax=1)
#         ax.set_title(people.target_names[label].split()[-1])
# plt.show()
