import unittest
from car import Car
from component import Component


class TestComponent(unittest.TestCase):
    def test_init(self):
        component = Component("Component")
        self.assertEqual(component.name, "Component")

    def test_apply(self):
        component = Component("Component")
        car = Car("Test Model", 350.0, 2.5, 5)
        with self.assertRaises(NotImplementedError, msg="Must raise an exception when apply is called."):
            component.apply(car)

    def test_add(self):
        component1 = Component("Component1")
        component2 = Component("Component2")
        composite = component1 + component2
        self.assertEqual(composite.name, "Composite")

    def test_add_fail(self):
        component = Component("Component")
        with self.assertRaises(TypeError, msg="Must raise an exception when adding a non-Component object."):
            composite = component + 5

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestComponent)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
