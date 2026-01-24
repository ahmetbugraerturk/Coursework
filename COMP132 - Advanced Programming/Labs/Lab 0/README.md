[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/DNbh6wN5)
# Spring2025 Lab0

**The objective of this Lab-0 is to make sure that you are able to clone the lab assignment template, and commit and push your solution to GitHub. You must follow the instructions provided on the course website.**

# IMPORTANT:
For each lab assignment, you must include and sign (by writing your name and student id number) the following Pledge of Honor statement at the beginning of your main method source code file. After including this statement, make sure that you do the commit and push operation on GitHub. Otherwise, your lab solution will not be graded.

```
/* *********** Pledge of Honor *************************** *
I hereby certify that I have completed this lab assignment on my own
without any help from anyone else. I understand that the only sources of authorized
information in this lab assignment are (1) the course textbook, (2) the
materials posted at the course website and (3) any study notes handwritten by myself.
I have not used, accessed or received any information from any other unauthorized
source in taking this lab assignment. The effort in the assignment thus belongs
completely to me.

READ AND SIGN BY WRITING YOUR NAME SURNAME AND STUDENT ID
SIGNATURE: <Name Surname, Student id>

**********************************************************/
```

# Lab-0 Information and Tasks:

You are expected to build a simple tool to help calculating the power consumption. The program will calculate the total energy cost of an electronic device based on factors like the usage time, the device's power consumption rate, and the power price. Additionally, you will personalize your program by printing your name and ID number and exploring how Java represents characters using the Unicode system. To this end, you need to follow these steps:

  <div align="center">
  <img src="/img/01.jpg" alt="Matrix Operations" />
</div>


Inside the cloned Eclipse project, you will find a public class named Comp132Lab0. In this class’ main method, you are asked to implement the following tasks as indicated by the comments in the code.

- **1.** **Define Variables:** Define three variables of type `double`, namely `time`, `powerConsumptionRate`, and `powerPrice`.

- **2.** **User Input:** Let the user input three values:
  - `time`: The total time of the usage (in hour).
  - `powerConsumptionRate`: The power consumption rate of the device (in KW per minute).
  - `powerPrice`: The price of power per KW (in your local currency).

**Note:** You can use the defined input object of type Scanner to get input from the user and can assume that the user enters positive integers.
```
  Scanner input = new Scanner(System.in);
```

- **3.** **Calculation:** Write code that calculates the Total Fuel Cost, and save the result in a new `double` variable called `totalCost`.
  ```
     totalCost = (time * 60) * powerConsumptionRate * powerPrice
  ```
- **4.** **Display the Result**: Use `System.out.println` to display the total cost of the trip to the user.
- **5.** **Personalize with Your Information:**
  - Define an object of type String, and store the string values of your name and surname in this object.
  - Define a variable of type int, and store your KUSIS ID number in this variable.
  - Use `System.out.println` to display your name, surname, and KUSIS ID number.
- **6.** **Explore Unicode:** Write the code for displaying the integer equivalents of the letters in your name and surname.

**Information:** *ASCII* (American Standard Code for Information Interchange) is a character encoding standard for electronic communication. ASCII codes are used to represent characters in computers and telecom devices.
ASCII is used to represent 128 English characters in the form of numbers, with each letter being assigned to a specific number in the range 0 to 127. For example, the ASCII code for uppercase A is 65, uppercase B is 66, and so on.
In Java, you can determine a character’s integer equivalent by preceding that character with (int), as in (int) 'A'. An operator of this form is called a cast operator. The following statement outputs a character and its integer equivalent:
```
System.out.printf("Character %c has the value %d%n", 'A', ((int) 'A'));
```
When the preceding statement executes, it displays the character A and the value 65 (from the Unicode character set). The format specifier %c is a placeholder for a character (in this case, the character 'A').


### After you complete the tasks, do not forget to commit your changes and push them to your repository on GitHub.

