def list_rotate(list1: list, k: int) -> list:
    """
    Rotate the list cyclically to the right if k is positive, and to the left if k is negative.

    Parameters:
        list1 (list): The list to rotate.
        k (int): The number of positions to rotate the list.

    Returns:
        list: The rotated list.
    """
    
    if len(list1)!=0:
        if k<0:
            k=k%len(list1)-len(list1)
        else:
            k=k%len(list1)

    return list1[-k:]+list1[:-k]