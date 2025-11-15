
'''Given a list of 2-element integer tuples, write a Python program that sorts the list
 in increasing order of the last element in each tuple. Use Python's built-in sorted() 
 function with an appropriate key function.'''

num = int(input())
li = []
while num>0:
    a,b = map(int,input().split(" "))
    li.append((a,b))

    num-=1

def my_func(tup):
    return tup[-1]

print(sorted(li,key=my_func))

