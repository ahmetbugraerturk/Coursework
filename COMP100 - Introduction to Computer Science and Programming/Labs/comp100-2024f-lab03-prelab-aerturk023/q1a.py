def approximate_square_root(N, epsilon=1e-10, max_iterations=1000):
    """""
    Approximates square root of given positive number N
    """""
    #Implement here
    if N < 0:
        return None
    if N == 0:
        return 0
    guess = N/2.0
    for i in range(max_iterations+1):
        guess = (guess+(N/guess))/2
        if abs(guess**2-N)<epsilon:
            return guess
    return None