[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/s41T0i2N)
# COMP100 2024F Lab 02: Branching, String Manipulation, and Loops - In Lab 12:00 PM
### Deadline Friday, October 25, 2024 01:40 PM

The testcases given are just sample tests, and additional testcases may be used while grading.

## Question 1: Leap Year Checker (35 Points)

Write a function named `is_leap_year` that takes an integer representing a year and returns `True` if it is a leap year, and `False` otherwise.

### Rules for a leap year:

- The year is evenly divisble by 4;
- If the year can be evenly divided by 100, it is NOT a leap year, unless;
- The year is also evenly divisible by 400. Then it is a leap year.

### Example Usage:

```python
print(is_leap_year(2000))  # Output: True
print(is_leap_year(1999))  # Output: False
print(is_leap_year(1900))  # Output: False
```

## Question 2: Weighted Digit Sum (65 Points)

You are tasked to write a **weighted sum of digits** for a given number `n`. The rightmost digit of the number has a weight 1, the second-rightmost digit has a weight of 2, and so on. Your task is split in two parts:

### Part A: Weighted Sum of Digits (40 Points)

Write a function `weighted_sum_of_digits` that takes a positive integer `n` and returns the **weighted sum of its digits**. Each digit of `n` is multiplied by its respective weight: the rightmost digit has a weight of 1, the second-rightmost has a weight of 2, and so on.

#### Requirements:
- You **cannot** convert the number into a string. Otherwise, your solution will not be accepted and you will be graded 0.
- If `n` is a negative number, convert it to positive before processing.

#### Example Usage:

```python
print(weighted_sum_of_digits(987))   # Output: 50  # (7*1) + (8*2) + (9*3) = 7 + 16 + 27 = 50
print(weighted_sum_of_digits(-456))  # Output: 28  # (6*1) + (5*2) + (4*3) = 6 + 10 + 12 = 28
```

### Part B: Repeated Weighted Sum to Single Digit (25 Points)

Write a function `repeated_weighted_digit_sum` that takes an integer `n` and repeatedly calculates the **weighted sum of digits** (using the `weighted_sum_of_digits` function from Part A) until the result is a single-digit number.

#### Requirements:
- You **must** use the `weighted_digit_sum` function from Part A to calculate the weighted sum.
- If `n` is negative, convert it to positive before processing.
- You are **not** allowed to directly implement the digit summing logic inside this function.

#### Example Usage:

```python
print(repeated_weighted_digit_sum(987))  # Output: 5
```

#### Explanation:
For `n = 987`:
1. Apply weights: (7 * 1) + (8 * 2) + (9 * 3) = 50.
2. Sum the digits of 50: (0 * 1) + (5 * 2) = 10.
4. Sum the digits of 10: (0 * 1) + (1 * 2) = 2.
3. Since 2 is a single-digit number, the function returns 2.
