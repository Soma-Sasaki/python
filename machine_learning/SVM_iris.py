import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_iris
from sklearn.svm import SVC
from mlxtend.plotting import plot_decision_regions

iris = load_iris()

iris_df = pd.DataFrame(iris['data'], columns = iris['feature_names'])
iris_df['species'] = iris['target']

X = iris_df[['sepal length (cm)','sepal width (cm)']].values
y = iris_df['species'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

model = SVC(gamma='scale')
model.fit(X_train, y_train)

print("training score is : {:.2f}".format(model.score(X_train, y_train)))
print("test score is : {:.2f}".format(model.score(X_test, y_test)))

#以下グラフ描画
plt.style.use('ggplot')

#訓練データとテストデータの結合
X_combined = np.vstack((X_train, X_test))
y_combined = np.hstack((y_train, y_test))

plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')

fig = plt.figure(figsize=(13,8))
plot_decision_regions(X_combined, y_combined, clf=model,  res=0.02)
plt.show()
