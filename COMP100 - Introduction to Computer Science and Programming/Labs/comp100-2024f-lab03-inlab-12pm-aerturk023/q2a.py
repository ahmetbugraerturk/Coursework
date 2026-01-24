"""
YOU SHOULD NOT CHANGE ANYTHING IN THIS CODE
"""
def f(x):
    """
    Function to find the extremum of, DO NOT CHANGE anything here
    """
    return x**3 - 6*x**2 -4*x + 12

def approximate_slope(x, h=0.01):
     """
     This function should return the approximation of the first derivative of f(x) at x, using the given formula,
     DO NOT CHANGE ANYTHING HERE
     """
     return (f(x + h) - f(x - h)) / (2 * h)
