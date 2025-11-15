'''Write a Python program to remove duplicate elements from a list using a loop. 
You may not use any built-in set or dictionary methods for deduplication—only loops and basic list operations.'''

inp = "[7,7,7,7]"

tp = eval(inp)

li = list(tp)
length = len(li)
for i in range(length-1,0,-1):

   num = li[i]

   subli = li[:i]

   for j in range(len(subli)):
     if subli[j]==num:
        del li[i]
        break

print(li)        