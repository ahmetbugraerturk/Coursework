import unittest
from q3 import list_rotate


class TestRotateList(unittest.TestCase):
    def test_1(self):
        self.assertEqual(list_rotate([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3], "Should be [4, 5, 1, 2, 3]")

    def test_2(self):
        self.assertEqual(list_rotate([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5], "Should be [1, 2, 3, 4, 5]")

    def test_3(self):
        self.assertEqual(list_rotate([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5], "Should be [1, 2, 3, 4, 5]")

    def test_4(self):
        self.assertEqual(list_rotate([1, 2, 3, 4, 5], 10), [1, 2, 3, 4, 5], "Should be [1, 2, 3, 4, 5]")

    def test_5(self):
        self.assertEqual(list_rotate([], 10), [], "Should be []")

    def test_6(self):
        self.assertEqual(list_rotate([1, 2, 3, 4, 5], -2), [3, 4, 5, 1, 2], "Should be [3, 4, 5, 1, 2]")

    def test_7(self):
        self.assertEqual(list_rotate([1, 2, 3, 4, 5], -5), [1, 2, 3, 4, 5], "Should be [1, 2, 3, 4, 5]")

    def test_8(self):
        self.assertEqual(list_rotate([1, 2, 3, 4, 5], -10), [1, 2, 3, 4, 5], "Should be [1, 2, 3, 4, 5]")

    def test_9(self):
        self.assertEqual(list_rotate([1, 2, 3, 4, 5], -15), [1, 2, 3, 4, 5], "Should be [1, 2, 3, 4, 5]")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRotateList)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
