import unittest
from q1 import most_likely_to_be_friends
class TestMostLikelyToBeFriends(unittest.TestCase):

    def setUp(self):
        self.users = {
    "id1": {"name": "Alice", "age": 30, "city": "New York", "friends": ["id2", "id3", "id5", "id6"]},
    "id2": {"name": "Bob", "age": 25, "city": "New York", "friends": ["id1", "id5", "id6", "id7"]},
    "id3": {"name": "Charlie", "age": 35, "city": "Los Angeles", "friends": ["id1", "id7", "id8", "id12"]},
    "id4": {"name": "Diana", "age": 23, "city": "Chicago", "friends": ["id9", "id10","id11", "id12"]},
    "id5": {"name": "Eve", "age": 27, "city": "New York", "friends": ["id1", "id2", "id10", "id11"]},
    "id6": {"name": "Frank", "age": 40, "city": "Miami", "friends": ["id1", "id2", "id10", "id12"]},
    "id7": {"name": "Grace", "age": 29, "city": "Los Angeles", "friends": ["id2", "id3", "id8", "id11"]},
    "id8": {"name": "Hank", "age": 33, "city": "Los Angeles", "friends": ["id3", "id7", "id9", "id10"]},
    "id9": {"name": "Ivy", "age": 26, "city": "Chicago", "friends": ["id4", "id8", "id11", "id12"]},
    "id10": {"name": "Jack", "age": 41, "city": "Chicago", "friends": ["id4", "id5", "id6", "id8"]},
    "id11": {"name": "Karen", "age": 24, "city": "Miami", "friends": ["id4", "id9", "id5", "id7"]},
    "id12": {"name": "Leo", "age": 37, "city": "Miami", "friends": ["id3", "id4", "id6", "id9"]},
    }

    def test_most_likely_to_be_friends_with_mutual_friends(self):
        # Test case with users who have mutual friends
        result = most_likely_to_be_friends(self.users)
        expected = [('Eve', 'Frank', 3)]
        self.assertEqual(result, expected)

    def test_most_likely_to_be_friends_no_mutual_friends(self):
        # Test case where no mutual friends exist
        users_no_mutual = {
            "id1": {"name": "Alice", "age": 30, "city": "New York", "friends": ["id2"]},
            "id2": {"name": "Bob", "age": 25, "city": "New York", "friends": ["id1"]},
            "id3": {"name": "Charlie", "age": 35, "city": "Los Angeles", "friends": []},
        }
        result = most_likely_to_be_friends(users_no_mutual)
        self.assertEqual(result, [])

    def test_most_likely_to_be_friends_with_multiple_mutual_friends(self):
        # Test case with multiple pairs having the same number of mutual friends
        users_multiple_mutual = {
            "id1": {"name": "Alice", "age": 30, "city": "New York", "friends": ["id2", "id3"]},
            "id2": {"name": "Bob", "age": 25, "city": "New York", "friends": ["id1"]},
            "id3": {"name": "Charlie", "age": 35, "city": "Los Angeles", "friends": ["id1"]},
            "id4": {"name": "Diana", "age": 23, "city": "Chicago", "friends": ["id6"]},
            "id5": {"name": "Eve", "age": 27, "city": "New York", "friends": ["id6"]},
            "id6": {"name": "Frank", "age": 40, "city": "Miami", "friends": ["id4", "id5"]},
        }
        result = most_likely_to_be_friends(users_multiple_mutual)
        expected = [
            ('Bob', 'Charlie', 1),
            ('Diana', 'Eve', 1),
        ]
        self.assertEqual(result, expected)

    def test_most_likely_to_be_friends_empty_users(self):
        # Test case with empty user data
        users_empty = {}
        result = most_likely_to_be_friends(users_empty)
        self.assertEqual(result, [])

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMostLikelyToBeFriends)
    result = unittest.TextTestRunner().run(suite)
    total_tests_run = result.testsRun
    total_failures = len(result.failures) + len(result.errors)
    total_passed = total_tests_run - total_failures
    print(f"Test Passed: {total_passed}/{total_tests_run}")