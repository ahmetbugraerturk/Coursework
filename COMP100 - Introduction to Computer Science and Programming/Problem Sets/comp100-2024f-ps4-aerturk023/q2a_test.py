import unittest
from q2a import count_files


class test_count_files(unittest.TestCase):
    def test_count_files1(self):
        self.assertEqual(count_files("root[file1(10),file2(20),files[file(15),subdir2[myfile4(25),file5(30)]]]"),5, msg= "Test 1 Failed")      
    def test_count_files2(self):
        self.assertEqual(count_files("main1[fileA(5),subdirect[fileBash(10),fileC(20)]]"), 3, msg= "Test 2 Failed")
    def test_count_files3(self):
        self.assertEqual(count_files("Docs[file1(10),fil(20),tests[file3(15),subdir2[fi(25),doc(30)]],subdir[fileB(10),fileC(20)]]"), 7, msg= "Test 3 Failed")
        


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_count_files)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")