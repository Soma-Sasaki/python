import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from dateutil.relativedelta import relativedelta

#絶対パス指定
os.chdir(r"C:\Users\shira\デスクトップ\programming\python\data_analysis\sample_100knocks\サンプルコード_20201021\3章")

uselog = pd.read_csv('use_log.csv')
uselog
customer = pd.read_csv('customer_master.csv')
customer
class_master = pd.read_csv('class_master.csv')
class_master
campaign_master = pd.read_csv('campaign_master.csv')
campaign_master

#顧客データを主
customer_join = pd.merge(customer, class_master, on='class', how='left')
customer_join = pd.merge(customer_join, campaign_master, on='campaign_id', how='left')
customer_join


customer_join.groupby('class_name').count()['customer_id'] #会員区分
customer_join.groupby('campaign_name').count()['customer_id'] #キャンペーン区分
customer_join.groupby('gender').count()['customer_id'] #男女比
customer_join.groupby('is_deleted').count()['customer_id'] #退会したかどうか
customer_join['start_date'] = pd.to_datetime(customer_join['start_date'])
customer_start = customer_join.loc[customer_join['start_date'] > pd.to_datetime('20180401')]
customer_start

#最新月顧客の集計
customer_join['end_date'] = pd.to_datetime(customer_join['end_date'])
customer_newer = customer_join.loc[(customer_join['end_date'] >= pd.to_datetime('20190331'))|(customer_join['end_date'].isna())]
customer_newer['end_date'].unique()
customer_newer
customer_newer.groupby('class_name').count()['customer_id'] #会員区分
customer_newer.groupby('campaign_name').count()['customer_id'] #キャンペーン区分
customer_newer.groupby('gender').count()['customer_id'] #会員区分

#利用履歴データを主
#月/顧客ごとの利用回数
uselog['usedate'] = pd.to_datetime(uselog['usedate'])
uselog
uselog['年月'] = uselog['usedate'].dt.strftime('%Y%m')
uselog
uselog_months = uselog.groupby(['年月', 'customer_id'], as_index=False).count()
uselog_months.rename(columns={'log_id':'count'}, inplace=True)
del uselog_months['usedate']
uselog_months
#顧客ごとの月内利用回数
uselog_customer = uselog_months.groupby('customer_id').agg(['mean', 'median', 'max', 'min'])['count']
uselog_customer = uselog_customer.reset_index(drop=False)
uselog_customer
#定期利用フラグ
uselog['weekday'] = uselog['usedate'].dt.weekday
uselog_weekday = uselog.groupby(['customer_id', '年月', 'weekday'], as_index=False).count()[['customer_id', '年月', 'weekday', 'log_id']]
uselog_weekday.rename(columns={'log_id':'count'}, inplace=True)
uselog_weekday = uselog_weekday.groupby('customer_id', as_index=False).max()[['customer_id', 'count']]
uselog_weekday['routine_flg'] = 0
# uselog_weekday['routine_flg'].loc[uselog_weekday['count'] >= 4] = 1
uselog_weekday['routine_flg'] = uselog_weekday['routine_flg'].where(uselog_weekday['count']<4, 1)
uselog_weekday

#顧客データと利用履歴データの結合
customer_join = pd.merge(customer_join, uselog_customer, on='customer_id', how='left')
customer_join = pd.merge(customer_join, uselog_weekday, on='customer_id', how='left')
customer_join

#会員期間の計算
customer_join['calc_date'] = customer_join['end_date']
customer_join['calc_date'] = customer_join['calc_date'].fillna(pd.to_datetime('20190430'))
customer_join['membership_period'] = 0
for i in range(len(customer_join)):
    delta = relativedelta(customer_join['calc_date'].iloc[i], customer_join['start_date'].iloc[i])
    customer_join['membership_period'].iloc[i] = delta.years*12 + delta.months
customer_join
plt.hist(customer_join['membership_period'])
customer_end = customer_join.loc[customer_join['is_deleted']==1]
customer_end
customer_stay = customer_join.loc[customer_join['is_deleted']==0]
customer_stay
customer_join.to_csv('customer_join.csv', index=False)
