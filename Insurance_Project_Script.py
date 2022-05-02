# %% [markdown]
# # U.S. Medical Insurance Costs

# %% [markdown]
# Objective: import csv of insurance data, and complete an analysis to determine if age or sex has a larger influence on cost of insurance, specifially looking at difference between those over vs under 40 years old, compared to differnce between male vs female. Will attempt to account for potential differnces in sample size.

# %%
# Importing CSV and seperating out what data I need
import pandas as pd
df= pd.read_csv('https://raw.githubusercontent.com/diverson1/Medical-Insurance-Project/master/insurance.csv')
print(df)


# %%

under_40_cost = 0
under_40_count = 0
equal_or_over_40_cost = 0
equal_or_over_40_count = 0
male_cost = 0
male_count = 0
female_cost = 0
female_count = 0
sample_size = 1338

#Getting the total cost and calculating the averages
for i in range(1338):
    if df.sex[i] == 'male':
        male_cost += df.charges[i]
        male_count += 1
    else:
        female_cost += df.charges[i]
        female_count += 1

for i in range(1338):
    if df.age[i] < 40 :
        under_40_cost += df.charges[i]
        under_40_count += 1
    else:
        equal_or_over_40_cost += df.charges[i]
        equal_or_over_40_count += 1

average_equal_or_over_40_cost = equal_or_over_40_cost / equal_or_over_40_count
average_under_40_cost = under_40_cost / under_40_count
average_female_cost = female_cost / female_count
average_male_cost = male_cost / male_count
    
#Getting the total cost and calculating the averages

print('Average cost for individuals under 40 years of age is $' + str(round(average_under_40_cost, 2)))
print('Average cost for individuals equal to or over 40 years of age is $' + str(round(average_equal_or_over_40_cost, 2)))
print('Average cost for individuals of male gender is $' + str(round(average_male_cost, 2)))
print('Average cost for individuals of female gender is $' + str(round(average_female_cost, 2)))



# %% [markdown]
# Now that I have gathered together my data into a format that is easier to work with and have calculated the average cost for the attributes of intrest, I'll now begin to actually compare and test the data and look for any potential issues that could result from drawing any conclusion from the data.

# %%
#determining the portion of the sample size men and women both make up, as well as caluculating the percent differnce in the amount they pay
number_of_females = print('Females account for '+ str(round(female_count/sample_size, 2)*100) + '% of the sample size' )
number_of_males = print('Males account for '+ str(round(male_count/sample_size, 2)*100) + '% of the sample size' )
if average_male_cost > average_female_cost:
    print('The average insurance cost for men is ' + str(round(((average_male_cost - average_female_cost)/average_female_cost), 2)*100) + '% higher than for women')
elif average_female_cost > average_male_cost:
    print('The average insurance cost for women is ' + str(round(((average_female_cost - average_male_cost)/average_male_cost), 2)*100) + '% higher than for men')
else:
    print('Men and women pay the same amount on average for insurance')

# %%
#determining the portion of the sample size both age groups make up, as well as caluculating the percent differnce in the amount they pay
number_of_under_40 = print('Individuals under 40 years of age account for '+ str(round(under_40_count/sample_size, 2)*100) + '% of the sample size' )
number_of_equal_or_over_40 = print('Individuals 40 years of age or older account for '+ str(round(equal_or_over_40_count/sample_size, 2)*100) + '% of the sample size' )
if average_under_40_cost > average_equal_or_over_40_cost:
    print('The average insurance cost for individuals under 40 years of age is ' + str(round(((average_under_40_cost - average_equal_or_over_40_cost)/average_equal_or_over_40_cost), 2)) + '% higher than for those equal to or over 40')
elif average_equal_or_over_40_cost > average_under_40_cost:
    print('The average insurance cost for individuals equal to or over 40 years of age is ' + str(round(((average_equal_or_over_40_cost - average_under_40_cost)/average_under_40_cost), 2)*100) + '% higher than for those under 40')
else:
    print('Individuals of both age groups pay the same amount on average for insurance')

# %% [markdown]
# Conclusion: Age has a significantly higher affect on insurance cost than gender. There was no sample size issues that would call into question the validity of the results
# 


