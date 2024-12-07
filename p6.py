# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data using NumPy
x = np.linspace(0, 10, 100)          # 100 points between 0 and 10
y_sin = np.sin(x)                    # Sine function
y_cos = np.cos(x)                    # Cosine function
categories = ['A', 'B', 'C', 'D']    # Category labels for bar chart and pie chart
values = [10, 15, 7, 9]              # Sample data for bar chart and pie chart

# 1. Line Plot (Sine and Cosine Functions)
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)  # 2 rows, 3 columns, 1st plot
plt.plot(x, y_sin, label='Sine', color='blue')
plt.plot(x, y_cos, label='Cosine', color='red')
plt.title('Line Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()
plt.grid(True)

# 2. Bar Chart
plt.subplot(2, 3, 2)  # 2nd plot
plt.bar(categories, values, color=['blue', 'orange', 'green', 'red'])
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# 3. Histogram
data = np.random.randn(1000)  # Generate 1000 random numbers from normal distribution
plt.subplot(2, 3, 3)  # 3rd plot
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Data')
plt.ylabel('Frequency')

# 4. Scatter Plot
x_scatter = np.random.rand(50) * 10  # 50 random x values between 0 and 10
y_scatter = np.random.rand(50) * 10  # 50 random y values between 0 and 10
sizes = np.random.rand(50) * 500     # Random sizes for scatter plot points
colors = np.random.rand(50)          # Random colors for scatter plot points

plt.subplot(2, 3, 4)  # 4th plot
plt.scatter(x_scatter, y_scatter, s=sizes, c=colors, cmap='viridis', alpha=0.6)
plt.colorbar()  # Show color scale
plt.title('Scatter Plot')
plt.xlabel('X values')
plt.ylabel('Y values')

# 5. Pie Chart
plt.subplot(2, 3, 5)  # 5th plot
plt.pie(values, labels=categories, autopct='%1.1f%%', colors=['blue', 'orange', 'green', 'red'])
plt.title('Pie Chart')

# 6. Multiple Line Plots
plt.subplot(2, 3, 6)  # 6th plot
y_tan = np.tan(x)  # Tangent function
y_exp = np.exp(x / 5)  # Exponential function

plt.plot(x, y_sin, label='Sine', color='blue')
plt.plot(x, y_cos, label='Cosine', color='red')
plt.plot(x, y_tan, label='Tangent', color='green')
plt.plot(x, y_exp, label='Exponential', color='orange')
plt.ylim(-10, 10)  # Limit the y-axis for better visibility
plt.title('Multiple Line Plots')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.legend()
plt.grid(True)

# Show all plots
plt.tight_layout()
plt.show()
