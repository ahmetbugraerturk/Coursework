import unittest
from q2 import generate_pairs


class TestGeneratePairs(unittest.TestCase):
    def test_1(self):
        self.assertEqual(generate_pairs([1, 2, 3]), [(1, 2), (1, 3), (2, 3)], "Should be [(1, 2), (1, 3), (2, 3)]")

    def test_2(self):
        self.assertEqual(generate_pairs([1, 2, 3, 4]), [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)], "Should be [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]")

    def test_3(self):
        self.assertEqual(generate_pairs([1, 2]), [(1, 2)], "Should be [(1, 2)]")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGeneratePairs)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
