import unittest
from q3a import transpose


class TestTranspose(unittest.TestCase):
    def test_1(self):
        result = transpose([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(result, [[1, 3, 5], [2, 4, 6]])

    def test_2(self):
        result = transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(result, [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_3(self):
        result = transpose([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        self.assertEqual(result, [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]])

    def test_4(self):
        result = transpose([[1]])
        self.assertEqual(result, [[1]])

    def test_5(self):
        result = transpose([[1], [2], [3]])
        self.assertEqual(result, [[1, 2, 3]])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTranspose)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
