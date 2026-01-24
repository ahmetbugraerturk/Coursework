import unittest
from complex_number import ComplexNumber

class TestComplexNumber(unittest.TestCase):
    def test_1(self):
        cn = ComplexNumber(3, 4)
        self.assertEqual(cn.x, 3, "x should be set correctly.")
        self.assertEqual(cn.y, 4, "y should be set correctly.")

    def test_2(self):
        cn = ComplexNumber(3, 4)
        cn2 = ComplexNumber(1, 2)
        self.assertEqual(cn + cn2, ComplexNumber(4, 6), "Addition should be correct.")

    def test_3(self):
        cn = ComplexNumber(3, 4)
        cn2 = ComplexNumber(1, 2)
        self.assertEqual(cn - cn2, ComplexNumber(2, 2), "Subtraction should be correct.")

    def test_4(self):
        cn = ComplexNumber(3, 4)
        cn2 = ComplexNumber(1, 2)
        self.assertEqual(cn * cn2, ComplexNumber(-5, 10), "Multiplication should be correct.")

    def test_5(self):
        cn = ComplexNumber(3, 4)
        cn2 = ComplexNumber(1, 2)
        self.assertEqual(cn / cn2, ComplexNumber(2.2, -0.4), "Division should be correct.")

    def test_6(self):
        cn = ComplexNumber(3, 4)
        cn2 = ComplexNumber(1, 2)
        self.assertTrue(cn != cn2, "Equality should be correct.")

    def test_7(self):
        cn = ComplexNumber(3, 4)
        cn2 = ComplexNumber(3, 4)
        self.assertTrue(cn == cn2, "Equality should be correct.")

    def test_8(self):
        cn = ComplexNumber(3, 4)
        self.assertEqual(str(cn), "3 + 4i", "String representation should be correct.")

    def test_9(self):
        cn = ComplexNumber(3, -4)
        self.assertEqual(str(cn), "3 - 4i", "String representation should be correct.")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestComplexNumber)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
