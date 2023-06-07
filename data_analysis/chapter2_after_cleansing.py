import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir(r"C:\Users\shira\Desktop\python\data_analysis\sample_100knocks\サンプルコード_20201021\2章")

import_data = pd.read_csv('chapter2_dump_data.csv')
byItem = import_data.pivot_table(index='purchase_month', columns='item_name', aggfunc='size', fill_value=0)
byItem
byPrice = import_data.pivot_table(index='purchase_month', columns='item_name', values='item_price', aggfunc='sum', fill_value=0)
byPrice
byCustomer = import_data.pivot_table(index='purchase_month', columns='顧客名', aggfunc='size', fill_value=0)
byCustomer
byRegion = import_data.pivot_table(index='purchase_month', columns='地域', aggfunc='size', fill_value=0)
byRegion
