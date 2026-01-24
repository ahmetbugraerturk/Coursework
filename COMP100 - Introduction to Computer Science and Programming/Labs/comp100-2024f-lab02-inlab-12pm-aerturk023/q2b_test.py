import unittest
from q2b import repeated_weighted_digit_sum


class TestRepeatedWeightedDigitSum(unittest.TestCase):
    def test_1(self):
        result = repeated_weighted_digit_sum(1)
        self.assertEqual(result, 1, "Should be 1")

    def test_2(self):
        result = repeated_weighted_digit_sum(2)
        self.assertEqual(result, 2, "Should be 2")

    def test_3(self):
        result = repeated_weighted_digit_sum(44)
        self.assertEqual(result, 4, "Should be 4")

    def test_4(self):
        result = repeated_weighted_digit_sum(987 )
        self.assertEqual(result, 2, "Should be 2")

    def test_5(self):
        result = repeated_weighted_digit_sum(-456)
        self.assertEqual(result, 4, "Should be 4")

    def test_6(self):
        result = repeated_weighted_digit_sum(12)
        self.assertEqual(result, 4, "Should be 4")

    def test_7(self):
        result = repeated_weighted_digit_sum(15)
        self.assertEqual(result, 7, "Should be 7")

    def test_8(self):
        result = repeated_weighted_digit_sum(27)
        self.assertEqual(result, 3, "Should be 3")

    def test_9(self):
        result = repeated_weighted_digit_sum(50)
        self.assertEqual(result, 2, "Should be 2")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRepeatedWeightedDigitSum)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
