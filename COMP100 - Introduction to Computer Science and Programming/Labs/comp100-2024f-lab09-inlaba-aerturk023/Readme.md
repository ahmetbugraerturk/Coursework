[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/PIax9iB7)
The testcases given are just sample tests, and additional testcases will be used while grading. 

## Q1: Count Paths in a Grid


In this question, your task is to calculate the number of distinct paths in an `m x n` grid, starting from the top-left corner `(0, 0)` and moving only to the right or downward to reach the bottom-right corner `(m-1, n-1)`.

Your task is to write the function `count_paths(m, n)`, which takes two integers `m` and `n` as input and returns the number of unique paths.

#### Your solution:
*  **MUST** use **RECURSION**.
*  **MUST NOT** use global variables.
*  **MUST NOT** use any libraries.
* Otherwise, your solution **WILL NOT** be accepted.

---

### Example 2x2 Grid:

#### Input:
```
m = 2
n = 2
```

#### Output:
```
2
```

#### Explanation:

You can think of the grid as a graph where each cell is a node, and moving **down** or **right** corresponds to selecting the next node. Consider a 2x2 grid. The paths can be represented as a binary tree of choices:

```
Start (0, 0)
   /       \
 Down      Right
(1, 0)    (0, 1)
     \        /   
     Right   Down  
    (1, 1)  (1, 1) 
        |      |
      End     End
```

### Explanation of the Tree:
1. Each step is a decision: move **down** or **right**.
2. The tree's leaves with (1, 1) represent reaching the bottom-right corner.


### Example: 2x3 Grid

#### Input:
```
m = 2
n = 3
```

#### Output:
```
3
```

Consider a 2x3 grid. The paths can be represented as a binary tree of choices:

```
        Start (0, 0)
        /       \
       Down      Right
      (1, 0)     (0, 1)
       \          /   \
    Right       Down  Right
    (1, 1)     (1, 1) (0, 2)
        \       \     /       
    Right    Right   Down
    (1, 2)  (1, 2)    (1, 2)
        |       |       |
       End     End      End
```

### Explanation of the Tree:
1. Each step is a decision: move **down** or **right**.
2. The tree's leaves with (1, 2) represent reaching the bottom-right corner.

---