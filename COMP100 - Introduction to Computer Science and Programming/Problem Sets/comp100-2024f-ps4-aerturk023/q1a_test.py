import unittest
from q1a import calculate


class test_calculate(unittest.TestCase):
    def test_calculate1(self):
        self.assertAlmostEqual(calculate('sin(cos(x))+sin(cos(sin(x)))*cos(x)', 0.7), 1.24, delta=0.005,msg= "Test 1 Failed")      
    def test_calculate2(self):
        self.assertAlmostEqual(calculate('cos(x)+sin(cos(x))', 0.2), 1.81, delta=0.005,msg= "Test 2 Failed")
    def test_calculate3(self):
        self.assertAlmostEqual(calculate('sin(cos(x))+sin(cos(sin(x)))*cos(x)', 0.7), 1.24, delta=0.005,msg= "Test 3 Failed")
        


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_calculate)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")