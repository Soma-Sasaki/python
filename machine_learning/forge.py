import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sample import make_forge


X, y = make_forge()

fig, ax = plt.subplots()

ax.scatter(X[:, 0][y==0], X[:, 1][y==0], marker='o', c='blue', label="class-0")
ax.scatter(X[:, 0][y==1], X[:, 1][y==1], marker='^', c='red', label="class-1")

plt.legend(loc=4)
plt.xlabel('First feature')
plt.ylabel('Second feature')
plt.show()
