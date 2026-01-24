def weekday_message(day: int, has_class: bool = False, has_event: bool = False) -> str:
    """
    Returns a custom message for each day of the week based on the given integer.

    Parameters:
        day (int): An integer representing the day of the week (1 for Monday, 7 for Sunday).
        has_class (bool): Specifies if there is a class on the selected day.
        has_event (bool): Specifies if there is a special event on the weekend (Saturday or Sunday).

    Returns:
        str: A custom message for the day, or "Invalid day" if the input is outside the range 1-7.
    """
    
    match day:
        case 1:
            if has_class:
                return 'Monday: Start of a new week! Wake-up alarm set for 6:00 AM.'
            else:
                return 'Monday: Start of a new week! Wake-up alarm set for 7:00 AM.'
        case 2:
            if has_class:
                return 'Tuesday: Keep at it! Wake-up alarm set for 6:00 AM.'
            else:
                return 'Tuesday: Keep at it! Wake-up alarm set for 7:00 AM.'
        case 3:
            if has_class:
                return 'Wednesday: Halfway there! Wake-up alarm set for 6:00 AM.'
            else:
                return 'Wednesday: Halfway there! Wake-up alarm set for 7:00 AM.'
        case 4:
            if has_class:
                return 'Thursday: Almost Friday! Wake-up alarm set for 6:00 AM.'
            else:
                return 'Thursday: Almost Friday! Wake-up alarm set for 7:00 AM.'
        case 5:
            if has_class:
                return 'Friday: Time to relax! Wake-up alarm set for 6:00 AM.'
            else:
                return 'Friday: Time to relax! Wake-up alarm set for 7:00 AM.'
        case 6:
            if has_event:
                return 'Saturday: Enjoy the weekend! Wake-up alarm set for 8:00 AM.'
            else:
                return 'Saturday: Enjoy the weekend! Wake-up alarm set for 9:00 AM.'
        case 7:
            if has_event:
                return 'Sunday: Prep for the week! Wake-up alarm set for 8:00 AM.'
            else:
                return 'Sunday: Prep for the week! Wake-up alarm set for 9:00 AM.'
        case _:
            return 'Invalid day'

