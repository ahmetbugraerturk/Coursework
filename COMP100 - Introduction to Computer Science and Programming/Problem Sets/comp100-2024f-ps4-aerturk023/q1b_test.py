import unittest
from q1b import derivative


class test_derivative(unittest.TestCase):
    def test_derivative1(self):
        self.assertAlmostEqual(derivative('sin(cos(x))*sin(cos(sin(x)))*cos(x)+sin(cos(x))', 1.2), -1.265, delta=0.005,msg= "Test 1 Failed")      
    def test_derivative2(self):
        self.assertAlmostEqual(derivative('cos(x)+sin(cos(x))', 0.2), -0.309, delta=0.005,msg= "Test 2 Failed")
    def test_derivative3(self):
        self.assertAlmostEqual(derivative('sin(cos(x))+sin(cos(sin(x)))*cos(x)', 0.7), -1.17, delta=0.005,msg= "Test 3 Failed")
        


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_derivative)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")