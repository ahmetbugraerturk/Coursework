import unittest
from car import Car


class TestCar(unittest.TestCase):
    def test_initialization(self):
        car = Car("Mercedes F1 W11", 360.0, 2.4, 9)
        self.assertEqual(car.model, "Mercedes F1 W11", "Car model should be set correctly.")
        self.assertEqual(car.top_speed, 360.0, "Top speed should be set correctly.")
        self.assertAlmostEqual(car.acceleration, 2.4, delta=0.02, msg="Acceleration should be set correctly.")
        self.assertEqual(car.handling, 9, "Handling should be set correctly.")

    def test_invalid_type_model(self):
        with self.assertRaises(TypeError):
            _ = Car(123, 360.0, 2.4, 9)

    def test_invalid_type_top_speed(self):
        with self.assertRaises(TypeError):
            _ = Car("Mercedes F1 W11", "360", 2.4, 9)

    def test_invalid_type_acceleration(self):
        with self.assertRaises(TypeError):
            _ = Car("Mercedes F1 W11", 360.0, "2.4", 9)

    def test_invalid_type_handling(self):
        with self.assertRaises(TypeError):
            _ = Car("Mercedes F1 W11", 360.0, 2.4, "9")

    def test_top_speed_out_of_range(self):
        with self.assertRaises(ValueError):
            _ = Car("Mercedes F1 W11", 400.0, 2.4, 9)

    def test_acceleration_out_of_range(self):
        with self.assertRaises(ValueError):
            _ = Car("Mercedes F1 W11", 360.0, 2.7, 9)

    def test_handling_out_of_range(self):
        with self.assertRaises(ValueError):
            _ = Car("Mercedes F1 W11", 360.0, 2.4, 11)

    def test_calculate_lap_time(self):
        car = Car("Mercedes F1 W11", 360.0, 2.6, 10)
        track_length = 6.17
        lap_time = car.calculate_lap_time(track_length)
        self.assertIsInstance(lap_time, float, "Lap time should be a float.")
        self.assertAlmostEqual(lap_time, 1.3368, delta=0.02, msg="Acceleration should be set correctly.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCar)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
