[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/oQWYeMYJ)
# PS2 - Avengers Airline Seating Protocol 
### Deadline: November 25, 2024 23:59

The testcases given are just sample tests, and additional testcases may be used while grading.

## Introduction

Welcome aboard the Avengers Airline! With the latest Stark Industries' flight upgrade, the Avengers are set for their next world-saving mission. But there is a small catch - the AI entity known as Ultron has successfully taken posession of the very core of Jarvis. This hostile takeover has resulted in the impairment of Jarvis's algorithmic functions. Now it is up to you, the brightest new recruit at Stark Industries, to assign seats manually. Using your Python skills, help the Earth's Mightiest Heroes find their seats without sparking a civil war. But remember, in programming as in superheroics: with great power comes great responsibility (and a fair bit of debugging). Fear not, for Infinity Stones or hammers are not required; just *good old loops*, *conditions*, *string operations*, and *functions*.

## Airplane Seating Configuration

The seats on the plane are arranged as follows, with aisles and windows:
- 'O': Empty seat
- 'X': Occupied seat
- '|': Aisle
- 'H': Hero seat assigned to the current group
- 'D': Reserved seat for an accessible seat for a disabled or injured hero

Seats on either side are window seats and seats adjacent to an aisle are aisle seats. For example: **WXA|AXXA|AXW** where **W** is window seat and **A** is an aisle seat.

#### Examples
- 10 seats separated by 2 aisles:
```
XXX|XOOX|XXX
```
- 6 seats separated by 2 aisles (middle two seats are occupied):
```
OO|XX|OO
```
- 4 seats separated by 2 aisles:
```
O|XO|X
```

Each class has the following configurations:
- First Class: Rows of 1-2-1 seats (VIP seating with extra legroom!)
- Business Class: Rows of 2-2-2 seats (Because heroes need to stretch too.)
- Economy Class: Rows of 3-4-3 seats (For the sidekicks, probably.)

A visual representation of the plane seating plane would be as follows:
```
First Class:
O|OO|O
O|OO|O
.
.
.

Business Class:
OO|OO|OO
OO|OO|OO
.
.
.

Economy Class:
OOO|OOOO|OOO
OOO|OOOO|OOO
.
.
.
```

## PART 1: Seats Allocation (20 pts)

In Part 1, you are tasked with allocating seats without any conditions. The primary goal is to seat the entire group; whenever an empty seat `O` is encountered, it should be immediately allocated to one of the group members.

### A) Avengers Assemble?

Implement a function `can_assemble(total_avengers: int, seat_config: str) -> str` to determine if it is possible to seat all the Avengers in their designated seats.

If there are enough seats, return `'Yes, you may board!'`; otherwise, return `'Boarding Denied!'`

#### Parameters' validation:
- If `seat_config` does not belong to any of the classes (First, Business, or Economy), return `'Invalid seat configuration!'`.
- If `seat_config` is correct but has invalid characters, return `'Invalid seat letters!'`.

#### Examples:

```python
print(can_assemble(4, "OXO|OXXO|XOO")) # Expected output: 'Yes, you may board!'
```

```python
print(can_assemble(7, "OO|OO|OO")) # Expected output: 'Boarding Denied!'
# Although whole row is empty but cannot be allocated to 7 avengers
```
```python
print(can_assemble(3, "OX|XX|OX")) # Expected output: 'Boarding Denied!'
# Not enough empty seats available
```

```python
print(can_assemble(4, "OXO|OXXO|XO")) # Expected output: 'Invalid seat configuration!'
```

```python
print(can_assemble(4, "O|Ox|x")) # Expected output: 'Invalid seat letters!'
```

### B) Show Me the Heroes' Seats

Next, implement a function `show_allocated_seats(total_avengers: int, seat_config: str) -> str` to show new seat configuration after seating the Avengers, or `'Boarding Denied!'` if not possible.

**Important Note:** Starting from the leftmost seat, please allocate the first empty seats and do not skip any empty seats. You will be graded based on these solutions. For example, if you want to allocate seats for 3 characters in the seat configuration ```OO|OX|OX```, you should allocate the first three empty seats from the left.

**Correct**: `HH|HX|OX`
<br>
**Incorrect**: `HH|OX|HX`

#### Parameters' validation:
- If `seat_config` does not belong to any of the classes (First, Business, or Economy), return `'Invalid seat configuration!'`.
- If `seat_config` is correct but has invalid characters, return `'Invalid seat letters!'`.

#### Examples:

