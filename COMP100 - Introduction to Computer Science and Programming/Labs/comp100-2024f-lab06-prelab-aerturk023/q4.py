def zigzag_merge(list1: list, list2: list) -> list:
    """
    Merges two lists into a single list in a zigzag manner.

    Parameters:
        list1 (list): The first list to merge.
        list2 (list): The second list to merge.

    Returns:
        list: The merged list.
    """
    
    zigzag = []

    for i in range(max(len(list1),len(list2))):
        if len(list1)<=i:
            zigzag.append(list2[i])
        elif len(list2)<=i:
            zigzag.append(list1[i])
        else:
            zigzag.append(list1[i])
            zigzag.append(list2[i])
    return zigzag
