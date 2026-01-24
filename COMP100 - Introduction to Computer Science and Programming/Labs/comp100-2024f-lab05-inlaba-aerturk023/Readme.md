[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PKDDvy0P)

# InLabA Quiz

This InLabA quiz consists of two questions that test your understanding of string manipulation. The functions are described in detail below along with example input and expected output.

# Question 1: `check_rotation(s1, s2)`

### Description:
Given two strings, s1 and s2, determine if one string is a rotation of the other. For two strings to be rotationally identical, they must be the same length, and one string should be achievable by shifting the characters in the other string.



### Function Signature:
```python
def check_rotation(s1, s2):
    """
    Given two strings s1 and s2, determine if one string is a rotation of the other.

    """
    pass
```
## Example Usage

```python
>>> check_rotation("abcd", "dabc")
True
>>> check_rotation("python","npytho")
True              
>>> check_rotation("abcd","acbd")      
False                     
```

# Question 2: `compress_string(s)`

### Description:
Write a function `compress_string(s)` that takes a string `s` as input and returns a compressed version of the string. The compressed string should replace consecutive duplicates of a character with the character and the count of the consecutive duplicates. If the compressed string is not smaller than the original string, return the original string.

### Function Signature:
```python
def compress_string(s):
    """
    Write a function `compress_string(s)` that takes a string `s` as input 
    and returns a compressed version of the string. The compressed string should replace consecutive 
    duplicates of a character with the character and the count of the consecutive duplicates. If the compressed 
    string is not smaller than the original string, return the original string.
    """
    pass
```

### Examples:
```python
>>> compress_string("aabcccccaaa")
"a2b1c5a3"

>>> compress_string("abcd")
"abcd"  # Since the compressed string is not smaller, return the original string

>>> compress_string("aabbcc")
"aabbcc"  # The compressed string would be the same length as the original
```

### Notes:
- The compression only occurs when consecutive characters are identical.
- The compressed string should only be returned if it's shorter than the original.

---


1. Implement both functions according to the problem descriptions.
2. Note that the grading will be done with different test cases.

--- 
