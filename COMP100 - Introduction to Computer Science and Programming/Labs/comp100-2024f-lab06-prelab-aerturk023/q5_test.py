import unittest
from q5 import longest_consecutive_subsequence_len


class TestFindLongestConsecutiveSubsequence(unittest.TestCase):
    def test_1(self):
        self.assertEqual(longest_consecutive_subsequence_len([10, 4, 20, 1, 3, 2, 5]), 5, "Should be 5")

    def test_2(self):
        self.assertEqual(longest_consecutive_subsequence_len([1, 2, 3, 4, 5]), 5, "Should be 5")

    def test_3(self):
        self.assertEqual(longest_consecutive_subsequence_len([]), 0, "Should be 0")

    def test_4(self):
        self.assertEqual(longest_consecutive_subsequence_len([1, 1, 2, 2, 3, 3, 4, 4]), 4, "Should be 4")

    def test_5(self):
        self.assertEqual(longest_consecutive_subsequence_len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10, "Should be 10")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFindLongestConsecutiveSubsequence)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
