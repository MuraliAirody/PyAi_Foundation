'''Write a Python program that generates and prints a 4×4 2D matrix representing 
the multiplication table for indices 0 through 3. Specifically, the element at row i and column j is i * j.
You are encouraged to use Python’s built-in range function together with both of the following approaches:
Nested loops
A single list comprehension
Your program should output the matrix in the exact format shown below (with no extra spaces):
[[0,0,0,0],[0,1,2,3],[0,2,4,6],[0,3,6,9]]
'''

# 4×4 Multiplication Matrix

matrix = [[j*i for j in range(4)] for i in range(4)]

print(matrix)
