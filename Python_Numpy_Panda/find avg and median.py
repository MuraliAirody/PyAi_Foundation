

scores = [[10,45,70,20],[30,55,80],[45,66,90]]
avg=[]
median = []
def findAvg(s):
    for sc in scores:
        total = 0
        for i in sc:
            total+=i
        avg.append(total/len(sc))

def findMedian(s):
    for sc in scores:
        sc = sorted(sc)
        mid = len(sc)//2
        if len(sc)%2!=0:
            median.append(sc[mid])
        else:
            median.append((sc[mid-1]+sc[mid])/2)    

findAvg(scores)
findMedian(scores)

print(avg)
print(median)


import numpy as np

np_scores = np.array([[10,45,70],[30,55,80],[45,66,90]])

print(np.mean(np_scores,axis=1))
print(np.median(np_scores,axis=1))