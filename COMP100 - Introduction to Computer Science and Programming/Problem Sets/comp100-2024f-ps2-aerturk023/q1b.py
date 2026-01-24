import q1a

def show_allocated_seats(total_avengers: int, seat_config: str) -> str:
    """
    Determines the new seat configuration after seating the Avengers.

    Parameters:
        total_avengers (int): The total number of Avengers to be seated.
        seat_config (str): The seat configuration as a string.

    Validations:
        - If `seat_config` does not belong to any of the classes (First, Business, or Economy), return `'Invalid seat configuration!'`.
        - If `seat_config` is correct but has invalid characters, return `'Invalid seat letters!'`.

    Returns:
        str: The new seat configuration after seating the Avengers or 'Boarding Denied!' if not possible.
    """
    can_as = q1a.can_assemble(total_avengers, seat_config)
    if can_as=="Yes, you may board!":
        return seat_config.replace("O", "H", total_avengers)
    else:
        return can_as
