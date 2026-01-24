def generate_triangle(n: int) -> None:
    """
    Prints out a triangle of numbers, with each row containing increasing numbers starting from 1 up to the row number.

    Parameters:
        n (int): The number of rows in the triangle.
    """
    
    for i in range(1,n+1):
        line = " " * ((n-i)*2)
        for j in range(1,i+1):
            line = line + str(j) + " "
        print(line)
