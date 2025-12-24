import re

# Read a single line of input from the user
inp = "Python's Programming: is very easy to learn" 

# Regular expression explanation:
# [A-Za-z]  -> matches any ASCII letter (uppercase A–Z or lowercase a–z)
# +          -> matches one or more consecutive letters
#
# This extracts all contiguous sequences of letters (words)
# and ignores digits, punctuation, and special characters.
opt = re.findall(r'[A-Za-z]+', inp)

# Print the list of extracted words in the order they appear
print(opt)
