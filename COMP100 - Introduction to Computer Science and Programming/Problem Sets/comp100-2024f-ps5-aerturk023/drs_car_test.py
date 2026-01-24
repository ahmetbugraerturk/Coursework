import unittest
from drs_car import DRSCar


class TestDRSCar(unittest.TestCase):
    def test_init(self):
        car = DRSCar("Mercedes F1 W11", 360.0, 2.4, 9)
        self.assertEqual(car.model, "Mercedes F1 W11")
        self.assertEqual(car.top_speed, 360.0)
        self.assertEqual(car.acceleration, 2.4)
        self.assertEqual(car.handling, 9)
        self.assertFalse(car.drs_active)

    def test_activate_drs(self):
        car = DRSCar("Mercedes F1 W11", 360.0, 2.4, 9)
        car.activate_drs()
        self.assertEqual(car.top_speed, 360.0)
        self.assertEqual(car.acceleration, 2.4)
        self.assertEqual(car.handling, 9)
        self.assertTrue(car.drs_active)

    def test_deactivate_drs(self):
        car = DRSCar("Mercedes F1 W11", 360.0, 2.4, 9)
        car.activate_drs()
        car.deactivate_drs()
        self.assertEqual(car.top_speed, 360.0)
        self.assertEqual(car.acceleration, 2.4)
        self.assertEqual(car.handling, 9)
        self.assertFalse(car.drs_active)

    def test_calculate_lap_time(self):
        car = DRSCar("Mercedes F1 W11", 360.0, 2.4, 9)
        car.activate_drs()
        lap_time = car.calculate_lap_time(5.79)
        self.assertAlmostEqual(lap_time, 1.20249, delta=0.02)

        car.deactivate_drs()
        lap_time = car.calculate_lap_time(5.79)
        self.assertAlmostEqual(lap_time, 1.28666, delta=0.02)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDRSCar)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
