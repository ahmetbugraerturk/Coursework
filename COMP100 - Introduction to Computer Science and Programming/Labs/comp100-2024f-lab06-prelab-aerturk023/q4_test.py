import unittest
from q4 import zigzag_merge


class TestZigzagMerge(unittest.TestCase):
    def test_1(self):
        self.assertEqual(zigzag_merge([1, 2, 3], [10, 20, 30, 40, 50]), [1, 10, 2, 20, 3, 30, 40, 50], "Should be [1, 10, 2, 20, 3, 30, 40, 50]")

    def test_2(self):
        self.assertEqual(zigzag_merge([1, 2, 3], []), [1, 2, 3], "Should be [1, 2, 3]")

    def test_3(self):
        self.assertEqual(zigzag_merge([], [1, 2, 3]), [1, 2, 3], "Should be [1, 2, 3]")

    def test_4(self):
        self.assertEqual(zigzag_merge([1, 2, 3], [10, 20, 30, 40, 50, 60, 70]), [1, 10, 2, 20, 3, 30, 40, 50, 60, 70], "Should be [1, 10, 2, 20, 3, 30, 40, 50, 60, 70]")

    def test_5(self):
        self.assertEqual(zigzag_merge([1, 2, 3, 4, 5], [10, 20, 30]), [1, 10, 2, 20, 3, 30, 4, 5], "Should be [1, 10, 2, 20, 3, 30, 4, 5]")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestZigzagMerge)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
