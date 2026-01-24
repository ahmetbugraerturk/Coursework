from math import pi # You should use only for comparison with the approximated value

def approximate_pi(max_iterations=100000, epsilon=1e-4):
    """
    This functions approximates pi to the error rate of given epsilon value
    """
    
    app_piover4 = 0
    
    for i in range(max_iterations):
        if abs(pi-4*app_piover4)<=epsilon:
            return 4*app_piover4
        app_piover4 += ((-1)**i)/(2*i+1)
    
    return None