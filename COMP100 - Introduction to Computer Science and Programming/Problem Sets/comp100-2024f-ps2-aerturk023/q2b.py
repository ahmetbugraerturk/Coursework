import additional_functions
import q2a

def show_preferred_seats(total_avengers: int, seat_config: str, preference: str) -> str:
    """
    Determines the new seat configuration after seating the Avengers according to their preference.

    Parameters:
        total_avengers (int): The total number of Avengers to be seated.
        seat_config (str): The seat configuration as a string.
        preference (str): The preference of the Avengers as a string.

    Validations:
        - If `seat_config` does not belong to any of the classes (First, Business, or Economy), return `'Invalid seat configuration!'`.
        - If `seat_config` is correct but has invalid characters, return `'Invalid seat letters!'`.
        - If `preference` has invalid characters, return `'Invalid seat preference!'`.

    Returns:
        str: The new seat configuration after seating the Avengers or 'Boarding Denied!' if not possible.
    """

    fl_class = additional_functions.indicate_class(seat_config)
    o_seats = additional_functions.seat_indices_indicator(seat_config)[0]
    can_as = q2a.can_board_with_preference(total_avengers, seat_config, preference)
    
    if can_as == "Yes, you may board!":
        w, m, a = additional_functions.indices_of_pref_seats(fl_class)
        match preference:
            case "W":
                inters = additional_functions.find_intersection(w, o_seats)
                for i in range(total_avengers):
                    seat_config = additional_functions.replace_with_index(seat_config, inters[i], "H")
            case "M":
                inters = additional_functions.find_intersection(m, o_seats)
                for i in range(total_avengers):
                    seat_config = additional_functions.replace_with_index(seat_config, inters[i], "H")
            case "A":
                inters = additional_functions.find_intersection(a, o_seats)
                for i in range(total_avengers):
                    seat_config = additional_functions.replace_with_index(seat_config, inters[i], "H")
            case "D":
                inters = additional_functions.find_intersection(a, o_seats)
                for i in range(total_avengers):
                    seat_config = additional_functions.replace_with_index(seat_config, inters[i], "D")
            case _:
                return 'Invalid seat preference!'
    else:
        return can_as
    return seat_config

