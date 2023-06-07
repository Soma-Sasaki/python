import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import os
from dateutil.relativedelta import relativedelta
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.model_selection import train_test_split

#絶対パス指定
os.chdir(r"C:\Users\shira\Desktop\python\data_analysis\sample_100knocks\サンプルコード_20201021\5章")

customer = pd.read_csv("customer_join.csv")
customer
uselog_months = pd.read_csv("use_log_months.csv")
uselog_months

year_months = list(uselog_months["年月"].unique())
year_months
uselog = pd.DataFrame()
for i in range(1, len(year_months)):
    tmp = uselog_months.loc[uselog_months["年月"] == year_months[i]]
    tmp.rename(columns={"count":"count_pred"}, inplace=True)
    tmp_before = uselog_months.loc[uselog_months["年月"] == year_months[i-1]]
    del tmp_before["年月"]
    tmp_before.rename(columns={"count": "count_before"}, inplace=True)
    tmp = pd.merge(tmp, tmp_before, on="customer_id", how='left')
    uselog = pd.concat([uselog, tmp], ignore_index=True)
uselog

#退会顧客データ
exit_customer = customer.loc[customer["is_deleted"] == 1]
exit_customer["exit_date"] = None
exit_customer["end_date"] = pd.to_datetime(exit_customer["end_date"])
for i in range(len(exit_customer)):
    exit_customer["exit_date"].iloc[i] = exit_customer["end_date"].iloc[i] - relativedelta(months=1)
exit_customer["年月"] = pd.to_datetime(exit_customer["exit_date"])
exit_customer["年月"] = exit_customer["年月"].dt.strftime("%Y%m")
uselog["年月"] = uselog["年月"].astype(str)
exit_uselog = pd.merge(uselog, exit_customer, on=["customer_id", "年月"], how='left')
exit_uselog = exit_uselog.dropna(subset=["name"])
exit_uselog

#継続顧客データ
conti_customer = customer.loc[customer["is_deleted"] == 0]
conti_uselog = pd.merge(uselog, conti_customer, on=["customer_id"], how='left')
conti_uselog = conti_uselog.dropna(subset=["name"])
conti_uselog
conti_uselog = conti_uselog.sample(frac=1).reset_index(drop=True)
conti_uselog = conti_uselog.drop_duplicates(subset="customer_id")
conti_uselog

#継続顧客データと退会顧客データとの縦結合
predict_data = pd.concat([conti_uselog, exit_uselog], ignore_index=True)
predict_data

predict_data["period"] = 0
predict_data["now_date"] = pd.to_datetime(predict_data["年月"], format="%Y%m")
predict_data["start_date"] = pd.to_datetime(predict_data["start_date"])
for i in range(len(predict_data)):
    delta = relativedelta(predict_data["now_date"].iloc[i], predict_data["start_date"].iloc[i])
    predict_data["period"].iloc[i] = int(delta.years*12 + delta.months)
predict_data
predict_data.isna().sum()
predict_data = predict_data.dropna(subset=["count_before"])
predict_data.isna().sum()
predict_data = predict_data[["campaign_name", "class_name", "gender", "count_before", "routine_flg", "period", "is_deleted"]]
predict_data
predict_data = pd.get_dummies(predict_data)
del predict_data["campaign_name_通常"]
del predict_data["class_name_ナイト"]
del predict_data["gender_M"]
predict_data

#決定木を用いた退会予測モデル
exit = predict_data.loc[predict_data["is_deleted"]==1]
conti = predict_data.loc[predict_data["is_deleted"]==0].sample(len(exit))
X = pd.concat([exit, conti], ignore_index=True)
y = X["is_deleted"]
del X["is_deleted"]
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = DTC(random_state=0, max_depth=5)
model.fit(X_train, y_train)
model.score(X_train, y_train)
model.score(X_test, y_test)
