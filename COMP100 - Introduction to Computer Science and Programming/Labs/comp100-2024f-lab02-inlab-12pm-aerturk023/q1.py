def is_leap_year(year):
    """
    This function checks if a year is a leap year or not.

    Parameters:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """

    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False