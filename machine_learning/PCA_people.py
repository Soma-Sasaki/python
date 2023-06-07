import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from sklearn.model_selection import train_test_split

from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier as knn
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

X_train, X_test, y_train, y_test = train_test_split(X_people, y_people, stratify=y_people, random_state=0)

#PCA処理前
# knn = knn(n_neighbors=1).fit(X_train, y_train)
# print("training score is : {:.3f}".format(knn.score(X_train, y_train)))
# print("test score is : {:.3f}".format(knn.score(X_test, y_test)))

pca = PCA(n_components=100, whiten=True, random_state=0).fit(X_train)
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

#PCA処理後
knn = knn(n_neighbors=1).fit(X_train_pca, y_train)
print("training score is : {:.3f}".format(knn.score(X_train_pca, y_train)))
print("test score is : {:.3f}".format(knn.score(X_test_pca, y_test)))

fix, axes = plt.subplots(3, 5, figsize=(15, 12), subplot_kw ={'xticks' : (), 'yticks' : ()})
for i, (component, ax) in enumerate(zip(pca.components_, axes.ravel())):
    ax.imshow(component.reshape(image_shape), cmap='viridis')
    ax.set_title("{}. component".format((i+1)))
plt.show()

mglearn.plots.plot_pca_faces(X_train, X_test, image_shape)
plt.show()

mglearn.discrete_scatter(X_train_pca[:, 0], X_train_pca[:, 1], y_train)
plt.xlabel("First principal component")
plt.ylabel("Second principal component")
plt.show()
