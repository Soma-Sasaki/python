import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC, export_graphviz
import graphviz
import pydotplus
from IPython.display import Image
from six import StringIO

a_df = pd.DataFrame({
    "high":[4, 5, 3, 1, 6, 3, 4, 1, 2, 1, 1, 1, 3],
    "size":[30, 45, 32, 20, 35, 40, 38, 20, 18, 20, 22, 24, 25],
    "autolock":[1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
    "buy":[True,True,True,True,True,True,True,False,False,False,False,False,False]
    })

X = a_df[['high','size','autolock']].values
y = a_df['buy'].values

print(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

model = DTC()
model.fit(X, y)

score = model.score(X, y)

print('score is', score)

#決定木の可視化
# dot_data = StringIO() #dotファイル情報の格納先
# export_graphviz(model, out_file=dot_data,
#                      feature_names=["high", "size","autolock"],#編集するのはここ
#                      class_names=["False","True"],#編集するのはここ（なぜFase,Trueの順番なのかは後程触れます）
#                      filled=True, rounded=True,
#                      special_characters=True)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# graph.write_pdf("graph.pdf") #pdf出力
