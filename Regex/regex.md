# Python Regular Expressions (Regex)

## 1. Introduction
Regular Expressions (Regex) in Python are used for pattern matching and text processing. Python provides the built-in `re` module for working with regex.

```python
import re
```

## 2. Common Regex Functions

### 2.1 re.match()
Matches the pattern only at the beginning of the string.

```python
text = "Python is powerful"
result = re.match("Python", text)
print(result.group())  # Python
```

### 2.2 re.search()
Searches for the pattern anywhere in the string.
```python
text = "I love Python"
result = re.search("Python", text)


print(result.group())  # Python
```

### 2.3 re.findall()
Returns all matches as a list.
```python
text = "cat bat rat mat"
result = re.findall("at", text)

print(result)  # ['at', 'at', 'at', 'at']
```
### 2.4 re.finditer()
Returns an iterator of match objects.
```python
text = "cat bat rat"
for match in re.finditer("at", text):
    print(match.start(), match.group())
```    
### 2.5 re.sub()
Replaces matched patterns.
```python
text = "I like Java"
result = re.sub("Java", "Python", text)

print(result)  # I like Python
```
### 2.6 re.split()
Splits a string using a regex pattern.

```python
text = "one,two;three four"
result = re.split("[,; ]", text)

print(result)  # ['one', 'two', 'three', 'four']
```
## 3. Regex Metacharacters


| Symbol  | Description                  |    |
| ------- | ---------------------------- | -- |
| `.`     | Any character except newline |    |
| `^`     | Start of string              |    |
| `$`     | End of string                |    |
| `*`     | 0 or more occurrences        |    |
| `+`     | 1 or more occurrences        |    |
| `?`     | 0 or 1 occurrence            |    |
| `{n}`   | Exactly n times              |    |
| `{n,m}` | Between n and m times        |    |
| `[]`    | Character set                |    |
| `       | `                            | OR |
| `()`    | Grouping                     |    |


## 4. Character Classes

| Pattern | Meaning                           |
| ------- | --------------------------------- |
| `\d`    | Digit (0–9)                       |
| `\D`    | Non-digit                         |
| `\w`    | Word character (a–z, A–Z, 0–9, _) |
| `\W`    | Non-word                          |
| `\s`    | Whitespace                        |
| `\S`    | Non-whitespace                    |


```python
text = "User123"
print(re.findall(r"\d", text))  # ['1', '2', '3']
```

## 5. Quantifiers
```python

re.findall("a*", "aaab")   # ['aaa', '', '', '']
re.findall("a+", "aaab")   # ['aaa']
re.findall("a?", "aaab")   # ['a', 'a', 'a', '', '']
```

## 6. Grouping and Capturing
```python
text = "My phone number is 9876543210"
pattern = r"(\d{10})"

match = re.search(pattern, text)
print(match.group())

#Multiple groups:
text = "Date: 12-08-2025"
pattern = r"(\d{2})-(\d{2})-(\d{4})"

match = re.search(pattern, text)
print(match.groups())
```
## 7. Regex Flags
Flag	Description
| Flag            | Description                |
| --------------- | -------------------------- |
| `re.IGNORECASE` | Case-insensitive matching  |
| `re.MULTILINE`  | `^` and `$` work line-wise |
| `re.DOTALL`     | `.` matches newline        |

## 8. Raw Strings
Use raw strings to avoid escape issues.
```python
pattern = r"\d{4}"
```
## 9. Practical Examples
```python
#Email Validation
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
email = "test@gmail.com"

print(bool(re.match(pattern, email)))

#Indian Mobile Number Validation
pattern = r"^[6-9]\d{9}$"
number = "9876543210"

print(bool(re.match(pattern, number)))
```


