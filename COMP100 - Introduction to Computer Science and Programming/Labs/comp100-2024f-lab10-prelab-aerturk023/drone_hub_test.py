import unittest
import sys
from io import StringIO

from drone import Drone
from delivery_drone import DeliveryDrone
from survey_drone import SurveyDrone
from drone_hub import DroneHub


class TestDroneHub(unittest.TestCase):
    def test_1(self):
        self.hub = DroneHub("Central Fleet")
        self.assertEqual(self.hub.name, "Central Fleet")
        self.assertEqual(self.hub.drones, [])

    def test_2(self):
        self.hub = DroneHub("Central Fleet")
        self.hub.add_drone(Drone(id="#D1001", max_speed=100, current_location=(34.0522, -118.2437)))
        self.assertEqual(len(self.hub.drones), 1)
        self.assertEqual(self.hub.drones[0].id, "#D1001")
        self.assertEqual(self.hub.drones[0].max_speed, 100)
        self.assertEqual(self.hub.drones[0].current_location, (34.0522, -118.2437))

    def test_3(self):
        self.hub = DroneHub("Central Fleet")
        self.hub.add_drone(Drone(id="#D1001", max_speed=100, current_location=(34.0522, -118.2437)))
        self.hub.add_drone(Drone(id="#D1002", max_speed=100, current_location=(34.0522, -118.2437)))
        self.assertEqual(len(self.hub.drones), 2)
        self.assertEqual(self.hub.drones[0].id, "#D1001")
        self.assertEqual(self.hub.drones[1].id, "#D1002")

    def test_4(self):
        self.hub = DroneHub("Central Fleet")
        self.hub.add_drone(DeliveryDrone(id="#D1001", max_speed=100, current_location=(34.0522, -118.2437), cargo_capacity=100))
        self.hub.add_drone(SurveyDrone(id="#S1001", max_speed=100, current_location=(34.0522, -118.2437), camera_quality="HD"))
        self.assertEqual(len(self.hub.drones), 2)
        self.assertEqual(self.hub.drones[0].id, "#D1001")
        self.assertEqual(self.hub.drones[1].id, "#S1001")

    def test_5(self):
        expected_output = "Drone ID: #D1001, Type: Delivery Drone\nDrone ID: #S1001, Type: Survey Drone"
        captured_output = StringIO()
        sys.stdout = captured_output
        self.hub = DroneHub("Central Fleet")
        self.hub.add_drone(DeliveryDrone(id="#D1001", max_speed=100, current_location=(34.0522, -118.2437), cargo_capacity=100))
        self.hub.add_drone(SurveyDrone(id="#S1001", max_speed=100, current_location=(34.0522, -118.2437), camera_quality="HD"))
        self.hub.list_drones()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_6(self):
        self.hub = DroneHub("Central Fleet")
        self.hub.add_drone(DeliveryDrone(id="#D1001", max_speed=100, current_location=(34.0522, -118.2437), cargo_capacity=100))
        self.hub.add_drone(SurveyDrone(id="#S1001", max_speed=100, current_location=(34.0522, -118.2437), camera_quality="HD"))
        self.hub.relocate_all_drones((50.0, -120.0))
        self.assertEqual(all(drone.current_location == (50.0, -120.0) for drone in self.hub.drones), True)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDroneHub)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
