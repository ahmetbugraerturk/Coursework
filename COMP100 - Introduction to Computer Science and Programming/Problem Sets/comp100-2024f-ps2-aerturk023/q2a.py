import q1a
import additional_functions

def can_board_with_preference(total_avengers: int, seat_config: str, preference: str) -> str:
    """
    Determines if it is possible to seat certain Avengers according to their preference.

    Parameters:
        total_avengers (int): The total number of Avengers to be seated.
        seat_config (str): The seat configuration as a string.
        preference (str): The preference of the Avengers as a string.

    Validations:
        - If `seat_config` does not belong to any of the classes (First, Business, or Economy), return `'Invalid seat configuration!'`.
        - If `seat_config` is correct but has invalid characters, return `'Invalid seat letters!'`.
        - If `preference` has invalid characters, return `'Invalid seat preference!'`.

    Returns:
        str: 'Yes, you may board!' if it is possible to seat the Avengers according to their preference, otherwise 'Boarding Denied!'.
    """

    fl_class = additional_functions.indicate_class(seat_config)
    o_seats = additional_functions.seat_indices_indicator(seat_config)[0]
    can_as = q1a.can_assemble(total_avengers, seat_config)
    
    if can_as == "Yes, you may board!":
        w, m, a = additional_functions.indices_of_pref_seats(fl_class)
        match preference:
            case "W":
                if len(additional_functions.find_intersection(w, o_seats))<total_avengers:
                    return 'Boarding Denied!'
                else:
                    return 'Yes, you may board!'
            case "M":
                if len(additional_functions.find_intersection(m, o_seats))<total_avengers:
                    return 'Boarding Denied!'
                else:
                    return 'Yes, you may board!'
            case "A":
                if len(additional_functions.find_intersection(a, o_seats))<total_avengers:
                    return 'Boarding Denied!'
                else:
                    return 'Yes, you may board!'
            case "D":
                if len(additional_functions.find_intersection(a, o_seats))<total_avengers:
                    return 'Boarding Denied!'
                else:
                    return 'Yes, you may board!'
            case _:
                return 'Invalid seat preference!'
    else:
        return can_as




