[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Jyo7fSui)
# COMP100 2024F Lab 06: Lists and Tuples - Prelab
### Deadline Friday, November 22, 2024 10:00 AM

The testcases given are just sample tests, and additional testcases may be used while grading. You **CANNOT** use dictionaries or sets for any of the problems.

## Question 1: Sublist Finder (5 Points)

Write a function `is_sublist(list1, list2)` that takes two lists: `list1` and `list2`. Check if `list2` is a sublist of `list1`. Return `True` if `list2` is a sublist, and `False` otherwise.

### Example Usage:

```python
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4]
print(is_sublist(list1, list2)) # Expected Output: True
```

## Question 2: Generate Pairs (10 Points)

Write a function `generate_pairs(list1)` that takes a list of unique integers and generates a list of all possible **unordered pairs** from the list as tuples. When we say **unordered pairs**, it means (1, 2) and (2, 1) are same; no need to add (2, 1) again if you have added (1, 2).

### Example Usage:

```python
list1 = [1, 2, 3]
print(generate_pairs(list1)) # Expected Output: [(1, 2), (1, 3), (2, 3)]
```

## Question 3: Cyclic Rotation (15 Points)

Write a function `list_rotate(list1, k)` that takes a list and an integer `k`. If `k > 0`, rotate to the right; if `k < 0`, rotate to the left.

### Example Usage:

```python
list1 = [10, 20, 30, 40, 50]
k = 2
print(list_rotate(list1, k)) # Expected Output: [40, 50, 10, 20, 30]
```

```python
list1 = [10, 20, 30, 40, 50]
k = -2
print(list_rotate(list1, k)) # Expected Output: [30, 40, 50, 10, 20]
```

## Question 4: Zig-Zag Merge (15 Points)

Write a function `zigzag_merge(list1, list2)`, that takes two lists of integers, merges them into a single list in a **zig-zag** manner. If one list is longer, append the remaining elements at the end.

### Example Usage:

```python
list1 = [1, 2, 3]
list2 = [10, 20, 30, 40, 50]
print(zigzag_merge(list1, list2)) # Expected Output: [1, 10, 2, 20, 3, 30, 40, 50]
```

## Question 5: Longest Consecutive Subsequence (15 Points)

Write a function `longest_consecutive_subsequence_len(list1)` that takes a list of integers and finds the length of the longest subsequence of consecutive numbers (not necessarily contiguous).

### Example Usage:

```python
list1 = [10, 4, 20, 1, 3, 2, 5]
print(longest_consecutive_subsequence_len(list1)) # Expected Output: 5
# Explanation: The longest consecutive sequence is [1, 2, 3, 4, 5].
```

## Question 6: Element Frequency (20 Points)

Write a function `element_frequency(list1)` to count frequency of each element by replacing consecutive repeated elements with tuples of the elements and its count.

### Example Usage:

```python
list1 = [1, 1, 2, 2, 2, 3, 4, 4]
print(element_frequency(list1)) # Expected Output: [(1, 2), (2, 3), (3, 1), (4, 2)]
```

## Question 7: Matrix Manipulation Using Lists of Tuples (20 Points)

Write a function `transpose_tuples(matrix)` that takes a `matrix` represented as a list of tuples and transposes the `matrix`.

A matrix is a 2D collection of numbers organized as `N` rows and `M` columns.

```
1  2  3
4  5  6
7  8  9
10 11 12

This matrix has N = 4 rows and M = 3 columns. Transpose of this matrix will transform into a new matrix of M rows and N columns as follows:

1  4  7  10
2  5  8  11
3  6  9  12
```

Note that the rows of the original matrix have become columns of the Transpose matrix, and the columns have become rows.

### Example Usage:

```python
matrix = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(transpose_tuples(matrix)) # Expected Output: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

```python
matrix = [(1, 2), (3, 4), (5, 6)]
print(transpose_tuples(matrix)) # Expected Output: [(1, 3, 5), (2, 4, 6)]
```
