import unittest
from q1 import count_paths


class test_count_paths(unittest.TestCase):
    def test_count_paths1(self):
        self.assertEqual(count_paths(3,3), 6, msg= "Test 1 Failed")
    def test_count_paths2(self):
        self.assertEqual(count_paths(2,4), 4, msg= "Test 2 Failed")
    def test_count_paths3(self):
        self.assertEqual(count_paths(1,1), 1, msg= "Test 3 Failed")
    def test_count_paths4(self):
        self.assertEqual(count_paths(5,3), 15, msg= "Test 4 Failed")
    def test_count_paths5(self):
        self.assertEqual(count_paths(0,0), 0, msg= "Test 5 Failed")
        


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_count_paths)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")