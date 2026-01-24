import unittest
from q1 import parse_date, YearRangeError

class TestParseDate(unittest.TestCase):

    def test_valid_date(self):
        # Valid leap year date
        self.assertEqual(parse_date("2020", "02", "29"), "2020-02-29")

    def test_invalid_year_low(self):
        # Year too low
        with self.assertRaises(YearRangeError) as context:
            parse_date("1899", "12", "15")
        self.assertIn("Year must be between 1900 and 2100.", str(context.exception))

    def test_invalid_year_high(self):
        # Year too high
        with self.assertRaises(YearRangeError) as context:
            parse_date("2101", "01", "01")
        self.assertIn("Year must be between 1900 and 2100.", str(context.exception))

    def test_non_integer_values(self):
        # Non-integer month
        with self.assertRaises(ValueError) as context:
            parse_date("2021", "Feb", "10")
        self.assertIn("Year, month, and day strings must contain integers.", str(context.exception))

    def test_invalid_date_day(self):
        # Invalid date (April 31 doesn't exist)
        with self.assertRaises(ValueError) as context:
            parse_date("2021", "04", "31")
        self.assertIn("Invalid date specified.", str(context.exception))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestParseDate)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
