import unittest
from car import Car
from turbo_charge import TurboCharge


class TestTurboCharge(unittest.TestCase):
    def test_initialization(self):
        turbo_charge = TurboCharge()
        self.assertEqual(turbo_charge.name, "TurboCharge", "Component name should be set correctly.")

    def test_apply(self):
        car = Car("Test Model", 350.0, 2.5, 5)
        turbo_charge = TurboCharge()
        turbo_charge.apply(car)
        self.assertEqual(car.top_speed, 367.5, "Top speed should be increased by 5%.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTurboCharge)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
