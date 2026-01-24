def transpose(m: list[list[int]]) -> list[list[int]]:
    """
    Transpose a matrix.

    Parameters:
        m (list[list[int]]): The matrix to transpose.

    Returns:
        list[list[int]]: The transpose of the matrix.
    """
    
    if m == []:
        return []
    
    matrix = []
    
    for i in range(len(m[0])):
        row = []
        for j in m:
            row.append(j[i])
        matrix.append(row)
    return matrix
