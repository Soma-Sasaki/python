import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as LR

adult_path = os.path.join(mglearn.datasets.DATA_PATH, "adult.data")
data = pd.read_csv(adult_path, header=None, index_col=False, names=["age", "workclass", "fnlwgt", "education", "education-num", \
"marital-status", "occupation", "relationship", "race", "gender", "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"])
data = data[["age", "workclass","education", "gender", "hours-per-week", "occupation", "income"]]

data_dummies = pd.get_dummies(data)

X = data_dummies.iloc[:,:-2].values
y = data_dummies['income_ >50K'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
lr = LR()
lr.fit(X_train, y_train)

print("training score is : {:.3f}".format(lr.score(X_train, y_train)))
print("test score is : {:.3f} \n".format(lr.score(X_test, y_test)))
