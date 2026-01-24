import unittest

from q2a import can_board_with_preference


class TestCanBoardWithPreference(unittest.TestCase):
    def test_1(self):
        result = can_board_with_preference(2, "OXO|OXXO|XOO", "W")
        self.assertEqual(result, "Yes, you may board!")

    def test_2(self):
        result = can_board_with_preference(3, "OO|OO|OO", "A")
        self.assertEqual(result, "Yes, you may board!")

    def test_3(self):
        result = can_board_with_preference(3, "OX|XX|OO", "W")
        self.assertEqual(result, "Boarding Denied!")

    def test_4(self):
        result = can_board_with_preference(3, "OXO|XOOX|XOO", "M")
        self.assertEqual(result, "Yes, you may board!")

    def test_5(self):
        result = can_board_with_preference(1, "OXO|XOOX|XOO", "D")
        self.assertEqual(result, "Yes, you may board!")

    def test_6(self):
        result = can_board_with_preference(3, "OO|OO|OO", "Z")
        self.assertEqual(result, "Invalid seat preference!")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCanBoardWithPreference)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
