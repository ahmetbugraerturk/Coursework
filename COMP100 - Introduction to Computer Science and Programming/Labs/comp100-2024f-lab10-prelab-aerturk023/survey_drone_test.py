import unittest
import sys
from io import StringIO

from survey_drone import SurveyDrone


class TestSurveyDrone(unittest.TestCase):
    def test_1(self):
        self.drone = SurveyDrone(id="#S1001", max_speed=100, current_location=(34.0522, -118.2437), camera_quality="HD")
        self.assertEqual(self.drone.id, "#S1001")
        self.assertEqual(self.drone.max_speed, 100)
        self.assertEqual(self.drone.current_location, (34.0522, -118.2437))
        self.assertEqual(self.drone.camera_quality, "HD")
        self.assertEqual(self.drone.survey_data, [])

    def test_2(self):
        expected_output = "Survey completed!"
        captured_output = StringIO()
        sys.stdout = captured_output
        self.drone = SurveyDrone(id="#S1001", max_speed=100, current_location=(34.0522, -118.2437), camera_quality="HD")
        self.drone.scan_area([(34.0522, -118.2437), (34.0522, -118.2437), (34.0522, -118.2437)])
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)
        self.assertEqual(self.drone.survey_data, [(34.0522, -118.2437), (34.0522, -118.2437), (34.0522, -118.2437)])

    def test_3(self):
        expected_output = "Survey completed!\nSurvey completed!"
        captured_output = StringIO()
        sys.stdout = captured_output
        self.drone = SurveyDrone(id="#S1001", max_speed=100, current_location=(34.0522, -118.2437), camera_quality="4K")
        self.drone.scan_area([(34.0522, -118.2437), (34.0522, -118.2437), (34.0522, -118.2437)])
        self.drone.scan_area([(37.4, -122.1), (-42.4, 174.3), (34.0522, -118.2437)])
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)
        self.assertEqual(self.drone.survey_data, [(34.0522, -118.2437), (34.0522, -118.2437), (34.0522, -118.2437), (37.4, -122.1), (-42.4, 174.3), (34.0522, -118.2437)])

    def test_4(self):
        self.drone = SurveyDrone(id="#S1001", max_speed=100, current_location=(34.0522, -118.2437), camera_quality="4K")
        self.assertEqual(self.drone.get_type(), "Survey Drone")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSurveyDrone)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
