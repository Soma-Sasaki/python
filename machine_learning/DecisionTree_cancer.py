import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier as DTC, export_graphviz
import graphviz
import pydotplus
from IPython.display import Image
from six import StringIO

breast_cancer = load_breast_cancer()

breast_cancer_df = pd.DataFrame(breast_cancer["data"], columns = breast_cancer["feature_names"])
breast_cancer_df["label"] = breast_cancer["target"]

X = breast_cancer_df.iloc[:,:-1].values
y = breast_cancer_df["label"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

tree = DTC(max_depth=2)
tree.fit(X, y)

print("training score is : {:.3f}".format(tree.score(X_train, y_train)))
print("test score is : {:.3f}".format(tree.score(X_test, y_test)))

#決定木の可視化
dot_data = StringIO() #dotファイル情報の格納先
export_graphviz(tree, out_file=dot_data,
                      feature_names=breast_cancer.feature_names, #編集するのはここ
                      class_names=["malignant","benign"],#編集するのはここ
                      filled=True, rounded=True,
                      special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("graph_2depth.pdf") #pdf出力

# #特徴量の重要度
# def plot_feature_importances_cancer(model):
#     n_features = breast_cancer["data"].shape[1]
#     plt.barh(range(n_features), model.feature_importances_, align='center')
#     plt.yticks(np.arange(n_features), breast_cancer["feature_names"])
#     plt.xlabel("Feature importance")
#     plt.ylabel("Feature")
#     plt.show()
#
# plot_feature_importances_cancer(tree)
