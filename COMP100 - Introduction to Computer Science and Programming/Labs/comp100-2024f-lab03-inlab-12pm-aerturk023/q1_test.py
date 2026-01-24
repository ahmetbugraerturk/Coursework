import unittest
from math import pi
from q1 import approximate_pi

class TestApproximatePi(unittest.TestCase):
    def test_default_parameters(self):
        """Test with default parameters."""
        result = approximate_pi()
        self.assertIsNotNone(result)  # Check that the result is not None
        self.assertAlmostEqual(result, pi, delta=1e-4)  # Check if close to actual pi

    def test_small_epsilon(self):
        """Test with a small epsilon value."""
        result = approximate_pi(max_iterations=10000000, epsilon=1e-6)
        self.assertIsNotNone(result)  # Check that the result is not None
        self.assertAlmostEqual(result, pi, delta=1e-6)  # Check if close to actual pi

    def test_max_iterations_without_convergence(self):
        """Test with a scenario where max_iterations is not sufficient."""
        result = approximate_pi(max_iterations=100, epsilon=1e-10)
        self.assertIsNone(result)  # Check that the result is None

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApproximatePi)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
