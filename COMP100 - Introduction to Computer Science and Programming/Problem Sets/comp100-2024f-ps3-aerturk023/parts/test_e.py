import unittest
from ps3e import encrypt_files

def are_files_identical(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                return False
        if f1.read() or f2.read():
            return False
    return True

class TestEncryptFiles(unittest.TestCase):
    def test_encrypt_files(self):
        input_houses_file = "solution_outputs/final_houses.txt"
        input_assignments_file = "solution_outputs/final_assignments.txt"
        output_houses_file = "solution_outputs/encrypted_final_houses.txt"
        output_assignments_file = "solution_outputs/encrypted_final_assignments.txt"
        shift = 3

        encrypt_files(input_houses_file, shift, output_houses_file)
        encrypt_files(input_assignments_file, shift, output_assignments_file)

        file1 = "solution_outputs/encrypted_final_houses.txt"
        file2 = "expected_outputs/encrypted_final_houses.txt"
        
        identical = are_files_identical(file1, file2)
        print(f"Comparing {file1} and {file2}: {'Identical' if identical else 'Not identical'}")
        self.assertTrue(identical)

        file3 = "solution_outputs/encrypted_final_assignments.txt"
        file4 = "expected_outputs/encrypted_final_assignments.txt"
        
        identical = are_files_identical(file3, file4)
        print(f"Comparing {file3} and {file4}: {'Identical' if identical else 'Not identical'}")
        self.assertTrue(identical)

if __name__ == "__main__":
    unittest.main()
