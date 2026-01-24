import unittest

from q3a import can_allocate_priority_seats


class TestCanAllocatePrioritySeats(unittest.TestCase):
    def test_1(self):
        result = can_allocate_priority_seats("First", "O|OO|O", "TBS")
        self.assertEqual(result, "Boarding Denied!")

    def test_2(self):
        result = can_allocate_priority_seats("First", "O|OO|O", "TAB")
        self.assertEqual(result, "Yes, you may board!")

    def test_3(self):
        result = can_allocate_priority_seats("Business", "XO|XX|OO", "TNC")
        self.assertEqual(result, "Boarding Denied!")

    def test_4(self):
        result = can_allocate_priority_seats("Economy", "XOX|OXOO|OOX", "BAHHS")
        self.assertEqual(result, "Yes, you may board!")

    def test_5(self):
        result = can_allocate_priority_seats("first", "O|OO|O", "TBA")
        self.assertEqual(result, "Unrecognized class!")

    def test_6(self):
        result = can_allocate_priority_seats("First", "OO|OO|OO", "TBA")
        self.assertEqual(result, "Mismatch between 'airplane_class' and 'seat_config'!")

    def test_7(self):
        result = can_allocate_priority_seats("First", "O|OO|O", "TBF")
        self.assertEqual(result, "Unrecognized hero, not allowed to board!")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCanAllocatePrioritySeats)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
