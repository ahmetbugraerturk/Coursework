import unittest
import os
from ps3a import decrypt_the_message


class TestDecryptTheMessage(unittest.TestCase):
    def setUp(self):
        # Setup temporary files for testing
        self.input_file = "test_input.txt"
        self.output_file = "test_output.txt"
        
    def tearDown(self):
        # Cleanup temporary files after each test
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_decrypt_lowercase_letters(self):
        # Create a sample input file
        with open(self.input_file, "w") as f:
            f.write("orzhufdvh")
        decrypt_the_message(self.input_file, 3, self.output_file)
        with open(self.output_file, "r") as f:
            output = f.read()
        self.assertIn("lowercase", output, "Lowercase decryption failed")

    def test_decrypt_uppercase_letters(self):
        with open(self.input_file, "w") as f:
            f.write("XSSHUFDVH")
        decrypt_the_message(self.input_file, 3, self.output_file)
        with open(self.output_file, "r") as f:
            output = f.read()
        self.assertIn("UPPERCASE", output, "Uppercase decryption failed")
    
    def test_decrypt_numbers(self):
        with open(self.input_file, "w") as f:
            f.write("45678901")
        decrypt_the_message(self.input_file, 3, self.output_file)
        with open(self.output_file, "r") as f:
            output = f.read()
        self.assertIn("12345678", output, "Numeric decryption failed")
    
    def test_special_characters_remain_unchanged(self):
        with open(self.input_file, "w") as f:
            f.write(",, : ?")
        decrypt_the_message(self.input_file, 3, self.output_file)
        with open(self.output_file, "r") as f:
            output = f.read()
        self.assertIn(",, : ?", output, "Special characters should remain unchanged")
    
    def test_empty_input_file(self):
        # Test with an empty file
        with open(self.input_file, "w") as f:
            pass  # Create an empty file
        decrypt_the_message(self.input_file, 2, self.output_file)
        with open(self.output_file, "r") as f:
            output = f.read()
        self.assertEqual(output, "", "Empty input should result in empty output")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDecryptTheMessage)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
