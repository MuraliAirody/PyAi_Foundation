'''Given a list of strings, write a Python program that counts how many strings in the list 
have a length greater than 2 and are palindromes. Use Python’s built-in features 
(like slicing or the reversed() function) to perform the palindrome check.
A palindrome is a string that reads the same forwards and backwards, for example, "aba" or "1991".'''

lis = "ab abc aba xyz 1991".split(" ")

p_count = 0

for i in lis:
    if len(i)>2:
        if i == "".join(reversed(i)):
            p_count+=1
print(p_count)            
