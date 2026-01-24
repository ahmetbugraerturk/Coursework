import unittest
import os
from ps3b import aggregate_house_contributions
import json 

class TestAggregateHouseContributions(unittest.TestCase):
    def setUp(self):
        # Prepare test directories and files
        self.encrypted_file = "test_encrypted.txt"
        self.decrypted_file = "test_decrypted.txt"
        self.output_file = "test_output.txt"

    def tearDown(self):
        # Clean up test files
        for file in [self.encrypted_file, self.output_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_valid_input(self):
        # Create an encrypted input file
        with open(self.encrypted_file, "w") as f:
            f.write("cde,5,7\nfgh,46,4\ncde,6,8\n")  
        
        # Call the function
        aggregate_house_contributions(self.encrypted_file, self.decrypted_file, self.output_file)

        # Verify the output
        with open(self.output_file, "r") as f:
            output = f.read()
        expected_output = (
            'zab: {"soldiers": 5, "weapons": 9}\n'
            'cde: {"soldiers": 13, "weapons": 1}\n'
        )
        def parse_output(output_str):
            result = {}
            for line in output_str.strip().split("\n"):
                house, data = line.split(": ", 1)
                result[house.strip()] = json.loads(data.replace("'", '"'))
            return result

        actual_dict = parse_output(output)
        expected_dict = parse_output(expected_output)

        self.assertEqual(actual_dict, expected_dict, "Actual data test failed")


    def test_empty_file(self):
        # Create an empty encrypted input file
        with open(self.encrypted_file, "w") as f:
            f.write("")
        
        # Call the function
        aggregate_house_contributions(self.encrypted_file, self.decrypted_file, self.output_file)

        # Verify the output
        with open(self.output_file, "r") as f:
            output = f.read()
        self.assertEqual(output, "", "Empty file test failed")

    def test_actual_data(self):
        with open(self.encrypted_file, "w") as f:
            f.write("Vwdun,93,4213\nOdqqlvwhu,1773,6823\nEdudwkhrq,1963,8903\nWdujdubhq,4833,833\nJuhbmrb,1203,1933\nWbuhoo,0933,0393\nPduwhoo,8013,4403\nErowrq,1623,8733\nVwdun,83,7923\nOdqqlvwhu,4013,4373")

        # Call the function to aggregate contributions
        aggregate_house_contributions(self.encrypted_file, self.decrypted_file, self.output_file)

        # Verify the output
        with open(self.output_file, "r") as f:
            output = f.read()

        expected_output = (
            'Stark: {"soldiers": 110, "weapons": 6670}\n'
            'Lannister: {"soldiers": 10220, "weapons": 4630}\n'
            'Baratheon: {"soldiers": 8630, "weapons": 5670}\n'
            'Targaryen: {"soldiers": 1500, "weapons": 500}\n'
            'Greyjoy: {"soldiers": 8970, "weapons": 8600}\n'
            'Tyrell: {"soldiers": 7600, "weapons": 7060}\n'
            'Martell: {"soldiers": 5780, "weapons": 1170}\n'
            'Bolton: {"soldiers": 8390, "weapons": 5400}\n'
        )
        def parse_output(output_str):
            result = {}
            for line in output_str.strip().split("\n"):
                house, data = line.split(": ", 1)
                result[house.strip()] = json.loads(data.replace("'", '"'))
            return result

        actual_dict = parse_output(output)
        expected_dict = parse_output(expected_output)

        self.assertEqual(actual_dict, expected_dict, "Actual data test failed")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAggregateHouseContributions)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")


