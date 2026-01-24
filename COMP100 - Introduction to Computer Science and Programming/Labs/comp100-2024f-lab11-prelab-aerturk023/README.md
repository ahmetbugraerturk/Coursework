[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hNwCIRkZ)
# COMP100-2024F-LAB11

## Prelab Questions - Testing and Debugging

### Deadline: Friday, 27 December, 10:00 AM

The following exercises are designed to test your ability to implement robust error checking, proper exception handling, and careful validation of inputs and data formats.

---

### Q1: Date Parser with Validation

**File:** `q1.py`

Implement a function called `parse_date(year_str, month_str, day_str)` that:

1. Attempts to convert `year_str`, `month_str`, and `day_str` into integers.
2. Validates that the year is between 1900 and 2100.
3. Validates that the month is between 1 and 12.
4. Validates that the day is valid for the given month and year (e.g., February 30 should not be allowed).
5. Returns the date as a string

Use Python's `datetime` module to attempt creating a `datetime.date` object. This will naturally raise a `ValueError` for invalid dates, which you should catch and re-raise with a more descriptive message.

**Example Usage of `datetime.date` function:**
```python
  year = 2024
  month = 12
  day = 30

  date = datetime.date(year, month, day)
  print(date) # Output: 2020-02-29
```

**Error Conditions:**

- If any of `year_str`, `month_str`, or `day_str` cannot be converted to an integer, raise a `ValueError` with the message:  
  `"Year, month, and day strings must contain integers."`

- If `year` is outside the range [1900, 2100], raise a custom exception `YearRangeError` with the message:  
  `"Year must be between 1900 and 2100."`

- If the date is invalid (e.g., April 31, or month=13, or day=0), raise a `ValueError` with the message:  
  `"Invalid date specified."`

**If Successful:**  
Return the date as a string in the format `"YYYY-MM-DD"`.

**Example Usage:**
```python
parse_date("2020", "02", "29")  # returns "2020-02-29"
parse_date("1899", "12", "15")  # raises YearRangeError("Year must be between 1900 and 2100.")
parse_date("2021", "13", "10")  # raises ValueError("Invalid date specified.")
parse_date("2021", "Feb", "10") # raises ValueError("Year, month, and day must be integers.")
```

### Q2: Tab-Delimited File Validator

**File:** `q2.py`

Implement a function `validate_tab_file(file_path, expected_fields, required_pattern)` that:

1. Attempts to open and read a file line-by-line.
2. Checks that each line contains exactly `expected_fields` fields, separated by tabs (`'\t'`).
3. Confirms that **at least one line** contains a field that matches the given `required_pattern` (a substring).

You will create and use a custom exception `TabFileValidationError` to handle validation failures.

**Behavior:**

- If the file is not found, return `"File not found."`

- If any line does not have the correct number of fields (`expected_fields`), raise `TabFileValidationError`.  
  Include in the exception message:
  - The `file_path`
  - The line number (1-based index) of the first offending line
  - The discrepancy in the number of fields found vs. expected

- If none of the lines contains a field that includes `required_pattern` as a substring, raise `TabFileValidationError` indicating the missing pattern.

**Normal Output:**  
If all criteria are met, return `"Tab-delimited file validation passed."`

**Custom Exception Details:**

- `TabFileValidationError` should provide clear, detailed information. For example:
  - If a line is malformed:  
    `"File path: data.txt, Line 3: Expected 4 fields, found 2."`
  - If the required pattern is missing:  
    `"File path: data.txt, No field contains required pattern 'user_id'."`

- `FileNotFoundError` should provide:
  - `File Not Found.` If the file does not exist.


**Example Usage:**
```python
# Suppose data.txt contents are:
# name    age    country    email
# John    30     Canada     john@example.com
# Alice   25     USA        alice@example.com

validate_tab_file("data.txt", expected_fields=4, required_pattern="example")  
# returns "Tab-delimited file validation passed."

validate_tab_file("data.txt", expected_fields=4, required_pattern="missing_pattern")  
# raises TabFileValidationError("File path: data.txt, No field contains required pattern 'missing_pattern'.")

validate_tab_file("missing_file.txt", 4, "example")  
# returns "File not found."

# If data.txt had a line with fewer fields, for example:
# John    30    Canada

validate_tab_file("data.txt", 4, "example")
# raises TabFileValidationError("File path: data.txt, Line 2: Expected 4 fields, found 3.")
```