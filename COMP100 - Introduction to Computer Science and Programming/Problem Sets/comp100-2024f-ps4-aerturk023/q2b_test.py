import unittest
from q2b import sum_file_sizes


class test_sum_file_sizes(unittest.TestCase):
    def test_sum_file_sizes1(self):
        self.assertEqual(sum_file_sizes("rootText[file1(10),file2o(20),subdirT[filetrash(15),subdir2[file4(25),file5(30)]]]"),100, msg= "Test 1 Failed")      
    def test_sum_file_sizes2(self):
        self.assertEqual(sum_file_sizes("main[fileAT(5),subdir[fileB(10),filetrash(20)]]"), 35, msg= "Test 2 Failed")
    def test_sum_file_sizes3(self):
        self.assertEqual(sum_file_sizes("root12[file1(10),file2(20),subdir1[file3(15),subdir2[file4(25),file5(30)]],subdir[fileB(10),fileC(20)]]"), 130, msg= "Test 3 Failed")
        


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_sum_file_sizes)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")