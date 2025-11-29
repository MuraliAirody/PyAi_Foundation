'''
Problem Description

Implement a function
bool is_prime(int n);
that returns true if n is a prime number (an integer > 1 whose only positive divisors are 1 and itself) and false otherwise.
Then, in your main, read a single integer N from standard input and print all prime numbers p such that 2 ≤ p ≤ N. Print one prime per line.

'''

import math as m

num = int(input())

def is_prime(n):
    if n<2:
       return False
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            return False
    return True


for i in range(2,num+1):
    if is_prime(i):
        print(i)
