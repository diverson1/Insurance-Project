# %%
# Importing CSV and seperating out what data I need
import pandas as pd


df= pd.read_csv('https://raw.githubusercontent.com/diverson1/Medical-Insurance-Project/master/insurance.csv')
print(df)
df2 = df.groupby('sex').charges.mean()



print(df2)



