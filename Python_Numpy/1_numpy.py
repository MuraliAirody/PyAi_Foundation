li = [2,3,4,5]
print(type(li))

import numpy as np

npLi = np.array(li)
print(type(npLi))

print(npLi.shape) #4 represent four element and 1 diemension

npTwoDim = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(npTwoDim)
print(npTwoDim.shape) #3 rows and 3 columns

#scores of three students, by using loop add 5 to the each score 
scores = [[10,45,70],[30,55,80],[45,66,90]]
for i in range(len(scores)):
    for j in range(len(scores[i])):
        scores[i][j]+=5
print(scores)    


scores_np = np.array([[10,45,70],[30,55,80],[45,66,90]])

print(scores_np+5)

