[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/UEmVXlJL)
# InLabA Quiz

This InLabB quiz consists of two questions that test your understanding of string processing. The functions are described in detail below along with example input and expected output.

## Question 1: `first_non_repeating_character(s)`

### Description:
Write a Python function `first_non_repeating_character(s)`to find the first character in a string that appears exactly once (non-repeating character). The goal is to identify its position in the string (its index). If no such character exists, meaning every character repeats at least once, the function should return -1.

### Function Signature:
```python
def first_non_repeating_character(s):
    """
    Given a string s, find the first character that doesn’t repeat in the string and return its index.
    If every character in the string repeats, return -1.

    """
    # Delete the pass and code
    pass
```
### Examples:
```python
>>> first_non_repeating_character("aabbcd")
4

>>> reverse_only_letters("ccoommpp")
-1

>>> reverse_only_letters("python")
0

```

## Question 2: `longest_common_prefix(strs)`

### Description:
Write a Python function `longest_common_prefix(strs)` that takes a string containing three strings seperated by whitespace and returns the longest common prefix among all the strings in the list. If there is no common prefix, return an empty string.
### Function Signature:
```python
def longest_common_prefix(strs):
    """
    Write a Python function longest_common_prefix(strs) that takes a string containing three strings seperated by whitespace
    and returns the longest common prefix among all the strings in the list. 
    If there is no common prefix, return an empty string.
    """
    pass

```
### Examples:
```python
>>> longest_common_prefix("flower flow flight")
"fl"

>>> longest_common_prefix("dog racecar car")
""

>>> longest_common_prefix("interspecies interstellar interstate")
"inters"
```
---

### Instructions:

1. Implement both functions according to the problem descriptions.
2. Note that the grading will be done with different test cases.

--- 
### Note:
You can use string.split() method to seperate the given string, and make sure the list returned has exactly 3 elements, after the verification store each element of the list as w1, w2, w3 = string.split(...)

