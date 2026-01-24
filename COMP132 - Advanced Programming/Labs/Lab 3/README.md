[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/VvMuPy2w)
# COMP132, Spring2025, Lab 3 PreLab

# IMPORTANT

For each lab assignment, **you must include and sign (by writing your name and student ID number) the following Pledge of Honor statement at the beginning of your main method source code file. After including this statement, make sure that you do the commit and push operation on GitHub. Otherwise, your lab solution will not be graded.**
```
/* *********** Pledge of Honor ************************************************ *

I hereby certify that I have completed this lab assignment on my own
without any help from anyone else. I understand that the only sources of authorized
information in this lab assignment are (1) the course textbook, (2) the
materials posted on the course website, and (3) any study notes handwritten by myself.
I have not used, accessed, or received any information from any other unauthorized
source in taking this lab assignment. The effort in the assignment thus belongs
completely to me.
READ AND SIGN BY WRITING YOUR NAME SURNAME, AND STUDENT ID
SIGNATURE: <Name Surname, Student id>
********************************************************************************/
```
## Please carefully review the following important notes. Violating each one of them will result in a grade deduction.

## IMPORTANT NOTES: 

   ##### :pushpin: - All instance variables MUST be private unless specified otherwise, and they should have the exact name written in the instructions.
   ##### :pushpin: - You should implement getter/setter methods whenever needed (for example, if you are going to access the instance variables from other classes). You may use auto-generator for getter/setter methods (under the Source menu in Eclipse). Do NOT implement unused Getter/Setter methods. You will be penalized for each unused Getter/Setter.
   ##### :pushpin: -  You MUST follow the instructions (Package name, Class name, method name, variables, ...) so carefully. The packages, classes, instance variables, and methods MUST be created following the descriptions given in the assignment.
   ##### :pushpin: -  Please check the sample output provided at the end of this assignment. Your output MUST be exactly the same as the provided sample output.
   ##### :pushpin: -  After you complete the tasks, do not forget to commit your changes and push them to your repository on GitHub BEFORE 9.30 :clock930: AM, Friday.
   ##### :pushpin: -  This README.md file only contains the instructions for PRELAB. You will also have INLAB questions.

   # Space Colony Resource Management

   In this prelab, your task is to develop a Java application to manage and analyze resource distribution among different space stations in a colony on Mars. Each space station is responsible for storing essential resources (oxygen, water, food, and energy) in grid-based storage units, which will be represented as 2D arrays.
   
This assignment will help you practice multidimensional arrays, which have many real-world applications, such as scientific computing, simulations, and robotics.

## Assignment Details:

Your Java project should be structured into three packages:

- resources (contains ResourceHelper and ResourceGrid classes)
- order (contains Order class)
- main (contains ResourceMain class for testing, given)

- Package: resources
  - ResourceHelper Class: Contains utility methods for checking resource grids.
  - ResourceGrid Class: Represents a space station’s storage and provides resource management methods.
- Package: order
  - Order Class: Represents new orders for the space station’s storage and processes such orders.
- Package: main
  - ResourceMain Class: Contains the main method for testing the resource operations.

<div align="center">
  <img src="/img/01.png" alt="Matrix Operations" />
</div>

# Class Details

## ResourceHelper Class

This class provides utility methods for common operations on resource grids.

### Methods:
- `public static int[][] deepCopy(int[][] grid)`: Creates a deep copy of a resource grid.
- `public static boolean areSameSize(int[][] grid1, int[][] grid2)`: Checks if two space stations have the same resource storage dimensions.

## ResourceGrid Class

This class encapsulates a space station’s resource storage grid and provides various operations.

### Fields:
- `stationName`:  Name of the space station as a String.
- `resources: 2D fixed-size array of int ( int [][] )`: representing the resources stored in the station. The grid-like structure of the array reflects the actual layout of resource storage within the base, making it easy to map resources to their physical positions.

### Constructors:
- `public ResourceGrid(String stationName, int[][] resources)`: initializes a ResourceGrid instance with a given name and 2D array of resources.
- `public ResourceGrid(String stationName)`: initializes a ResourceGrid instance with a given name and with an empty 2D array of resources with 3 rows and 3 columns, using the 2 parameter constructor. In other words, you will be calling the constructor with the two parameters in this constructor.
- `public ResourceGrid()`: initializes a ResourceGrid instance with the name “Unknown Station”, using the constructor with name as a parameter.

#### Note: Whenever you perform an operation that produces a new grid, you MUST use the deepCopy() method from ResourceHelper Class to ensure that changes to the new grid do not affect the original grid.

#### Note: Please note that Grid summation and subtraction operations only work if the grids have the same dimensions (same x and y). For this, check the dimensions and print a warning if they are not equal. You must do it by using the areSameSize() method from the ResourceHelper Class. 

### Methods:

