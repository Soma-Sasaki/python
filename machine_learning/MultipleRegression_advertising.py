import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
df = pd.read_csv('http://logopt.com/data/Advertising.csv', index_col =0)

X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)


#予測誤差プロット
from yellowbrick.regressor import PredictionError

visualizer = PredictionError(model)

#訓練データ
visualizer.fit(X_train, y_train)
visualizer.score(X_train, y_train)
visualizer.show();

# #テストデータ
# visualizer.fit(X_test, y_test)
# visualizer.score(X_test, y_test)
# visualizer.show();

#残差プロット
from yellowbrick.regressor import ResidualsPlot

visualizer = ResidualsPlot(model)

visualizer.fit(X_train, y_train)
visualizer.score(X_train, y_train)
visualizer.show();

# visualizer.fit(X_test, y_test)
# visualizer.score(X_test, y_test)
# visualizer.show();
