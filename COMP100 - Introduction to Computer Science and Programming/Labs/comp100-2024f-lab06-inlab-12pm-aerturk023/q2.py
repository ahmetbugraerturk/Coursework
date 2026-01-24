def zeros(dim: tuple[int, int]) -> list[list[int]]:
    """
    Create a matrix of zeros with the given dimensions.

    Parameters:
        dim (tuple[int, int]): A tuple representing the dimensions of the matrix.

    Returns:
        list[list[int]]: A matrix of zeros with the given dimensions.
    """
    
    row = []
    matrix = []

    for i in range(dim[1]):
        row.append(0)
    for i in range(dim[0]):
        matrix.append(row)
        
    return matrix
