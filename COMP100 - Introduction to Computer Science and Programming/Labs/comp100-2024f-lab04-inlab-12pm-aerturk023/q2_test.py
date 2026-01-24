import random
import unittest
from q2 import estimate_e

def is_close(x, y):
    return abs(x - y) < 1e-8  

class TestEstimateE(unittest.TestCase):
    
    def test_case_1(self):
        random.seed(1)
        expected = 2.71791 
        result = estimate_e(100000)
        self.assertTrue(is_close(result, expected), f"Test Case 1 Failed: Expected {expected}, but got {result}")

    def test_case_2(self):
        random.seed(1)
        expected = 2.7159  
        result = estimate_e(10000)
        self.assertTrue(is_close(result, expected), f"Test Case 2 Failed: Expected {expected}, but got {result}")

    def test_case_3(self):
        random.seed(1)
        expected = 2.727  
        result = estimate_e(5000)
        self.assertTrue(is_close(result, expected), f"Test Case 3 Failed: Expected {expected}, but got {result}")

    def test_case_4(self):
        random.seed(1)
        expected = 2.83  
        result = estimate_e(100)
        self.assertTrue(is_close(result, expected), f"Test Case 4 Failed: Expected {expected}, but got {result}")

    def test_case_5(self):
        random.seed(1)
        expected = 3.3  
        result = estimate_e(10)
        self.assertTrue(is_close(result, expected), f"Test Case 5 Failed: Expected {expected}, but got {result}")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEstimateE)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Tests Passed: {total_passed}/{total_tests_run}")