```python
print(show_allocated_seats(4, "OXO|OXXO|XOO")) # Expected output: 'HXH|HXXH|XOO'
```

```python
print(show_allocated_seats(3, "OO|OX|OX")) # Expected output: 'HH|HX|OX'
```

```python
print(show_allocated_seats(7, "OO|OO|OO")) # Expected output: 'Boarding Denied!'
# Although whole row is empty but cannot be allocated to 7 avengers
```

```python
print(show_allocated_seats(3, "OX|XX|OX")) # Expected output: 'Boarding Denied!'
# Not enough empty seats available
```

**Hint**: You may use the ```replace(old, new, count)``` function to replace occurrences of a character in a string. After you have determined that there is a solution, you may replace the 'O's with 'H's using this function.

For further information about the replace() function, you may refer to the Python documentation or other relevant resources such as: https://docs.python.org/3.12/library/stdtypes.html#str.replace

## PART 2: Window or Aisle Preference (30 pts)

Some avengers might have a seating preference for window ('W'), middle ('M'), or aisle ('A') seats.

### A) Can Sit by Preference?

Implement a function `can_board_with_preference(total_avengers: int, seat_config: str, preference: str) -> str` to determine if it is possible to seat certain avengers according to their preference.

`preference` can be one of the characters -> `'W'`, `'M'`, `'A'`, or `'D'`

If they can be seated, return `'Yes, you may board!'`; otherwise, return `'Boarding Denied!'`

#### Parameters' validation:
- If `seat_config` does not belong to any of the classes (First, Business, or Economy), return `'Invalid seat configuration!'`.
- If `seat_config` is correct but has invalid characters, return `'Invalid seat letters!'`.
- If `preference` has invalid characters, return `'Invalid seat preference!'`.

**Note**:
- Middle seat can only exist in Economy class. A seat surrounded by two seats on each side, is a middle seat. For example O**M**O|O**MM**O|O**M**O; middle seat is represented by **M**.
- Aisle seat is a seat that is adjacent to an aisle (**|**). In First class, a window seat can also be an aisle seat at the same time. For example, **O**|OO|**O**; seats in bold letters are aisle and window seats at the same time.
- Disable or injured hero can only be assigned the aisle seats.

#### Examples:

```python
print(can_board_with_preference(2, "OXO|OXXO|XOO", "W")) # Expected output: 'Yes, you may board!'
```

```python
print(can_board_with_preference(3, "OO|OO|OO", "A")) # Expected output: 'Yes, you may board!'
```

```python
print(can_board_with_preference(3, "OX|XX|OO", "W")) # Expected output: 'Boarding Denied!'
# Although both window seats are empty, but 3 avengers cannot be allocated window seats
```

```python
print(can_board_with_preference(3, "OXO|XOOX|XOO", "M")) # Expected output: 'Yes, you may board!'
# 3 middle seats are available -> OXO|XHHX|XHO
```

```python
print(can_board_with_preference(1, "OXO|XOOX|XOO", "D")) # Expected output: 'Yes, you may board!'
# an aisle seat is available -> OXD|XOOX|XOO
```

```python
print(can_board_with_preference(3, "OO|OO|OO", "Z")) # Expected output: 'Invalid seat preference!'
```

### B) Preferred Placement

Next, implement a function `show_preferred_seats(total_avengers: int, seat_config: str, preference: str) -> str` to print the new seat configuration after seating the Avengers, or `'Boarding Denied!'` if not possible.

#### Parameters' validation:
- If `seat_config` does not belong to any of the classes (First, Business, or Economy), return `'Invalid seat configuration!'`.
- If `seat_config` is correct but has invalid characters, return `'Invalid seat letters!'`.
- If `preference` has invalid characters, return `'Invalid seat preference!'`.

**Note**:
- Middle seat can only exist in Economy class. A seat surrounded by two seats on each side, is a middle seat. For example O**M**O|O**MM**O|O**M**O; middle seat is represented by **M**.
- Aisle seat is a seat that is adjacent to an aisle (**|**). In First class, a window seat can also be an aisle seat at the same time. For example, **O**|OO|**O**; seats in bold letters are aisle and window seats at the same time.
- You should seat them starting from left side. For example, the answer for `3` avengers with seat configuration: `OO|OO|OO` and seat preference: `A`:
  - **Correct**: `OH|HH|OO`
  - **Incorrect**: `OH|HO|HO`

#### Examples:

