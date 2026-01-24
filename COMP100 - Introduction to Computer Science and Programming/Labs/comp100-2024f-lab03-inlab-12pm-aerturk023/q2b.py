from q2a import approximate_slope

def bisection_method_for_extrema(a=1, b=12, epsilon=1e-8):
    """
    This function should use bisection method to find x where the slope is approximately 0
    """
    
    neg = a
    pos = b
    extremumX = (a+b)/2
    while abs(approximate_slope(extremumX))>epsilon:
        if approximate_slope(extremumX)<0:
            neg = extremumX
        else:
            pos = extremumX
        extremumX = (neg+pos)/2
    return extremumX

