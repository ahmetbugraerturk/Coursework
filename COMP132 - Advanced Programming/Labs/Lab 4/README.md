[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/4iIDVY0x)
# COMP132, Spring2025, Lab 4 PreLab

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

  # Lab 4 Prelab: AlienNet
  In this lab, you will be practicing **Inheritance and related object-oriented programming concepts**. Inheritance models an “is-a” relationship between a base class (Superclass) and its more specific types (Subclasses), and promotes code reuse.

To practice these concepts, you are going to implement a fictional alien communication platform called AlienNet. Think of it as an interplanetary Twitter for aliens, where different types of alien species post their transmissions to each other!

## Note: In addition, you are expected to implement simple GUI tasks as a preparation for your upcoming project, which is part of your current prelab assignment.

## Assignment Details:

Packages:
- alien
  - Alien Class: superclass for all aliens
  - CommonAlien Class: subclass of Alien for regular aliens
  - EliteAlien Class: subclass of Alien for elite aliens with advanced rights
  - RoyalAlien Class: subclass of EliteAlien 
  - Transmission Class
- aliennet
  - AlienNet Class: manages aliens and transmissions.
- alienNetGUI
  - AlienNetGUI: GUI-related implementation should be in this class.
- main
  - Main Class: Given. Should not be modified.

##### You must decide on access modifiers (private, protected, public) and appropriate data types where necessary.

<div align="center">
  <img src="/img/01.png" alt="Matrix Operations" />
</div>

# Class Details

## alien package

## Alien class

### All aliens have:
- `name (String)`
- `id (int)`
- `static idCounter (int)`
- `transmissions (ArrayList of Transmission)`

### Methods:
- `Alien(String name)`: constructor that assigns a unique id (use static counter)
- `void displayTransmissions()`: displays all transmissions. Take a closer look at the sample output to see the method behavior in more detail.
- `void sendTransmission(String message)`: creates and adds a new transmission
- Add getter/setter methods if needed

## CommonAlien class

- Common aliens can delete their transmissions but not edit them.
- `CommonAlien(String name)`: constructor, must call superclass constructor.
- `void deleteTransmission(int id)`: deletes transmission at index id
- _Override_ `displayTransmissions()`: print (Common) before name and messages

## EliteAlien class

- Elite aliens have the power to edit their transmissions but cannot delete them.
- `EliteAlien(String name)`: constructor, must call superclass constructor.
- `void editTransmission(int id, String newMessage)`: edits transmission at index id
- _Override_ `displayTransmissions()`: print (Elite) before name and messages

## RoyalAlien Class

This class is a subclass of EliteAlien, representing royalty from elite alien species. These aliens not only have the privilege to edit transmissions like any EliteAlien, but they also have special diplomatic status and can issue declarations to all commoners.

### Additional Field:
- `title (String)`: Their royal title (e.g., “Emperor,” “Queen,” “Prince”), by default, should be “Emperor”.

- Constructor: `public RoyalAlien(String name)`: Calls the EliteAlien constructor, and initializes the royal title with default value field. 

### Methods:
- `public void declare(String announcement)`: Displays a formal declaration in this format:
 `"👑 [title] [name] declares: [announcement]"`

- _Override_ `displayTransmissions()`: Instead of (Elite), prefix with (Royal - `title`).

## Transmission class

### Each transmission contains:

- `message (String)`: The actual content sent by the alien.

### Methods:

- `Transmission(String message)`: constructor
- `void edit(String newMessage)`: edits the message
- `String toString()`: returns string representation of the transmission
- Add getters/setters if needed

## aliennet package

## AlienNet class

### Field:
- `ArrayList<Alien> aliens`

### Methods:
- `Alien addAlien(String name, String type)`: adds a new alien of the given type ("Elite" or "Common"). Returns the new alien. If invalid, display:
 _No such alien type: "type"_.
- `int calculateRevenue()`: Each Elite alien pays 10 galactic credits. (Iterate the list of aliens and add 10 to the sum for each Elite Alien object)
- `void displayAllTransmissions()`: display transmissions from all aliens

## alienNetGUI package

## AlienNetGUI Class

You are asked to implement a simple Swing GUI-related application that will help you get familiar with the framework as a preparation for the project. Check the details of the task at the end of the document after the sample output. 

## main package

The provided **Main.java** class is for testing your implemented Java application. This class is a driver class to demonstrate and test the functionalities of your implementation. You are not allowed to change the given file. You are only allowed to add the **pledge of honor** to it. Any other changes may lead to grade reduction.

# Important note:
There are three **GUI Tasks** that you **MUST** implement as the prelab assignment. You may find the GUI Tasks in the shared PFD file (GUI.pdf) in this repository.

## Sample Output
```
(Common) Zorg:
Transmission: Found an energy source on Asteroid 44-Z.
Transmission: I need to report this to the Council.

(Elite) Xarn:
Transmission: My fleet is heading toward the Kuiper Belt.
Transmission: Meeting with Queen Vela was successful.

(Common) Blip:
Transmission: I discovered a new fungus on Mars.

(Elite) N'Kora:
Transmission: These humans are fascinating.
Transmission: I’m monitoring their broadcasts.

(Elite) Elthor:
Transmission: Warp drive malfunction. Stuck near Saturn.

(Royal - Emperor) Zylara:
Transmission: Peace has been negotiated with the Andromeda Federation.
Transmission: Our knowledge-sharing treaty begins tomorrow.

(Royal - Queen) Astralyn:
Transmission: Peace is so important.

👑 Emperor Zylara declares: All spaceports shall be renamed in honor of the Galactic Harmony Treaty.
👑 Queen Astralyn declares: A new era of peace begins today, all alliances shall be honored across galaxies, and conflict shall be silenced under the stars.
------------------------------------
(Common) Zorg:
Transmission: Found an energy source on Asteroid 44-Z.

(Elite) Xarn:
Transmission: Fleet will now survey Pluto instead.
Transmission: Meeting with Queen Vela was successful.

(Common) Blip:
Transmission: I discovered a new fungus on Mars.

(Elite) N'Kora:
Transmission: These humans are fascinating.
Transmission: I’m monitoring their broadcasts.

(Elite) Elthor:
Transmission: Warp drive malfunction. Stuck near Saturn.

(Royal - Emperor) Zylara:
Transmission: Peace has been negotiated with the Andromeda Federation.
Transmission: Our knowledge-sharing treaty begins tomorrow.

(Royal - Queen) Astralyn:
Transmission: Peace is so important.

Revenue for this month: 50 galactic credits
No such alien type: TimeTraveler
```