```python
print(show_preferred_seats(2, "OXO|OXXO|XOO", "W")) # Expected output: 'HXO|OXXO|XOH'
```

```python
print(show_preferred_seats(3, "OO|OO|OO", "A")) # Expected output: 'OH|HH|OO'
```

```python
print(show_preferred_seats(3, "OX|XX|OO", "W")) # Expected output: 'Boarding Denied!'
# Although both window seats are empty, but 3 avengers cannot be allocated window seats
```

```python
print(show_preferred_seats(3, "OXO|XOOX|XOO", "M")) # Expected output: 'OXO|XHHX|XHO'
```

```python
print(show_preferred_seats(1, "OXO|XOOX|XOO", "D")) # Expected output: 'OXD|XOOX|XOO'
```

## PART 3: Preferences Puzzler (50 pts)

It is time to consider our heroes' preferences. Although they are still willing to split into smaller groups, they have specified where they would like to sit.

#### The Avengers' Woes:

You must keep in mind the ranking of a superhero while allocating the seats. Ranking is as follows where 0 being the highest rank:

0. **D** -> Disabled or injured heroes get the highest priority.
1. **T** -> Tony Stark (Iron Man) - Genius, billionaire, playboy, philanthropist, and a central figure with significant influence and resources.
2. **S** -> Steve Rogers (Captain America) - Often portrayed as the tactical leader of the team, showing integrity and courage.
3. **N** -> Natasha Romanoff (Black Widow) - A super-spy and an integral operative with extensive espionage skills.
4. **B** -> Dr. Bruce Banner (The Hulk) - Possessing both the incredible strength of the Hulk and Banner's scientific genius, he is a dual asset in both brains and brawn.
5. **A** -> Thor Odinson (Asgardian) - A powerful ally, often dealing with cosmic threats.
6. **C** -> Clint Barton (Hawkeye) - A strategic member with exceptional marksmanship.
7. **L** -> Loki (God of Mischief) - Despite being a wildcard, his cunning and occasional alliances with the Avengers can prove beneficial, though unpredictably so.
8. **H** -> Other Heroes - This group represents the extended family of the Avengers. They bring diverse abilities, backgrounds, and perspectives. This collective "H" category can encompass heroes like Wanda Maximoff (Scarlet Witch), Sam Wilson (Falcon), Peter Parker (Spider-Man), and many others.

- Tony Stark refuses to fly unless he is in a window seat in First Class.
- Dr. Bruce Banner must have an aisle seat to quickly move in case of a "Hulk" situation.
- Thor Odinson will sit anywhere except by the 'portal' (he means the window).
- Clint Barton and Natasha Romanoff prefer to sit together in Business class at window seats on either the far left or right. However, if boarding with others (not as a couple but alone), such as: TSN or TSC; Natasha will then prefer a window seat in any class, while Clint remains flexible with no specific seating preference.
- Thor and Loki, due to royal Asgaridan reasons, cannot sit in the same row.
- Let us not forget Stever Rogers, who always volunteers to sit in the middle - "I can do this all day."
- Disabled or injured heroes will only be seated on aisle seats.

**Note**: Here preferences are rules that you **must** follow while allotting the seats. You can use initials of a superhero to refer him/her.


Keeping in mind the above conditions, all heroes must be seated from left to right with highest rank starting from the left; following is an example:
- First Class seating configuration `'O|OO|O'`, can have following correct result.
  - **Correct**: `T|BA|O` -> 1. Tony, 2. Bruce, 3. Thor
  - **Incorrect**: `T|AB|O`, `O|BA|T`, `O|AB|T`

#### Probable Scenarios:

Scenarios can occur where you might have to change the order, for example:
- Natasha and Clint prefer to sit together; if there exist such a scenario where you have to seat a third avenger with them and he/she has higher priority than Clint (but not higher than that of Natasha), seats will be assigned according to the preference of Natasha and Clint i.e. first seat them on window seats (Natasha will always have window seat on either side) and then the third or the remaining one will be seated. In this scenario, if an avenger has higher priority than Natasha's, he/she will be seated first.
- Disabled/injured ones have the highest priority as such they must be seated first. Scenario: O|OO|O seats, and requirement is to seat Tony, an injured, and Hulk, then the correct order is -> D|BO|T.

### A) Priority Seating Check

Implement a function `can_allocate_priority_seats(airplane_class: str, class_config: str, heroes: str) -> str` to determine if it is possible to seat certain avengers according to their preference.

- `airplane_class`: First, Business, or Economy (`str`)
- `class_config`: current seat configuration for a class section (`str`)
- `heroes`: initials of heroes that require seats (`str`)

