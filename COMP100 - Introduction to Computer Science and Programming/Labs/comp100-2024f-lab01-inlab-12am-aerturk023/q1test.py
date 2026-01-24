import unittest
from q1 import interest_calculator

class TestTriangleProperties(unittest.TestCase):
    
    def test1(self):
        result = interest_calculator(1000, 55, 2)
        self.assertAlmostEqual(result, 2402.5, delta=0.01, msg = "Incorrect returns")
        print("Test 1 passed")
    def test2(self):
        result = interest_calculator(123, 123, 3)
        self.assertAlmostEqual(result, 1364.016, delta=0.01, msg= "Incorrect returns")
        print("Test 2 passed")
    def test3(self):
        result = interest_calculator(2500, 0, 10)
        self.assertAlmostEqual(result, 2500, delta=0.01, msg= "Incorrect returns")
        print("Test 3 passed")
    def test4(self):
        result = interest_calculator(1600, 10, 5)
        self.assertAlmostEqual(result, 2576.816, delta=0.01, msg= "Incorrect returns")
        print("Test 4 passed")

if __name__ == '__main__':
    unittest.main()

