import additional_functions

def can_assemble(total_avengers: int, seat_config: str) -> str:
    """
    Determines if it is possible to seat all the Avengers in their designated seats.

    Parameters:
        total_avengers (int): The total number of Avengers to be seated.
        seat_config (str): The seat configuration as a string.

    Validations:
        - If `seat_config` does not belong to any of the classes (First, Business, or Economy), return `'Invalid seat configuration!'`.
        - If `seat_config` is correct but has invalid characters, return `'Invalid seat letters!'`.

    Returns:
        str: 'Yes, you may board!' if it is possible to seat all the Avengers, otherwise 'Boarding Denied!'.
    """
    
    seats = additional_functions.seat_indices_indicator(seat_config)
    fl_class = additional_functions.indicate_class(seat_config)
    
    if fl_class!=None:
        if seats[5]:
            return "Invalid seat letters!"
        else:
            if len(seats[0]) < total_avengers:
                return "Boarding Denied!"
            else:
                return "Yes, you may board!"
    else:
        return 'Invalid seat configuration!'
        
    
    
    
        
        
        
        
        
        