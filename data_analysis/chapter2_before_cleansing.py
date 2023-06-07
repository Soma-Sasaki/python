import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

os.chdir(r"C:\Users\shira\Desktop\python\data_analysis\sample_100knocks\サンプルコード_20201021\2章")

uriage_data = pd.read_csv('uriage.csv')
kokyaku_data = pd.read_excel('kokyaku_daicho.xlsx', engine='openpyxl')
uriage_data
kokyaku_data
#データに揺れが有るまま集計
uriage_data['purchase_date'] = pd.to_datetime(uriage_data['purchase_date'])
uriage_data["purchase_month"] = uriage_data['purchase_date'].dt.strftime("%Y%m")
res = uriage_data.pivot_table(index='purchase_month', columns='item_name', aggfunc='size', fill_value=0)

#商品名の揺れ補正
uriage_data['item_name'] = uriage_data['item_name'].str.upper() #全て大文字に
uriage_data['item_name'] = uriage_data['item_name'].str.replace(" ","") #半角スペース除去
uriage_data['item_name'] = uriage_data['item_name'].str.replace("　","") #全角スペース除去
uriage_data.sort_values(by=['item_name'], ascending=True)
item_check = pd.unique(uriage_data['item_name'])

uriage_data
#金額欠損値の補完
fig_is_null = uriage_data['item_price'].isnull()
for trg in list(uriage_data.loc[fig_is_null, 'item_name'].unique()):
    price = uriage_data.loc[(~fig_is_null) & (uriage_data['item_name']==trg), 'item_price'].max()
    uriage_data['item_price'].loc[(fig_is_null) & (uriage_data['item_name']==trg)] = price
uriage_data

#欠損値チェック
uriage_data.isnull().any(axis=0)
for trg in list(uriage_data['item_name'].sort_values().unique()):
    print(trg + " 最大値:" + str(uriage_data.loc[uriage_data['item_name']==trg]['item_price'].max()) + " 最小値:" + str(uriage_data.loc[uriage_data['item_name']==trg]['item_price'].min(skipna=False)))

#顧客名の揺れ補正
kokyaku_data['顧客名'] = kokyaku_data['顧客名'].str.replace(" ", "")
kokyaku_data['顧客名'] = kokyaku_data['顧客名'].str.replace("　", "")
kokyaku_data

#日付の揺れ補正
fig_is_serial = kokyaku_data['登録日'].astype(str).str.isdigit()
fig_is_serial
fromSerial = pd.to_timedelta(kokyaku_data.loc[fig_is_serial, '登録日'].astype('float'), unit='D') + pd.to_datetime('1899/12/30')
fromString = pd.to_datetime(kokyaku_data.loc[~fig_is_serial, '登録日'])
kokyaku_data['登録日'] = pd.concat([fromSerial, fromString])
kokyaku_data['登録年月'] = kokyaku_data['登録日'].dt.strftime('%Y%m')
rslt = kokyaku_data.groupby('登録年月').count()['顧客名']
rslt

#売上履歴と顧客台帳の結合
join_data = pd.merge(uriage_data, kokyaku_data, left_on='customer_name', right_on='顧客名', how='left')
join_data = join_data.drop('customer_name', axis=1)

#クレンジングしたデータのダンプ(出力)
dump_data = join_data[["purchase_date", 'purchase_month', 'item_name', 'item_price', '顧客名', 'かな', '地域', 'メールアドレス', '登録日']]
dump_data.to_csv("chapter2_dump_data.csv", index=False)
