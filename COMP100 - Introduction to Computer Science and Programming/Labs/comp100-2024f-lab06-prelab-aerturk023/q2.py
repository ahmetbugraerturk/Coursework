def generate_pairs(list1: list) -> list[tuple]:
    """
    Generate all possible unordered pairs from a list of unique integers.

    Parameters:
        list1 (list): A list of unique integers.

    Returns:
        list[tuple]: A list of all possible unordered pairs from the input list.
    """
    
    pairs = []
    
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            pairs.append((list1[i],list1[j]))
    return pairs
