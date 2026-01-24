def is_sublist(list1: list, list2: list) -> bool:
    """
    Check if list2 is a sublist of list1.

    Parameters:
        list1 (list): The list to check if list2 is a sublist of.
        list2 (list): The list to check if it is a sublist of list1.

    Returns:
        bool: True if list2 is a sublist of list1, False otherwise.
    """
    
    is_subset = True

    for i in list2:
        if i not in list1:
            is_subset = False
    return is_subset
