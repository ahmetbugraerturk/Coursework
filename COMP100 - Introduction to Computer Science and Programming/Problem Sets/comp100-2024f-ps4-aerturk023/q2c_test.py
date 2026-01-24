import unittest
from q2c import largest_file


class test_largest_file(unittest.TestCase):
    def test_largest_file1(self):
        self.assertEqual(largest_file("root[file1(10),file2(20),subdir1[file3(15),subdir2[file4(25),file5(30)]]]"),'file5', msg= "Test 1 Failed")      
    def test_largest_file2(self):
        self.assertEqual(largest_file("main[fileA(5),subdir[fileB(10),fileC(20)]]"), 'fileC', msg= "Test 2 Failed")
    def test_largest_file3(self):
        self.assertEqual(largest_file("root[file1(10),file2(20),subdir1[file3(15),subdir2[file4(25),file5(30)]],subdir[fileB(10),fileC(20)]]"), 'file5', msg= "Test 3 Failed")
        


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_largest_file)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")