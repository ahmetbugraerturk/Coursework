def dims(m: list[list[int]]) -> tuple[int, int]:
    """
    Get the dimensions of a matrix.

    Parameters:
        m (list[list[int]]): The matrix to get the dimensions of.

    Returns:
        tuple[int, int]: A tuple representing the dimensions of the matrix.
    """

    if len(m)>0:
        return (len(m), len(m[0]))
    else:
        return (0,0)