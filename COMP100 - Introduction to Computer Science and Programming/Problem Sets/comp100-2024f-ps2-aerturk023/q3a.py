import additional_functions

def can_allocate_priority_seats(airplane_class: str, class_config: str, heroes: str) -> str:
    """
    Determines if it is possible to seat certain Avengers according to their preference.

    Parameters:
        airplane_class (str): The class of the airplane.
        class_config (str): The current seat configuration for a class section.
        heroes (str): The initials of the Avengers that require seats.

    Validations:
        - If `airplane_class` input is incorrect, return `'Unrecognized class!'`.
        - If `seat_config` does not belong to any of the classes (First, Business, or Economy), return `'Invalid seat configuration!'`.
        - If `seat_config` is correct but has invalid characters, return `'Invalid seat letters!'`.
        - If `airplane_class` and `seat_config` do not match, return `'Mismatch between 'airplane_class' and 'seat_config'!'`.
        - If `heroes` has invalid characters, return `'Unrecognized hero, not allowed to board!'`.

    Returns:
        str: 'Yes, you may board!' if it is possible to seat the Avengers according to their preference, otherwise 'Boarding Denied!'.
    """
    
    if airplane_class != "First" and airplane_class != "Business" and airplane_class != "Economy":
        return 'Unrecognized class!'
    elif additional_functions.indicate_class(class_config)==None:
        return "Invalid seat configuration!"
    elif additional_functions.seat_indices_indicator(class_config)[5]:
        return 'Invalid seat letters!'
    elif additional_functions.indicate_class(class_config)!=airplane_class:
        return "Mismatch between 'airplane_class' and 'seat_config'!"
    for char in heroes:
        if char not in "DTSNBACLH":
            return 'Unrecognized hero, not allowed to board!'
    
    priority = "DTSNBACLH"
    prior_heroes = ""
    
    for char in priority:
        if char in heroes:
            prior_heroes += char*heroes.count(char)
            
    for hero in prior_heroes:
        o_seats = additional_functions.seat_indices_indicator_with_heroes(class_config)[0]
        w, m, a = additional_functions.indices_of_pref_seats(airplane_class)
        match hero:
            case "D":
                inters = additional_functions.find_intersection(a, o_seats)
                class_config = additional_functions.replace_with_index(class_config, inters[0], "D")
            case "T":
                inters = additional_functions.find_intersection(w, o_seats)
                if not (airplane_class == "First" and len(inters)>0):
                    return 'Boarding Denied!'
            case "S":
                inters = additional_functions.find_intersection(m, o_seats)
                if len(inters)<=0:
                    return 'Boarding Denied!'
            case "N":
                if "C" in heroes:
                    inters = additional_functions.find_intersection(w, o_seats)
                    if not ((inters[0] == 0 and 1 in o_seats) or (inters[0] != 0 and inters[0]-1 in o_seats) or (len(inters) == 2 and inters[1]-1 in o_seats)):
                        return 'Boarding Denied!'
                else:
                    inters = additional_functions.find_intersection(w, o_seats)
                    if len(inters)<=0:
                        return 'Boarding Denied!'
            case "B":
                inters = additional_functions.find_intersection(a, o_seats)
                if len(inters)<=0:
                    return 'Boarding Denied!'
            case "A":
                intersM = additional_functions.find_intersection(m, o_seats)
                intersA = additional_functions.find_intersection(a, o_seats)
                if intersM == () and intersA == ():
                    return 'Boarding Denied!'
            case "C":
                if "N" not in heroes:
                    if o_seats == ():
                        return 'Boarding Denied!'
            case "L":
                if "A" not in heroes:
                    if o_seats == ():
                        return 'Boarding Denied!'
                else:
                    return 'Boarding Denied!'
            case "H":
                if o_seats == ():
                    return 'Boarding Denied!'
    return "Yes, you may board!"

        
        
        
        