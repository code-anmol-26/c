# Import necessary libraries
import pandas as pd
import numpy as np

# Step 1: Importing Dataset
df=pd.read_csv('C:\\Users\\user\\Desktop\\emp.data.csv' )
print("Original Dataset:")
print(df)

# Step 2: Cleaning the Data
#Column names can be assigned
#df=pd.read_csv('C:\\Users\\user\\Desktop\\iriss.data.csv',names=['a','b','c','d','e'] )
#print(df)

# 2.1 Handling missing values: Let's fill missing 'Age' with NaN and 'Salary' with mean.
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
df['Age'] = df['Age'].replace('', np.nan)
#df = df.replace('', np.nan)  # Replace empty 
print(df.head())
#df = df.fillna(0)            # Fills all NaN with Zeros

# 2.2 Remove duplicates: Removing rows where 'Name' and 'Age' are duplicated.
df.drop_duplicates(subset=['Name', 'Age'], inplace=True)

print("\nDataset after cleaning:")
print(df)

# Step 3: Data Frame Manipulation using NumPy
# 3.1 Creating a NumPy array from the 'Age' and 'Salary' columns
age_salary_array = df[['Age', 'Salary']].values

# 3.2 Perform a NumPy operation: Let's increase everyone's salary by 10%
age_salary_array[:, 1] = age_salary_array[:, 1] * 1.1

print("\nNumPy Array after increasing Salary by 10%:")
print(age_salary_array)

# 3.3 Update the original DataFrame with the new Salary
df['Salary'] = age_salary_array[:, 1]

print("\nFinal DataFrame with updated salary:")
print(df)
