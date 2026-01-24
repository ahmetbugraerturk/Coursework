from q2a import weighted_sum_of_digits


def repeated_weighted_digit_sum(n):
    """
    Repeatedly calculates the weighted sum of digits until a single-digit number is obtained.

    Parameters:
        n (int): A positive integer whose weighted sum of digits is repeatedly calculated.

    Returns:
        int: The single-digit result after repeatedly calculating the weighted sum.
    """

    # TODO: Convert negative numbers to positive
    if n < 0:
        n = -n

    # TODO: Utilize a loop to repeatedly calculate the weighted sum of digits
    while n // 10 >= 1:
        n = int(weighted_sum_of_digits(n))
    
    return n
        
    # TODO: Return the single-digit result
