def find_primes(start: int, end: int) -> str:
    """
    Returns a string containing all prime numbers within a given range, separated by commas.

    Parameters:
        start (int): The starting integer of the range.
        end (int): The ending integer of the range.

    Returns:
        str: A string of prime numbers within the range, separated by commas.
    """

    primes = ""

    if start < 2:
        start = 2
        
    for i in range(start, end+1):
        isPrime = True
        for j in range(i-2):
            if i%(j+2)==0:
                isPrime = False
                break
        if isPrime:
            primes = primes + str(i) + ", "
    if primes == "":
        return "No prime numbers found"
    else:
        return primes.removesuffix(", ")
            