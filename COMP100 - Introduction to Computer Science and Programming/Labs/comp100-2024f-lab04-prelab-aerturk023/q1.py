import random

def estimate_pi_dart_game(num_darts, radius):
    """
    Estimates the value of pi through a dart-throwing game.

    Parameters:
        num_darts (int): The number of darts to throw in the game.
        radius (float): The radius of the circle (target) for the dart game.

    Returns:
        float: The estimated value of pi based on the dart-throwing simulation.
    """
    
    inCircle = 0
    for i in range(num_darts):
        if random.uniform(-radius,radius)**2 + random.uniform(-radius,radius)**2 <= radius**2:
            inCircle += 1
    return (inCircle/num_darts)*4