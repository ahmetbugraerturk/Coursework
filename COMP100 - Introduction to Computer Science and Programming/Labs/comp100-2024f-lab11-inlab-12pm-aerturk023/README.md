[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SfH73Sad)
# COMP100 Lab11 LabA Inlab Assignment

**Due date:** 27, December, 2024 13:40

## Q1: Data Parsing with Custom Exceptions (Variant)

### Objective

You will implement a function `parse_and_calculate` that processes a list of strings, converts them to integers, and performs arithmetic operations. The function should handle various exceptions using `try-except` blocks.

---

### Function Specifications

- **Function Name**: `parse_and_calculate`
- **Parameters**:
  - `data` (list of strings): A list containing string representations of numbers.
  - `operator` (str): A string representing an arithmetic operator. For this variant, supported operators are `+`, `-`, `//`, and `%`.

---

### Behavior

1. Convert each string in `data` to an integer.
2. Apply the specified arithmetic operation **sequentially** on the list of integers.
   - For example, for `["4", "2", "1"]` with `"-"`, compute `4 - 2 - 1`.
3. Assert that the number of operands in the list should be at least 2, and if that condition is not met the Assertion message should be `There must be at least 2 operands`
4. Handle exceptions using **custom exception classes** and specific messages:
   - If a string cannot be converted to an integer, raise `NumberConversionError` with the message:  
     > `"Failed to parse one or more strings into integers."`
   - If the arithmetic operator is not valid, raise `OperatorNotSupportedError` with the message:  
     > `"Operator not supported. Valid operators are '+', '-', '//', '%'."`
   - If a division or modulo by zero occurs, catch the `ZeroDivisionError` and **print** a meaningful message:  
     > `"Cannot perform integer division or modulo by zero."`

---

### Implementation Details

- Use `try-except` blocks to catch:
  - Conversion errors (and raise `NumberConversionError`).
- Return the integer result in an else clause (this will happen only if no errors occur)
- Make sure each custom exception class is defined appropriately.

---

### Return Value

- If the function completes successfully without any exceptions, return the **integer result** of the arithmetic operation in an else clause.

---

### Example Usage

```python
# 1) Successful addition
parse_and_calculate(["2", "3", "4"], "+")
# Expected result: 2 + 3 + 4 = 9

# 2) Conversion failure
parse_and_calculate(["5", "abc", "7"], "//")
# Should raise NumberConversionError

# 3) Invalid operator
parse_and_calculate(["10", "2", "3"], "^")
# Should raise OperatorNotSupportedError

# 4) Division by zero
parse_and_calculate(["8", "0"], "//")
# Should print "Cannot perform integer division or modulo by zero."

# 5) Modulo by zero
parse_and_calculate(["15", "0"], "%")
# Should print "Cannot perform integer division or modulo by zero."

# 6) Less than 2 operands
parse_and_calculate(["2"], "+")
# Should return AssertionError: There must be at least 2 operands
```