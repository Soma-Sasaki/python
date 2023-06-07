import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re
import os

#絶対パス指定
os.chdir(r"C:\Users\shira\デスクトップ\E資格\スキルアップAI\Day7_vr1_7_0")

train = pd.read_csv("titanic/train.csv")
test = pd.read_csv("titanic/test.csv")
train
test

train.isnull().sum()

sns.heatmap(train.corr(), cmap="summer", annot=True)

#性別と生死の関係
sex = train.groupby(["Sex", "Survived"])["Survived"].count()
sns.barplot(np.array(sex.keys()), sex.values)

train.groupby("Sex")["Survived"].mean()

#乗船港と生死の関係
embarked = train.groupby(["Embarked", "Survived"])["Survived"].count()
sns.barplot(np.array(embarked.keys()), embarked.values)
train.groupby("Embarked")["Survived"].mean()

#前処理すたーーーと

def get_title(name):
    title_search = re.search("([A-Za-z]+)\.", name)
    if title_search:
        return title_search.group(1)
    return ""

for df in [train, test]:
    df["Title"] = df["Name"].apply(get_title)

for df in [train, test]:
    df["Title"] = df["Title"].replace(["Mlle", "Ms", "Mme"], "Miss")
    df["Title"] = df["Title"].replace(["Lady", "Countess", "Capt", "Col", "Don", "Dr", "Major", "Rev", "Sir", "Jonkheer", "Dona"], "Others")

train.Title.value_counts()

#Embarkedの欠損値処理(確率が高いSにする)
train.Embarked = train.Embarked.fillna("S")

#Ageの欠損値処理(敬称ごとの平均)
train.groupby("Title")["Age"].mean()

for df in [train, test]:
    mean = df.groupby("Title")["Age"].mean()
    for title in mean.keys():
        df.loc[(df.Age.isnull()) & (df.Title==title), "Age"] = mean[title]

#Fareの欠損値処理(中央値でおｋ)
test.Fare = test.Fare.fillna(test.Fare.median())

#数値データのカテゴライズ
train.Fare.describe()


for df in [train, test]:
    df["Fare_band"] = pd.cut(df["Fare"], [0, 8, 15, 31, 66, 529], labels=range(5), right=False)
    df["Age_band"] = pd.cut(df["Age"], [0, 22, 30, 37, 59, 100], labels=range(5), right=False)

train = train.drop(["PassengerId", "Name", "Ticket", "Cabin", "Age", "Fare"], axis=1)
test = test.drop(["PassengerId", "Name", "Ticket", "Cabin", "Age", "Fare"], axis=1)

for df in [train, test]:
    df.loc[df['Sex']=="female", "Sex"]=0
    df.loc[df['Sex']=='male','Sex']=1

    df.loc[df['Title']=='Mr', 'Title']=0
    df.loc[df['Title']=='Miss', 'Title']=1
    df.loc[df['Title']=='Mrs', 'Title']=2
    df.loc[df['Title']=='Master', 'Title']=3
    df.loc[df['Title']=='Others', 'Title']=4

    df.loc[df['Embarked']=='S', 'Embarked']=0
    df.loc[df['Embarked']=='C', 'Embarked']=1
    df.loc[df['Embarked']=='Q', 'Embarked']=2

train.to_pickle("titanic/titanic_train.pkl")
test.to_pickle("titanic/titanic_test.pkl")
