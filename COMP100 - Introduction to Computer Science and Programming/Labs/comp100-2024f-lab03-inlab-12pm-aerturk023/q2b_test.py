import unittest
from q2b import bisection_method_for_extrema
from q2a import f

class TestBisectionMethodForExtrema(unittest.TestCase):
    def test_extremum_with_default_interval(self):
        """Test the default interval for the extremum."""
        extremum_x = bisection_method_for_extrema()
        extremum_y = f(extremum_x)
        self.assertAlmostEqual(extremum_y, -36.633611485063156, places=7)  

    def test_extremum_with_custom_interval(self):
        """Test a custom interval that is known to contain an extremum."""
        extremum_x = bisection_method_for_extrema(a=0, b=10)
        extremum_y = f(extremum_x)
        self.assertAlmostEqual(extremum_y, -36.633611485063156, places=7) 

    def test_extremum_convergence_with_small_epsilon(self):
        """Test convergence with a very small epsilon."""
        extremum_x = bisection_method_for_extrema(epsilon=1e-10)
        extremum_y = f(extremum_x)
        self.assertAlmostEqual(extremum_y, -36.633611485063156, places=7)

    def test_extremum_at_known_location(self):
        """Test for known extremum location."""
        extremum_x = bisection_method_for_extrema(a=1, b=12)
        self.assertAlmostEqual(extremum_x, 4.3093938594684005, places=7)  

    def test_return_type(self):
        """Ensure that the function returns a float."""
        extremum_x = bisection_method_for_extrema()
        self.assertIsInstance(extremum_x, float)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBisectionMethodForExtrema)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
