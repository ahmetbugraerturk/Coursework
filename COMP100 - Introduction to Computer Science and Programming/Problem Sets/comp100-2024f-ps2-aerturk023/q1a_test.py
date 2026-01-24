import unittest

from q1a import can_assemble


class TestCanAssemble(unittest.TestCase):
    def test_1(self):
        result = can_assemble(4, "OXO|OXXO|XOO")
        self.assertEqual(result, "Yes, you may board!")

    def test_2(self):
        result = can_assemble(7, "OO|OO|OO")
        self.assertEqual(result, "Boarding Denied!")

    def test_3(self):
        result = can_assemble(3, "OX|XX|OX")
        self.assertEqual(result, "Boarding Denied!")

    def test_4(self):
        result = can_assemble(4, "OXO|OXXO|XO")
        self.assertEqual(result, "Invalid seat configuration!")

    def test_5(self):
        result = can_assemble(4, "O|Ox|x")
        self.assertEqual(result, "Invalid seat letters!")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCanAssemble)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
