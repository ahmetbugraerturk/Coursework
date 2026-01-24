# Do not change the code below
import unittest
from q2 import compress_string

class Testcompress_string(unittest.TestCase):
    def test_compress_string1(self):
        self.assertEqual(compress_string("aabcccccaaa"), "a2b1c5a3")
    def test_compress_string2(self):
        self.assertEqual(compress_string("abcdef"), "abcdef")
    def test_compress_string3(self):
        self.assertEqual(compress_string("aabb"), "aabb")
    def test_compress_string4(self):
        self.assertEqual(compress_string(""), "")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Testcompress_string)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
