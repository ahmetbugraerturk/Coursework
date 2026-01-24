# Do not change below
import unittest
from q3b import add_binary


class test_add_binary(unittest.TestCase):
    def test_add_binary1(self):
        self.assertEqual(add_binary('0b1010','0b1011'),'0b10101', msg= "Test 1 Failed")
        
    def test_add_binary2(self):
        self.assertEqual(add_binary('0b11','0b1'),'0b100', msg= "Test 2 Failed")
        
    def test_add_binary3(self):
        self.assertEqual(add_binary('0b001','0b010'),'0b11', msg= "Test 3 Failed")
        
    def test_add_binary4(self):
        self.assertEqual(add_binary('0b10101', '0b1001'),'0b11110', msg= "Test 4 Failed")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_add_binary)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")