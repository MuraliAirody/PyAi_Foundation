'''Description

Given an integer vector of length n that may contain many zeros, we want to store only the non-zero entries along with their positions. Implement a program that reads a vector from standard input, converts it into a dictionary (or map) where:
Each key is the 0-based index of a non-zero element.
Each value is the corresponding non-zero element.
Your program should print the dictionary in Python-style format: curly braces {}, colon : between key and value, commas , separating entries, and entries sorted by ascending key.
You are free to use any built-in functions or library routines your language provides for filtering, mapping or formatting.
'''

l = int(input())

vec = list(map(int,input().split(" ")))

res = {}

for i in range(l):
    if vec[i]==0:
        continue
    else:
       res[i]=vec[i]

print(res)       
