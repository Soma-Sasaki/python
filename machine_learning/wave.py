import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sample import make_wave

X, y = make_wave()

plt.plot(X, y, 'o')
plt.legend(loc=4)
plt.xlabel('Feature')
plt.ylabel('Target')
plt.show()
