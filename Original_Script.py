# Importing CSV
import pandas as pd
df= pd.read_csv('https://raw.githubusercontent.com/diverson1/Medical-Insurance-Project/master/insurance.csv')
print(df)

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
    
#Converting the averages into more legible output

print(f'Average cost for individuals under 40 years of age is ${average_under_40_cost:,.2f}')
print(f'Average cost for individuals equal to or over 40 years of age is ${average_equal_or_over_40_cost:,.2f}')
print(f'Average cost for individuals of male gender is ${average_male_cost:,.2f}')
print(f'Average cost for individuals of female gender is ${average_female_cost:,.2f}')



# Calculating sample size make up and which group pays more for insurance

#determining the portion of the sample size men and women both make up, as well as caluculating the percent differnce in the amount they pay
number_of_females = print(f'Females account for {female_count/sample_size:.2%} of the sample size')
number_of_males = print(f'Males account for {male_count/sample_size:.2%} of the sample size')
if average_male_cost > average_female_cost:
    print(f'The average insurance cost for men is {(average_male_cost - average_female_cost)/average_female_cost:.2%} higher than for women')
elif average_female_cost > average_male_cost:
    print(f'The average insurance cost for women is {(average_female_cost - average_male_cost)/average_male_cost:.2%} higher than for men')
else:
    print('Men and women pay the same amount on average for insurance')

number_of_under_40 = print('Individuals under 40 years of age account for '+ str(round(under_40_count/sample_size, 2)*100) + '% of the sample size' )
number_of_equal_or_over_40 = print('Individuals 40 years of age or older account for '+ str(round(equal_or_over_40_count/sample_size, 2)*100) + '% of the sample size' )
if average_under_40_cost > average_equal_or_over_40_cost:
    print('The average insurance cost for individuals under 40 years of age is ' + str(round(((average_under_40_cost - average_equal_or_over_40_cost)/average_equal_or_over_40_cost), 2)) + '% higher than for those equal to or over 40')
elif average_equal_or_over_40_cost > average_under_40_cost:
    print('The average insurance cost for individuals equal to or over 40 years of age is ' + str(round(((average_equal_or_over_40_cost - average_under_40_cost)/average_under_40_cost), 2)*100) + '% higher than for those under 40')
else:
    print('Individuals of both age groups pay the same amount on average for insurance')

# Conclusion: Age has a significantly higher affect on insurance cost than gender. There was no sample size issues that would call into question the validity of the results
# 


