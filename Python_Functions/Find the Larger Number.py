'''
Write a function getBiggerNumber(x, y) that takes two numbers and returns the larger of the two using your language’s built-in max function.
Details

Read two numbers from standard input (on one line separated by a space or on separate lines).
Use the built-in max function (e.g., max(x, y) in Python, Math.max(x, y) in JavaScript) to determine the larger number.
Print the result to standard output.
'''

a_str,b_str = input().split()

def parse(a_str,b_str):
    try:
        return (int(a_str),int(b_str))
    except ValueError as e:
        return (float(a_str),float(b_str))

a,b = parse(a_str,b_str)

def getBiggerNumber(x,y):
    if x>y:
       print(x)
    else:
        print(y)   

getBiggerNumber(a,b)    
