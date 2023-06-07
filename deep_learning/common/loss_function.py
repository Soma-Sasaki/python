import numpy as np

def sum_squared_error(y, t):
    return 0.5* np.sum((y-t)**2)

def cross_entropy_error(y, t):
    delta = 1e-7 #log(0)になることを防ぐための微小な値
    return -np.sum(t * np.log(y + delta))

#バッチ対応版
def cross_entropy_error_onehot(y, t): #教師データが one-hot表現のとき
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7)) / batch_size

def cross_entropy_error_label(y, t): #教師データがラベルのとき
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
