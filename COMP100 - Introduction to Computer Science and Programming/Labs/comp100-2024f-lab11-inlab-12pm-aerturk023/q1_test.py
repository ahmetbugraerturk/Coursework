import unittest
from q1 import parse_and_calculate, NumberConversionError, OperatorNotSupportedError

class TestParseAndCalculate(unittest.TestCase):
    def test_addition(self):
        """
        Test basic addition using valid strings and the '+' operator.
        """
        result = parse_and_calculate(["1", "2", "3"], "+")
        self.assertEqual(result, 6, "Expected 1 + 2 + 3 to equal 6")

    def test_only_one_operand(self):
        """
        Test that an AssertionError is raised if less than two operands are provided.
        """
        with self.assertRaises(AssertionError) as context:
            parse_and_calculate(["1"], "+")
        self.assertEqual(str(context.exception), "There must be at least 2 operands")
            
    def test_invalid_conversion(self):
        """
        Test that a NumberConversionError is raised
        if any string in the list cannot be converted to an integer.
        """
        with self.assertRaises(NumberConversionError):
            parse_and_calculate(["1", "2", "a"], "+")
    
    def test_invalid_operator(self):
        """
        Test that an OperatorNotSupportedError is raised
        if an unsupported operator is provided.
        """
        with self.assertRaises(OperatorNotSupportedError):
            parse_and_calculate(["1", "2", "3"], "?")
    
    def test_integer_division_by_zero(self):
        """
        Test that a ZeroDivisionError is handled by printing a message
        and returning None for the '//' operator.
        """
        result = parse_and_calculate(["1", "0"], "//")
        self.assertIsNone(result, "Expected None when dividing by zero")
    
    def test_modulo_by_zero(self):
        """
        Test that a ZeroDivisionError is handled by printing a message
        and returning None for the '%' operator.
        """
        result = parse_and_calculate(["10", "0"], "%")
        self.assertIsNone(result, "Expected None when taking modulo by zero")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestParseAndCalculate)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
