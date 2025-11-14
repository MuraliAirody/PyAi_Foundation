
# ***A list in Python is a collection of ordered, changeable (mutable) items.***

It is one of the most commonly used data types.
- ✅ Definition
A list is:
Ordered → items have indexes (0, 1, 2…)
Mutable → you can change, add, delete items
Allows duplicates
Can contain different data types (int, str, float, objects)
- ✅ How to create a list
numbers = [10, 20, 30]
names = ["Ravi", "Raj", "Kumar"]
mixed = [10, "apple", 3.5, True]

# Python List Operations

## 1. Creating List using `range()`

``` python
l = list(range(1, 6))
print(l)
```

Output:

    [1, 2, 3, 4, 5]

## 2. Updating List Elements

``` python
l = [10, 20, 30]
l[1] = 200
```

## 3. Concatenation of Lists

``` python
l1 = [1, 2]
l2 = [3, 4]
result = l1 + l2
```

## 4. Repetition of Lists

``` python
l = [1, 2]
print(l * 3)
```

## 5. Membership in Lists

``` python
l = [10, 20, 30]
20 in l
40 not in l
```

## 6. Aliasing in Lists

``` python
l1 = [10, 20, 30]
l2 = l1
l2[0] = 999
```

## 7. Sorting a List

``` python
l = [5, 3, 9, 1]
l.sort()
l.sort(reverse=True)
```

## 8. Deleting from a List

``` python
del l[1]
l.remove(30)
l.pop(0)
l.clear()
```

## 9. List Comprehension

``` python
squares = [x*x for x in range(1, 6)]
evens = [x for x in range(10) if x % 2 == 0]
upper = [ch.upper() for ch in "ravi"]
```
