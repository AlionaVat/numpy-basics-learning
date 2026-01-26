import numpy as np

# -------------------------------
# Creating NumPy Arrays
# -------------------------------

# 1D array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr_1d)

# 2D array
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("\n2D Array:\n", arr_2d)

# -------------------------------
# Array Attributes
# -------------------------------

print("\nArray Dimensions (ndim):", arr_2d.ndim)
print("Array Shape:", arr_2d.shape)
print("Array Size:", arr_2d.size)

# -------------------------------
# Indexing and Slicing
# -------------------------------

print("\nElement from 1D array (index 2):", arr_1d[2])
print("Second row of 2D array:", arr_2d[1])
print("Second column of 2D array:", arr_2d[:, 1])

# -------------------------------
# Array Operations
# -------------------------------

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Addition
addition_result = array1 + array2
print("\nArray Addition:", addition_result)

# Multiplication
multiplication_result = array1 * array2
print("Array Multiplication:", multiplication_result)

# -------------------------------
# Matrix Multiplication
# -------------------------------

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

matrix_result = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication Result:\n", matrix_result)

# -------------------------------
# Statistical Operations
# -------------------------------

data = np.array([1, 2, 3, 4, 5])
mean_value = np.mean(data)
print("\nMean of data:", mean_value)
