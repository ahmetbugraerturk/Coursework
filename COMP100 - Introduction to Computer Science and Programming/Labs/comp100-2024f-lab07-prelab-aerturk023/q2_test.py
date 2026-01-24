import unittest
from q2 import compute_bill, stock

class TestComputeBill(unittest.TestCase):
    def setUp(self):
        """Reset the global stock dictionary before each test."""
        global stock
        stock.update({  # Reset stock to its original values
            "ram": 6,
            "ssd": 0,
            "monitor": 32,
            "power_supply": 15,
            "keyboard": 20
        })

    def test_basic_order(self):
        order = ["ram", "ssd", "monitor"]
        expected_bill = 275  # Only "ram" and "monitor" are in stock
        self.assertEqual(compute_bill(order), expected_bill)
        self.assertEqual(stock["ram"], 5)  # Stock decreases for "ram"
        self.assertEqual(stock["monitor"], 31)  # Stock decreases for "monitor"
        self.assertEqual(stock["ssd"], 0)  # No change for "ssd"

    def test_partial_order(self):
        order = ["monitor", "keyboard"]
        expected_bill = 245  # Monitor: 220, Keyboard: 25
        self.assertEqual(compute_bill(order), expected_bill)
        self.assertEqual(stock["monitor"], 31)  # Stock decreases for "monitor"
        self.assertEqual(stock["keyboard"], 19)  # Stock decreases for "keyboard"

    def test_out_of_stock_item(self):
        order = ["ssd"]
        expected_bill = 0  # "ssd" is out of stock
        self.assertEqual(compute_bill(order), expected_bill)
        self.assertEqual(stock["ssd"], 0)  # Stock remains unchanged

    def test_no_order(self):
        order = []
        expected_bill = 0  # No items ordered
        self.assertEqual(compute_bill(order), expected_bill)
        self.assertEqual(stock, {  # Stock remains unchanged
            "ram": 6,
            "ssd": 0,
            "monitor": 32,
            "power_supply": 15,
            "keyboard": 20
        })

    def test_multiple_quantities(self):
        order = ["ram", "ram", "ram"]
        expected_bill = 165  # 3 RAMs: 55 * 3
        self.assertEqual(compute_bill(order), expected_bill)
        self.assertEqual(stock["ram"], 3)  # Stock decreases by 3

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestComputeBill)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
