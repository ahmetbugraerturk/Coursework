import random
import unittest
from q2 import estimate_joint_probability 

def is_close(x, y):
    return abs(x - y) < 1e-8

class TestJointProbability(unittest.TestCase):
    
    def test_case_1(self):
        random.seed(1)
        expected = 0.239 
        result = estimate_joint_probability(1000, 7, 11)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 1 Failed: Expected {expected}, but got {result}")

    def test_case_2(self):
        random.seed(1)
        expected = 0.226
        result = estimate_joint_probability(500, 7, 11)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 2 Failed: Expected {expected}, but got {result}")

    def test_case_3(self):
        random.seed(1)
        expected = 0.168 
        result = estimate_joint_probability(500, 3, 8)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 3 Failed: Expected {expected}, but got {result}")

    def test_case_4(self):
        random.seed(1)
        expected = 0.1108
        result = estimate_joint_probability(5000, 2, 9)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 4 Failed: Expected {expected}, but got {result}")

    def test_case_5(self):
        random.seed(1)
        expected = 0.11128 
        result = estimate_joint_probability(50000, 2, 9)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 5 Failed: Expected {expected}, but got {result}")
        
    def test_case_6(self):
        random.seed(1)
        expected = 0.10991 
        result = estimate_joint_probability(100000, 2, 9)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 5 Failed: Expected {expected}, but got {result}")
    
    def test_case_7(self):
        random.seed(1)
        expected = 0.0556 
        result = estimate_joint_probability(100000, 1, 3)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 5 Failed: Expected {expected}, but got {result}")
        
    def test_case_8(self):
        random.seed(1)
        expected = 0.22
        result = estimate_joint_probability(50, 7, 11)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 1 Failed: Expected {expected}, but got {result}")
        
    def test_case_9(self):
        random.seed(1)
        expected = 0.2
        result = estimate_joint_probability(5, 7, 11)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 1 Failed: Expected {expected}, but got {result}")
        
    def test_case_10(self):
        random.seed(1)
        expected = 0.1695 
        result = estimate_joint_probability(2000, 6, 4)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 1 Failed: Expected {expected}, but got {result}")    

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestJointProbability)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Tests Passed: {total_passed}/{total_tests_run}")
