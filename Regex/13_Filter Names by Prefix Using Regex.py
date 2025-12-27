import re

# Read a single line of space-separated lowercase names
inp = input()

# Use re.findall with a single regex call
# \b        → word boundary (start of a word)
# (?:an|ak) → non-capturing group matching prefixes "an" or "ak"
# [a-z]*    → zero or more lowercase letters after the prefix
# \b        → word boundary (end of the word)
result = re.findall(r'\b(?:an|ak)[a-z]*\b', inp)

# Print the result as a Python list
print(result)
