import pandas as pd
import numpy as np

# Define the data dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', np.nan],
    'Age': [25, 30, np.nan, 22, 35],
    'Salary': [50000, 60000, 55000, np.nan, 70000]
}

# Convert the dictionary to a pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('data.csv', index=False)

print("CSV file created successfully.")
