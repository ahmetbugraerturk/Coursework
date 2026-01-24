# Do not change below
import unittest
from q2 import longest_common_prefix

class Test_longest_common_prefix_test(unittest.TestCase):
    def test_lcp1(self):
        self.assertEqual(longest_common_prefix("flower flow flight"), "fl")
    def test_lcp2(self):
        self.assertEqual(longest_common_prefix("hello hell heap"),"he")
    def test_lcp3(self):
        self.assertEqual(longest_common_prefix("worker hard easy"),"")
    def test_lcp4(self):
        self.assertEqual(longest_common_prefix("ieeyyy ieeyw ieethy"),"iee")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_longest_common_prefix_test)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
