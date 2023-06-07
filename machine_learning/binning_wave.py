import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as LR
from sklearn.tree import DecisionTreeRegressor as DTR
from sklearn.preprocessing import OneHotEncoder

X, y = mglearn.datasets.make_wave(n_samples=100)
line = np.linspace(-3, 3, 1000, endpoint=False).reshape(-1, 1)

# dtr = DTR(min_samples_split=3).fit(X, y)
# plt.plot(line, dtr.predict(line), label="decision tree")
#
# lr = LR().fit(X, y)
# plt.plot(line, lr.predict(line), label="linear regression")
#
# plt.plot(X[:, 0], y, 'o', c='k')
# plt.ylabel("Regression output")
# plt.xlabel("Input feature")
# plt.legend(loc='best')
# plt.show()

#ビニング
bins = np.linspace(-3, 3, 11)
which_bin = np.digitize(X, bins=bins)
encoder = OneHotEncoder(sparse=False)
encoder.fit(which_bin)
X_binned = encoder.transform(which_bin)
line_binned = encoder.transform(np.digitize(line, bins=bins))

dtr = DTR(min_samples_split=3).fit(X_binned, y)
plt.plot(line, dtr.predict(line_binned), label="decision tree binned")

lr = LR().fit(X_binned, y)
plt.plot(line, lr.predict(line_binned), label="linear regression binned")

plt.plot(X[:, 0], y, 'o', c='k')
plt.ylabel("Regression output")
plt.xlabel("Input feature")
plt.legend(loc='best')
plt.show()
