[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/5ewX4MkP)
# COMP100 2024F Lab 07: List and Dictionary Prelab
## Deadline: Friday 10:00 AM, 29 November 2024

- The testcases given are just sample tests, and additional testcases may be used while grading.

## Question 1: Reconstruct Directories (40 Points)
Write a function `reconstruct_dir` that:
- Parses the paths into a nested list structure where:
- Directories are represented as lists, with the directory name as the first element.
- Files are represented as strings.
Returns the nested list structure.

### Input:
- The input to the function is a list of strings, where each string represents a file path in the file system.

- Each file path follows a format like: "/home/user/docs/file1.txt", where directories and files are separated by a forward slash (/).

- The paths can be nested, meaning there may be directories inside directories, and these paths may or may not contain files.

- Sample Input:
```python
paths = [
    "/home/user/docs/file1.txt",
    "/home/user/docs/file2.txt",
    "/home/user/videos/ibiza_trip.mp4",
    "/home/user/videos/christmas_party.mp4",
    "/home/user/videos/movies/isle_of_dogs.mp4",
    "/home/user/videos/movies/la_haine.mp4",
    "/home/user/downloads",
    "/home/system/system32",
    "/home/system/config.ini",
    "/dev/input/mouse",
    "/dev/input/gamepad/ps5_controller_conf.ini",
]
```
### Output:
The function returns a nested list structure, where:
- Each directory is represented as a list, where the first element is the directory name.
- Subdirectories are nested inside their parent directory's list.
- Files are represented as simple strings inside the respective directory list.
- If a directory has no files, it is represented by an empty list [].
- Each directory in the tree is represented by its name as the first element, followed by its contents (files or subdirectories) as nested lists.
- Expected output:
```python
[
    'home', [
        'user', [
            'docs', ['file1.txt', 'file2.txt'], 
            'videos', [
                'ibiza_trip.mp4', 'christmas_party.mp4', 
                'movies', ['isle_of_dogs.mp4', 'la_haine.mp4']
                      ], 
            'downloads', []
                ], 
        'system', ['system32', [], 'config.ini']
            ], 
    'dev', [
        'input', ['mouse', [], 'gamepad', ['ps5_controller_conf.ini']]
        ]
]
```
### Notes for Edge Cases:
- Empty Directories: If a directory is mentioned but has no files, an empty list is added to that directory (e.g 'system32', []).
- Nested Directories: The function handles multiple levels of nested directories.
- Top-Level Directories: The function can handle paths that start from different top-level directories (e.g., /home and /dev).

## Question 2: Compute Order Receipt (30 Points)

Write a function `compute_bill` that calculates the total price for a list of ordered items, updating the stock by decrementing the count of each item that is successfully billed. The function will only bill the items that are available in stock, and any items out of stock will be ignored.

### Implementation Method: 
- Iterates through the order list, checks stock, computes total cost, and decrements stock. Returns total cost.

### Inputs: 
- The function takes an order list, which contains the items ordered by their names (e.g., ["ram", "ssd", "monitor"]).
- The function relies on two dictionaries, stock and prices:
- stock: This dictionary holds the current stock level for each hardware item.
```python
stock = {
    "ram": 6,
    "ssd": 0,
    "monitor": 32,
    "power_supply": 15,
    "keyboard": 20
}
```
- prices: This dictionary stores the price for each hardware item.
```python
prices = {
    "ram": 55,
    "ssd": 90,
    "monitor": 220,
    "power_supply": 35,
    "keyboard": 25
}
```
- Sample Input: `order = ["ram", "ssd", "monitor"]`

### Output:
- The function returns the total price of the items -`total (float)`- in the order that are available in stock.
- The stock dictionary is updated to reflect the reduced quantities of the items that were billed. 
- Note: stock dictionary is not an output of the function, it is updated as result of your function.
- Sample Output:
- `compute_bill(order)` Output: `275`
- Updated stock: `{"ram": 5, "ssd": 0, "monitor": 31, "power_supply": 15, "keyboard": 20}`

## Question 3: Monthly Balance Calculator (40 Points)
Write a function `generate_monthly_report` that is is designed to group a list of transactions by month, calculate the total credits and debits for each month, and compute the net balance for each month. It generates a report in the form of a dictionary with monthly breakdowns.

### Inputs:
The function takes a list of transactions. Each transaction is represented by a dictionary with the following fields:
- 'id': A unique identifier for the transaction.
- 'type': A string that indicates the type of transaction, either 'credit' or 'debit'.
- 'amount': A numerical value representing the amount involved in the transaction.
- 'timestamp': A string representing the date of the transaction in the format YYYY-MM-DD.
- Sample Input:
```python
transactions = [
    {'id': 1, 'type': 'credit', 'amount': 500, 'timestamp': '2024-01-05'},
    {'id': 2, 'type': 'debit', 'amount': 300, 'timestamp': '2024-01-10'},
    {'id': 3, 'type': 'credit', 'amount': 700, 'timestamp': '2024-01-15'},
    {'id': 4, 'type': 'credit', 'amount': 900, 'timestamp': '2024-02-01'},
    {'id': 5, 'type': 'debit', 'amount': 400, 'timestamp': '2024-02-05'}
]
```
### Output:
The function returns a dictionary where the keys are the months in YYYY-MM format, and the values are dictionaries with:
- 'total_credit': Total amount of credits for that month.
- 'total_debit': Total amount of debits for that month.
- 'net_balance': The difference between total_credit and total_debit (i.e., total_credit - total_debit).

After processing all transactions, the function returns a regular dictionary containing the summary for each month. The dictionary has the structure:
```python
{
    'YYYY-MM': {'total_credit': <total>, 'total_debit': <total>, 'net_balance': <balance>}
}
```
Sample Output:
```python
'2024-01': {'total_credit': 1200, 'total_debit': 300, 'net_balance': 900},
'2024-02': {'total_credit': 900, 'total_debit': 400, 'net_balance': 500}
...
```

