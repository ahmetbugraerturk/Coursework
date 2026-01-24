import unittest
from ps1c import find_acceptable_wc_growth_rate

class TestPartC(unittest.TestCase):

    def test_acceptable_growth_rate_found(self):
        result = find_acceptable_wc_growth_rate(total_bacteria=10000, total_white_cells=500, bacterial_growth_rate=0.1)
        self.assertIsNotNone(result, "Expected an acceptable white cell production rate.")
        bacteria, white_cells, white_cell_growth_rate = result
        self.assertTrue(bacteria - 1000 <= white_cells <= bacteria + 1000, "White cells should be within acceptable range of bacteria.")

    def test_bacteria_growth_outpaces_white_cells(self):
            result = find_acceptable_wc_growth_rate(total_bacteria=10000, total_white_cells=50, bacterial_growth_rate=0.8)
            self.assertIsNone(result, "Expected 'None' return when white cells cannot match bacterial growth.")
    
    def test_exact_result(self):
        result = find_acceptable_wc_growth_rate(total_bacteria=65000, total_white_cells=40000, bacterial_growth_rate=0.1)
        self.assertIsNotNone(result, "Expected an acceptable white cell production rate.")
        bacteria, white_cells, white_cell_growth_rate = result
        self.assertTrue(bacteria - 1000 <= white_cells <= bacteria + 1000, "White cells should be within acceptable range of bacteria.")
        self.assertAlmostEqual(white_cell_growth_rate, 0.117919921875, delta=1e-2)

    
    def test_no_bacteria_reproduction_result(self):
        result = find_acceptable_wc_growth_rate(total_bacteria=60000, total_white_cells=60000, bacterial_growth_rate=0.0)
        self.assertIsNotNone(result, "Expected an acceptable white cell production rate.")
        bacteria, white_cells, white_cell_growth_rate = result
        self.assertTrue(bacteria - 1000 <= white_cells <= bacteria + 1000, "White cells should be within acceptable range of bacteria.")
        self.assertAlmostEqual(white_cell_growth_rate, 0.0, delta=1e-2)

    
    def test_low_initial_white_cells_with_slow_bacterial_growth(self):
        result = find_acceptable_wc_growth_rate(total_bacteria=20000, total_white_cells=10000, bacterial_growth_rate=0.05)
        self.assertIsNotNone(result, "Expected an acceptable white cell production rate for low bacterial growth.")
        bacteria, white_cells, white_cell_growth_rate = result
        self.assertTrue(bacteria - 1000 <= white_cells <= bacteria + 1000, "White cells should be within acceptable range of bacteria.")

    def test_high_initial_bacteria_count(self):
            result = find_acceptable_wc_growth_rate(total_bacteria=50000000, total_white_cells=3, bacterial_growth_rate=0.2)
            self.assertIsNone(result, "Expected 'None' return when initial bacteria count is significantly higher than white cells.")

    def test_initial_white_cells_greater_than_bacteria(self):
        result = find_acceptable_wc_growth_rate(total_bacteria=30000, total_white_cells=60000, bacterial_growth_rate=0.1)
        self.assertIsNotNone(result, "Expected an acceptable white cell production rate when initial white cells outnumber bacteria.")
        bacteria, white_cells, white_cell_growth_rate = result
        self.assertTrue(bacteria - 1000 <= white_cells <= bacteria + 1000, "White cells should be within acceptable range of bacteria.")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPartC)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
