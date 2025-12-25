import re

# Read a line of input from the user
inp = input()

# Regular expression explanation:
# \b        -> word boundary (ensures matching starts at a word boundary)
# \d        -> matches a single digit (0–9)
# \w*       -> matches zero or more word characters (letters, digits, underscore)
# \b        -> word boundary (end of the word)
#
# This finds all "words" that start with a digit and may be followed
# by letters, digits, or underscores.
opt = re.findall(r'\b\d\w*\b', inp)

# Print the list of matched substrings
print(opt)
