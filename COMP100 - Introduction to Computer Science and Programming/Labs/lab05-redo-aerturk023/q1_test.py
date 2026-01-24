# Do not change below
import unittest
from q1 import first_non_repeating_character

class Test_first_non_repeating_character(unittest.TestCase):
    def test_first_non_repeating_character1(self):
        self.assertEqual(first_non_repeating_character("aabbcd"), 4)
    def test_first_non_repeating_character2(self):
        self.assertEqual(first_non_repeating_character("ccoommpp"), -1)
    def test_first_non_repeating_character3(self):
        self.assertEqual(first_non_repeating_character("python"), 0)
    def test_first_non_repeating_character4(self):
        self.assertEqual(first_non_repeating_character("112a"), 2)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_first_non_repeating_character)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")