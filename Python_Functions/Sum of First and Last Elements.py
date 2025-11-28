'''
Write a function addFirstAndLast that takes a list of integers and returns the sum of the first and last elements of the list.
If the list is empty, return 0.
If the list contains exactly one element, return that element.
Input Format

The first line contains an integer n, the number of elements in the list.
If n > 0, the second line contains n space-separated integers.
Output Format

Print a single integer: the sum of the first and last elements of the list (or 0 if the list is empty).

'''

num = int(input())


def addFirstAndLast(li):

    if len(li)==1:
        return li[0]
    else:
        return li[0]+li[len(li)-1]    

if num==0:
    print(0)
else:
    li = list(map(int,input().split()))
    print(addFirstAndLast(li))   