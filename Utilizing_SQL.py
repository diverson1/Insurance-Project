# %%
# Importing CSV and seperating out what data I need
import pandas as pd
from pandasql import sqldf


df= pd.read_csv('https://raw.githubusercontent.com/diverson1/Medical-Insurance-Project/master/insurance.csv')
print(df)



df2 = sqldf("""SELECT sex AS 'Target Group', ROUND((SUM(charges))/COUNT(*), 2) AS 'AVG Cost in $', COUNT(*) AS 'Sample Size', (100 * COUNT(*))/1338 AS '% of Sample Size' FROM df 
WHERE sex == 'male' 
GROUP BY sex 
UNION ALL
SELECT sex, ROUND((SUM(charges))/COUNT(*), 2) AS 'AVG COST', COUNT(*), (100 * COUNT(*))/1338 FROM df 
WHERE sex == 'female' GROUP BY sex
UNION ALL 
SELECT age, ROUND((SUM(charges))/COUNT(*), 2), COUNT(*), (100 * COUNT(*))/1338 FROM df WHERE age >= 40 GROUP BY age >= 40
UNION ALL
SELECT age, ROUND((SUM(charges))/COUNT(*), 2), COUNT(*), ROUND((100 * COUNT(*))/1338,1) FROM df WHERE age < 40 GROUP BY age < 40""")

print(df2)




