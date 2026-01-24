import unittest
import sys
from io import StringIO

from q1 import convert_distance


class TestConvertDistance(unittest.TestCase):
    def test_kilometers_to_miles(self):
        result = convert_distance(10, 'K')
        self.assertEqual(result, 6.21, "Should be 6.21")

    def test_miles_to_kilometers(self):
        result = convert_distance(5, 'M')
        self.assertEqual(result, 8.05, "Should be 8.05")

    def test_invalid_unit(self):
        expected_output = "Invalid unit"
        captured_output = StringIO()
        sys.stdout = captured_output
        result = convert_distance(100, 'X')
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)
        self.assertEqual(result, None, "Should be None")

    def test_kilometers_to_miles_zero(self):
        result = convert_distance(0, 'K')
        self.assertEqual(result, 0, "Should be 0")

    def test_miles_to_kilometers_zero(self):
        result = convert_distance(0, 'M')
        self.assertEqual(result, 0, "Should be 0")

    def test_kilometers_to_miles_negative(self):
        expected_output = "Negative distance"
        captured_output = StringIO()
        sys.stdout = captured_output
        result = convert_distance(-40, 'K')
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)
        self.assertEqual(result, None, "Should be None")

    def test_miles_to_kilometers_negative(self):
        expected_output = "Negative distance"
        captured_output = StringIO()
        sys.stdout = captured_output
        result = convert_distance(-40, 'M')
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)
        self.assertEqual(result, None, "Should be None")

    def test_kilometers_to_miles_decimal(self):
        result = convert_distance(37.5, 'K')
        self.assertEqual(result, 23.3, "Should be 23.3")

    def test_miles_to_kilometers_decimal(self):
        result = convert_distance(99.5, 'M')
        self.assertEqual(result, 160.13, "Should be 160.13")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestConvertDistance)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
