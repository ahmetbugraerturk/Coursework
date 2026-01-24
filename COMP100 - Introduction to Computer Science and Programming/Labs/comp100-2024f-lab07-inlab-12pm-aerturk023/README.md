[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/H9P0Z_t8)
# COMP100 2024F Lab 07: List and Dictionary InLab A
## Deadline: Friday 13:40 AM, 29 November 2024

- The testcases given are just sample tests, and additional testcases may be used while grading.

## Question 1: Find People Who Are Most Likely to Be Friends (Based on Common Friends) (100 Points)
Write a function `most_likely_to_be_friends` that identifies two people who are most likely to be friends based on the number of mutual friends they have. The function should identify pairs of users who are not already friends but have the highest number of mutual friends.

### Input:
The input is a dictionary where each key is a user ID, and the value is a dictionary containing `name`, `age`, `city`, and `friends` attributes. The `friends` attribute is a list of user IDs that represent the user's friends.

- Example Input:
```python
users = {
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
```

### Output:
The function should return a list of tuples where each tuple contains two user names and the number of mutual friends they have. Only pairs of users who are not already friends should be considered.
- If everyone has no friends or all friends are already mutuals, then your function should return an empty list as `[]`.
- Multiple users may have the same number of mutual friends.
**Expected Output:**
```python
[('Eve', 'Frank', 3)]
```
- There may be multiple pairs with the same number of mutual friends.
---
