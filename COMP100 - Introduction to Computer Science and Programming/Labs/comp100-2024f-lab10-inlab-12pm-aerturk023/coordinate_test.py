import unittest
from coordinate import Coordinate

class TestCoordinate(unittest.TestCase):
    def test_1(self):
        coord = Coordinate(3, 4)
        self.assertEqual(coord.x, 3, "x should be set correctly.")
        self.assertEqual(coord.y, 4, "y should be set correctly.")


    def test_2(self):
        coord = Coordinate(3, 4)
        self.assertEqual(coord.distance(Coordinate(0, 0)), 5, "Distance should be calculated correctly.")

    def test_3(self):
        coord = Coordinate(3, 4)
        self.assertEqual(str(coord), "<3, 4>", "String representation should be correct.")

    def test_4(self):
        coord = Coordinate(-3, -4)
        self.assertAlmostEqual(coord.distance(Coordinate(2, 7)), 12.083, msg="Distance should be calculated correctly.", delta=0.001)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCoordinate)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
