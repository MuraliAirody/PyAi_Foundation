'''
Write a program that reads a dictionary from standard input in JSON format and inverts it so that the original values become keys and the original keys become values. If the input dictionary contains any duplicate values, the program should output an empty dictionary instead.
Example:
Input: {"a": 1, "b": 2, "c": 3}
Output: {"1": "a", "2": "b", "3": "c"}
'''

import json

dic = json.loads(input())

res = {}

if len(list(dic.values()))!=len(set(dic.values())):
    print({})
else:
    for key,value in dic.items():
        res[value]=key

    print(json.dumps(res))    
