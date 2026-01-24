def convert_distance(distance: float, unit: str) -> float | None:
    """
    Convert distance from Kilometers to Miles or vice versa.

    Parameters:
        distance (float): The distance to be converted.
        unit (str): The unit of the distance, either 'K' or 'M'.

    Returns:
        float: The converted distance.
    """

    # TODO: Complete the function to convert the distance
    if distance < 0:
        print("Negative distance")
        return None
    elif unit == "K":
        return float(format(distance * 0.621371, '.2f'))
    elif unit == "M":
        return float(format(distance / 0.621371, '.2f'))
    else:
        print("Invalid unit")
        return None
