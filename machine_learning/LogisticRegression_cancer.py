import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression as LR

cancer = load_breast_cancer()

cancer_df = pd.DataFrame(cancer["data"], columns = cancer["feature_names"])
cancer_df["label"] = cancer["target"]

X = cancer_df.drop("label", axis=1).values
y = cancer_df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = LR(C=100)
model.fit(X_train, y_train)

print("training score is : {:.2f}".format(model.score(X_train, y_train)))
print("test score is : {:.2f}".format(model.score(X_test, y_test)))
