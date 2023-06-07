import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer

iris = load_iris()
breast_cancer = load_breast_cancer()
X_iris = pd.DataFrame(iris["data"], columns = iris["feature_names"]).values
y_iris = iris["target"]
X_cancer = pd.DataFrame(breast_cancer["data"], columns = breast_cancer["feature_names"]).values
y_cancer = breast_cancer["target"]
tmp_iris_train, tmp_iris_test, tmp_cancer_train, tmp_cancer_test = 0, 0, 0, 0

for j in range(100):
    X_iris_train, X_iris_test, y_iris_train, y_iris_test = \
    train_test_split(X_iris, y_iris, test_size = 0.3, random_state = j)
    X_cancer_train, X_cancer_test, y_cancer_train, y_cancer_test = \
    train_test_split(X_cancer, y_cancer, test_size = 0.3, random_state = j)
    iris_tree = RFC()
    iris_tree.fit(X_iris_train, y_iris_train)
    cancer_tree = RFC()
    cancer_tree.fit(X_cancer_train, y_cancer_train)
    tmp_iris_train += iris_tree.score(X_iris_train, y_iris_train)
    tmp_iris_test += iris_tree.score(X_iris_test, y_iris_test)
    tmp_cancer_train += cancer_tree.score(X_cancer_train, y_cancer_train)
    tmp_cancer_test += cancer_tree.score(X_cancer_test, y_cancer_test)


print("Random Forest \n")
print("iris training score is : {:.3f}".format(tmp_iris_train/100))
print("iris test score is : {:.3f} \n".format(tmp_iris_test/100))
print("cancer training score is : {:.3f}".format(tmp_cancer_train/100))
print("cancer test score is : {:.3f}".format(tmp_cancer_test/100))

# #分類精度を格納する配列
# iris_train_score, iris_test_score = [], []
# cancer_train_score, cancer_test_score = [], []
#
# x = np.arange(1, 10, 0.5) / 10
#
# #テストデータの割合を 0.1 から 0.9 まで 0.05 ずつ変化させる
# for i, test in enumerate(x):
#     X_iris_train, X_iris_test, y_iris_train, y_iris_test = \
#      train_test_split(X_iris, y_iris, test_size = test, random_state = 1)
#     X_cancer_train, X_cancer_test, y_cancer_train, y_cancer_test = \
#      train_test_split(X_cancer, y_cancer, test_size = test, random_state = 1)
#
#     iris_tree = RFC(max_depth=3, n_estimators=100, random_state=0)
#     iris_tree.fit(X_iris_train, y_iris_train)
#     cancer_tree = RFC(max_depth=3, n_estimators=100, random_state=0)
#     cancer_tree.fit(X_cancer_train, y_cancer_train)
#
#     iris_train_score.append(iris_tree.score(X_iris_train, y_iris_train))
#     iris_test_score.append(iris_tree.score(X_iris_test, y_iris_test))
#     cancer_train_score.append(cancer_tree.score(X_cancer_train, y_cancer_train))
#     cancer_test_score.append(cancer_tree.score(X_cancer_test, y_cancer_test))
#
# fig, ax = plt.subplots()
# ax.set_xlabel("test_size")
# ax.set_ylabel("Accuracy")
# ax.set_title("Random Forest")
# ax.set_xlim([0, 1])
# ax.plot(x, iris_train_score, color = "red", linestyle="dashed", label="iris training score")
# ax.plot(x, iris_test_score, color = "red", label="iris test score")
# ax.plot(x, cancer_train_score, color = "blue", linestyle="dashed", label="cancer training score")
# ax.plot(x, cancer_test_score, color = "blue", label="cancer test score")
# ax.legend()
# plt.show()

# #木の数を変えたとき
#
# #分類精度を格納する配列
# iris_train_score, iris_test_score = [], []
# cancer_train_score, cancer_test_score = [], []
#
# #訓練データとテストデータの割合を 7:3 に固定
# X_iris_train, X_iris_test, y_iris_train, y_iris_test = \
#  train_test_split(X_iris, y_iris, test_size = 0.3, random_state = 1)
# X_cancer_train, X_cancer_test, y_cancer_train, y_cancer_test = \
#  train_test_split(X_cancer, y_cancer, test_size = 0.3, random_state = 1)
#
# x = np.arange(2, 101, 1)
#
# #木の数を  から 100 まで 1 ずつ変化させる
#
# for i, test in enumerate(x):
#     iris_tree = RFC(max_depth=3, n_estimators=x[i], random_state=0)
#     iris_tree.fit(X_iris_train, y_iris_train)
#     cancer_tree = RFC(max_depth=3, n_estimators=x[i], random_state=0)
#     cancer_tree.fit(X_cancer_train, y_cancer_train)
#
#     iris_train_score.append(iris_tree.score(X_iris_train, y_iris_train))
#     iris_test_score.append(iris_tree.score(X_iris_test, y_iris_test))
#     cancer_train_score.append(cancer_tree.score(X_cancer_train, y_cancer_train))
#     cancer_test_score.append(cancer_tree.score(X_cancer_test, y_cancer_test))
#
# fig, ax = plt.subplots()
# ax.set_xlabel("n_estimators")
# ax.set_ylabel("Accuracy")
# ax.set_title("Random Forest")
# ax.set_ylim([0.9, 1])
# ax.plot(x, iris_train_score, color = "red", linestyle="dashed", label="iris training score")
# ax.plot(x, iris_test_score, color = "red", label="iris test score")
# ax.plot(x, cancer_train_score, color = "blue", linestyle="dashed", label="cancer training score")
# ax.plot(x, cancer_test_score, color = "blue", label="cancer test score")
# ax.legend()
# plt.show()

#
# #クラスの割合変えたとき
#
# iris_df = pd.DataFrame(iris["data"], columns = iris["feature_names"])
# iris_df["species"] = iris["target"]
#
# #分類精度を格納する配列
# iris_train_score, iris_test_score = [], []
#
# x = np.arange(45, 0, -5)
# iris_rate = [50/(150-z*2) for z in x] #setosaの割合を計算
#
# for i in x:
#     iris_df_ = iris_df.drop(range(50, 50+i))
#     iris_df_ = iris_df.drop(range(100, 100+i))
#     X_iris = iris_df_.drop("species",axis=1)
#     y_iris = iris_df_["species"]
#
#     X_iris_train, X_iris_test, y_iris_train, y_iris_test = \
#      train_test_split(X_iris, y_iris, test_size=0.3, random_state = 1)
#
#     iris_tree = RFC(max_depth=3, random_state=0)
#     iris_tree.fit(X_iris_train, y_iris_train)
#
#     iris_train_score.append(iris_tree.score(X_iris_train, y_iris_train))
#     iris_test_score.append(iris_tree.score(X_iris_test, y_iris_test))
#
# fig, ax = plt.subplots()
# ax.set_xlabel("setosa rate")
# ax.set_ylabel("Accuracy")
# ax.set_title("Random Forest")
# ax.plot(iris_rate, iris_train_score, color = "red", linestyle="dashed", label="iris training score")
# ax.plot(iris_rate, iris_test_score, color = "red", label="iris test score")
# ax.legend()
# plt.show()
