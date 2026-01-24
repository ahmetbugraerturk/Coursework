[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/1g37A6et)

# Lab 01 Functions and Variables Instructions

Welcome to the quiz! Below, you will find the description of two questions. Each requires you to write a Python function according to the specifications provided.

## Question 1: Compound Interest Calculator

### Task:
You need to write a function that calculates the future value of a given investment or loan, applying the **compound interest formula**. 

### Function Definition:
```python
def interest_calculator(total_money, interest_rate, years):
    """
    Write a function that takes the total money, 
    interest rate, and years as input, then calculates 
    the future value using the compound interest formula.
    """
    pass
```

### Formula:
The formula for compound interest is:

A = P * (1 + (r / 100))^t

Where:
- A is the amount of money accumulated after t years, including interest.
- P is the initial amount (the principal or `total_money`).
- r is the annual interest rate (percentage, `interest_rate`).
- t is the number of years (`years`).

### Requirements:
- You need to implement the function `interest_calculator` that takes `total_money`, `interest_rate`, and `years` as inputs.
- The function should return the final amount A after applying the compound interest.

---

## Question 2: Triangle Area Calculator

### Task:
You need to write a function that calculates the **area** of a triangle based on the lengths of its sides using **Heron’s formula**.

### Function Definition:
```python
def triangle_area(a, b, c):
    """
    Parameters:
    ----------
    a, b, c : float
        The side lengths of the triangle.

    Returns:
    -------
    area : float
        The area squared of the triangle calculated using Heron's formula.
    
    """
    # Your code goes here
    pass
```

### Formula:
The formula for the **perimeter** of a triangle is straightforward:


Perimeter = a + b + c

For the **area**, we will use **Heron's formula**. First, calculate the **semi-perimeter** s:


s = (a + b + c) / 2


Then, the **area squared** is given by:


(Area)^2 = s * (s - a) * (s - b) * (s - c)

Take the square root to get the area

### Requirements:
- You need to implement the function `triangle_properties` that takes the side lengths `a`, `b`, and `c` as inputs.
- The function should return **area**.
- **Important**: Ensure you calculate the **area squared** using Heron’s formula before taking the square root to obtain the actual area.

---


Good luck!