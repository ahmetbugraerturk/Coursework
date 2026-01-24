[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Ek3szehP)
# COMP132, Spring2025, Lab 8 PreLab

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

   ##### :pushpin: - All instance variables MUST have the exact name written in the instructions.
   ##### :pushpin: - You should implement getter/setter methods whenever needed (for example, if you are going to access the instance variables from other classes). You may use auto-generator for getter/setter methods (under the Source menu in Eclipse). Do NOT implement unused Getter/Setter methods. You will be penalized for each unused Getter/Setter.
   ##### :pushpin: -  You MUST follow the instructions (Package name, Class name, method name, variables, ...) so carefully. The packages, classes, instance variables, and methods MUST be created following the descriptions given in the assignment.
   ##### :pushpin: -  Please check the sample output provided at the end of this assignment. Your output MUST be exactly the same as the provided sample output.
   ##### :pushpin: -  After you complete the tasks, do not forget to commit your changes and push them to your repository on GitHub BEFORE 9.30 :clock930: AM, Friday.
   ##### :pushpin: -  This README.md file only contains the instructions for PRELAB. You will also have INLAB questions.

  # Lab 8 Prelab: KU-IMS: Inventory Management System

  This programming lab focuses on **data validation using Regular Expressions and Generics concepts**. The assignment aims to enhance your understanding of **Regular Expressions** and **Generics** by implementing an inventory management system that validates, filters, and retrieves items.

Your task is to implement an inventory management system (KU-IMS) that validates product information, applies transformations for standardization, and retrieves important data using generics. The application will ensure all items follow strict validation rules and allow items to be retrieved.

## Requirements

- Use Regular Expressions.
- Use Generics for implementing type-safe operations.
- Do **not** use lambda expressions or streams.
- Add getter/setter methods when applicable.

<div align="center">
  <img src="/img/02.png" alt="inventory" />
</div>

You are provided with the **Main.java** file and an input text file. Check the main file to understand the sample output better and how each method and field is used. You need to develop your assignment by following the instructions below.

## Package Structure
```
src/ 
   - main/
      - Main.java 
      - inventory.txt
   - item/
      - InventoryItem.java
      - Item.java
   - functions/ 
      - InventoryManager.java 
      - InventoryFilter.java 
   - util/ 
      - FileUtils.java
```
## item package:

## Item Class

This class is an abstract class that must implement the generic Comparable interface of Collections.

### Instance Variable:
- `double price`: Price of the item.

### Method:
- `public Item(double price)`: Constructor for the Item class.

## InventoryItem Class

This class must extend Item. 

### Instance Variables:
- `String itemID`: Unique identifier for the item.
- `String name`: Name of the item.
- `String code`: Code of the item.
- `int quantity`: Quantity available in the stock.

### Methods:
- `public InventoryItem(String itemID, String name, double price, int quantity)`: The constructor initializes the inventory item with the necessary information.
- `toString()`: Displays item details in a format.

#### Sample Output:
```ID: AB1234*, Name: SmartWatch, Code: AMS342, Price: 10.00, Quantity: 20```

## functions package:

## InventoryManager Class

### Instance Variable:
- `private static final Pattern ID_PATTERN = Pattern.compile("your_regex_here")`: Pattern to match.

