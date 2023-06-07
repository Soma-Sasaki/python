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

bins = np.linspace(-3, 3, 11)
which_bin = np.digitize(X, bins=bins)
encoder = OneHotEncoder(sparse=False)
encoder.fit(which_bin)
X_binned = encoder.transform(which_bin)
line_binned = encoder.transform(np.digitize(line, bins=bins))

# #もとの特徴量を加え直す(11次元にする)
# X_combined = np.hstack([X, X_binned])
# line_combined = np.hstack([line, line_binned])
# lr = LR().fit(X_combined, y)
# plt.plot(line, lr.predict(line_combined), label="linear regression combined")
#
# for bin in bins:
#     plt.plot([bin, bin], [-3, 3], ':', c='k')
#
# plt.plot(X[:, 0], y, 'o', c='k')
# plt.ylabel("Regression output")
# plt.xlabel("Input feature")
# plt.legend(loc='best')
# plt.show()

#ビンの指示子ともとの特徴量の積を加える(20次元にする)
X_product = np.hstack([X_binned, X * X_binned])
line_product = np.hstack([line_binned, line * line_binned])
lr = LR().fit(X_product, y)
plt.plot(line, lr.predict(line_product), label="linear regression product")

for bin in bins:
    plt.plot([bin, bin], [-3, 3], ':', c='k')

plt.plot(X[:, 0], y, 'o', c='k')
plt.ylabel("Regression output")
plt.xlabel("Input feature")
plt.legend(loc='best')
plt.show()
