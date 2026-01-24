import unittest
from q1 import dims


class TestDims(unittest.TestCase):
    def test_1(self):
        result = dims([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(result, (3, 2))

    def test_2(self):
        result = dims([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(result, (3, 3))

    def test_3(self):
        result = dims([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        self.assertEqual(result, (3, 4))

    def test_4(self):
        result = dims([[1]])
        self.assertEqual(result, (1, 1))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDims)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
