import re

inp = input()

# \b           -> word boundary
# p            -> word must start with 'p'
# (?!er\b)     -> negative lookahead to exclude the exact word 'per'
# [a-zA-Z]*    -> remaining letters of the word
# IGNORECASE   -> match both 'p' and 'P'
res = re.findall(r'\bp(?!er\b)[a-zA-Z]*', inp, flags=re.IGNORECASE)

print(res)