If they can be seated, return `'Yes, you may board!'`; otherwise, return `'Boarding Denied!'`

#### Parameters' validation:
- If `airplane_class` input is incorrect, return `'Unrecognized class!'`.
- If `seat_config` does not belong to any of the classes (First, Business, or Economy), return `'Invalid seat configuration!'`.
- If `seat_config` is correct but has invalid characters, return `'Invalid seat letters!'`.
- If `airplane_class` and `seat_config` do not match, return `'Mismatch between 'airplane_class' and 'seat_config'!'`.
- If `heroes` has invalid characters, return `'Unrecognized hero, not allowed to board!'`.

#### Examples:

```python
print(can_allocate_priority_seats("First", "O|OO|O", "TBS")) # Expected output: 'Boarding Denied!'
```

```python
print(can_allocate_priority_seats("First", "O|OO|O", "TBA")) # Expected output: 'Yes, you may board!'
# Tony on window seat, Thor and Bruce on aisle seats -> T|BA|O
```

```python
print(can_allocate_priority_seats("Business", "XO|XX|OO", "TNC")) # Expected output: 'Boarding Denied!'
# Although Clint and Natasha can sit on right window seats, Tony cannot be allocated a seat in Business class
```

```python
print(can_allocate_priority_seats("Economy", "XOX|OXOO|OOX", "BAHHS")) # Expected output: 'Yes, you may board!'
# Steve with higest priority, followed by Bruce, Thor, and other Avengers -> XSX|BXAH|HOX
```

```python
print(can_allocate_priority_seats("first", "O|OO|O", "TBA")) # Expected output: 'Unrecognized class!'
```

```python
print(can_allocate_priority_seats("First", "OO|OO|OO", "TBA")) # Expected output: 'Mismatch between 'airplane_class' and 'seat_config'!'
```

```python
print(can_allocate_priority_seats("First", "O|OO|O", "TBF")) # Expected output: 'Unrecognized hero, not allowed to board!'
```

### B) Avengers, Take Your Seats!

Next, implement a function `show_priority_seats(airplane_class: str, class_config: str, heroes: str) -> str` to print the new seat configuration after seating the Avengers, or `'Boarding Denied!'` if not possible.

#### Parameters' validation:
- If `airplane_class` input is incorrect, return `'Unrecognized class!'`.
- If `seat_config` does not belong to any of the classes (First, Business, or Economy), return `'Invalid seat configuration!'`.
- If `seat_config` is correct but has invalid characters, return `'Invalid seat letters!'`.
- If `airplane_class` and `seat_config` do not match, return `'Mismatch between 'airplane_class' and 'seat_config'!'`.
- If `heroes` has invalid characters, return `'Unrecognized hero, not allowed to board!'`.

#### Examples:

```python
print(show_priority_seats("First", "O|OO|O", "TBS")) # Expected output: 'Boarding Denied!'
# Although, Tony and Bruce can be alloted window and aisle seats, respectively, Steve's priority is middle seat.
```

```python
print(show_priority_seats("First", "O|OO|O", "TAB")) # Expected output: 'T|BA|O'
# Tony on window seat, Thor and Bruce on aisle seats.
```

```python
print(show_priority_seats("Business", "XO|XX|OO", "NCT")) # Expected output: 'Boarding Denied!'
# Although Clint and Natasha can sit on right window seats, Tony cannot be allocated a seat in Business class.
```

```python
print(show_priority_seats("Economy", "XOX|OXOO|OOX", "BAHHS")) # Expected output: 'XSX|BXAH|HOX'
# Steve with higest priority, followed by Bruce, Thor, and other Avengers.
```

```python
print(show_priority_seats("Economy", "XOX|OXOO|OOX", "LAH")) # Expected output: 'Boarding Denied!'
# All conditions are met except that Loki and Thor cannot be in the same row.
```

<hr>

When executing your algorithm, remember: Tony has got a suit for every occasion, but only his Mark Window Seat will be used for travel. Bruce’s aisle seat is not just a preference - it is a safety measure. Thor’s disdain for window seats is matched only by his love for mid-air lightning shows, so let us keep him away from the windows. And for Natasha and Clint, well, they are the best at what they do, but even they cannot fight the laws of airplane logistics.

Be alert and vigilant, and sort those seats! The Avengers Airline departure time is upon us, and Director Fury dislikes delay almost as much as he dislikes coding errors. Good luck!
