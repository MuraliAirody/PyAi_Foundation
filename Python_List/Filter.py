''' Write a Python program that reads a single line of text and produces a list of all unique words with 
length greater than or equal to 4. Your solution should:

Use Python built-in functions such as split(), filter(), map(), and/or comprehensions.
Treat words case-insensitively when checking for duplicates, but output them in lowercase.
Preserve the order of first occurrence in the input string.
Assume the input contains only English letters and spaces (no punctuation).'''

inp = "To be or not. to be that is the question"
li = inp.lower().split(" ")

res = []

def check_for_punc(x):
    for i in x:
        if not 'a'<=i<='z':
            return False
    return True

def my_func(x):
    if len(x)>=4 and x not in res:
        puncRes=check_for_punc(x)
        if puncRes:
           res.append(x)
           return True
    else:
        return False    
        
print(list(filter(my_func,li)))


