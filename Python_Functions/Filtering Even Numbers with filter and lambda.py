'''
Write a program that reads a list of integers from standard input, uses Python’s built-in filter function together with a lambda expression to select only the even numbers, and prints them in the order they appeared.
Input Format

The first line contains an integer n, the number of elements in the list.
The second line contains n space-separated integers.
Output Format

Print a single line of space-separated even integers in the same order they appeared in the input.
If there are no even numbers, print an empty line.
'''

num = int(input())

li = list(map(int,input().split()))

def filterEven(x):
    return x%2==0 

res = list(filter(filterEven,li))

print(" ".join(map(str,res)))