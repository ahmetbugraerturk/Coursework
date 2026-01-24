import unittest
from advanced_tires import AdvancedTires
from car import Car


class TestAdvancedTires(unittest.TestCase):
    def test_initialization(self):
        advanced_tires = AdvancedTires()
        self.assertEqual(advanced_tires.name, "AdvancedTires", "Component name should be set correctly.")

    def test_apply(self):
        car = Car("Test Model", 350.0, 2.5, 5)
        advanced_tires = AdvancedTires()
        advanced_tires.apply(car)
        self.assertEqual(car.handling, 7, "Handling should be improved by 2.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAdvancedTires)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
