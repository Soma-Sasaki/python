import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re
import os

#絶対パス指定
os.chdir(r"C:\Users\shira\Desktop\就活\スキルアップAI\Day7_vr1_7_0")

train = pd.read_csv("titanic/train.csv")
test = pd.read_csv("titanic/test.csv")


fizz_buzz = ["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 51)]
fizz_buzz
