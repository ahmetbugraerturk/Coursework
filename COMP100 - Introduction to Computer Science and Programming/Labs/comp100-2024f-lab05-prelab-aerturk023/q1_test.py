# Do not change below
import unittest
from q1 import longest_palindromic_substring


class test_longest_palindromic_substring(unittest.TestCase):
    def test_longest_palindromic_substring1(self):
        self.assertEqual(longest_palindromic_substring('baabaad'),'aabaa', msg= "Test 1 Failed")
        
    def test_longest_palindromic_substring2(self):
        self.assertEqual(longest_palindromic_substring('cbfbdc'),'bfb', msg= "Test 2 Failed")
        
    def test_longest_palindromic_substring3(self):
        self.assertEqual(longest_palindromic_substring('Melonnothanks'),'onno', msg= "Test 3 Failed")
        
    def test_longest_palindromic_substring4(self):
        self.assertEqual(longest_palindromic_substring('nopalindrome'),'', msg= "Test 4 Failed")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_longest_palindromic_substring)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")