import unittest
from q1 import is_leap_year

class TestIsLeapYear(unittest.TestCase):
    def test_1(self):
        result = is_leap_year(2000)
        self.assertEqual(result, True, "Should be True")

    def test_2(self):
        result = is_leap_year(1999)
        self.assertEqual(result, False, "Should be False")

    def test_3(self):
        result = is_leap_year(1900)
        self.assertEqual(result, False, "Should be False")

    def test_4(self):
        result = is_leap_year(2004)
        self.assertEqual(result, True, "Should be True")

    def test_5(self):
        result = is_leap_year(2024)
        self.assertEqual(result, True, "Should be True")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsLeapYear)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
