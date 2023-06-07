import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import os
import networkx as nx
from dateutil.relativedelta import relativedelta

#絶対パス指定
os.chdir(r"C:\Users\shira\Desktop\python\data_analysis\sample_100knocks\サンプルコード_20201021\6章")

factories = pd.read_csv("tbl_factory.csv", index_col=0)
factories
warehouses = pd.read_csv("tbl_warehouse.csv", index_col=0)
warehouses
cost = pd.read_csv("rel_cost.csv", index_col=0)
cost
trans = pd.read_csv("tbl_transaction.csv", index_col=0)
trans
join_data = pd.merge(trans, cost, left_on=["ToFC", "FromWH"], right_on=["FCID", "WHID"], how="left")
join_data
join_data = pd.merge(join_data, factories, on="FCID", how="left")
join_data = pd.merge(join_data, warehouses, on="WHID", how="left")
join_data = join_data[["TransactionDate", "Quantity", "Cost", "ToFC", "FCName", "FCDemand", "FromWH", "WHName", "WHSupply", "WHRegion"]]
join_data
kanto = join_data.loc[join_data["WHRegion"]=="関東"]
tohoku = join_data.loc[join_data["WHRegion"]=="東北"]

print("関東支社の総コスト: {} 万円 \n東北支社の総コスト: {} 万円 \n\n関東支社の総部品輸送個数: {} 個 \n東北支社の総部品輸送個数: {} 個" \
.format(kanto["Cost"].sum(), tohoku["Cost"].sum(), kanto["Quantity"].sum(), tohoku["Quantity"].sum()))
print("\n関東支社の部品1つ当たりの輸送コスト: {} 円 \n東北支社の部品1つ当たりの輸送コスト: {} 円" \
.format(int((kanto["Cost"].sum()*10000)/(kanto["Quantity"].sum())), int((tohoku["Cost"].sum()*10000)/(tohoku["Quantity"].sum()))))
cost_chk = pd.merge(cost, factories, on="FCID", how="left")
print("\n東京支社の平均輸送コスト: {} 万円 \n東北支社の平均輸送コスト: {} 万円" \
.format(cost_chk["Cost"].loc[cost_chk["FCRegion"]=="関東"].mean(), cost_chk["Cost"].loc[cost_chk["FCRegion"]=="東北"].mean()))

#ネットワークの可視化
G = nx.Graph() #グラフオブジェクトの作成
G.add_node("nodeA") #頂点
G.add_node("nodeB")
G.add_node("nodeC")
G.add_edge("nodeA", "nodeB") #辺
G.add_edge("nodeA", "nodeC")
G.add_edge("nodeB", "nodeC")
pos = {} #座標の設定
pos["nodeA"] = (0, 0)
pos["nodeB"] = (1, 1)
pos["nodeC"] = (0, 1)
nx.draw(G, pos)
plt.show()
