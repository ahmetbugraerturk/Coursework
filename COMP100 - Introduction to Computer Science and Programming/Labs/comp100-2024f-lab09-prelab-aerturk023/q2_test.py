import unittest
from q2 import simulate


class test_simulate(unittest.TestCase):
    def test_simulate1(self):
        self.assertEqual(simulate('AbbaCC'), 'Aa', msg= "Test 1 Failed")
        
    def test_simulate2(self):
        self.assertEqual(simulate('AaBbCc'), 'AaBbCc', msg= "Test 2 Failed")
        
    def test_simulate3(self):
        self.assertEqual(simulate('aabaccd'),'bad', msg= "Test 3 Failed")
    def test_simulate4(self):
        self.assertEqual(simulate('AbbAxxccfggf'), 'Literal Crush!', msg="Test 4 Failed")
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_simulate)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")