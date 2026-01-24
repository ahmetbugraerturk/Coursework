def transpose_tuples(matrix: list[tuple]) -> list[tuple]:
    """
    Manipulates a matrix by transposing it.

    Parameters:
        matrix (list[tuple]): The matrix to manipulate.

    Returns:
        list[tuple]: The transposed matrix.
    """
    
    matrixT = []
    if matrix != []:
        for i in range(len(matrix[0])):
            rowT = ()
            for j in matrix:
                rowT += (j[i],)
            matrixT.append(rowT)
            print(rowT, matrixT)
    return matrixT
            
