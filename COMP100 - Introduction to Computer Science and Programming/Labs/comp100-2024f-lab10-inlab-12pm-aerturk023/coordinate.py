class Coordinate:
    """
    A class to represent a coordinate in a 2D space.

    Attributes:
        x (int): The x-coordinate of the coordinate.
        y (int): The y-coordinate of the coordinate.

    Methods:
        distance(self, other): Calculate the distance between two coordinates.
        __str__(self): Return a string representation of the coordinate.
    """
    def __init__(self, x, y):
        """
        Initialize the coordinate with the given x and y values.

        Args:
            x (int): The x-coordinate of the coordinate.
            y (int): The y-coordinate of the coordinate.
        """
        self.x = x
        self.y = y


    def distance(self, other):
        """
        Calculate the distance between two coordinates.

        Args:
            other (Coordinate): The other coordinate to calculate the distance to.

        Returns:
            float: The distance between the two coordinates.
        """
        return ((self.x-other.x)**2+(self.y-other.y)**2)**(1/2)


    def __str__(self):
        """
        Return a string representation of the coordinate.

        Returns:
            str: A string representation of the coordinate in the format "<x, y>".
        """
        return f"<{self.x}, {self.y}>"
