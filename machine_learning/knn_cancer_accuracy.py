import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
cancer_df = pd.DataFrame(cancer["data"], columns=cancer["feature_names"])
cancer_df["label"] = cancer["target"]

X = cancer_df.drop("label",axis=1).values
y = cancer_df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

training_accuracy = []
test_accuracy = []
neighbors = range(1, 11)

for n in neighbors:
    model = knn(n_neighbors=n)
    model.fit(X_train, y_train)
    training_accuracy.append(model.score(X_train, y_train))
    test_accuracy.append(model.score(X_test, y_test))

plt.plot(neighbors, training_accuracy, label="training accuracy")
plt.plot(neighbors, test_accuracy, label="test accuracy")
plt.xlabel("n_neighbors")
plt.ylabel("accuracy")
plt.legend()
plt.show()
