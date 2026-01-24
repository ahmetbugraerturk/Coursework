import unittest
import random
from driver import Driver
from car import Car
from drs_car import DRSCar
from track import Track
from race import Race


class TestRace(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        self.track = Track("Monza", 5.79, 11, 5)
        self.drivers = [Driver("Max Verstappen", 8, 0.25), Driver("Charles Leclerc", 6, 0.22), Driver("Lewis Hamilton", 10, 0.2)]
        self.cars = [Car("Red Bull RB16", 350.0, 2.5, 8), Car("Ferrari F1", 350.0, 2.6, 8), Car("Mercedes F1 W11", 360.0, 2.4, 10)]
        self.drs_cars = [DRSCar("Red Bull RB16", 350.0, 2.5, 8), DRSCar("Ferrari F1", 350.0, 2.6, 8), DRSCar("Mercedes F1 W11", 360.0, 2.4, 10)]
        self.number_of_laps = 20
        self.race = Race(self.track, self.drivers, self.cars, self.number_of_laps, "Sunny")

    def test_initialization(self):
        race = Race(self.track, self.drivers, self.cars, self.number_of_laps, "Sunny")
        drs_race = Race(self.track, self.drivers, self.drs_cars, self.number_of_laps, "Sunny")
        self.assertEqual(race.track, self.track, "Track should be set correctly.")
        self.assertEqual(race.drivers, self.drivers, "Drivers should be set correctly.")
        self.assertEqual(race.cars, self.cars, "Cars should be set correctly.")
        self.assertEqual(drs_race.cars, self.drs_cars, "Cars should be set correctly.")
        self.assertEqual(race.number_of_laps, self.number_of_laps, "Number of laps should be set correctly.")
        self.assertEqual(race.weather_condition, "Sunny", "Weather condition should be set correctly.")

    def test_race_in_rainy_weather(self):
        race = Race(self.track, self.drivers, self.cars, self.number_of_laps, "Rainy")
        race_results = race.start_race()
        expected_time = 64.366480
        self.assertAlmostEqual(race_results[0][1], expected_time, delta=0.02, msg=f"Total time in rainy weather should be {expected_time}")

    def test_drs_race_in_rainy_weather(self):
        race = Race(self.track, self.drivers, self.drs_cars, self.number_of_laps, "Rainy")
        race_results = race.start_race()
        expected_time = 64.366480
        self.assertAlmostEqual(race_results[0][1], expected_time, delta=0.02, msg=f"Total time in rainy weather should be {expected_time}")

    def test_race_in_foggy_weather(self):
        race = Race(self.track, self.drivers, self.cars, self.number_of_laps, "Foggy")
        race_results = race.start_race()
        expected_time = 65.701320
        self.assertAlmostEqual(race_results[0][1], expected_time, delta=0.02, msg=f"Total time in foggy weather should be {expected_time}")

    def test_drs_race_in_foggy_weather(self):
        race = Race(self.track, self.drivers, self.drs_cars, self.number_of_laps, "Foggy")
        race_results = race.start_race()
        expected_time = 65.701320
        self.assertAlmostEqual(race_results[0][1], expected_time, delta=0.02, msg=f"Total time in foggy weather should be {expected_time}")

    def test_race_with_random_event(self):
        race = Race(self.track, self.drivers, self.cars, self.number_of_laps, "Sunny")
        race_results = race.start_race()
        expected_time = 61.696799
        self.assertAlmostEqual(race_results[0][1], expected_time, delta=0.02, msg=f"Total time with random events should be {expected_time}")

    def test_drs_race_with_random_event(self):
        race = Race(self.track, self.drivers, self.drs_cars, self.number_of_laps, "Sunny")
        race_results = race.start_race()
        expected_time = 61.548316
        self.assertAlmostEqual(race_results[0][1], expected_time, delta=0.02, msg=f"Total time with random events should be {expected_time}")

    def test_drs_race_with_random_event_lap_2(self):
        race = Race(self.track, self.drivers, self.drs_cars, 2, "Sunny")
        race_results = race.start_race()
        expected_time = 2.66968
        self.assertAlmostEqual(race_results[0][1], expected_time, delta=0.02, msg=f"Total time with random events should be {expected_time}")

    def test_invalid_weather_condition(self):
        with self.assertRaises(ValueError):
            _ = Race(self.track, self.drivers, self.cars, self.number_of_laps, "Stormy")

    def test_driver_skill_impact(self):
        race_results = self.race.start_race()
        time_difference = race_results[0][1] - race_results[1][1]
        self.assertNotEqual(time_difference, 0, "Driver skill should impact the total race time.")

    def test_driver_reaction_time_impact(self):
        race_results = self.race.start_race()
        self.assertNotEqual(race_results[0][1], race_results[1][1], "Driver reaction time should impact the total race time.")

    def test_sorted_race_results(self):
        race_results = self.race.start_race()
        sorted_times = sorted([result[1] for result in race_results])
        race_times = [result[1] for result in race_results]
        self.assertEqual(race_times, sorted_times, "Race results should be sorted by time.")

    def test_fastest_time_at_index_zero(self):
        race_results = self.race.start_race()
        self.assertEqual(race_results[0][1], min(result[1] for result in race_results), "Fastest time should be at index 0 in race results.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRace)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
