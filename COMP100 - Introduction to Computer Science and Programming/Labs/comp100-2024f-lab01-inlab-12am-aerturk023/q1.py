def interest_calculator(total_money, interest_rate, years):
    """
    Write a function that takes total money,
    interest rate, and years as input then using the compound
    interest formula.

    """

    # Your code goes here, delete 'pass' !
    A = total_money * (1 + (interest_rate / 100))**years
    return A