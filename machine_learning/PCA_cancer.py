import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from sklearn.model_selection import train_test_split

from sklearn.decomposition import PCA
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

cancer = load_breast_cancer()

cancer_df = pd.DataFrame(cancer["data"], columns = cancer["feature_names"])
cancer_df["label"] = cancer["target"]

X = cancer_df.iloc[:,:-1].values
y = cancer_df["label"]

scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)

pca = PCA(n_components=2)
pca.fit(X_scaled)
X_pca = pca.transform(X_scaled)

plt.figure(figsize=(8, 8))
mglearn.discrete_scatter(X_pca[:, 0], X_pca[:, 1], y)
plt.legend(cancer["target_names"], loc="best")
plt.xlabel("First principal component")
plt.ylabel("Second principal component")
plt.show()
