'''
Problem Description

Write a Python function sum_of_cubes(nums) that takes a list of integers and returns the sum of their cubes. 
Your implementation must leverage Python’s built-in map() and sum() functions. Also implement a main() function to handle input/output as described below.
'''

import math as m
def sum_of_cubes(li):
    return sum(int(m.pow(i,3)) for i in li)

num = int(input())
li = list(map(int,input().split()))
print(sum_of_cubes(li))
