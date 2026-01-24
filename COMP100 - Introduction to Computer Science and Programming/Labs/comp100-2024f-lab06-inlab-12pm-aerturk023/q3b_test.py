import unittest
from q3b import mat_mul


class TestMatMul(unittest.TestCase):
    def test_1(self):
        result = mat_mul([[1, 2], [3, 4]], [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(result, [[9, 12, 15], [19, 26, 33]])

    def test_2(self):
        result = mat_mul([[1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4], [5, 6]])
        self.assertEqual(result, [[22, 28], [49, 64]])

    def test_3(self):
        result = mat_mul([[1, 2], [3, 4]], [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(result, [[9, 12, 15], [19, 26, 33]])

    def test_4(self):
        result = mat_mul([[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(result, None)

    def test_5(self):
        result = mat_mul([[1]], [[1]])
        self.assertEqual(result, [[1]])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMatMul)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
