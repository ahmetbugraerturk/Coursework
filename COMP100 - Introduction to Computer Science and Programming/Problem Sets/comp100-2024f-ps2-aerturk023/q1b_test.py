import unittest

from q1b import show_allocated_seats


class TestShowAllocatedSeats(unittest.TestCase):
    def test_1(self):
        result = show_allocated_seats(4, "OXO|OXXO|XOO")
        self.assertEqual(result, "HXH|HXXH|XOO")

    def test_2(self):
        result = show_allocated_seats(3, "OO|OX|OX")
        self.assertEqual(result, "HH|HX|OX")

    def test_3(self):
        result = show_allocated_seats(7, "OO|OO|OO")
        self.assertEqual(result, "Boarding Denied!")

    def test_4(self):
        result = show_allocated_seats(3, "OX|XX|OX")
        self.assertEqual(result, "Boarding Denied!")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestShowAllocatedSeats)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
