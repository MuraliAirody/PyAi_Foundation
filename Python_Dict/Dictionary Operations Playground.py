'''You’ll write a program that starts with an empty Python dictionary d and processes a sequence of operations. There are four supported operations:
assign k vResets the dictionary d so that it contains only the single key–value pair {k: v}.
bracket k vDoes d[k] = v (adds or overwrites key k).
update k vDoes d.update({k: v}) (adds or overwrites key k).
setdefault k vDoes d.setdefault(k, v) (adds key k with value v only if k is not already in d).
After applying all operations in the given order, your program should print the final contents of d. Output each key: value on its own line, sorted in ascending lexicographical order of the keys.'''


num = int(input())

dic = {}

while num>0:
    type,k,v = input().split()
    
    if type=="bracket":
        dic[k]=v
    elif type=="update":
        dic.update({k:v})
    elif type=="assign":
        dic.clear()
        dic[k]=v
    else:
        dic.setdefault(k,v)  
    num-=1


for i in sorted(dic):
    print(f"{i}: {dic[i]}")    
