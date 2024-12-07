import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate a date range
date_range = pd.date_range(start='2023-01-01', periods=30, freq='D')  # 30 daily periods from Jan 1, 2023

# Create a synthetic time series dataset (simulating stock prices)
stock_prices = np.random.randn(30).cumsum() + 100  # Random walk

# Create a DataFrame to store the time series data
df = pd.DataFrame({'Date': date_range, 'Stock Price': stock_prices})

# Display the first few rows of the time series data
print("First five rows of the time series data:")
print(df.head())

# Plot the time series data
plt.figure(figsize=(10, 5))
df['Stock Price'].plot(title="Stock Price Time Series", color='blue')
plt.ylabel("Stock Price")
plt.grid(True)
plt.show()

# Moving Average: Calculate 7-day rolling average
df['7-Day Moving Avg'] = df['Stock Price'].rolling(window=7).mean()

# Plot the original and the moving average
plt.figure(figsize=(10, 5))
df['Stock Price'].plot(label='Stock Price', color='blue')
df['7-Day Moving Avg'].plot(label='7-Day Moving Avg', linestyle='--', color='red')
plt.title("Stock Prices with 7-Day Moving Average")
plt.ylabel("Stock Price")
plt.legend()
plt.grid(True)
plt.show()

# Display the DataFrame with moving averages
print("Time series data with moving averages:")
print(df.head(15))  # Display first 15 rows for brevity
