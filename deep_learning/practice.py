import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def svd(A):
    B = np.dot(A.T, A)
    eigen_values, eigen_vectors = np.linalg.eig(B)

    singular_values = np.sqrt(eigen_values)
    singular_index = np.argsort(singular_values)[::-1]

    S = np.diagflat(singular_values[singular_index])

    V = eigen_vectors[:, singular_index]

    dig = S.diagonal()
    U = [np.dot(A, V[:, i]) / dig[i] for i in range(len(dig))]
    U = np.array(U).T
    return U, S, V

def pca(X, n_components):
    X = X - X.mean(axis=0)
    U, S, V = svd(X)
    n = n_components

    X_new = np.dot(U[:, :n], S[:n, :n].T)

    return X_new


math = np.array([41, 37, 40, 30, 40, 60, 46, 61, 67, 68, 55, 61, 59, 66, 69])
physics = np.array([26, 32, 31, 24, 60, 40, 26, 27, 33, 25, 26, 30, 29, 37, 41])
X = np.vstack((math, physics)).T
X_new = pca(X, n_components=1)
print(X_new.shape)
print(X_new)

df_test = pd.DataFrame({"math": math, "physics": physics})
mean = df_test[["math", "physics"]].mean(axis=0)
U, S, V = svd(X)

fig = plt.figure()
ax = fig.add_subplot(111, aspect="equal")
ax.scatter(X[:, 0], X[:, 1])
ax.set_xlim([0, 100])
ax.set_ylim([0, 100])
ax.quiver(mean[0], mean[1], V[0,0], V[1,0], color="b", width=0.01, scale=3)
ax.quiver(mean[0], mean[1], V[0,1], V[1,1], color="r", width=0.01, scale=3)
plt.show()
