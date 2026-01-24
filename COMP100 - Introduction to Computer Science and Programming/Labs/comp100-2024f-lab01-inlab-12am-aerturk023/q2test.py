import unittest
from q2 import triangle_area
from math import sqrt

class TestTriangleProperties(unittest.TestCase):
    
    def test_right_triangle(self):
        result = triangle_area(3, 4, 5)
        self.assertAlmostEqual(result, 6.0, "Area of right triangle (3, 4, 5) is incorrect.")
        print("Test passed: Right triangle with sides 3, 4, 5 has correct area.")

    def test_equilateral_triangle(self):
        result = triangle_area(5, 5, 5)
        self.assertAlmostEqual(result, 10.8253, places=4, msg="Area of equilateral triangle (5, 5, 5) is incorrect.")
        print("Test passed: Equilateral triangle with sides 5, 5, 5 has correct area.")

    def test_isosceles_triangle(self):
        result = triangle_area(5, 5, 8)
        self.assertAlmostEqual(result, 12.0, msg="Area of isosceles triangle (5, 5, 8) is incorrect.")
        print("Test passed: Isosceles triangle with sides 5, 5, 8 has correct area.")

if __name__ == '__main__':
    unittest.main()
