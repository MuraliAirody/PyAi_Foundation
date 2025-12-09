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


# -----------------------------------------------
# SQUARE & SQUARE ROOT (ufuncs)
# -----------------------------------------------

print(np.square(nums))  
# np.square → squares each element (element-wise)
# Same as nums * nums

print(np.sqrt(nums))
# np.sqrt → square root of each element (element-wise)


# -----------------------------------------------
# INDEXING & SLICING
# -----------------------------------------------

# nums = square of numbers 0 to 4 → [0, 1, 4, 9, 16]
nums = np.arange(5) ** 2
print(nums)

# Accessing 3rd element → index 2
print(nums[2])   # Output: 4

# Slicing from index 1 to 3 (4 is excluded)
print(nums[1:4])  # Output: [1, 4, 9]


# -----------------------------------------------
# 2D ARRAY INDEXING
# -----------------------------------------------

a = np.arange(12).reshape(4, 3)
print(a)
# a =
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]

print(a[2][1])
# a[2] → third row → [6, 7, 8]
# a[2][1] → second element → 7

print(a[1][1:])
# a[1] → second row → [3, 4, 5]
# [1:] → from index 1 to end
# Output → [4, 5]


# -----------------------------------------------
# PART OF A MATRIX (IMPORTANT!)
# -----------------------------------------------

b = np.arange(24).reshape(6, 4)
print(b)
# b =
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]


# ❌ WRONG WAY: b[2:4][1:3]
print(b[2:4][1:3])

# Why wrong?
# - b[2:4] → gives a NEW array:
#   [[ 8  9 10 11]
#    [12 13 14 15]]
#
# - Now [1:3] runs on THIS new array, not original
# So it takes rows 1 to 2 from the sliced result:
# Output → [[12 13 14 15]]
#
# This is NOT the intended [(rows 2-3), (cols 1-2)] slice.


# ✅ CORRECT WAY: Use comma notation
print(b[2:4, 1:3])
# This means:
# rows 2 to 3 → [ [8 9 10 11], [12 13 14 15] ]
# columns 1 to 2 → values from index 1 & 2
#
# Output:
# [[ 9 10]
#  [13 14]]


# -----------------------------------------------
# STEP SLICING
# -----------------------------------------------

# b[::3, ::3]
print(b[::3, ::3])
# ::3 → step of 3
# Picks every 3rd row and 3rd column
#
# Selected rows: 0, 3
# Selected cols: 0, 3
#
# Output:
# [[ 0  3]
#  [12 15]]

# Reverse stepping
print(b[::-3, ::-3])
# Row: ::-3 → reverse, pick every 3rd row from bottom
# Col: ::-3 → reverse, pick every 3rd col from right
#
# Rows picked: 5, 2
# Columns picked: 3, 0
#
# Output:
# [[23 20]
#  [11  8]]
