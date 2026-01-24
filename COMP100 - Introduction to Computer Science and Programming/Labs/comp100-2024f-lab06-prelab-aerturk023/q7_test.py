import unittest
from q7 import transpose_tuples


class TestTransposeTuples(unittest.TestCase):
    def test_1(self):
        matrix = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        expected = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
        self.assertEqual(transpose_tuples(matrix), expected, f"Should be {expected}")

    def test_2(self):
        matrix = [(1, 2), (3, 4)]
        expected = [(1, 3), (2, 4)]
        self.assertEqual(transpose_tuples(matrix), expected, f"Should be {expected}")

    def test_3(self):
        matrix = [(1, 2), (3, 4), (5, 6)]
        expected = [(1, 3, 5), (2, 4, 6)]
        self.assertEqual(transpose_tuples(matrix), expected, f"Should be {expected}")

    def test_4(self):
        matrix = []
        expected = []
        self.assertEqual(transpose_tuples(matrix), expected, f"Should be {expected}")

    def test_5(self):
        matrix = [(1,)]
        expected = [(1,)]
        self.assertEqual(transpose_tuples(matrix), expected, f"Should be {expected}")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTransposeTuples)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
