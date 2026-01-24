import unittest
from q2a import weighted_sum_of_digits


class TestWeightedSumOfDigits(unittest.TestCase):
    def test_1(self):
        result = weighted_sum_of_digits(1)
        self.assertEqual(result, 1, "Should be 1")

    def test_2(self):
        result = weighted_sum_of_digits(2)
        self.assertEqual(result, 2, "Should be 2")

    def test_3(self):
        result = weighted_sum_of_digits(456)
        self.assertEqual(result, 28, "Should be 28")

    def test_4(self):
        result = weighted_sum_of_digits(987 )
        self.assertEqual(result, 50, "Should be 50")

    def test_5(self):
        result = weighted_sum_of_digits(-456)
        self.assertEqual(result, 28, "Should be 28")

    def test_6(self):
        result = weighted_sum_of_digits(12)
        self.assertEqual(result, 4, "Should be 4")

    def test_7(self):
        result = weighted_sum_of_digits(15)
        self.assertEqual(result, 7, "Should be 7")

    def test_8(self):
        result = weighted_sum_of_digits(27)
        self.assertEqual(result, 11, "Should be 11")

    def test_9(self):
        result = weighted_sum_of_digits(50)
        self.assertEqual(result, 10, "Should be 10")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWeightedSumOfDigits)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
