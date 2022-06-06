# %%
# Importing CSV and seperating out what data I need
import pandas as pd


df= pd.read_csv('https://raw.githubusercontent.com/diverson1/Medical-Insurance-Project/master/insurance.csv')

df2 = df.groupby(['smoker', 'sex']).charges.mean().reset_index()
df3 = df[df.age >= 40]
df4 = df[df.age < 40].groupby('sex').charges.mean().reset_index()

pivoted = df2.pivot(columns=('smoker'), index='sex', values='charges').reset_index()
print(df3)
print(df4)


# bmi and age seems to have very little affect on the cost of insurance incomparision to being a smoker
# lets compare the min and max bmi levels and their respective charge in comparision to 18yr who does and does not smoke






