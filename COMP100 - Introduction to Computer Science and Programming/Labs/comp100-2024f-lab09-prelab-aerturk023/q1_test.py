import unittest
from q1 import generate_all_strings


class test_generate_all_strings(unittest.TestCase):
    def test_generate_all_strings1(self):
        self.assertEqual(generate_all_strings('abc'),['abc', 'ab', 'ac', 'bc', 'a', 'b', 'c', ''] 
                         , msg= "Test 1 Failed")
        
    def test_generate_all_strings2(self):
        self.assertEqual(generate_all_strings('abcd'),['abcd', 'abc', 'abd', 'acd', 'bcd', 'ab', 'ac', 'ad', 'bc', 'bd', 'cd', 'a', 'b', 'c', 'd', '']
                         , msg= "Test 2 Failed")
        


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_generate_all_strings)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")