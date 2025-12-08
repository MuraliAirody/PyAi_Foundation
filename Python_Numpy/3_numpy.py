import numpy as np   # Importing NumPy library and giving it a short name "np"

# Creating a 1D numpy array with elements 1 to 5
np_arr = np.array([1, 2, 3, 4, 5])

# -----------------------------------------------
# SUM, MIN, MAX OPERATIONS ON 1D ARRAY
# -----------------------------------------------

# Sum of all the elements → 1+2+3+4+5 = 15
print(np_arr.sum())       

# Minimum value in the array → 1
print(np_arr.min())       

# Maximum value in the array → 5
print(np_arr.max())       


# -----------------------------------------------
# CREATING A 2D ARRAY USING arange() + reshape()
# -----------------------------------------------

# np.arange(24) creates numbers from 0 to 23 (total 24 numbers)
# reshape(6,4) converts it into a matrix with 6 rows & 4 columns
nums = np.arange(24).reshape(6, 4)

print(nums)   
# Output looks like:
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]


# -----------------------------------------------
# SUM OPERATIONS ON 2D ARRAY
# -----------------------------------------------

# Sum of all the elements in the entire 6x4 matrix
print(nums.sum())   
# Output = 0+1+2+...+23 = 276


# Sum of all elements ROW-WISE (axis=1)
# axis=1 → perform operation across columns for each row
print(nums.sum(axis=1))  
# Output = [ 6, 22, 38, 54, 70, 86 ]
# Example: Row 0 → 0+1+2+3 = 6


# Sum of all elements COLUMN-WISE (axis=0)
# axis=0 → perform operation down the rows for each column
print(nums.sum(axis=0))
# Output = [60, 66, 72, 78]
# Example: Column 0 → 0+4+8+12+16+20 = 60

# ---------------------------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------------
# MIN & MAX WITH AXIS
# -----------------------------------------------

# Minimum element in each ROW (axis=1)
# axis=1 → operate ACROSS columns for each row
print(nums.min(axis=1))
# Example for Row 0 → min(0,1,2,3) = 0
# Output: [0, 4, 8, 12, 16, 20]

# Minimum element in each COLUMN (axis=0)
# axis=0 → operate DOWN rows for each column
print(nums.min(axis=0))
# Example for Column 0 → min(0,4,8,12,16,20) = 0
# Output: [0, 1, 2, 3]


# Maximum element in each ROW  
print(nums.max(axis=1))
# Example for Row 0 → max(0,1,2,3) = 3
# Output: [ 3, 7, 11, 15, 19, 23]

# Maximum element in each COLUMN
print(nums.max(axis=0))
# Example for Column 0 → max(0,4,8,12,16,20) = 20
# Output: [20, 21, 22, 23]


# Mean (average) of entire 2D array
print(nums.mean())
# (0 + 1 + ... + 23) / 24 = 11.5
# Mean is calculated over **all elements** when axis is not specified


# -----------------------------------------------
# UNIVERSAL FUNCTIONS (ufuncs)
# These operate element-wise on NumPy arrays.
# -----------------------------------------------

# Creating two 3x4 matrices
a = np.arange(12).reshape(3, 4)
# a =
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

b = np.arange(12, 24).reshape(3, 4)
# b =
# [[12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]

# Element-wise addition
print(np.add(a, b))
# Same as: a + b
# Output: 
# [[12 14 16 18]
#  [20 22 24 26]
#  [28 30 32 34]]

# Element-wise subtraction
print(np.subtract(a, b))
# Same as: a - b

# Element-wise multiplication
print(np.multiply(a, b))
# Same as: a * b

# Element-wise division
print(np.divide(a, b))
# Same as: a / b
# Returns floating-point results
