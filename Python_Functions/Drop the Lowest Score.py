'''
In many grading systems, a student’s final exam score is computed by dropping the lowest test score and then averaging the rest.
Your task is to implement getScore(), which:
Reads an integer N (number of test scores, (N \ge 2)).
Reads N space-separated integers (each in [0…100]).
Drops the single lowest score.
Computes the arithmetic mean of the remaining (N–1) scores.
Prints the integer part of the mean (i.e. floor of the average).
You should leverage Python’s built-in functions (such as sum(), min()) to keep your solution clean and concise.

'''

num = int(input())

li = list(map(int,input().split()))

def getScore(li):
    low = min(li)

    li.remove(low)

    return sum(li)/len(li)


print(int(getScore(li)))    