- `public void transferResources(ResourceGrid other)`: Transfers resources from another station to the current one (element-wise addition). The method should do the element-wise addition and display the result using the `toString()` method. If the stations don’t have the same grid dimensions, the method should display: "_Resource transfer between `this stationName` and `other stationName` failed: Different storage capacities._"
- `public void depleteResources(ResourceGrid other)`: Subtracts resources of another station from the current station’s resources, i.e. sending the resources to the other grid. 
  - After subtraction, if any resource becomes less than `zero`, make it equal to `zero`. Then, the method should display the result using the `toString()` method.
  - If the stations don’t have the same dimensions, the method should display: "_Resource depletion failed: Different storage capacities._"

Note: Both `transferResources` and `depleteResources` methods should keep the original resource unchanged.

- `public void scaleResources(int factor)`: Multiplies each resource value by a given factor and displays the result using the `toString()` method.
- `public void redistributeResources()`: Redistributes resources by swapping rows and columns. Uses `toString()` method to display the new distribution. This method does the redistribution in place, which means that it replaces the original ResourceGrid resources.
- `public void checkIfBalanced()`: Checks if the space station’s resource storage is balanced (if each row has the same total resource count). The method should display either "_Station stationName is balanced_." OR "_Station stationName is not balanced._"
- `public void checkIfEmptyStorage()`: Checks if the space station’s storage is completely empty (all values are zero). The method should display either "_Storage at station stationName is completely empty_." OR "_Storage at station stationName is not empty_."
- `public void checkIfMajorityResource(int resourceType)`: Determines if a given resource type is the majority across the grid. The method should display either "_Station stationName has a majority of resourceType._" OR "_Station stationName does not have a majority of resourceType._". A resource type is considered a majority if it appears in at least half of the total grid cells.
- `public String toString()`: Provides a string representation of the resource grid.

## order package

### Order Class

This class represents the order amounts for the resource grid fields.

### Fields:
- `orderGrid(int [][])`: 2D fixed-size array representing the order amounts for each resource.

### Constructor:
- Initializes an Order object with the given `orderGrid`.

### Methods:

- `public boolean canMultiply(ResourceGrid grid)`: Determines whether the `orderGrid` can be multiplied with the given `ResourceGrid`. This method takes a `ResourceGrid` object as input and retrieves its resource grid. It returns `true` if the number of columns in the resource grid matches the number of rows in `orderGrid`, ensuring that grid multiplication is feasible. Otherwise, it returns `false`.

#### Note: Grid multiplication between two grids, A and B, is only possible if the number of columns in A matches the number of rows in B. Specifically, if A has dimensions m x n and B has dimensions p x q, then n must be equal to p for the multiplication to be valid. If these dimensions do not align, it is not possible to perform multiplication.

- `public ResourceGrid makeOrder(ResourceGrid grid)`: perform grid multiplication between the `orderGrid` and the given `ResourceGrid`. The method first should call `canMultiply(grid)` to check compatibility. If the grids are not compatible, it prints a message "_Multiplication is not possible: Dimension mismatch._" and returns the original `ResourceGrid` without modification. If the grid and the order grid are compatible, it performs grid multiplication, storing the results in a new grid. The method then returns a new `ResourceGrid` containing the computed grid, with the same name of the given grid.

## main package

## ResourceMain Class

The provided ResourceMain class is for testing your implemented Java application. This class is a driver class to demonstrate and test the functionalities of your implementation. You are not allowed to change the given file. You are only allowed to add the pledge of honor to it. Any other changes may lead to grade reduction.

### Sample Output
```
--- Initial Storage ---

  Storage 1 ---

[ 3 2 1 ]
[ 5 6 4 ]
[ 7 3 9 ]

  Storage 2 ---

[ 1 4 2 ]
[ 6 8 3 ]
[ 2 1 7 ]

--- New Storage at Alpha after transfer ---

[ 4 6 3 ]
[ 11 14 7 ]
[ 9 4 16 ]

--- Original Alpha  Storage was ---

[ 3 2 1 ]
[ 5 6 4 ]
[ 7 3 9 ]

--- New Storage at Alpha after depleting Resources ---

[ 2 0 0 ]
[ 0 0 1 ]
[ 5 2 2 ]

--- Original Alpha  Storage was ---

[ 3 2 1 ]
[ 5 6 4 ]
[ 7 3 9 ]

New Storage at Alpha after scaling:
[ 6 4 2 ]
[ 10 12 8 ]
[ 14 6 18 ]

New Storage at Alpha after redistribution :
[ 6 10 14 ]
[ 4 12 6 ]
[ 2 8 18 ]

Resource transfer between  Alpha and Omega failed: Different storage capacities.
Station Beta is not balanced.
Storage at station Unknown Station is completely empty.
Station Alpha does not have a majority of 5.

--- Processing orders for Alpha Storage ---

[ 118 88 100 ]
[ 92 56 78 ]
[ 116 92 92 ]

--- Processing orders for Beta Storage ---

[ 38 25 ]
[ 87 84 ]
[ 49 35 ]

--- Processing orders for Omega Storage ---

Multiplication is not possible: Dimension mismatch.
[ 3 2 ]
[ 5 6 ]
[ 7 3 ]

```


