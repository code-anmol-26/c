import pandas as pd
import numpy as np

# 1) Importing Datasets
# Replace 'data.csv' with the actual path to your CSV file
data = pd.read_csv("data.csv")

print("Original Dataset:")
print(data)

# 2) Cleaning the Data
# Handling missing values by filling them with the mean (for numerical columns) and 'Unknown' (for string columns)
data['Age'].fillna(data['Age'].mean(), inplace=True)  # Filling missing 'Age' with the mean
data['Salary'].fillna(data['Salary'].mean(), inplace=True)  # Filling missing 'Salary' with the mean
data['Name'].fillna('Unknown', inplace=True)  # Filling missing 'Name' with 'Unknown'

print("\nDataset After Cleaning:")
print(data)

# 3) Data frame manipulation using Numpy
# Let's create a new column 'Adjusted Salary' which is the 'Salary' * 1.10 (an increase of 10%)
data['Adjusted Salary'] = data['Salary'] * 1.10

# Using Numpy to apply a condition on the 'Age' column (add 5 years for all users above 30 years)
data['Age'] = np.where(data['Age'] > 30, data['Age'] + 5, data['Age'])

print("\nDataset After Manipulating Data with Numpy:")
print(data)
