from coordinate import Coordinate

class ComplexNumber(Coordinate):
    """
    A class to represent a complex number.

    Attributes:
        real (int): The real part of the complex number.
        imaginary (int): The imaginary part of the complex number.

    Methods:
        __add__(self, other): Add two complex numbers.
        __sub__(self, other): Subtract two complex numbers.
        __mul__(self, other): Multiply two complex numbers.
        __truediv__(self, other): Divide two complex numbers.
        __eq__(self, other): Check if two complex numbers are equal.
        __str__(self): Return a string representation of the complex number.
    """
    def __init__(self, real, imaginary):
        """
        Initialize the complex number with the given real and imaginary parts.

        Args:
            real (int): The real part of the complex number.
            imaginary (int): The imaginary part of the complex number.
        """
        super().__init__(real, imaginary)


    def __add__(self, other):
        """
        Add two complex numbers.

        Args:
            other (ComplexNumber): The other complex number to add.

        Returns:
            ComplexNumber: The result of the addition.
        """
        return ComplexNumber(self.x+other.x, self.y+other.y)
    
    def __sub__(self, other):
        return ComplexNumber(self.x-other.x, self.y-other.y)
    
    def __mul__(self, other):
        return ComplexNumber(self.x*other.x-self.y*other.y, self.x*other.y+self.y*other.x)
    
    def __truediv__(self, other):
        return ComplexNumber((self.x*other.x+self.y*other.y)/(other.x**2+other.y**2), (self.y*other.x-self.x*other.y)/(other.x**2+other.y**2))
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    def __str__(self):
        if self.y == 0:
            return f"{self.y}"
        elif self.y > 0:
            return f"{self.x} + {self.y}i"
        elif self.y < 0:
            return f"{self.x} - {-self.y}i"
        
        
        