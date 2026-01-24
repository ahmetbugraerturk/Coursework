import random

def estimate_joint_probability(num_trials, first_target_sum, second_target_sum):
    """
    Estimates the probability of rolling a target sum (e.g., 7 or 11) with two six-sided dice,
    given that both dice show different numbers.

    Parameters:
        num_trials (int): The number of trials to run in the simulation.
        first_target_sum (int): The first target sum (e.g., 7).
        second_target_sum (int): The second target sum (e.g., 11).

    Returns:
        float: The estimated probability of the event.
    """
    
    firsProb = 0
    secondProb = 0

    if num_trials==0:
        return 0
    for i in range(num_trials):
        firstDice = random.randint(1,6)
        secondDice = random.randint(1,6)
        if firstDice != secondDice:
            if firstDice+secondDice == first_target_sum:
                firsProb += 1
            elif firstDice+secondDice == second_target_sum:
                secondProb += 1
    return (firsProb+secondProb)/num_trials
