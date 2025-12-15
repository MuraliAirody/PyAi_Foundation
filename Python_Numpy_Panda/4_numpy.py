import numpy as np

# ----------------------------------------------------
# Splitting a 1D array
# ----------------------------------------------------

# Create array from 8 to 23 and multiply each element by 2
arr = np.arange(8, 24) * 2
print(arr)
# Output: [16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46]


# ----------------------------------------------------
# Split 1D array EQUALLY into 4 parts
# ----------------------------------------------------
print(np.split(arr, 4))
# 16 elements / 4 = 4 elements each
# Output:
# [array([16,18,20,22]),
#  array([24,26,28,30]),
#  array([32,34,36,38]),
#  array([40,42,44,46])]


# ----------------------------------------------------
# Split 1D array using INDEX POSITIONS
# ----------------------------------------------------
print(np.split(arr, [2, 4, 7]))
# Split at indices 2, 4, 7
#
# Parts:
# arr[0:2] → [16,18]
# arr[2:4] → [20,22]
# arr[4:7] → [24,26,28]
# arr[7:]  → [30,32,34,36,38,40,42,46]
#
# Output:
# [array([16,18]),
#  array([20,22]),
#  array([24,26,28]),
#  array([30,32,34,36,38,40,42,46])]


# ----------------------------------------------------
# Splitting a 2D array by axis
# ----------------------------------------------------

# Reshape 16 elements into a 4×4 matrix
arr_two = arr.reshape(4, 4)
print(arr_two)
# Output:
# [[16 18 20 22]
#  [24 26 28 30]
#  [32 34 36 38]
#  [40 42 44 46]]


# ----------------------------------------------------
# Split matrix into 2 equal parts ALONG axis=0 (row-wise)
# ----------------------------------------------------
print(np.split(arr_two, 2, axis=0))
# axis=0 → split rows
# 4 rows / 2 = 2 rows per split
#
# Output:
# [array([[16,18,20,22],
#         [24,26,28,30]]),
#
#  array([[32,34,36,38],
#         [40,42,44,46]])]


# ----------------------------------------------------
# Split matrix into 2 equal parts ALONG axis=1 (column-wise)
# ----------------------------------------------------
print(np.split(arr_two, 2, axis=1))
# axis=1 → split columns
# 4 columns / 2 = 2 columns per split
#
# Output:
# [array([[16,18],
#        [24,26],
#        [32,34],
#        [40,42]]),
#
#  array([[20,22],
#        [28,30],
#        [36,38],
#        [44,46]])]


# ----------------------------------------------------
# Split 2D array using INDEX POSITIONS on rows
# ----------------------------------------------------
print(np.split(arr_two, [1, 3], axis=0))
# Split at row indices 1 and 3
#
# Parts:
# arr_two[0:1] → first row
# arr_two[1:3] → second & third rows
# arr_two[3:]  → last row
#
# Output:
# [array([[16,18,20,22]]),
#  array([[24,26,28,30],
#         [32,34,36,38]]),
#  array([[40,42,44,46]])]


# ----------------------------------------------------
# Horizontal & Vertical splits
# ----------------------------------------------------

print(np.hsplit(arr_two, 2))
# hsplit → split along columns (axis=1)
# Equivalent to: np.split(arr_two, 2, axis=1)


print(np.vsplit(arr_two, 2))
# vsplit → split along rows (axis=0)
# Equivalent to: np.split(arr_two, 2, axis=0)

# ------------------------------------------------------------------------------------------------------------------------



a = np.array([['a','b'],['c','d']])
b = np.array([['e','f'],['g','h']])

# ------------------------------------------------------------
# CONCATENATE HORIZONTALLY (axis = 1)
# ------------------------------------------------------------
print(np.concatenate((a, b), axis=1))
# axis=1 → join columns
# Both arrays must have SAME number of rows
# Output:
# [['a' 'b' 'e' 'f']
#  ['c' 'd' 'g' 'h']]


# ------------------------------------------------------------
# CONCATENATE VERTICALLY (axis = 0)
# ------------------------------------------------------------
print(np.concatenate((a, b), axis=0))
# axis=0 → join rows
# Both arrays must have SAME number of columns
# Output:
# [['a' 'b']
#  ['c' 'd']
#  ['e' 'f']
#  ['g' 'h']]


# ------------------------------------------------------------
# HSTACK and VSTACK
# ------------------------------------------------------------
print(np.hstack((a, b)))
# hstack = horizontal = axis=1
# Must have same number of rows

print(np.vstack((a, b)))
# vstack = vertical = axis=0
# Must have same number of columns


# ------------------------------------------------------------
# Another example
# ------------------------------------------------------------
c = np.array([['a','b','A'],['c','d','C']])
d = np.array([['e','f'],['g','h']])

print(np.concatenate((c, d), axis=0))
# Vertical join → allowed
# c has 3 columns, d has 2 columns → BUT vertical joining only requires:
# SAME number of columns? No.
# Numpy will pad the smaller? No.  
# Actually this will raise an ERROR:
# ValueError: all the input array dimensions except for the concatenation axis must match

# c: shape (2,3)
# d: shape (2,2)
# Columns mismatch → cannot concatenate vertically without reshaping.


print(np.concatenate((c, d), axis=1))
# Horizontal join
# Requirement: SAME number of rows → both have 2 rows → OK.
# Output:
# [['a' 'b' 'A' 'e' 'f']
#  ['c' 'd' 'C' 'g' 'h']]
