import unittest
from ps3d import allocate_resources

def are_files_identical(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                return False
        if f1.read() or f2.read():
            return False
    return True

class TestAllocateResources(unittest.TestCase):
    def test_allocate_resources(self):
        houses_file = "solution_outputs/updated_houses.txt"
        assignments_file = "solution_outputs/updated_assignments.txt"
        white_walkers = {
            "Eastwatch by the Sea": 3350,
            "Castle Black": 6580,
            "Shadow Tower": 5380
        }

        allocate_resources(houses_file, assignments_file, white_walkers)

        file1 = "solution_outputs/final_houses.txt"
        file2 = "expected_outputs/final_houses.txt"
        
        identical = are_files_identical(file1, file2)
        print(f"Comparing {file1} and {file2}: {'Identical' if identical else 'Not identical'}")
        self.assertTrue(identical)

        file3 = "solution_outputs/final_assignments.txt"
        file4 = "expected_outputs/final_assignments.txt"
        
        identical = are_files_identical(file3, file4)
        print(f"Comparing {file3} and {file4}: {'Identical' if identical else 'Not identical'}")
        self.assertTrue(identical)

if __name__ == "__main__":
    unittest.main()
