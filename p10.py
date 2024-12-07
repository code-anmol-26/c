# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate a date range
date_range = pd.date_range(start='2023-01-01', periods=100, freq='D')  # 100 daily periods from Jan 1, 2023

# Create a synthetic time series dataset (simulating stock prices)
np.random.seed(42)
stock_prices = np.random.randn(100).cumsum() + 100  # Random walk

# Create a DataFrame to store the time series data
df = pd.DataFrame({'Date': date_range, 'Stock Price': stock_prices})
df.set_index('Date', inplace=True)

# Display the first few rows of the time series data
print("First five rows of the time series data:")
print(df.head())

# Plot the time series data
plt.figure(figsize=(10, 6))
df['Stock Price'].plot(title="Stock Price Time Series")
plt.ylabel("Stock Price")
plt.grid(True)
plt.show()

# Resampling: Convert daily data to weekly average
weekly_df = df['Stock Price'].resample('W').mean()

# Plot the resampled data (weekly average)
plt.figure(figsize=(10, 6))
weekly_df.plot(title="Weekly Average of Stock Prices")
plt.ylabel("Stock Price")
plt.grid(True)
plt.show()

# Moving Average: Calculate 7-day rolling average
df['7-Day Moving Avg'] = df['Stock Price'].rolling(window=7).mean()

# Plot the original and the moving average
plt.figure(figsize=(10, 6))
df['Stock Price'].plot(label='Stock Price', alpha=0.5)
df['7-Day Moving Avg'].plot(label='7-Day Moving Avg', linestyle='--', color='red')
plt.title("Stock Prices with 7-Day Moving Average")
plt.ylabel("Stock Price")
plt.legend()
plt.grid(True)
plt.show()

# Display the DataFrame with the moving average
print("Time series data with 7-day moving average:")
print(df.head(15))  # Display first 15 rows for brevity
