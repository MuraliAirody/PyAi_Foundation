import re

try:
    inp = input().strip()
except EOFError:
    print("No match")
    exit()

res = re.search(r"\brat\b",inp)

if res:
  print(res.group())
else:
  print("No match")  