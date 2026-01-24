import random

def estimate_odd_divisible_probability(n_trials, divisor):
    """
    Estimates the probability that the sum of two dice rolls is an odd number divisible by a given odd divisor.

    Parameters:
        n_trials (int): The number of trials to simulate.
        divisor (int): The odd divisor to check divisibility in the sum (must be an odd number).

    Returns:
        float: The estimated probability that the sum of two dice rolls results in an odd number divisible by `divisor`.
    """
    spec_cond = 0

    for i in range(n_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if (dice1+dice2)%2==1 and (dice1+dice2)%divisor==0:
            spec_cond += 1
            
    return spec_cond/n_trials
