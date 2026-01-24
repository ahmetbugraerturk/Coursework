import unittest
from car import Car
from light_weight_body import LightweightBody


class TestLightweightBody(unittest.TestCase):
    def test_init(self):
        lightweight_body = LightweightBody()
        self.assertEqual(lightweight_body.name, "LightweightBody")

    def test_apply(self):
        lightweight_body = LightweightBody()
        car = Car("Test Model", 350.0, 2.5, 5)
        car.acceleration = 10
        lightweight_body.apply(car)
        self.assertEqual(car.acceleration, 9.5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLightweightBody)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
