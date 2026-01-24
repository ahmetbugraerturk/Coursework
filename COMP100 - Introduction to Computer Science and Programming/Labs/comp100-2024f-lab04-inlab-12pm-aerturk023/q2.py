import random

def estimate_e(n_trials):
    """
    Estimates the value of the mathematical constant e using random numbers.

    Parameters:
        n_trials (int): The number of trials to simulate.

    Returns:
        float: The estimated value of e.
    """
    
    sums = 0
    need = 0
    sumsis1 = 0
    needs = 0
    while sumsis1 < n_trials:
        sums += random.random()
        need += 1
        if sums>=1:
            needs += need
            need = 0
            sumsis1 += 1
            sums = 0

        
    return (needs/sumsis1)

print(estimate_e(10000))  # Output should be 2.7159
print(estimate_e(5000))   # Output should be 2.727