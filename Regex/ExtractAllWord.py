'''Given a single line of text containing words separated by spaces, write a program that uses Python’s built-in re module to find all words that:
Are exactly three letters long
Start with the lowercase letter “m”
Appear as whole words (i.e., surrounded by word boundaries)
Print the list of matching words in the order they appear in the input string.
'''

import re

inp = input()

res = re.findall(r'\bm\w{2}\b',inp)

print(res)