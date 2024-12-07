import numpy as np
import matplotlib.pyplot as plt

# a) Array Manipulation
print("\n--- Array Manipulation ---")
arr = np.arange(10)
print("Original Array:", arr)

# Reshaping the array
reshaped_arr = arr.reshape(2, 5)
print("Reshaped Array (2x5):\n", reshaped_arr)

# b) Searching in Array
print("\n--- Searching in Array ---")
search_value = 5
index = np.where(arr == search_value)
print(f"Index of {search_value} in array: {index}")

# c) Sorting Array
print("\n--- Sorting Array ---")
arr_unsorted = np.array([9, 1, 5, 7, 3])
sorted_arr = np.sort(arr_unsorted)
print("Unsorted Array:", arr_unsorted)
print("Sorted Array:", sorted_arr)

# d) Splitting Array
print("\n--- Splitting Array ---")
arr_split = np.array_split(arr, 3)
print("Splitted Array into 3 parts:", arr_split)

# Part 2: Broadcasting in NumPy
print("\n--- Broadcasting in NumPy ---")
# Create two arrays with different shapes
a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]])

# Broadcasting the arrays and performing addition
result = a + b
print("Broadcasted Array:\n", result)

# Part 3: Plotting NumPy Arrays using Matplotlib
print("\n--- Plotting NumPy Arrays ---")
# Create x and y arrays for plotting
x = np.linspace(0, 10, 100)    # 100 points between 0 and 10
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot sine and cosine graphs
plt.plot(x, y_sin, label="Sine", color="blue")
plt.plot(x, y_cos, label="Cosine", color="red")
plt.title("Sine and Cosine Waves")
plt.xlabel("x values ")
plt.ylabel("y values")
plt.legend()
plt.grid(True)
plt.show()
