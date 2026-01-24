[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ObR9CyXY)
# Note:
- In this assignment you are NOT allowed to use built-in data structures
such as lists and dictionaries.

- Functional Decomposition: In all of these problems figure out if there
are one or more little functions which would help you solve the
overall problem. Then write your solution in terms of those functions.

# Deadline: 10am Friday Nov 15th


# Question 1: `longest_palindromic_substring(s)`

### Description:
Write a function `longest_palindromic_substring(s)` that takes a string `s` as input and returns the longest palindromic substring within `s`. A **palindromic substring** is a substring that reads the same forwards and backwards. If there are multiple palindromic substrings of the maximum length, return the first one that appears in the string.

### Function Signature:
```python
def longest_palindromic_substring(s):
    """
    Write a function `longest_palindromic_substring(s)` that takes a string `s` as input 
    and returns the longest palindromic substring within `s`. If there are multiple 
    palindromic substrings of the maximum length, return the first one.
    """
    pass
```

### Examples:
```python
>>> longest_palindromic_substring("baabaad")
"aabaa"  

>>> longest_palindromic_substring("cbbd")
"bb"

>>> longest_palindromic_substring("a")
""  # Single characters strings are not palindromic
```

### Notes:
- The function should return only the longest palindromic substring.
- If multiple palindromic substrings of the maximum length exist, return the one that appears first.
- The function should handle strings with a length of up to 10^3 characters.

---

# Question 2: `remove_adjacent_duplicates(s)`

### Description:
Write a function `remove_adjacent_duplicates(s)` that removes adjacent duplicate characters in a string `s` repeatedly until no adjacent duplicates remain. For example, given the string `"abbacadd"`, after removing the adjacent `bb`, the string becomes `"aacadd"`. Then, `aa` are adjacent and are removed, resulting in `"cadd"`. Finally, `dd` are removed to yield `"ca"`, which has no adjacent duplicates left.

### Function Signature:
```python
def remove_adjacent_duplicates(s):
    """
    Write a function `remove_adjacent_duplicates(s)` that removes adjacent duplicate 
    characters in a string `s` repeatedly until no adjacent duplicates remain. 
    """
    pass
```

### Examples:
```python
>>> remove_adjacent_duplicates("abbacadd")
"ca"  # In this example, after removing "bb", "aa" becomes adjacent and is also removed, and so on.

>>> remove_adjacent_duplicates("azxxzy")
"ay"  # "xx" and "zz" are removed

>>> remove_adjacent_duplicates("aabccba")
""  # The entire string is removed after removing pairs consecutively
```

### Notes:
- The function should remove adjacent duplicates repeatedly until the string contains no adjacent duplicates.
- After each removal, new adjacent duplicates may appear, which should also be removed.
- Use only string operations; no extra data structures are required.

---

# Question 3: `add_binary(a, b)`

### Binary Strings in Python
Normally, binary strings in Python have a `'0b'` prefix to indicate they are binary. For example, the binary string `"0b101"` represents the number `5` in decimal.

- **Binary to Integer**: You can use the `int()` function with a base to convert a binary string to an integer. For example, `int("0b101", 2)` returns the decimal number `5`.
- **Integer to Binary**: You can go in the opposite direction using the `bin()` function. For instance, `bin(5)` returns the binary string `"0b101"`.


### Description:
Write a function `add_binary(a, b)` that takes two binary strings `a` and `b` as input and returns their sum as a binary string. The binary strings `a` and `b` represent non-negative integers, and the result should also be a binary string.

### Parts:

#### Part A:
In Part A, you are allowed to use both `int()` and `bin()` in your solution. The use of these built-in functions should help you write a very short and efficient solution.

#### Part B:
In Part B, you are **NOT** allowed to use either `int()` or `bin()` or any other built-in methods to convert between binary and integer formats. You must implement the binary addition manually by simulating binary addition without the help of these functions.

### Function Signature:
```python
def add_binary(a, b):
    """
    Write a function `add_binary(a, b)` that takes two binary strings `a` and `b` and 
    returns their sum as a binary string. Part A allows use of `int()` and `bin()`, 
    while Part B requires a solution without these functions.
    """
    pass
```
### Examples:

```python
>>> add_binary("0b11", "0b1")
"0b100"  # 3 + 1 = 4 in decimal, which is "100" in binary

>>> add_binary("0b1010", "0b1011")
"0b10101"  # 10 + 11 = 21 in decimal, which is "10101" in binary

>>> add_binary("0b0", "0b0")
"0b0"  # 0 + 0 = 0 in binary
```
