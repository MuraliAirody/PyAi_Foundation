num = 5

li = list(map(int,"1000 900 800 700 600 500".split()))

target = 1000

def findTraget(low,high,target):

    if low>high:
        return -1

    mid = (low+high)//2    

    if li[mid]==target:
        return mid
    elif li[mid]<target:
        return findTraget(low,mid-1,target)
    else:
        return findTraget(mid+1,high,target)    


print(findTraget(0,len(li)-1,target))



