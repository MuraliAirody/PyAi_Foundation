# Read the input string from the user
s = input()

# Initialize index 'i' to the length of the string
# This points just after the last character
i = len(s)

# Loop backwards through the string
# Continue while:
# 1. We have not reached the beginning of the string (i > 0)
# 2. The current character (s[i-1]) is a digit
while i > 0 and s[i-1].isdigit():
    # Move the index one position to the left
    # This effectively skips trailing digit characters
    i -= 1

# Slice the string from the beginning up to index 'i'
# This removes all trailing digits from the string
print(s[:i])
