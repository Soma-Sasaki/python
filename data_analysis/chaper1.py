import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

#絶対パス指定
os.chdir(r"C:\Users\shira\Desktop\python\data_analysis\sample_100knocks\サンプルコード_20201021\1章")

#相対パス指定
#os.chdir(r".\sample_100knocks\サンプルコード_20201021\1章")

customer_master = pd.read_csv('customer_master.csv')
item_master = pd.read_csv('item_master.csv')
transaction_1 = pd.read_csv('transaction_1.csv')
transaction_2 = pd.read_csv('transaction_2.csv')
transaction = pd.concat([transaction_1, transaction_2], ignore_index=True)
transaction_detail_1 = pd.read_csv('transaction_detail_1.csv')
transaction_detail_2 = pd.read_csv('transaction_detail_2.csv')
transaction_detail = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)

join_data = pd.merge(transaction_detail, transaction[['transaction_id', 'payment_date', 'customer_id']], on='transaction_id', how='left')
join_data = pd.merge(join_data, customer_master, on='customer_id', how='left')
join_data = pd.merge(join_data, item_master, on='item_id', how='left')
join_data['price'] = join_data['quantity'] * join_data['item_price']

#欠損値チェック
join_data.isnull().sum()
#全体の数字感チェック
join_data.describe()
#月別, 商品別でのデータ集計
join_data['payment_date'] = pd.to_datetime(join_data['payment_date'])
join_data["payment_month"] = join_data['payment_date'].dt.strftime("%Y%m")
join_data.groupby(['payment_month', 'item_name']).sum()[['price', 'quantity']]
pd.pivot_table(join_data, index='item_name', columns='payment_month', values=['price', 'quantity'], aggfunc='sum')

#データの可視化
graph_data = pd.pivot_table(join_data, index='item_name', columns='payment_month', values='price', aggfunc='sum')
graph_data
list(graph_data.columns)
list(graph_data.iloc[0,:])
for i, item in enumerate(["PC-A", "PC-B", "PC-C", "PC-D", "PC-E"]):
    plt.plot(list(graph_data.columns), list(graph_data.iloc[i,:]), label=item)
plt.legend()
plt.show()
