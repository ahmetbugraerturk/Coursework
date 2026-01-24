import random
import unittest
from q1 import estimate_pi_dart_game

def is_close(x, y):
    return abs(x - y) < 1e-8

class TestPiDartGame(unittest.TestCase):
    
    def test_case_1(self):
        random.seed(1)
        expected =  3.116
        result = estimate_pi_dart_game(10000, 1.8)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 1 Failed: Expected {expected}, but got {result}")

    def test_case_2(self):
        random.seed(1)
        expected =  3.1024
        result = estimate_pi_dart_game(5000, 3.6)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 2 Failed: Expected {expected}, but got {result}")

    def test_case_3(self):
        random.seed(1)
        expected =  3.084
        result = estimate_pi_dart_game(1000, 5.4)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 3 Failed: Expected {expected}, but got {result}")

    def test_case_4(self):
        random.seed(1)
        expected =  3.12
        result = estimate_pi_dart_game(100, 2.0)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 4 Failed: Expected {expected}, but got {result}")

    def test_case_5(self):
        random.seed(1)
        expected =  2.0
        result = estimate_pi_dart_game(10, 1.2)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 5 Failed: Expected {expected}, but got {result}")

    def test_case_6(self):
        random.seed(1)
        expected =  3.084
        result = estimate_pi_dart_game(1000, 1.0)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 6 Failed: Expected {expected}, but got {result}")

    def test_case_7(self):
        random.seed(1)
        expected =  3.1292
        result = estimate_pi_dart_game(50000, 1.5)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 7 Failed: Expected {expected}, but got {result}")

    def test_case_8(self):
        random.seed(1)
        expected =  3.141912
        result = estimate_pi_dart_game(500000, 1.5)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 8 Failed: Expected {expected}, but got {result}")

    def test_case_9(self):
        random.seed(1)
        expected =  3.140696
        result = estimate_pi_dart_game(1000000, 1.5)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 9 Failed: Expected {expected}, but got {result}")

    def test_case_10(self):
        random.seed(1)
        expected =  3.135466666666667
        result = estimate_pi_dart_game(75000, 1)
        self.assertTrue(is_close(result, expected), 
                        f"Test Case 10 Failed: Expected {expected}, but got {result}")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPiDartGame)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Tests Passed: {total_passed}/{total_tests_run}")
