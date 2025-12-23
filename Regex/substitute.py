import re

# Read input string from the user
st = input()

# re.sub() replaces parts of the string that match the regex pattern
# \'s  -> matches the literal characters "'s"
#
# This removes possessive "'s" from words
# Example: "John's book" -> "John book"
opt = re.sub(r"\'s", "", st)

# Print the modified string
print(opt)
