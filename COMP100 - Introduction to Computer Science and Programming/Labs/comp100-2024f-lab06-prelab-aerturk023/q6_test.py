import unittest
from q6 import element_frequency


class TestCompressList(unittest.TestCase):
    def test_1(self):
        self.assertEqual(element_frequency([1, 1, 2, 2, 2, 3, 4, 4]), [(1, 2), (2, 3), (3, 1), (4, 2)], "Should be [(1, 2), (2, 3), (3, 1), (4, 2)]")

    def test_2(self):
        self.assertEqual(element_frequency([1, 2, 3, 4, 5]), [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)], "Should be [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]")

    def test_3(self):
        self.assertEqual(element_frequency([1, 1, 1, 1, 1]), [(1, 5)], "Should be [(1, 5)]")

    def test_4(self):
        self.assertEqual(element_frequency([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]), [(1, 1), (2, 2), (3, 3), (4, 4)], "Should be [(1, 1), (2, 2), (3, 3), (4, 4)]")

    def test_5(self):
        self.assertEqual(element_frequency([]), [], "Should be []")

    def test_6(self):
        self.assertEqual(element_frequency([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1)], "Should be [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1)]")

    def test_7(self):
        self.assertEqual(element_frequency([1, 1, 3, 3, 3, 2, 2, 3, 3, 5, 6, 6, 6, 6, 6]), [(1, 2), (3, 3), (2, 2), (3, 2), (5, 1), (6, 5)], "Should be [(1, 2), (3, 3), (2, 2), (3, 2), (5, 1), (6, 5)]")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCompressList)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
