import unittest
import sys
from io import StringIO

from delivery_drone import DeliveryDrone


class TestDeliveryDrone(unittest.TestCase):
    def test_1(self):
        self.drone = DeliveryDrone(id="#D1001", max_speed=100, current_location=(34.0522, -118.2437), cargo_capacity=100)
        self.assertEqual(self.drone.id, "#D1001")
        self.assertEqual(self.drone.max_speed, 100)
        self.assertEqual(self.drone.current_location, (34.0522, -118.2437))
        self.assertEqual(self.drone.cargo_capacity, 100)
        self.assertEqual(self.drone.current_cargo, 0)

    def test_2(self):
        self.drone = DeliveryDrone(id="#D1001", max_speed=100, current_location=(34.0522, -118.2437), cargo_capacity=100)
        self.drone.load_cargo(50)
        self.assertEqual(self.drone.current_cargo, 50)

    def test_3(self):
        self.drone = DeliveryDrone(id="#D1001", max_speed=100, current_location=(34.0522, -118.2437), cargo_capacity=100)
        self.drone.load_cargo(100)
        self.assertEqual(self.drone.current_cargo, 100)

    def test_4(self):
        expected_output = "Weight exceeds maximum capacity!"
        captured_output = StringIO()
        sys.stdout = captured_output
        self.drone = DeliveryDrone(id="#D1001", max_speed=100, current_location=(34.0522, -118.2437), cargo_capacity=100)
        self.drone.load_cargo(150)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_5(self):
        expected_output = "Weight exceeds maximum capacity!"
        captured_output = StringIO()
        sys.stdout = captured_output
        self.drone = DeliveryDrone(id="#D1001", max_speed=100, current_location=(34.0522, -118.2437), cargo_capacity=100)
        self.drone.load_cargo(50)
        self.drone.load_cargo(60)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_6(self):
        expected_output = "Cargo delivered successfully!"
        captured_output = StringIO()
        sys.stdout = captured_output
        self.drone = DeliveryDrone(id="#D1001", max_speed=100, current_location=(34.0522, -118.2437), cargo_capacity=100)
        self.drone.load_cargo(50)
        self.drone.deliver_cargo()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)
        self.assertEqual(self.drone.current_cargo, 0)


    def test_7(self):
        self.drone = DeliveryDrone(id="#D1001", max_speed=100, current_location=(34.0522, -118.2437), cargo_capacity=100)
        self.assertEqual(self.drone.get_type(), "Delivery Drone")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDeliveryDrone)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
