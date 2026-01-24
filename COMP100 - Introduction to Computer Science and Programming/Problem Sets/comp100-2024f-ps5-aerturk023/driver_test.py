import unittest
from driver import Driver


class TestDriver(unittest.TestCase):
    def test_initialization(self):
        driver = Driver("Lewis Hamilton", 9, 0.2)
        self.assertEqual(driver.name, "Lewis Hamilton", "Driver name should be set correctly.")
        self.assertEqual(driver.experience, 9, "Experience level should be set correctly.")
        self.assertAlmostEqual(driver.reaction_time, 0.2, delta=0.02, msg="Reaction time should be set correctly.")

    def test_invalid_type_name(self):
        with self.assertRaises(TypeError):
            _ = Driver(123, 9, 0.2)

    def test_invalid_type_experience(self):
        with self.assertRaises(TypeError):
            _ = Driver("Lewis Hamilton", "9", 0.2)

    def test_invalid_type_reaction_time(self):
        with self.assertRaises(TypeError):
            _ = Driver("Lewis Hamilton", 9, "0.2")

    def test_experience_out_of_range(self):
        with self.assertRaises(ValueError):
            _ = Driver("Lewis Hamilton", 11, 0.2)

    def test_reaction_time_out_of_range(self):
        with self.assertRaises(ValueError):
            _ = Driver("Lewis Hamilton", 9, 1.1)

    def test_str_representation(self):
        driver = Driver("Lewis Hamilton", 9, 0.2)
        expected_str = "Lewis Hamilton, Experience: 9, Reaction Time: 0.2s"
        self.assertEqual(str(driver), expected_str, msg="String representation is incorrect.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDriver)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
