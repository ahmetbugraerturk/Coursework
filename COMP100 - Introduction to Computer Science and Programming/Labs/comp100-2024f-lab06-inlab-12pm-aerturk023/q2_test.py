import unittest
from q2 import zeros


class TestZeros(unittest.TestCase):
    def test_1(self):
        result = zeros((3, 2))
        self.assertEqual(result, [[0, 0], [0, 0], [0, 0]])

    def test_2(self):
        result = zeros((2, 3))
        self.assertEqual(result, [[0, 0, 0], [0, 0, 0]])

    def test_3(self):
        result = zeros((4, 4))
        self.assertEqual(result, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_4(self):
        result = zeros((1, 1))
        self.assertEqual(result, [[0]])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestZeros)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
