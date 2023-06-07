import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as LR
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()

iris_df = pd.DataFrame(iris["data"], columns=iris["feature_names"])
iris_df['species'] = iris["target"]

X = iris_df.drop("species", axis=1).values
y = iris_df["species"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = LR()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print('score is', score)


# #特徴に関する可視化
#
# #どの特徴が重要か
# from yellowbrick.features import RadViz
#
# visualizer = RadViz(classes=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],size=(600,400))
#
# visualizer.fit(X, y)
# visualizer.transform(X)
# visualizer.show();
#

# #分類に対する可視化
#
# #混合行列
# from yellowbrick.classifier import ConfusionMatrix
#
# cm = ConfusionMatrix(model, classes=["not spam", "is spam"])
#
# cm.fit(X_train, y_train)
# cm.score(X_train, y_train)
# cm.show();
#
# #分類レポート
# TP, FN, FP, TN = 1848, 118, 148, 1106
# precision =  TP/(TP+FP) #適合率(真陽性率)
# recall = TP/(FN+TP) #再現率(回収率？)
# print( "precision=", precision)
# print( "recall=", recall  )
# print( "F1 score=", 2*(precision*recall)/(precision+recall) ) #適合率と再現率の調和平均
# from yellowbrick.classifier import ClassificationReport
#
# visualizer = ClassificationReport(model,classes=["not spam","is spam"])
#
# visualizer.fit(X_train, y_train)
# visualizer.score(X_train, y_train)
# visualizer.show();
#
# #閾値変えてみる
# from yellowbrick.classifier import DiscriminationThreshold
#
# visualizer = DiscriminationThreshold(model)
#
# visualizer.fit(X_train, y_train)
# visualizer.score(X_train,y_train)
# visualizer.show();
#
# #ROC曲線
# from yellowbrick.classifier import ROCAUC
#
# visualizer = ROCAUC(model, size=(600,400))
#
# visualizer.fit(X_train, y_train)
# visualizer.score(X_train, y_train)
# visualizer.show();
