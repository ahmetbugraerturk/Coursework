from q3a import transpose
from q3b import mat_mul


def gram_matrix(m: list[list[int]]) -> list[list[int]]:
    """
    Compute the Gram matrix of a matrix.

    Parameters:
        m (list[list[int]]): The input matrix.

    Returns:
        list[list[int]]: The Gram matrix.
    """

    return mat_mul(m, transpose(m))
