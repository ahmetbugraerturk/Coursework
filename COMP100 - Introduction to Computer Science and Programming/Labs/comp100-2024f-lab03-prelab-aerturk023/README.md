[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/YN_0Xd8M)
# COMP100 2024F Lab 03: Guess-Check, Approximation, Bisection - Prelab
### Deadline: Friday 10:00 AM, 01 November 2024 

The testcases given are just sample tests, and additional testcases may be used while grading.

## Question 1: Square Root Approximation and Finding Polynomial Roots (100 Points)
 
This question consists of two parts. You will approximate the square root of a given number using approximation and bisection method and then use that function to find real roots of any given second order polynomial function.

## Part A: Approximate Square Root of Given Positive Number (50 Points)

Write a function `approximate_square_root` to approximate the square root of a given number 𝑁
using iterative guess-check and approximation with bisection method without directly using a square root or exponentiation function.

### Inputs:
`N`(float): A *non-negative* number for which to find the square root.

`epsilon`(float, optional): Acceptable tolerance for approximation (default, `1e-10`).

`max_iterations`(float, optional): Acceptable number of iterations for approximation (default, `1000`).

### Outputs:
`guess`(float): An approximation of the square root of N, within the given `epsilon` tolerance.

### Method:
Initialize `guess` to `N / 2.0`.

Approximate the `guess` iteratively until `∣guess^2−𝑁∣<epsilon`.

Return the approximation `guess`. If an approximation is not found within a reasonable number of iterations, return None.

### Example Usage:
`approximate_square_root(9)` Output: `3.0`

`approximate_square_root(2, epsilon=1e-10)` Output: `1.4142135623746899`

`approximate_square_root(-4)` Output: `None`

`approximate_square_root(2, epsilon=1e-20, max_iterations=10)` Output: `None`

## Part B: Finding Roots of Second Order Polynomials (50 Points)
Write a function `find_polynomial_roots` that finds the roots of a quadratic polynomial given by the equation `a⋅x^2+b⋅x+c=0` by using `approximate_square_root` function from Part A and discriminant formula. 

### Inputs:
`a`(float): Coefficient of x^2.

`b`(float): Coefficient of x.

`c`(float): Constant term.

`epsilon`(float, optional): Acceptable tolerance for approximation (default, `1e-10`).

`max_iterations`(float, optional): Acceptable number of iterations for approximation (default, `1000`).

### Outputs:
Returns a tuple containing the roots of the polynomial. If there are no real roots or if the equation is invalid, returns `None`.

### Method:
Check if `a` is zero:

  -If both `a` and `b` are zero, the equation is invalid. Return `None`.

  -If `a` is zero but `b` is not, return the single root calculated using `-c / b` (Since function becomes linear e.g., `bx+c=0`) 
  
  **Important notice:** Even if there is only one root, the function should return the root as a tuple with a single element. So that your outputs should be either `None` or `(-c/b,)` or `(root, root2)` for no valid roots, a single root, and two roots respectively. Do not omit the commas inside the brackets (See example outputs).

If `a` is not zero:

Calculate the `discriminant` using the formula `b^2 - 4ac`.

If the discriminant is less than zero, return `None` indicating no real roots.

Calculate the roots using the quadratic formula:

`root1= (-b + `&#8730;`discriminant) / 2a`, `root2= (-b - `&#8730;`discriminant) / 2a`

You should find the square root of the discriminant with the function `approximate_square_root` that you defined in Part A.

Return the roots as the output.

### Example Usage:
`find_polynomial_roots(1, -3, 2, epsilon=1e-7)` (x^2 - 3x + 2 = 0) Output: `(2.0,1.0)`

`find_polynomial_roots(1, -2, 1)`(x^2 - 2x + 1) Output: `(1.0,1.0)`

`find_polynomial_roots(1, 0, 1)` (x^2+1=0) Output: `None`

`find_polynomial_roots(0, 2, 1)` (2x+1 = 0) Output: `(-0.5,)`