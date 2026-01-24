[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/fDyc8MGj)
# COMP100 2024F Lab 10: Object Oriented Programming - In Lab 12:00 PM
### Deadline Friday, December 20, 2024 01:40 PM

Although sample test cases are provided, be aware that additional test cases may be used during grading.

## Overview

In this assignment, you will implement two classes:
1. **Coordinate**: A simple class to represent a point in 2D space.  
2. **ComplexNumber**: A class that *inherits from `Coordinate`* and interprets the `x` and `y` values as the real and imaginary parts of a complex number.

*No knowledge of complex numbers is required to implement this assignment.*

## What Is a Complex Number?

A **complex number** is a number that can be expressed as:

$$ z = a + bi $$

where:
- $a$ (the real part) and $b$ (the imaginary part) are real numbers.
- $i$ is the imaginary unit, defined by $i^2 = -1$.

For example, $3 + 4i$:
- Real part: $3$
- Imaginary part: $4$

## Coordinate Class

You will first implement a `Coordinate` class to represent a point $(x, y)$ in 2D space. This class will:

- Store two class members: `x` and `y`.
- Implement a `__str__` method to return a string like: `"<x, y>"`.
- Implement a `distance` method that, given another `Coordinate`, returns the distance between the two points. The distance between $(x_1, y_1)$ and $(x_2, y_2)$ is:
  
$$
\text{distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
$$

## ComplexNumber Class (Inherits from Coordinate)

`ComplexNumber` will inherit from `Coordinate`. In this class, we will treat:

- `x` from `Coordinate` as the real part ($a$).
- `y` from `Coordinate` as the imaginary part ($b$).

**No separate attributes are needed in `ComplexNumber`**, it reuses `x` and `y` from `Coordinate`.

### Operations on Complex Numbers

1. **Addition:**
   If $z_1 = a + bi$ and $z_2 = c + di$, then:

$$
z_1 + z_2 = (a + c) + (b + d)i
$$

2. **Subtraction:**

$$
z_1 - z_2 = (a - c) + (b - d)i
$$

3. **Multiplication:**

$$
z_1 \times z_2 = (ac - bd) + (ad + bc)i
$$

4. **Division:**

$$
\frac{z_1}{z_2} = \frac{(a + bi)(c - di)}{(c^2 + d^2)} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}
$$

5. **Equality (eq):**  
   $z_1 = z_2$ if and only if $a = c$ and $b = d$.

### String Representation for ComplexNumber

For `ComplexNumber`, the `__str__` method should return something like `"a + bi"` or `"a - bi"` depending on the sign of $b$.

**Note:** Since `ComplexNumber` inherits from `Coordinate`, it will have `x` and `y` available. Just remember:
- Use `x` as the real part (`a`).
- Use `y` as the imaginary part (`b`).

### Important Note

**You are not allowed to use Python's built-in `complex` type or related functions.** Implement the arithmetic yourself using the provided formulas.

## Assignment Steps

1. **Implement `Coordinate` Class:**
   - Attributes: `x`, `y`.
   - `__str__(self)`: returns `"Coordinate(x, y)"`.
   - `distance(self, other)`: returns the Euclidean distance between this coordinate and `other`.

2. **Implement `ComplexNumber` Class (Inherits from `Coordinate`):**
   - Use `super().__init__(a, b)` to initialize the complex number (real part `a`, imaginary part `b`).
   - `__add__(self, other)`: $(a + c) + (b + d)i$
   - `__sub__(self, other)`: $(a - c) + (b - d)i$
   - `__mul__(self, other)`: $(ac - bd) + (ad + bc)i$
   - `__truediv__(self, other)`: Use the division formula.
   - `__eq__(self, other)`: Checks if $a = c$ and $b = d$.
   - `__str__(self)`: Returns `"a + bi"` or `"a - bi"`.

**Remember:** No built-in `complex` utilities allowed.

## Example

If:

$$
z_1 = 3 + 4i
$$

$$
z_2 = 1 - 2i
$$

- $z_1 + z_2 = (3+1) + (4-2)i = 4 + 2i$
- $z_1 \times z_2 = (3 \times 1 - 4 \times (-2)) + (3 \times (-2) + 4 \times 1)i = (3+8) + (-6+4)i = 11 - 2i$

Check each operation manually and ensure your code matches these results.
