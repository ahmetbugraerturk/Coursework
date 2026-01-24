import unittest
from q1b import find_polynomial_roots

class TestPolynomialRoots(unittest.TestCase):

    def test_two_real_roots(self):
        roots = find_polynomial_roots(1, -3, 2)  # x^2 - 3x + 2 = 0
        self.assertAlmostEqual(roots[0], 2.0, places=7)
        self.assertAlmostEqual(roots[1], 1.0, places=7)

    def test_one_real_root(self):
        roots = find_polynomial_roots(1, -2, 1)  # x^2 - 2x + 1 = 0
        self.assertAlmostEqual(roots[0], 1.0, places=7)
        self.assertAlmostEqual(roots[1], 1.0, places=7)

    def test_no_real_roots(self):
        roots = find_polynomial_roots(1, 0, 1)  # x^2 + 1 = 0
        self.assertIsNone(roots)

    def test_large_coefficients(self):
        roots = find_polynomial_roots(1000, 500, -400)  # 1000x^2 + 500x + 400 = 0
        self.assertAlmostEqual(roots[0], 0.43007352543677213, places=7)
        self.assertAlmostEqual(roots[1], -0.9300735254367721, places=7)

    def test_zero_coefficients(self):
        roots = find_polynomial_roots(0, 1, 0)  # 0*x^2 + 1*x + 0 = 0
        self.assertAlmostEqual(roots[0], 0.0, places=7)  # Only one root is 0

    def test_invalid_case(self):
        roots = find_polynomial_roots(0, 0, 0)  # No valid equation
        self.assertIsNone(roots) # Expect None

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPolynomialRoots)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
