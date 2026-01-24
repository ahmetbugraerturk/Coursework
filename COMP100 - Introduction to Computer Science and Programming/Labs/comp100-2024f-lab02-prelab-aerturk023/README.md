[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AGjDqcUs)
# COMP100 2024F Lab 02: Branching and Loops - Prelab
### Deadline Wednesday, October 30, 2024 11:59 PM

The testcases given are just sample tests, and additional testcases may be used while grading.

## Question 1: Distance Converter (15 Points)

Write a function `convert_distance` that converts distances between kilometers and miles. The function should take two parameters: the distance to convert and the unit of the input distance ('K' for kilometers, 'M' for miles). Based on these parameters, the function should return the converted distance.

### Requirements:

- Use `if-else` statements to determine the direction of the conversion.
- Round the result to 2 decimal places.
- If an invalid unit is provided, print the string "Invalid unit" and return `None`.
- If a negative distance is provided, print the string "Negative distance" and return `None`.

### Formulae:

- Kilometers to Miles: `M = K * 0.621371`
- Miles to Kilometers: `K = M / 0.621371`

### Example Usage:

```
print(convert_distance(10, 'K'))  # Output: 6.21
print(convert_distance(5, 'M'))   # Output: 8.05
print(convert_distance(20, 'X'))  # Output: It will print "Invalid unit" and will return None
```

## Question 2: Day of the Week Message (25 Points)
Write a function `weekday_message` that takes an integer (1 through 7) corresponding to the days of the week (1 for Monday, 7 for Sunday) and returns a custom message for the day. Additionally, based on whether there are classes or events, adjust the wake-up alarm time.

### Requirements:
- The function should use a `match-case` statement to select the message based on the day.
- The function should take two additional boolean parameters:
    - `has_class`: Specifies if there is a class on the selected day.
    - `has_event`: Specifies if there is a special event on the weekend (Saturday or Sunday).
- If the input day is outside the range 1-7, the function should return "Invalid day."
- For each day the function should return a unique message (a string) which includes a wake-up time according to the following rules:
    - **Weekdays (Monday to Friday):**
        - If there is a class, the wake-up time is **6:00 AM**.
        - If there is no class, the wake-up time is **7:00 AM**.
    - **Weekends (Saturday and Sunday):**
        - If there is a special event, the wake-up time is **8:00 AM**.
        - Otherwise, the wake-up time is **9:00 AM**.
- Each day should have a unique message, for example, "Monday: Start of a new week! Wake-up alarm set for 6:00 AM".

### Example Usage:
```
print(weekday_message(1, has_class=True))   # Output: "Monday: Start of a new week! Wake-up alarm set for 6:00 AM."
print(weekday_message(6, has_event=True))   # Output: "Saturday: Enjoy the weekend! Wake-up alarm set for 8:00 AM."
print(weekday_message(5, has_class=False))  # Output: "Friday: Time to relax! Wake-up alarm set for 7:00 AM."
print(weekday_message(8))                   # Output: "Invalid day"
```

### Messages:
- Monday: Start of a new week!
- Tuesday: Keep at it!
- Wednesday: Halfway there!
- Thursday: Almost Friday!
- Friday: Time to relax!
- Saturday: Enjoy the weekend!
- Sunday: Prep for the week!

## Question 3: Prime Number Finder (30 Points)

Write a function named `find_primes` that accepts two integers: `start` and `end`, and returns a string containing all prime numbers within that range, inclusive, separated by commas. Use loops to iterate through the range and determine whether each number is prime.

### Requirements:

- Implement the function using a `for` loop and the `range` function.
- Use nested if-else statements within your loop to check for primality.
- If `start` is less than `2`, the function should adjust and start checking from `2` (since 2 is the smallest prime number).
- Break the loop if the current number is not prime.
- The function should return a string of prime numbers in the range, separated by commas. There should not be a comma at the end of the string.
- If no primes are found, return "No prime numbers found".

### Hints:

- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
- To check if a number is prime, you can try dividing it by all numbers less than its square root (plus one).
- Consider using string concatenation or other string manipulation methods to construct the return value.

### Example Usage:

```
print(generate_primes_string(10, 20)) # Output: "11, 13, 17, 19"
print(generate_primes_string(1, 5))  # Output: "2, 3, 5"
```

## Question 4: Generating a Number Triangle (30 Points)

Write a function named `generate_triangle` that prints out a triangle of numbers. The function should accept a single integer parameter `n` which represents the number of rows in the triangle. Each row should contain increasing numbers starting from 1 up to the row number.

### Requirements:

- Use a `for` loop to handle the printing of each row.
- Within the `for` loop
    - utilize another loop to print the empty spaces for each row upto `(n-1) * 2`.
    - utilize another loop to print the sequence of numbers for each row.
- Ensure that each row has the correct sequence of numbers, starting from 1 up to the row number.
- Each number must have a space after it.
- Do not return anything from this function; it should directly print the triangle.

### Example Usage:
```
generate_triangle(5)
# Output
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 

```

### Hints:

- You might find it helpful to use nested loops: an outer loop to iterate through the rows and an inner loop to print numbers within each row.
- Consider how the number of elements if each row relates to the row number itself.
