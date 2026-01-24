from q1 import dims
from q2 import zeros
from q3a import transpose


def mat_mul(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    """
    Compute the product of two matrices.

    Parameters:
        A (list[list[int]]): The first matrix.
        B (list[list[int]]): The second matrix.

    Returns:
        list[list[int]]: The product of the two matrices.
    """

    dims_a = dims(A)
    dims_b = dims(B)
    
    bt = transpose(B)
    
    C = []
    
    if dims_a[1]==dims_b[0]:
        for l in range(dims_b[1]):
            row = []
            for i in range(dims_a[0]):
                sums = 0
                for j in range(dims_a[1]):
                    sums += A[i][j]*bt[l][j]
                row.append(sums)
            C.append(row)
        return transpose(C)
    else:
        return None
        
            
            
