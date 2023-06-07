import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC

from sklearn.preprocessing import MinMaxScaler

cancer = load_breast_cancer()

cancer_df = pd.DataFrame(cancer["data"], columns = cancer["feature_names"])
cancer_df["label"] = cancer["target"]
cancer_df
cancer_df.dtypes

X = cancer_df.iloc[:,:-1].values
y = cancer_df["label"].values

len(X)
print(y)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

svc = SVC(C=10, gamma=0.1).fit(X_train, y_train)

print("training score is : {:.3f}".format(svc.score(X_train, y_train)))
print("test score is : {:.3f}".format(svc.score(X_test, y_test)))

#下処理(関数使わない)
# min = X_train.min(axis=0)
# max = X_train.max(axis=0)
# range = max - min
# X_train_scaled = (X_train - min)/range
# X_test_scaled = (X_test - min)/range
#
# svc_re = SVC(C=10, gamma=0.1).fit(X_train_scaled, y_train)

scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

svc_re = SVC(C=10, gamma=0.1).fit(X_train_scaled, y_train)

print("scaled training score is : {:.3f}".format(svc_re.score(X_train_scaled, y_train)))
print("scaled test score is : {:.3f}".format(svc_re.score(X_test_scaled, y_test)))
