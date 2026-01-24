import unittest
from q2 import weekday_message


class TestWeekdayMessage(unittest.TestCase):
    def test_monday(self):
        self.assertEqual(weekday_message(1, has_class=True), "Monday: Start of a new week! Wake-up alarm set for 6:00 AM.")

    def test_monday_no_class(self):
        self.assertEqual(weekday_message(1, has_class=False), "Monday: Start of a new week! Wake-up alarm set for 7:00 AM.")

    def test_tuesday(self):
        self.assertEqual(weekday_message(2, has_class=True), "Tuesday: Keep at it! Wake-up alarm set for 6:00 AM.")

    def test_tuesday_no_class(self):
        self.assertEqual(weekday_message(2, has_class=False), "Tuesday: Keep at it! Wake-up alarm set for 7:00 AM.")

    def test_wednesday(self):
        self.assertEqual(weekday_message(3, has_class=True), "Wednesday: Halfway there! Wake-up alarm set for 6:00 AM.")

    def test_wednesday_no_class(self):
        self.assertEqual(weekday_message(3, has_class=False), "Wednesday: Halfway there! Wake-up alarm set for 7:00 AM.")

    def test_thursday(self):
        self.assertEqual(weekday_message(4, has_class=True), "Thursday: Almost Friday! Wake-up alarm set for 6:00 AM.")

    def test_thursday_no_class(self):
        self.assertEqual(weekday_message(4, has_class=False), "Thursday: Almost Friday! Wake-up alarm set for 7:00 AM.")

    def test_friday(self):
        self.assertEqual(weekday_message(5, has_class=True), "Friday: Time to relax! Wake-up alarm set for 6:00 AM.")

    def test_friday_no_class(self):
        self.assertEqual(weekday_message(5, has_class=False), "Friday: Time to relax! Wake-up alarm set for 7:00 AM.")

    def test_saturday(self):
        self.assertEqual(weekday_message(6, has_event=True), "Saturday: Enjoy the weekend! Wake-up alarm set for 8:00 AM.")

    def test_saturday_no_event(self):
        self.assertEqual(weekday_message(6, has_event=False), "Saturday: Enjoy the weekend! Wake-up alarm set for 9:00 AM.")

    def test_sunday(self):
        self.assertEqual(weekday_message(7, has_event=True), "Sunday: Prep for the week! Wake-up alarm set for 8:00 AM.")

    def test_sunday_no_event(self):
        self.assertEqual(weekday_message(7, has_event=False), "Sunday: Prep for the week! Wake-up alarm set for 9:00 AM.")

    def test_invalid_day(self):
        self.assertEqual(weekday_message(0), "Invalid day")

    def test_invalid_day_negative(self):
        self.assertEqual(weekday_message(-1), "Invalid day")

    def test_invalid_day_large(self):
        self.assertEqual(weekday_message(8), "Invalid day")

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWeekdayMessage)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")
