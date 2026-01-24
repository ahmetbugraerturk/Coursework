import unittest
import sys
from io import StringIO

from q4 import generate_triangle


class TestGenerateTriangle(unittest.TestCase):
    def test_generate_triangle_1(self):
        expected_output = "  1 \n1 2 \n"
        captured_output = StringIO()
        sys.stdout = captured_output
        generate_triangle(2)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_generate_triangle_2(self):
        expected_output = "        1 \n      1 2 \n    1 2 3 \n  1 2 3 4 \n1 2 3 4 5 \n"
        captured_output = StringIO()
        sys.stdout = captured_output
        generate_triangle(5)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_generate_triangle_3(self):
        expected_output = "          1 \n        1 2 \n      1 2 3 \n    1 2 3 4 \n  1 2 3 4 5 \n1 2 3 4 5 6 \n"
        captured_output = StringIO()
        sys.stdout = captured_output
        generate_triangle(6)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_generate_triangle_4(self):
        expected_output = "            1 \n          1 2 \n        1 2 3 \n      1 2 3 4 \n    1 2 3 4 5 \n  1 2 3 4 5 6 \n1 2 3 4 5 6 7 \n"
        captured_output = StringIO()
        sys.stdout = captured_output
        generate_triangle(7)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGenerateTriangle)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
