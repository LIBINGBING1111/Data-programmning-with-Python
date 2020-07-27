# Week 1 - Assessed Exercises
# Fill in the following Python script and submit it on Brightspace.
# An empty line between the question and 'Ans:' implies that you will need to 
# write a piece of code to get the answer.
import pandas as pd
import numpy as np
# Import Heart Disease UCI data set and call is heart
heart = pd.read_csv('C:/Users/dell/Desktop/data programming with python/heart.csv')

# Q1 (a) How many rows and columns there are in the Heart Disease UCI data set?
rows_count=heart.shape[0]
columns_count=heart.shape[1]
print('This data set has',rows_count,'rows and',columns_count,'colums\n')
# Ans: This data set has __ rows and __ columns 

# Q1 (b) What sex is the 3rd person in the data set, i.e. on the third row?
sex_3rd=heart.at[4,'sex']
if(sex_3rd==0):
    print('The sex of the 3rd person in the data set is female\n')
else:
    print('The sex of the 3rd person in the data set is male\n')
# Ans: 

# Compute the table of different chest pain types. 

# Q2 How many people have type 3 chest pain? 
newdict1=dict(heart.cp.value_counts())
print(newdict1[3],'people have type 3 chest pain\n')
# Ans:

# Q3 (a) What age is the youngest person in this dataset? 
print('The youngest person in this dataset is',heart['age'].min(),'years old\n')
# Ans:

# Q3 (b) What age is the oldest person in this dataset? 
print('The oldest person in this dataset is',heart['age'].max(),'years old\n')
# Ans:

# Look up what the cut function (pd.cut) does and use it to create a new 
# variable which is age grouped into 20-30, 30-40, 40-50, 50-60, 60-70, 70-80. 
ages = heart['age']
heart['age_groups'] = pd.cut(ages,[20,30,40,50,60,70,80])
print(heart,'\n')
# Q4 How many people are in the group (50,60)? 
heart_agecount=heart.age_groups.value_counts()
print(heart_agecount.loc[pd.Interval(50,60)],'people are in the group(50,60)')
# Ans: 



