[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/-yyu6-V9)
# COMP100 2024F Problem Set 1: Guess-Check, Approximation, Bisection - Saving the Patient
Deadline: 14 November 2024, Thursday 11:59 PM

This problem set focuses on Python control flow and introduces Bisection Search. You will tackle four problems. For each part, save your code as `ps1{name of the part}`. For example, Part A should be `ps1a.py`.

## Introduction
A doctor rushes into the hospital emergency room. "We have a critical patient with a severe infection!" they exclaim. The patient is battling a bacterial infection that’s rapidly spreading within their body. The patient’s immune system, specifically white blood cells produced by the bone marrow, is fighting hard, but it may not be enough. Doctors turn to you to help manage the patient’s treatment and determine the best course of action.

Your mission is to calculate the survival chances by managing white blood cell production, accounting for bacterial growth, and strategically using drugs to help the patient.

## Parts
- __Initial Struggle__
- __Mounting Infection__
- __Critical Decision__

## PART A: Initial Struggle (20 Points)
The patient's immune system begins its fight. The number of bacteria in the body will be assumed to be constant for now, while the bone marrow produces a steady amount of new white blood cells each day. You must calculate how many days it will take for the white blood cell count to reach or exceed the bacteria count.

- Let `total_bacteria` represent the initial bacterial count.
- Let `total_white_cells` represent the initial white blood cell count.
- Let `white_cell_growth_rate` represent the daily rate of white blood cell production. Each day, the bone marrow produces an additional percentage of the current white blood cell count (e.g., if `white_cell_growth_rate` is `0.1` and there are 1000 white blood cells today, there will be 1100 cells tomorrow). 
- The added cells should be cast to an integer (rounded down) with `int()` method to avoid fractional cells.

Then your program should calculate how many days it will take for the white blood cell count to reach or exceed the bacteria count and return `days` (int).
- Note: If the white blood cells cannot reach or exceed the bacterial count within 90 days (i.e. upto and including the 90th day), your function should return None.

### Sample Runs:
- `wc_count_no_bacterial_growth(total_bacteria = 80000,total_white_cells = 30000, white_cell_growth_rate= 0.05)`  Output: `21`

- `wc_count_no_bacterial_growth(55000, 16000, 0.1)`  Output: `13`

- `wc_count_no_bacterial_growth(100000,100, white_cell_growth_rate= 0.02)`  Output: `None`

## PART B: Mounting Infection (30 points)
More realistically, the bacteria also reproduce daily now. Now, both the bacteria and white blood cells grow daily. The white blood cells continue to increase as before, but the bacteria also have a daily growth rate.

- Let `total_bacteria` represent the initial bacterial count.
- Let `total_white_cells` represent the initial white blood cell count.
- Let `white_cell_growth_rate` represent the daily rate of white blood cell production.
- Let `bacterial_growth_rate` represent the daily rate of white blood cell production.
- The added cells should be cast to an integer (rounded down) with `int()` method to avoid fractional cells.

Then your program should calculate how many days it will take for the white blood cell count to reach or exceed the bacteria count and return `days` (int).
- Note: If the white blood cells cannot reach or exceed the bacterial count within 90 days (i.e. upto and including the 90th day), your function should return None.

### Sample Runs:
- `wc_count_with_bacterial_growth(total_bacteria= 55000,total_white_cells= 16000,white_cell_growth_rate= 0.1,bacterial_growth_rate= 0.03)` Output: `19`

- `wc_count_with_bacterial_growth(120000, 60000, 0.3, 0.1)` Output: `5`

- `wc_count_with_bacterial_growth(150000, 50, 0.2, 0.1)` Output: `None`


## PART C: Critical Decision (50 points)
The infection reaches a critical stage, and it’s clear that the natural immune response won’t be enough within the needed time frame. Doctors say the patient now has 30 days left before losing against the infection. To help the patient survive, you must help white blood cells overcome the bacterial growth in 30 days. To do this, you need to use various drugs that will supply their immune system up to a point where daily `white_cell_growth_rate` can go up to `1.0`, but giving them high doses of medicine would create an overdose situation. Hence, you should calculate the minimum `white_cell_growth_rate` possible for patient to survive by matching the count of the bacteria within the given tolerance interval using bisection search so that the patient will not be exposed to any unnecessary drugs.

Your code should consist of three functions, `simulate_growth` and `wc_count_is_acceptable`are helper functions for your main function `find_acceptable_wc_growth_rate`.
- `simulate_growth` function simulates the growth of bacteria and white cells over 30 days. 
- `wc_count_is_acceptable` function checks if the white cell count is within an acceptable range compared to the bacteria count.

* While matching the count of the bacteria, we will be aiming for a range of 1000 white blood cells, i.e. if there are `x` bacteria, anything between `[x-1000, x+1000]` is acceptable.
* As mentioned above, even with drug use `white_cell_growth_rate` can increase up to `1.0` at max, so this should be upper bound for the search.
* The added cells should be cast to an integer (rounded down) with `int()` method to avoid fractional cells.

### Problem Setup
- If the white blood cell count can match or exceed the bacteria within 1000 cells (i.e., if bacteria count is `x`, anything between `[x-1000, x+1000]` is acceptable), the treatment is successful.
- You can adjust the `white_cell_growth_rate` up to a maximum of 1, but if an effective dose is impossible without exceeding this limit in 30 days, return `None`.
- If the bisection search exceeds 500 iterations and fails to produce an acceptable boost range within these parameters, return `None` .

---

`simulate_growth` function should take variables:
- Initial bacterial count (`total_bacteria`)
- Initial white blood cell count (`total_white_cells`)
- Daily white blood cell production rate (`white_cell_growth_rate`)
- Daily bacterial growth rate (`bacterial_growth_rate`)
- Simulation duration (`days=30`,optional)

And should simulate the growth during 30 days. While cells are being added according to the growth rates, the added cells should be cast to an integer (rounded down) with `int()` method to avoid fractional cells.

`simulate_growth` function should return;
- Final bacterial count (`total_bacteria`)
- Final white blood cell count (`total_white_cells`)

---

`wc_count_is_acceptable` function should take variables:
- Bacterial count (`total_bacteria`)
- White blood cell count (`total_white_cells`)

And should check if white cell count is within an acceptable range compared to the bacteria count.

- `wc_count_is_acceptable` function should return True or False according to the comparison.

---

Your main function `find_acceptable_wc_growth_rate` should take variables:

- Initial bacterial count (`total_bacteria`)
- Initial white blood cell count (`total_white_cells`)
- Daily bacterial growth rate (`bacterial_growth_rate`)

And should calculate `final_bacteria count, final_white_cell_count, white_cell_growth_rate` 

`find_acceptable_wc_growth_rate` function should return as a three element __tuple__:

- The final counts of both bacteria and white blood cells `(int final_bacteria count, int final_white_cell_count)`.
- The minimum effective antibiotic boost `(float white_cell_growth_rate)`.
- Your code do not have to *exactly* match all the floating points in the sample outputs, if your answer looks similar to the given sample output growth rate upto 3 decimal places then it's probably correct.
- If no effective dose is found within the given 30 days period, your code should return `None`.

### Sample Runs:

- `find_acceptable_wc_growth_rate(total_bacteria = 100000, total_white_cells= 50000, bacterial_growth_rate= 0.3)` Output:`(261998549, 261999017, 0.3303871154785156)`

- `find_acceptable_wc_growth_rate(150000, 5000, 0.3)` Output:`(392997909, 392997878, 0.456071138381958)`

- `find_acceptable_wc_growth_rate(100000, 500, 0.8)` Output:`None`
