[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/VCJnxiYa)
# COMP100 2024F Lab 04 InLab 12 PM:

## Deadline: Friday, 8 November 2024, 13:40 AM

The test cases given are just sample tests, and additional test cases may be used while grading.

# Question 1: Estimating the Probability of an Odd Sum Divisible by a Given Odd Number (50 Points)

Write a function `estimate_odd_divisible_probability` to estimate the probability that the sum of two six-sided dice rolls is an odd number divisible by a given odd `divisor`.

### Concept for Estimating Odd Sum Divisible by Divisor

Estimate the probability that the sum of two dice rolls meets specific conditions: being odd and divisible by a given odd divisor. Run the simulation over multiple trials to obtain a probability.

### Parameters:

- `n_trials` (int): The number of trials to simulate.
- `divisor` (int): The odd divisor to check for divisibility in the sum.

### Returns:

- `probability` (float): The estimated probability that the sum of two dice rolls results in an odd number divisible by `divisor`.

### Requirements and Restrictions

- **Random Module**: Use Python’s built-in `random` module for generating random numbers between 1 and 6.
- Do not use lists, dictionaries, sets, or any external libraries.

### Testing Hint

- If you want to test your function with consistent results, you can set a random seed before running your trials by using `random.seed(1)`.

### Example Usage:

```
print(estimate_odd_divisible_probability(10000, 3))  # Output should be 0.1613
print(estimate_odd_divisible_probability(5000, 5))   # Output should be 0.1138
```

# COMP100 2024F Lab 05 InLab 10 AM:

## Deadline: Friday, 15 November 2024, 11:40 AM

The test cases given are just sample tests, and additional test cases may be used while grading.

# Question 2: Estimating the Value of \( e \) Using Random Numbers (50 Points)

Write a function `estimate_e` to estimate the value of the mathematical constant \( e \) using a random simulation method.

### Concept

To estimate \( e \) using a probability-based approach:
1. Generate random numbers between 0 and 1, adding each to a running total.
2. Count how many random numbers are needed until the sum exceeds 1.
3. Repeat this process for multiple trials, then calculate the average count of numbers needed. 

The formula for this approximation is:

$$
e \approx \frac{\text{Total count of all numbers generated}}{n}
$$

where \( n_trials \) is the number of trials. This average approximates the value of \( e \).

### Parameters:

- `n_trials` (int): The number of trials to simulate.

### Returns:

- `float`: An estimated value of \( e \).

### Requirements and Restrictions

- **Random Module**: Use Python’s built-in `random` module for generating random numbers between 0 and 1.
- Do not use lists, dictionaries, sets, or any external libraries.

### Testing Hint

- If you want to test your function with consistent results, you can set a random seed before running your trials by using `random.seed(1)`.

### Example Usage:

```
print(estimate_e(10000))  # Output should be 2.7159
print(estimate_e(5000))   # Output should be 2.727
```