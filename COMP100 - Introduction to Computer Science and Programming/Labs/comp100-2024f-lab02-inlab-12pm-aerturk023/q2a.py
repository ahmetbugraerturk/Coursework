def weighted_sum_of_digits(n):
    """
    Calculates the weighted sum of digits for the given positive integer n.

    Parameters:
        n (int): A positive integer whose digits are weighted and summed.

    Returns:
        int: The weighted sum of the digits of n.
    """

    # TODO: Convert negative numbers to positive
    if n < 0:
        n = -n

    # TODO: Initialize total and weight
    total = 0
    weightCalc = 10
    maxWeight=1

    # TODO: Utilize a loop to calculate the weighted sum of digits
    while n//weightCalc>=1:
        weightCalc *= 10
        maxWeight+=1
    while maxWeight>=0:
        wNumber = n//(weightCalc/10)
        total += wNumber*maxWeight
        n -= wNumber*(weightCalc/10)
        maxWeight -= 1
        weightCalc /= 10
    
    return total

    # TODO: Return the total
