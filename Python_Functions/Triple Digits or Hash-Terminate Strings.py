'''
Problem Statement

You are given a list of strings. Write a Python program that processes each element as follows:
If the string consists only of digits (0–9), print it concatenated three times (e.g. "41" → "414141").
Otherwise, print the string with a trailing # (e.g. "ZARA" → "ZARA#").
Use Python’s built-in string methods to detect pure numeric strings.
'''


num = int(input())

li = [input() for _ in range(num)]

def stringFormat(ele):
    if ele.isdigit():
        return ele*3
    else:
        return ele+'#'

for i in range(num):
    print(stringFormat(li[i]))
    