import unittest
from track import Track


class TestTrack(unittest.TestCase):
    def test_track_name_initialization(self):
        track = Track("Monza", 5.79, 11, 5)
        self.assertEqual(track.name, "Monza", "Track name should be set correctly.")

    def test_track_lap_length_initialization(self):
        track = Track("Monza", 5.79, 11, 5)
        self.assertAlmostEqual(track.lap_length, 5.79, delta=0.02, msg="Lap length should be set correctly.")

    def test_track_number_of_turns_initialization(self):
        track = Track("Monza", 5.79, 11, 5)
        self.assertEqual(track.number_of_turns, 11, "Number of turns should be set correctly.")

    def test_track_difficulty_initialization(self):
        track = Track("Monza", 5.79, 11, 5)
        self.assertEqual(track.difficulty, 5, "Difficulty should be set correctly.")

    def test_invalid_name_type(self):
        with self.assertRaises(TypeError):
            _ = Track(123, 5.79, 11, 5)

    def test_invalid_lap_length_type(self):
        with self.assertRaises(TypeError):
            _ = Track("Monza", "5.79", 11, 5)

    def test_invalid_number_of_turns_type(self):
        with self.assertRaises(TypeError):
            _ = Track("Monza", 5.79, "11", 5)

    def test_invalid_difficulty_type(self):
        with self.assertRaises(TypeError):
            _ = Track("Monza", 5.79, 11, "5")

    def test_out_of_range_lap_length(self):
        with self.assertRaises(ValueError):
            _ = Track("Monza", 8.0, 11, 5)

    def test_out_of_range_number_of_turns(self):
        with self.assertRaises(ValueError):
            _ = Track("Monza", 5.79, 30, 5)

    def test_out_of_range_difficulty(self):
        with self.assertRaises(ValueError):
            _ = Track("Monza", 5.79, 11, 12)

    def test_str_representation(self):
        track = Track("Monza", 5.79, 11, 5)
        self.assertEqual(str(track), "Monza, Lap Length: 5.79 km, Number of Turns: 11, Difficulty: 5", "String representation is incorrect.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTrack)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
