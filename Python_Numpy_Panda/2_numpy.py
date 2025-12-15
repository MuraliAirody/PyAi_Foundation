import numpy as np

# -------------------------------
# BASIC ARRAY CREATION
# -------------------------------

np_arr = np.array([1, 2, 3, 4, 5, 6])
print(np_arr)

# -------------------------------
# RESHAPE()
# -------------------------------

# RULES:
# 1. Total elements BEFORE reshape == total elements AFTER reshape
# 2. reshape() on numpy array object works only on numpy arrays
# 3. np.reshape() (module version) works on lists as well
# 4. Only ONE dimension can be -1 (NumPy auto-calculates that dimension)

print(np_arr.reshape(2, 3))  # reshape using array method
print(np.reshape(np_arr, (2, 3)))  # reshape using numpy module (works for lists too)

# -------------------------------
# RESHAPING COUNTRIES ARRAY
# -------------------------------

countries = np.array([
    "India", "America", "China", "UAE",
    "Russia", "England", "Australia", "Africa"
])

# Convert 1D → 2D (4 rows, 2 columns)
print(np.reshape(countries, (4, 2)))

# Auto-calc with -1 (NumPy finds the correct row count)
# Here: 6 elements → (-1,2) becomes (3,2)
print(np.reshape(np_arr, (-1, 2)))  # Only one -1 is allowed!

# -------------------------------
# TRANSPOSE
# -------------------------------

# Meaning: Rows become columns, columns become rows
reshape_arr = np.reshape(countries, (4, 2))
print(np.transpose(reshape_arr))

# -------------------------------
# FLATTEN
# -------------------------------

# Convert ANY multi-dimensional array → 1D
print(reshape_arr.flatten())

# -------------------------------
# ELEMENT-WISE OPERATIONS
# -------------------------------

# Create two matrices of same shape
a = np.arange(12).reshape(3, 4)
b = np.arange(12, 24).reshape(3, 4)

# NumPy performs element-wise arithmetic
print(a + b)   # Add each element
print(a - b)   # Subtract each element
print(a * b)   # Multiply each element
print(a / b)   # Divide each element
print(a > 5)   # Compare each element → Boolean result

# -------------------------------
# MATRIX MULTIPLICATION (DOT PRODUCT)
# -------------------------------

# RULES for matrix multiplication:
# If A = (m × n) and B = (n × p)
# THEN result = (m × p)
# i.e., INNER dimensions must match (n == n)

A = np.arange(12).reshape(3, 4)  # 3 rows, 4 columns
B = np.arange(12, 24).reshape(4, 3)  # 4 rows, 3 columns

# Valid: (3 × 4) dot (4 × 3)  →  RESULT = (3 × 3)
print(A.dot(B))
