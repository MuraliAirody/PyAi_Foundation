'''You are given a sparse representation of a vector as a dictionary (map) where each key i is a zero-based index and its corresponding value v is the vector entry at that index. All indices not present in the dictionary should be interpreted as 0.
Write a program convertDictionary that reads this dictionary from standard input, reconstructs the full (dense) vector, and prints it.'''

l = int(input())

sparse = {}

while l>0:
    k,v = map(int,input().split())
    sparse[k]=v
    l-=1

def convertDictionary(dic):
    if not dic:
        return []
    res = []
    max_ind = max(dic.keys())
    for i in range(max_ind+1):
        if i in dic.keys():
            res.append(dic[i])
        else:
            res.append(0)      
    return res;    

res=convertDictionary(sparse) 

print(" ".join(str(i) for i in res) )  
