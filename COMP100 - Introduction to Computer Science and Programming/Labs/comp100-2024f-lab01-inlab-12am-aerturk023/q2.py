

def triangle_area(a, b, c):
    """
    Parameters:
    ----------
    a, b, c : float
        The side lengths of the triangle.

    Returns:
    -------
    area : float
        The area of the triangle calculated using Heron's formula.

    """
    # Your code goes here, delete 'pass' !

    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)
    return area
