import unittest

from q2b import show_preferred_seats


class TestShowPreferredSeats(unittest.TestCase):
    def test_1(self):
        result = show_preferred_seats(2, "OXO|OXXO|XOO", "W")
        self.assertEqual(result, "HXO|OXXO|XOH")

    def test_2(self):
        result = show_preferred_seats(3, "OO|OO|OO", "A")
        self.assertEqual(result, "OH|HH|OO")

    def test_3(self):
        result = show_preferred_seats(3, "OX|XX|OO", "W")
        self.assertEqual(result, "Boarding Denied!")

    def test_4(self):
        result = show_preferred_seats(3, "OXO|XOOX|XOO", "M")
        self.assertEqual(result, "OXO|XHHX|XHO")

    def test_5(self):
        result = show_preferred_seats(1, "OXO|XOOX|XOO", "D")
        self.assertEqual(result, "OXD|XOOX|XOO")

    def test_6(self):
        result = show_preferred_seats(3, "OO|OO|OO", "Z")
        self.assertEqual(result, "Invalid seat preference!")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestShowPreferredSeats)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
