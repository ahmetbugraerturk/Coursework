import unittest
from drone import Drone


class TestDrone(unittest.TestCase):
    def setUp(self):
        self.drone = Drone(id="#D1001", max_speed=100, current_location=(34.0522, -118.2437))

    def test_1(self):
        self.assertEqual(self.drone.id, "#D1001")
        self.assertEqual(self.drone.max_speed, 100)
        self.assertEqual(self.drone.current_location, (34.0522, -118.2437))

    def test_2(self):
        new_location = (40.7128, -74.0060)
        self.drone.move_to(new_location)
        self.assertEqual(self.drone.current_location, new_location)

    def test_3(self):
        drone_type = self.drone.get_type()
        self.assertEqual(drone_type, "Generic Drone")

    def test_4(self):
        self.assertIsInstance(self.drone.current_location, tuple)
        self.assertEqual(len(self.drone.current_location), 2)
        self.assertIsInstance(self.drone.current_location[0], float)
        self.assertIsInstance(self.drone.current_location[1], float)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDrone)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
