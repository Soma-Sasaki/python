import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from dateutil.relativedelta import relativedelta
from sklearn import linear_model
from sklearn.model_selection import train_test_split

#絶対パス指定
os.chdir(r"C:\Users\shira\Desktop\python\data_analysis\sample_100knocks\サンプルコード_20201021\3章")

uselog = pd.read_csv('use_log.csv')
uselog
customer = pd.read_csv('customer_join.csv')
customer

#クラスタリング
customer_clustering = customer[['mean', 'median', 'max', 'min', 'membership_period']]
customer_clustering

sc = StandardScaler()
customer_clustering_sc = sc.fit_transform(customer_clustering)
kmeans = KMeans(n_clusters=4, random_state=0)
clusters = kmeans.fit(customer_clustering_sc)
customer_clustering['cluster'] = clusters.labels_
customer_clustering
customer_clustering.columns = ["月内平均値", "月内中央値", "月内最大値", "月内最小値", "会員期間", "cluster"]
customer_clustering.groupby("cluster").mean()
pca = PCA(n_components=2)
pca_df = pd.DataFrame(pca.fit_transform(customer_clustering_sc))
pca_df['cluster'] = customer_clustering['cluster']
pca_df
for i in customer_clustering['cluster'].unique():
    tmp = pca_df.loc[pca_df['cluster']==i]
    plt.scatter(tmp[0], tmp[1])

#クラスタリング結果を基に退会顧客の傾向把握
customer_clustering['is_deleted'] = customer['is_deleted']
customer_clustering.groupby(['cluster', 'is_deleted'], as_index=False).count()[['cluster', 'is_deleted', '月内平均値']]
customer_clustering['routine_flg'] = customer['routine_flg']
customer_clustering.groupby(['cluster', 'routine_flg'], as_index=False).count()[['cluster', 'routine_flg', '月内平均値']]

#翌月の利用回数予測
uselog["usedate"] = pd.to_datetime(uselog["usedate"])
uselog["年月"] = uselog["usedate"].dt.strftime("%Y%m")
uselog_months = uselog.groupby(["年月", "customer_id"], as_index=False).count()
uselog_months.rename(columns={"log_id":"count"}, inplace=True)
del uselog_months["usedate"]
uselog_months
year_months = list(uselog_months["年月"].unique())
year_months
predict_data = pd.DataFrame()
for i in range(6, len(year_months)):
    tmp = uselog_months.loc[uselog_months["年月"] == year_months[i]]
    tmp.rename(columns={"count":"count_pred"}, inplace=True)
    for j in range(1, 7):
        tmp_before = uselog_months.loc[uselog_months["年月"] == year_months[i-j]]
        del tmp_before["年月"]
        tmp_before.rename(columns={"count":"count_{}".format(j-1)}, inplace=True)
        tmp = pd.merge(tmp, tmp_before, on="customer_id", how='left')
    predict_data = pd.concat([predict_data, tmp], ignore_index=True)

predict_data
predict_data = predict_data.dropna()
predict_data.reset_index(drop=True)
predict_data = pd.merge(predict_data, customer[["customer_id", "start_date"]], on="customer_id", how='left')
predict_data["now_date"] = pd.to_datetime(predict_data["年月"], format='%Y%m')
predict_data["start_date"] = pd.to_datetime(predict_data["start_date"])
predict_data['period'] = None
for i in range(len(predict_data)):
    delta = relativedelta(predict_data["now_date"].iloc[i], predict_data["start_date"].iloc[i])
    predict_data["period"][i] = delta.years*12 + delta.months
predict_data

predict_data = predict_data.loc[predict_data["start_date"] >= pd.to_datetime("20180401")]
X = predict_data[["count_0", "count_1", "count_2", "count_3", "count_4", "count_5", "period"]]
y = predict_data["count_pred"]
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = linear_model.LinearRegression()
model.fit(X_train, y_train)
model.score(X_train, y_train)
model.score(X_test, y_test)

uselog_months.to_csv("use_log_months.csv", index=False)
