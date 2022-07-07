# Importing CSV
import pandas as pd
import matplotlib.pyplot as plt 
df= pd.read_csv('https://raw.githubusercontent.com/diverson1/Medical-Insurance-Project/master/insurance.csv')

# Getting a feel for what the data looked like

print(df.head())
print(df.describe(include= 'all'))

# Finding total sample size and size of each group of interest

sample_size = df.shape[0]
m_f_count = df.groupby('sex').age.count()
equal_or_over_40_count = df[df.age >= 40].shape[0]
under_40_count = df[df.age < 40].shape[0]

#Calculating the average cost of each group

average_male_cost = df[df.sex=='male'].charges.mean()
average_female_cost = df[df.sex=='female'].charges.mean()
average_under_40_cost = df[df.age < 40].charges.mean()
average_equal_or_over_40_cost = df[df.age >= 40].charges.mean()

    
#Converting the averages into readable output

print(f'Average cost for individuals under 40 years of age is ${average_under_40_cost:,.2f}')
print(f'Average cost for individuals equal to or over 40 years of age is ${average_equal_or_over_40_cost:,.2f}')
print(f'Average cost for individuals of male gender is ${average_male_cost:,.2f}')
print(f'Average cost for individuals of female gender is ${average_female_cost:,.2f}')

# Calculating percent of group in sample size and difference in amount paid between male vs female

number_of_females = print(f'Females account for {m_f_count[0]/sample_size:.2%} of the sample size')
number_of_males = print(f'Males account for {m_f_count[1]/sample_size:.2%} of the sample size')

if average_male_cost > average_female_cost:
    print(f'The average insurance cost for men is {(average_male_cost - average_female_cost)/average_female_cost:.2%} higher than for women')
elif average_female_cost > average_male_cost:
    print(f'The average insurance cost for women is {(average_female_cost - average_male_cost)/average_male_cost:.2%} higher than for men')
else:
    print('Men and women pay the same amount on average for insurance')

# Calculating percent of group in sample size and difference in amount paid between over and under 40 years of age

number_of_under_40 = print(f'Individuals under 40 years of age account for {under_40_count/sample_size:.2%} of the sample size')
number_of_equal_or_over_40 = print(f'Individuals 40 years of age or older account for {equal_or_over_40_count/sample_size:.2%} of the sample size' )

if average_under_40_cost > average_equal_or_over_40_cost:
    print(f'The average insurance cost for individuals under 40 years of age is {((average_under_40_cost - average_equal_or_over_40_cost)/average_equal_or_over_40_cost):.2%} higher than for those equal to or over 40')
elif average_equal_or_over_40_cost > average_under_40_cost:
    print(f'The average insurance cost for individuals equal to or over 40 years of age is {((average_equal_or_over_40_cost - average_under_40_cost)/average_under_40_cost):.2%} higher than for those under 40')
else:
    print('Individuals of both age groups pay the same amount on average for insurance')

# Conclusion: Age has a significantly higher affect on insurance cost than gender. There was no sample size issues that would call into question the validity of the results

plt.hist(df.charges)
plt.show()
