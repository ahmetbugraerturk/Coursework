import unittest
from q3 import find_primes

class TestFindPrimes(unittest.TestCase):
    def test_start_2_end_10(self):
        self.assertEqual(find_primes(2, 10), "2, 3, 5, 7")
    def test_start_10_end_20(self):
        self.assertEqual(find_primes(10, 20), "11, 13, 17, 19")
    def test_start_20_end_30(self):
        self.assertEqual(find_primes(20, 30), "23, 29")
    def test_start_30_end_40(self):
        self.assertEqual(find_primes(30, 40), "31, 37")
    def test_start_40_end_50(self):
        self.assertEqual(find_primes(40, 50), "41, 43, 47")
    def test_start_50_end_60(self):
        self.assertEqual(find_primes(50, 60), "53, 59")
    def test_start_60_end_70(self):
        self.assertEqual(find_primes(60, 70), "61, 67")
    def test_start_70_end_80(self):
        self.assertEqual(find_primes(70, 80), "71, 73, 79")
    def test_start_80_end_90(self):
        self.assertEqual(find_primes(80, 90), "83, 89")
    def test_start_90_end_100(self):
        self.assertEqual(find_primes(90, 100), "97")
    def test_start_100_end_110(self):
        self.assertEqual(find_primes(100, 110), "101, 103, 107, 109")
    def test_start_110_end_120(self):
        self.assertEqual(find_primes(110, 120), "113")
    def test_start_120_end_130(self):
        self.assertEqual(find_primes(120, 130), "127")
    def test_start_130_end_140(self):
        self.assertEqual(find_primes(130, 140), "131, 137, 139")
    def test_no_primes_found(self):
        self.assertEqual(find_primes(170, 172), "No prime numbers found")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFindPrimes)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
