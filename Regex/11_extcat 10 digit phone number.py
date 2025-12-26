import re

inp = input()

# Extract all digits from the input
digits = re.findall(r'\d', inp)

# Join digits into a single string
digits_str = ''.join(digits)

# Extract the first 10 digits as the phone number
print(digits_str[:10] if len(digits_str) >= 10 else "")