### Methods:
- `public boolean isItemIDValid(InventoryItem item)`:
   - Validates the item ID using the following rules (implemented via Regular Expressions):
      - Starts with 2 uppercase letters.
      - Followed by 4 digits.
      - Ends with a special character from (*, #, @) only.
      - The total length of the characters should be exactly 7.	
   - Returns true if the item ID is valid and false otherwise.

- `public String generateItemCode(InventoryItem item)`:
   - Generates a unique code based on the item’s properties based on the following:
      - The first three letters of the item name in reverse in uppercase.
      - The last two digits of the digit part of the item ID.
      - The middle letter of the item ID. (For even IDs, take the ceiling.)
   - It should return the generated code.

- `public Map<String, Double>inventoryValueCalc(List<InventoryItem> items)`: 
   - Calculates the total value  (`price x quantity`) of each item in the inventory  
   - Returns a map where keys are the item names and the values are the values of the items.

## InventoryFilter Class

### Methods:
- `public Map<String, Double> removeBasedOnValue(Map<String, Double> inventoryValues, int n)`: Filters and transforms the inventory list based on a threshold `n`. It should remove any entry from the map where the inventory value is less than the specified integer `n`. For each remaining inventory item, `(i.e., >= n)`, the value of that item is doubled. It returns a new `Map<String, Double>` containing only the filtered and transformed items.

- `public <T extends Comparable<T>> T findMaximum(List<T> items)`: A method to return the highest value on the list items.

- `public <T extends Comparable<T>> List<T> orderByAscension(List<T> list)`: A method to compare inventory items based on price in ascending order. Two items with the same price are considered equal. Implement any necessary method before implementing this one.

- `public <T extends Item> List<T> makeDiscount(List<T> items, int discount)`: Takes a list of items and applies a discount on it based on an input value discount.

## util package:

## FileUtils Class

### Methods:
- `public static List<InventoryItem> readInventoryItems(String filePath, InventoryManager manager)`:
   - Using Scanner class methods, reads the `inventory.txt` and parses the line expecting the format: itemID, name, price, quantity.
   - Validates the itemID using the `isItemIDValid()` method from `InventoryManager`. It should generate a unique item code using the `generateItemCode()` method and inserts it after (name) to the appropriate field, namely code. The structure should be as follows: itemID, name, code, price, and quantity.
   - Constructs an `InventoryItem` using the updated and validated information.
   - Skips any malformed or invalid entries and logs a warning message: “Skipping malformed or invalid line: [line]”.
   - Returns a list of all successfully parsed and validated `InventoryItem` objects.


## main package

## Main.java

The provided **Main class** will test the implementation. You should add the **pledge of honor** to it. Any change more than that may lead to grade reduction.


## Sample output
```
Skipping malformed or invalid line: IJ7890*,Mouse,11.0,5,3
Skipping malformed or invalid line: INVALID,Item,1.0,1

All Inventory Items:
ID: AB1234*, Name: SmartWatch, Code: AMS342, Price: 10.00, Quantity: 20
ID: CD5678#, Name: Computer, Code: MOC786, Price: 5.00, Quantity: 50
ID: EF9012@, Name: Phone, Code: OHP120, Price: 25.00, Quantity: 3
ID: GH3456#, Name: Headset, Code: AEH564, Price: 12.00, Quantity: 10

Inventory Values:
SmartWatch: 200.0
Computer: 250.0
Phone: 75.0
Headset: 120.0

Filtered (for >=100 and doubled):
SmartWatch: 400.0
Computer: 500.0
Headset: 240.0

Ordering by ascension:
ID: CD5678#, Name: Computer, Code: MOC786, Price: 5.00, Quantity: 50
ID: AB1234*, Name: SmartWatch, Code: AMS342, Price: 10.00, Quantity: 20
ID: GH3456#, Name: Headset, Code: AEH564, Price: 12.00, Quantity: 10
ID: EF9012@, Name: Phone, Code: OHP120, Price: 25.00, Quantity: 3

Most expensive item: ID: EF9012@, Name: Phone, Code: OHP120, Price: 25.00, Quantity: 3

Items before Discount:
ID: CD5678#, Name: Computer, Code: MOC786, Price: 5.00, Quantity: 50
ID: AB1234*, Name: SmartWatch, Code: AMS342, Price: 10.00, Quantity: 20
ID: GH3456#, Name: Headset, Code: AEH564, Price: 12.00, Quantity: 10
ID: EF9012@, Name: Phone, Code: OHP120, Price: 25.00, Quantity: 3


Items after Discount:
ID: CD5678#, Name: Computer, Code: MOC786, Price: 4.00, Quantity: 50
ID: AB1234*, Name: SmartWatch, Code: AMS342, Price: 8.00, Quantity: 20
ID: GH3456#, Name: Headset, Code: AEH564, Price: 9.60, Quantity: 10
ID: EF9012@, Name: Phone, Code: OHP120, Price: 20.00, Quantity: 3
```






  
