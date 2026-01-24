import unittest
from ps1a import wc_count_no_bacterial_growth

class TestPartA(unittest.TestCase):

    def test_sufficient_growth_rate(self):
        days = wc_count_no_bacterial_growth(total_bacteria=1000, total_white_cells=500, white_cell_growth_rate=0.5)
        self.assertEqual(days, 2, "Expected recovery in 2 days.")

    def test_insufficient_growth_rate(self):
            result = wc_count_no_bacterial_growth(total_bacteria=10000, total_white_cells=500, white_cell_growth_rate=0.001)
            self.assertIsNone(result, "Expected 'None' return for low growth rate.")

    def test_exact_threshold(self):
        days = wc_count_no_bacterial_growth(total_bacteria=5000, total_white_cells=100, white_cell_growth_rate=0.25)
        self.assertEqual(days, 18, "Expected recovery in 18 days at threshold rate.")

    def test_strong_initial_white_cells(self):
        days = wc_count_no_bacterial_growth(total_bacteria=100, total_white_cells=150, white_cell_growth_rate=0.3)
        self.assertEqual(days, 0, "Expected 0 days as white cells are initially stronger.")

    def test_max_days_limit(self):
            result = wc_count_no_bacterial_growth(total_bacteria=50000, total_white_cells=10, white_cell_growth_rate=0.1)
            self.assertIsNone(result, "Expected 'None' return for max days limit exceeded.")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPartA)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
