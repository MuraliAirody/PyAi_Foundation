import re  # Import the regular expression module

# Read input string from the user
inp = input()

# First regex:
# \b               → word boundary
# [A-Za-z0-9_]     → letters, digits, underscore
# {5}              → exactly 5 characters
# \b               → word boundary
opt = re.findall(r'\b[A-Za-z0-9_]{5}\b', inp)

# Second regex (this line OVERRIDES the previous result):
# \w               → word character (letters, digits, underscore)
# {5}              → exactly 5 characters
opt = re.findall(r'\b\w{5}\b', inp)

# Print the final result
print(opt)
