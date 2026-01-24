[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/bL-yxdZW)
# COMP100 2024F Lab 03: Guess-Check, Approximation, Bisection - Lab A: 12PM
### Deadline: Friday 13:40 PM, 01 November 2024 

The testcases given are just sample tests, and additional testcases may be used while grading.

## Question 1: $`\pi`$ Approximation (40 Points)
 
Write a function `approximate_pi` to approximate $`\pi`$ number using iterative approximation and Leibniz Formula.

### Leibniz Formula for $`\pi`$

The Leibniz formula for $`\pi`$ is given by the infinite series:

$`
\frac{\pi}{4} = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n + 1}
`$

### Explanation

- The formula expresses $`\pi`$ as an alternating series, where:
  - `n` is a non-negative integer.
  - The term $`\frac{(-1)^n}{2n + 1}`$ alternates signs.
  - The sum converges to $`\pi`$ as `n` approaches infinity.

### Approximation

To approximate $`\pi`$ using this formula, you can compute the sum up to a certain number of terms `N`:

$`
\pi \approx 4 \sum_{n=0}^{N} \frac{(-1)^n}{2n + 1}
`$

As `N` increases, the approximation becomes more accurate.

### Inputs:

`epsilon`(float, optional): Acceptable tolerance for approximation (default, `1e-4`).

`max_iterations`(float, optional): Acceptable number of iterations for approximation (default, `100000`).

### Outputs:
Function should return the approximated $`\pi`$ value (float) if approximation is successful within the given tolerance epsilon.

If approximation is not successful, it should return None.

### Method:
Initialize `pi_approximation` to `0`.

Iteratively add the next term in Leibniz Formula until you reach `max_iterations` or a convergence to $`\pi`$ with an error rate smaller than `epsilon`.

`pi` from math module is imported at the start of the code to help you compare your approximated value with built-in $`\pi`$ value. You can use it by simply writing `pi` in your code (e.g., `print(pi)` #Output: `3.141592653589793`). You should __only__ use it for comparison with your approximated value.

Function should return the $`\pi`$ value (float) if difference of your approximation with the built-in $`\pi`$ value is less than `epsilon`.

Function should return None if difference of your approximation with the built-in $`\pi`$ value is higher than`epsilon` within `max_iterations`.

### Example Usage:
`print(approximate_pi())` Output: `3.140592653839794`

`print(approximate_pi(epsilon=1e-6))` Output: `None`

Output below took ~45 seconds in my environment to approximate $`\pi`$ to the 8th decimal point with below 10 billion iterations. You can try to find out how accurate you can approximate $`\pi`$ in a reasonable time with your function as a fun exercise.

`print(approximate_pi(max_iterations=10000000000, epsilon=1e-8))` Output: `3.141592663589793`

## Question 2: Extrema Finding with Bisection Method  (60 Points)

Write functions named `approximate_slope` and `bisection_method_for_extrema` to find extremum point of the function 
$`
x^3 - 6x^2 - 4x + 12
`$
within the interval [1,12]. The mathematical function is defined at the beginning of `q2a` as python function for you. You should not change it.

## Part A: Slope Approximation (0 Points)
In the `q2a` `approximate_slope` function is defined and implemented. This function uses finite central difference approximation for slope approximation that uses a small difference (h) to approximate the first derivative of the function 𝑓(𝑥) around point 𝑥. You are not supposed to write anything inside `q2a`, functions implemented here should be used in `q2b`.

$`f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}`$

### Inputs:
`x`(float): Input of the math function.

`h`(float, optional): Small positive value (step size) (default, `0.01`).

### Outputs:
Returns the approximated slope of the function `f'(x)` (float) around the point `x`.

### Method:
The function uses the central difference approximation formula for the first derivative, then returns the calculated slope.

### Example Usage:
`approximate_slope(1, h=0.05)`  Output: `-12.997500000000013`

`approximate_slope(6):` Output: `32.0001000000012`

## Part B: Extremum Finding with Bisection Method (60 Points)
You should write a function `bisection_method_for_extrema` that applies the Bisection Method to locate an extremum in the interval [a, b] by finding a point where the slope is approximately zero. The method iteratively narrows down the interval until it meets the tolerance `epsilon`. 

To get things easier, the given integral ([1, 12]) is guaranteed to have 1 extremum point so that you will not need to check extra cases.

### Inputs:
`a` (float, optional): Left endpoint of the interval (default is 1).

`b` (float, optional): Right endpoint of the interval (default is 12).

`epsilon` (float, optional): Tolerance for approximation (default is 1e-8).

### Outputs:
Returns the approximate x-coordinate (float) of the extremum where the slope is close to zero.

### Method:
You should find the slope of the function at the middle point of the interval by using `approximate_slope(midpoint)` where `midpoint` is simply the middle point of the interval [a, b] as the name suggests.

__For second order polynomials, if there's an extremum between two points, their slopes must have opposite signs: one increasing (positive) and one decreasing (negative), indicating a zero-crossing slope between them. This is generally not true for third order or more, but in our case, it holds within the given interval. Therefore, we will assume this is also right for our function.__

So, you should check if the slope at the *left* endpoint `a` has opposite sign with the slope at the `midpoint`:

-If they have opposite signs, your current `midpoint` should be assigned as your new *right* endpoint value `b` since we now know that there is an extremum point between `a` and `midpoint` for sure.

-If they do not have opposite signs, your current `midpoint` should be assigned as your new *left* endpoint value `a` since we now know that there is not an extremum point between `a` and `midpoint` for sure.

By following these steps iteratively, interval is narrowed down at each step to eventually become the extremum point.

When `approximate_slope(midpoint)`<=`epsilon` is provided, function should return the `midpoint`.


### Example Usage:
`extremum_x = bisection_method_for_extrema()`

`extremum_y = f(extremum_x)`

`print("Approximate extremum at x =", extremum_x, "with f(x) =", extremum_y)`

Output: `Approximate extremum at x = 4.3093938594684005 with f(x) = -36.633611485063156`

__Disclaimer:__ Your function should only return x-coordinate value as seen in the first line in the example, other lines are just for visualization and clarification.
