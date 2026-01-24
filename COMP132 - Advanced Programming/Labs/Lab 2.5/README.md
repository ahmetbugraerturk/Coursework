[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/lo-uPWXM)
# COMP 132, Spring2025, lab 2.5

# MUST READ

For each lab assignment, **you must include and sign (by writing your name and student id number) the following Pledge of Honor statement at the beginning of your _main method source code file_. After including this statement, make sure that you do the commit and push operation on GitHub. Otherwise, your lab solution will not be graded.**
```
/* *********** Pledge of Honor ************************************************ *

I hereby certify that I have completed this lab assignment on my own
without any help from anyone else. I understand that the only sources of authorized
information in this lab assignment are (1) the course textbook, (2) the
materials posted at the course website and (3) any study notes handwritten by myself.
I have not used, accessed or received any information from any other unauthorized
source in taking this lab assignment. The effort in the assignment thus belongs
completely to me.
READ AND SIGN BY WRITING YOUR NAME SURNAME AND STUDENT ID
SIGNATURE: <Name Surname, Student id>
********************************************************************************/
```

# Lab 2.5 (Debugging Lab)

### Before attempting this lab's prelab assignment, study the material about Debugging on the course site (Programming Labs tab). Also, as usual you will have in-lab assignment.

In this lab, you have been provided a partially completed Java source code with some array processing methods inside, which manage books in a library collection using arrays. 

<div align="center">
  <img src="/img/01.jpg" alt="Matrix Operations" />
</div>

## Your tasks:

- Use **debugging tools** to find and fix errors in the code so that all outputs match the expected results.
- Implement two new methods
  - `sortByPriceAscending`: This method will order books in the collection based on price, following the approach used in  `sortByPriceDescending`. 
  - `findCommonBooks`: This method has two 1-D String arrays, `String[] library1`, `String[] library2`, as its method parameters, representing books in two different library branches. The method does not return any value. This method should: 
    - Print the number of common books in two library collections provided as method arguments,
    - Keep the common books in a new array object,
    - Print the content of the new array object.


The provided source code file includes methods for **sorting books by price**, **calculating the total cost of books**, **finding the most expensive book**, and **removing an item from the collection**, and **swapping two array cells**. However, some methods have intentional errors, and certain functions need to be implemented by you.

## Your primary task is to use Debugging tools to:

- Identify the errors in the methods provided.
- Fix these errors by examining the program’s behavior through breakpoints, watch variables, or step-by-step execution.
- Ensure that all outputs match the expected results provided in the comments of the code.
- Implement the `sortByPriceAscending` method to order books in the collection by price, adapting the approach used in `sortByPriceDescending`.
- Implement the `findCommonBooks` method.
- Show the array while being sorted at a specific iteration using debugging tools.

#### Important: You must use the same general approach as `sortByPriceDescending` but modified for ascending instead. Do not write your own method, otherwise we will not grade that part of your lab solution.

## Requirements for Debugging and Demonstration

This lab places a strong emphasis on debugging. **Simply providing a fixed solution without demonstrating your debugging process will not meet the lab requirements.** Debugging is an essential skill that goes beyond fixing errors; it helps you understand the cause of the issue and how the code functions as a whole. We want you to showcase your ability to locate and understand errors, not just the fixed code.


# During the lab hours on Friday, you’ll be required to:

- **Demonstrate to the TA/SLs how you used debugging tools** (such as breakpoints, inspecting variable values, and stepping through code) to identify the issues in each method.
  
- **Explain the debugging steps you took** to understand what was going wrong with each method, why the error occurred, and how you resolved it.
  
- **Show that the corrected code works as expected** by producing the correct output in each case.


# Grading Criteria

## Your lab submission will be evaluated based on the following:

- **Debugging Process**: Your understanding and explanation of the debugging process. Show how you used debugging tools to identify errors.
- **Code Corrections**: The effectiveness of your fixes and whether they resolve the issues identified.
- **New Method Implementations**: Your implementation of `sortByPriceAscending`, following the same approach as `sortByPriceDescending`, and the implementation of `findCommonBooks`.
- **Final Output**: Verification that all corrected code produces the expected results as specified in the comments.

# Keep in mind that Simply providing a fixed solution without demonstrating your debugging process will not meet the lab requirements and in this case you will get Zero.
