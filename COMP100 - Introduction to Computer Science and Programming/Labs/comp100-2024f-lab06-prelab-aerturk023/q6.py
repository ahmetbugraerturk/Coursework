def element_frequency(list1: list) -> list:
    """
    Compresses a list by replacing consecutive repeated elements with tuples of the elements and its count.

    Parameters:
        list1 (list): The list of integers.

    Returns:
        list: The compressed list.
    """

    freq = []
    count = 0
    
    for i in range(1, len(list1)):
        count += 1
        if list1[i-1] != list1[i]:
            freq.append((list1[i-1], count))
            count=0
        if i == len(list1)-1:
            freq.append((list1[i], count+1))
    return freq

