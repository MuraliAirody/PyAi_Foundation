# Working with Python Lists and NumPy Arrays

# A normal Python list
li = [2, 3, 4, 5]
print(type(li))               # <class 'list'>

import numpy as np

# Converting Python list to NumPy array
npLi = np.array(li)
print(type(npLi))             # <class 'numpy.ndarray'>

# Shape of the array
# (4,) → 4 elements and 1 dimension
print(npLi.shape)

# -------------------------------------------
# Creating a 2D NumPy array (Matrix)
# -------------------------------------------
npTwoDim = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(npTwoDim)
print(npTwoDim.shape)         # (3, 3) → 3 rows, 3 columns

# -------------------------------------------
# Without NumPy → Add 5 to each student's score using loops
# -------------------------------------------
scores = [[10, 45, 70], [30, 55, 80], [45, 66, 90]]

# Nested loops to add +5 to every value
for i in range(len(scores)):
    for j in range(len(scores[i])):
        scores[i][j] += 5

print(scores)                 # Updated list values

# -------------------------------------------
# With NumPy → Add 5 to every element (Broadcasting)
# -------------------------------------------
scores_np = np.array([[10, 45, 70], [30, 55, 80], [45, 66, 90]])

# NumPy automatically adds 5 to each element
print(scores_np + 5)

# -------------------------------------------
# Basic NumPy Array Properties
# -------------------------------------------
numpy_arr = np.array(li)

print("size:", numpy_arr.size)       # Total number of elements
print("shape:", numpy_arr.shape)     # (4,) → 1D array with 4 elements
print("dimension:", numpy_arr.ndim)  # 1 dimension

# Checking dimension of 2D array
numpy_arr = np.array([[1, 2, 3, 4], [3, 5, 6, 7]])
print("dimension:", numpy_arr.ndim)  # 2 dimensions

# -------------------------------------------
# Creating Arrays Using NumPy Functions
# -------------------------------------------

# Using arange → creates array with a given range
# arange(start, stop, step)
print(np.arange(1, 10, 2))   # [1 3 5 7 9]

# Creating arrays filled with zeros
print(np.zeros((2, 3)))       # 2 rows × 3 columns
print(np.zeros((3, 2, 3)))    # 3D array → 3 blocks of (2×3)

# Creating arrays filled with ones
print(np.ones((1, 2)))        # 1 × 2 matrix
print(np.ones((3, 1, 2), int)) # 3D array of ones (integer type)

# -------------------------------------------
# Identity Matrix (Square matrix with diagonal = 1)
# -------------------------------------------
print(np.eye(5, 5))           # 5×5 identity matrix

# -------------------------------------------
# Random Array
# random.randint(low, high, size)
# -------------------------------------------
print(np.random.randint(1, 10, (2, 4)))   # 2×4 matrix with random integers 1–9
