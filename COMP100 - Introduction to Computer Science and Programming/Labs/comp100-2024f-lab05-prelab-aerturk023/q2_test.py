# Do not change below
import unittest
from q2 import remove_adjacent_duplicates

class test_remove_adjacent_duplicates(unittest.TestCase):

    def test_remove_adjacent_duplicates1(self):
        self.assertEqual(remove_adjacent_duplicates("abbacadd"), "ca")
    
    def test_eremove_adjacent_duplicates2(self):
        self.assertEqual(remove_adjacent_duplicates("compp1100"), "com")

    def test_remove_adjacent_duplicates3(self):
        self.assertEqual(remove_adjacent_duplicates("remove"), "remove")

    def test_remove_adjacent_duplicates4(self):
        self.assertEqual(remove_adjacent_duplicates("addtwoo"), "atw")
        

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(test_remove_adjacent_duplicates)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")