# %%
# Importing CSV and seperating out what data I need
import pandas as pd


df= pd.read_csv('https://raw.githubusercontent.com/diverson1/Medical-Insurance-Project/master/insurance.csv')
print(df.head())
df2 = df.groupby('sex').charges.mean().reset_index()
df3 = df.groupby(['sex','bmi','smoker']).charges.mean().reset_index()
df4 = df.groupby(['sex','bmi', 'age']).charges.mean().reset_index()
print(df3)
print(df4)

# bmi and age seems to have very little affect on the cost of insurance incomparision to being a smoker
# lets compare the min and max bmi levels and their respective charge in comparision to 18yr who does and does not smoke






