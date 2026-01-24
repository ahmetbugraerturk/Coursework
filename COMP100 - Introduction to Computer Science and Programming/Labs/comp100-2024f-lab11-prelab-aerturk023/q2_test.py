import unittest
from q2 import validate_tab_file, TabFileValidationError
import os

class TestValidateTabFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        
        # Success case
        with open("success_data.txt", "w") as f:
            f.write("name\tage\tcountry\temail\n")
            f.write("John\t30\tCanada\tjohn@example.com\n")
            f.write("Alice\t25\tUSA\talice@example.com\n")
            f.write("Mark\t22\tUK\tmark@example.com\n")
            f.write("Jane\t29\tAustralia\tjane@example.com\n")

        # Missing pattern
        with open("missing_pattern_data.txt", "w") as f:
            f.write("name\tage\tcountry\temail\n")
            f.write("John\t30\tCanada\tjohn@something.com\n")
            f.write("Alice\t25\tUSA\talice@something.com\n")
            f.write("Mark\t22\tUK\tmark@something.com\n")
            f.write("Jane\t29\tAustralia\tjane@something.com\n")

        # Fewer fields in one line
        with open("fewer_fields_data.txt", "w") as f:
            f.write("name\tage\tcountry\temail\n")
            f.write("John\t30\tCanada\tjohn@example.com\n")
            f.write("Alice\t25\tUSA\n")
            f.write("Mark\t22\tUK\tmark@example.com\n")
            f.write("Jane\t29\tAustralia\tjane@example.com\n")

        # More fields in one line
        with open("more_fields_data.txt", "w") as f:
            f.write("name\tage\tcountry\temail\n")
            f.write("John\t30\tCanada\tjohn@example.com\n")
            f.write("Alice\t25\tUSA\talice@example.com\n")
            f.write("Mark\t22\tUK\tmark@example.com\n")
            f.write("Jane\t29\tAustralia\tjane@example.com\textra_field\n")

    def test_success_case(self):
        result = validate_tab_file("success_data.txt", expected_fields=4, required_pattern="example")
        self.assertEqual(result, "Tab-delimited file validation passed.")

    def test_missing_pattern_case(self):
        with self.assertRaises(TabFileValidationError) as context:
            validate_tab_file("missing_pattern_data.txt", expected_fields=4, required_pattern="example")
        self.assertIn("No field contains required pattern 'example'", str(context.exception))

    def test_fewer_fields_case(self):
        with self.assertRaises(TabFileValidationError) as context:
            validate_tab_file("fewer_fields_data.txt", expected_fields=4, required_pattern="example")
        self.assertIn("Expected 4 fields, found 3.", str(context.exception))

    def test_more_fields_case(self):
        with self.assertRaises(TabFileValidationError) as context:
            validate_tab_file("more_fields_data.txt", expected_fields=4, required_pattern="example")
        self.assertIn("Expected 4 fields, found 5.", str(context.exception))

    def test_file_not_found(self):
        result = validate_tab_file("non_existent_file.txt", expected_fields=4, required_pattern="example")
        self.assertEqual(result, "File not found.")

    @classmethod
    def tearDownClass(cls):
        # Clean up test files
        test_files = [
            "success_data.txt",
            "missing_pattern_data.txt",
            "fewer_fields_data.txt",
            "more_fields_data.txt"
        ]
        for filename in test_files:
            if os.path.exists(filename):
                os.remove(filename)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestValidateTabFile)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
