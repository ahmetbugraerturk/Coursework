import unittest
from q1a import approximate_square_root


class TestApproximateSqrt(unittest.TestCase):
    def test_positive_integer(self):
        self.assertAlmostEqual(approximate_square_root(9), 3.0, places=3)

    def test_small_epsilon(self):
        self.assertAlmostEqual(approximate_square_root(2, epsilon=1e-10), 1.414213, places=5)

    def test_decimal_input(self):
        self.assertAlmostEqual(approximate_square_root(2.25), 1.5, places=3)

    def test_large_input(self):
        self.assertAlmostEqual(approximate_square_root(10000), 100.0, places=3)

    def test_non_perfect_square(self):
        self.assertAlmostEqual(approximate_square_root(10), 3.162, places=3)

    def test_zero_input(self):
        self.assertAlmostEqual(approximate_square_root(0), 0.0, places=3)

    def test_negative_input(self):
        self.assertIsNone(approximate_square_root(-4), "Cannot compute the square root of a negative number.")

    def test_max_iterations(self):
            result = approximate_square_root(2, epsilon=1e-20, max_iterations=10)
            self.assertIsNone(result, "The function should return None if max_iterations is reached without converging.")
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApproximateSqrt)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
