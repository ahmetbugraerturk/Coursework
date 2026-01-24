import random
import unittest
from q1 import estimate_odd_divisible_probability

def is_close(x, y):
    return abs(x - y) < 1e-8  

class TestOddDivisibleProbability(unittest.TestCase):
    
    def test_case_1(self):
        random.seed(1)
        expected = 0.1613 
        result = estimate_odd_divisible_probability(10000, 3)
        self.assertTrue(is_close(result, expected), f"Test Case 1 Failed: Expected {expected}, but got {result}")

    def test_case_2(self):
        random.seed(1)
        expected = 0.1138  
        result = estimate_odd_divisible_probability(5000, 5)
        self.assertTrue(is_close(result, expected), f"Test Case 2 Failed: Expected {expected}, but got {result}")

    def test_case_3(self):
        random.seed(1)
        expected = 0.124  
        result = estimate_odd_divisible_probability(500, 5)
        self.assertTrue(is_close(result, expected), f"Test Case 3 Failed: Expected {expected}, but got {result}")

    def test_case_4(self):
        random.seed(1)
        expected = 0.14 
        result = estimate_odd_divisible_probability(50, 5)
        self.assertTrue(is_close(result, expected), f"Test Case 4 Failed: Expected {expected}, but got {result}")

    def test_case_5(self):
        random.seed(1)
        expected = 0.2 
        result = estimate_odd_divisible_probability(100, 7)
        self.assertTrue(is_close(result, expected), f"Test Case 5 Failed: Expected {expected}, but got {result}")

    def test_case_6(self):
        random.seed(1)
        expected = 0.15 
        result = estimate_odd_divisible_probability(100, 9)
        self.assertTrue(is_close(result, expected), f"Test Case 6 Failed: Expected {expected}, but got {result}")

    def test_case_7(self):
        random.seed(1)
        expected = 0.114
        result = estimate_odd_divisible_probability(1000, 9)
        self.assertTrue(is_close(result, expected), f"Test Case 7 Failed: Expected {expected}, but got {result}")
    
    def test_case_8(self):
        random.seed(1)
        expected = 0.1675
        result = estimate_odd_divisible_probability(10000, 7)
        self.assertTrue(is_close(result, expected), f"Test Case 8 Failed: Expected {expected}, but got {result}")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOddDivisibleProbability)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Tests Passed: {total_passed}/{total_tests_run}")
