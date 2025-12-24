import re

inp = "The man met his mother at the market."

# Regex pattern explanation:
# \b     -> word boundary (ensures full word match, not part of a longer word)
# m      -> word must start with letter 'm'
# \w{2}  -> exactly 2 word characters after 'm' (letters, digits, underscore)
# \b     -> word boundary (end of word)
#
# Overall meaning:
# Match words of exactly 3 characters that start with 'm'

res = re.findall(r'\bm\w{2}\b', inp)

print(res)
