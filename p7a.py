import numpy as np
import matplotlib.pyplot as plt

# Create a mxn integer array (matrix)
m, n = 4, 5  # Define dimensions
matrix = np.random.randint(1, 10, size=(m, n))  # Create a random matrix with integers from 1 to 9

# Print the attributes of the matrix
print("Matrix:")
print(matrix)
print(f"Shape of the matrix: {matrix.shape}")
print(f"Dimensions of the matrix: {matrix.ndim}")
print(f"Size of the matrix (total elements): {matrix.size}")

# Visualizing the matrix as a heatmap
plt.imshow(matrix, cmap='viridis', interpolation='nearest')
plt.colorbar()  # Add a color bar to indicate the value scale
plt.title('Heatmap of mxn Matrix')
plt.show()
