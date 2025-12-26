import re  # Import Python's built-in regular expression module

# Read a single line of input (sentence) from the user
inp = input()

# Find all whole words that start with the letter 'c' or 'C'
# \b            → word boundary (ensures matching whole words)
# c             → the letter 'c'
# \w*           → zero or more word characters (letters, digits, underscore)
# flags=re.IGNORECASE → makes the match case-insensitive (c or C)
opt = re.findall(r'\bc\w*', inp, flags=re.IGNORECASE)

# If at least one matching word exists:
#   opt[-1] → fetches the last word starting with 'c'
#   [opt[-1]] → wraps that word inside a list (required output format)
# If no such word exists:
#   print an empty list []
print([opt[-1]] if opt else [])
