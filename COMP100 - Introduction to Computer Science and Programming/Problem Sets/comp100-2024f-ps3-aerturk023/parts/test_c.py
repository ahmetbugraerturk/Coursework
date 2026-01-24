import unittest
from ps3c import handling_assignments

def are_files_identical(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                return False
        if f1.read() or f2.read():
            return False
    return True

class TestHandlingAssignments(unittest.TestCase):
    def test_handling_assignments(self):
        # Input and output file paths
        assignments_path = "data/assignments_encrypted.txt"
        houses_path = "solution_outputs/aggregated_houses.txt"
        decrypted_assignment_path = "solution_outputs/assignments_decrypted.txt"
        updated_assignments_path = "solution_outputs/updated_assignments.txt"
        updated_houses_path = "solution_outputs/updated_houses.txt"
        
        # Expected output file paths
        expected_assignments_path = "expected_outputs/updated_assignments.txt"
        expected_houses_path = "expected_outputs/updated_houses.txt"

        # Run the function
        handling_assignments(assignments_path, houses_path, decrypted_assignment_path, updated_assignments_path, updated_houses_path)

        # Compare updated assignments with expected assignments
        identical_assignments = are_files_identical(updated_assignments_path, expected_assignments_path)
        print(f"Comparing {updated_assignments_path} and {expected_assignments_path}: {'Identical' if identical_assignments else 'Not identical'}")
        self.assertTrue(identical_assignments)

        # Compare updated houses with expected houses
        identical_houses = are_files_identical(updated_houses_path, expected_houses_path)
        print(f"Comparing {updated_houses_path} and {expected_houses_path}: {'Identical' if identical_houses else 'Not identical'}")
        self.assertTrue(identical_houses)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHandlingAssignments)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
