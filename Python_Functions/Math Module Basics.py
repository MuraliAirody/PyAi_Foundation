'''
In this exercise you’ll import Python’s built-in math module and use three of its members:
math.sqrt(x) to compute the square root of a nonnegative number
math.pow(a, b) to raise a number to a power
the constant math.pi to compute the area of a circle
Task
Write a program that reads four space-separated values from standard input:
x (nonnegative number)
a (number, the base)
b (number, the exponent)
r (nonnegative number, the circle’s radius)
Your program should compute:
A = √x
B = a^b
C = π · r²
'''

import math as m

x_s,a_s,b_s,r_s = input().split()

def parse(v_str):
    try:
        return int(v_str)
    except ValueError as e:
        return float(v_str)

x = parse(x_s)
a = parse(a_s)
b = parse(b_s)
r = parse(r_s)

print(m.sqrt(x))
print(m.pow(a,b))
print(m.pi*r**2)


