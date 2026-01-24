# Do not change the code below!
import unittest
from q1 import check_rotation

class Testcheck_rotation(unittest.TestCase):
    def test_check_rotation1(self):
        self.assertEqual(check_rotation("abcd", "dabc"), True)
    def test_check_rotation2(self):
        self.assertEqual(check_rotation("python","npytho"), True)
    def test_check_rotation3(self):
        self.assertEqual(check_rotation("abcd","acbd"), False)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Testcheck_rotation)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")