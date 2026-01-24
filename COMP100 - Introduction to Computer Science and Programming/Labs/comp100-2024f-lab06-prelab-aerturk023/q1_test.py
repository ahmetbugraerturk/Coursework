import unittest
from q1 import is_sublist


class TestIsSublist(unittest.TestCase):
    def test_1(self):
        result = is_sublist([1, 2, 3, 4, 5], [3, 4])
        self.assertEqual(result, True, "Should be True")

    def test_2(self):
        result = is_sublist([1, 2, 3, 4, 5], [4])
        self.assertEqual(result, True, "Should be True")

    def test_3(self):
        result = is_sublist([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
        self.assertEqual(result, True, "Should be True")

    def test_4(self):
        result = is_sublist([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6])
        self.assertEqual(result, False, "Should be False")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIsSublist)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
