import unittest
from q3c import gram_matrix


class TestGramMatrix(unittest.TestCase):
    def test_1(self):
        result = gram_matrix([[1, 2], [3, 4]])
        self.assertEqual(result, [[5, 11], [11, 25]])

    def test_2(self):
        result = gram_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(result, [[14, 32, 50], [32, 77, 122], [50, 122, 194]])

    def test_3(self):
        result = gram_matrix([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(result, [[5, 11, 17], [11, 25, 39], [17, 39, 61]])

    def test_4(self):
        result = gram_matrix([[1]])
        self.assertEqual(result, [[1]])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGramMatrix)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
