import unittest

from q3b import show_priority_seats


class TestShowPrioritySeats(unittest.TestCase):
    def test_1(self):
        result = show_priority_seats("First", "O|OO|O", "TBS")
        self.assertEqual(result, "Boarding Denied!")

    def test_2(self):
        result = show_priority_seats("First", "O|OO|O", "TAB")
        self.assertEqual(result, "T|BA|O")

    def test_3(self):
        result = show_priority_seats("Business", "XO|XX|OO", "NCT")
        self.assertEqual(result, "Boarding Denied!")

    def test_4(self):
        result = show_priority_seats("Economy", "XOX|OXOO|OOX", "BAHHS")
        self.assertEqual(result, "XSX|BXAH|HOX")

    def test_5(self):
        result = show_priority_seats("Economy", "XOX|OXOO|OOX", "LAH")
        self.assertEqual(result, "Boarding Denied!")

    def test_6(self):
        result = show_priority_seats("first", "O|OO|O", "TBA")
        self.assertEqual(result, "Unrecognized class!")

    def test_7(self):
        result = show_priority_seats("First", "OO|OO|OO", "TBA")
        self.assertEqual(result, "Mismatch between 'airplane_class' and 'seat_config'!")

    def test_8(self):
        result = show_priority_seats("First", "O|OO|O", "TBF")
        self.assertEqual(result, "Unrecognized hero, not allowed to board!")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestShowPrioritySeats)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
