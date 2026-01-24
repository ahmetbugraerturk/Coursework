[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/uL0vAIVB)
# COMP132, Spring2025, Lab1 PreLab

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
   
   # Galactic Challenge Game Project

   Your task is to implement a text-based game called "Galactic Challenge" between two players. In this game, each player will command a spaceship chosen from five categories:
   `0: Fighter, 1: Bomber, 2: Interceptor, 3: Battleship, or 4: Destroyer`.

   You should use the same numbering convention as explained above. Number 0 should represent Fighter, 1 should be Bomber, and so forth.

The game will run for a predetermined number of rounds. In each round, both players will randomly select a spaceship type. The winner of the round will be determined based on the following spaceship interactions:

   - Fighter outmaneuvers Bomber (Fighter wins)
   - Fighter overpowers Interceptor (Fighter wins)
   - Battleship's heavy armaments overpower Fighter (Battleship wins)
   - Destroyer's shields deflect Fighter's attacks (Destroyer wins)
   - Bomber's bombs overwhelm Interceptor (Bomber wins)
   - Bomber's explosives breach Battleship's hull (Bomber wins)
   - Destroyer's armor withstands Bomber's strikes (Destroyer wins)
   - Interceptor's speed outflanks Battleship (Interceptor wins)
   - Destroyer's advanced defense systems outmatch Interceptor (Destroyer wins)
   - Battleship's tactical maneuvers overcome Destroyer (Battleship wins)

<div align="center">
  <img src="/img/01.png" alt="Matrix Operations" />
</div>

## Classes and Methods

Your application should have two packages, namely game and main.
- game package
   - GalacticChallenge Class
   - Player Class
- main package
   - Main Class

# game package

## Player Class:

### Instance Variables:
- `int roundsWon`: Represents the total number of rounds won by the player.
- `String playerName`: The name of the player.
### Methods:
- `public Player(String name)`: Constructor that initializes the player with a given name and sets `roundsWon` to 0.
- `public void wonRound()`: Increments the `roundsWon` instance variable by 1.
- `public int getRoundsWon()`: Getter method for `roundsWon`.
- `public String getName()`: Getter method for `playerName`.

**Hint**: You can use Eclipse's built-in auto-generation feature to create getter and setter methods quickly.

## GalacticChallenge Class

### Instance Variables:
- `Player player1`: Represents the first player.
- `Player player2`: Represents the second player.
- `int numRounds`: Number of rounds to play.
- `static final Random RAND = new Random(2025)`;
  
#### Important Note 1: In this assignment, for generating a random number, we are using the Java Random class. Also, to obtain the same output, a constant seed of 2025 is being utilized, as shown above. 
#### Important Note 2: Wherever you need to generate a random number, you MUST use RAND.nextInt() from the Random class.

### Methods:
- `public GalacticChallenge(String name1, String name2, int numRounds)`: Constructor that initializes the players and the number of rounds.
- `private String getRandomChoice()`: Generates a random spaceship type from "Fighter", "Bomber", "Interceptor", "Battleship", or "Destroyer".
- `private String determineWinner(String choice1, String choice2)`: Determines the winner of a round based on the spaceship interactions described above.
- `public void printWinner()`: Prints the overall winner and the number of rounds each player won at the end of the game.
   - When there is no tie, the application should display: "There is no tie."
   - If the number of ties is more than one, the application should display: "There are X ties."
   - If the number of ties is one, the application should display: "There is 1 tie."
   - In case both players have the same number of won rounds, the application should display: "There is no winner, the game is tied."
- `public void runGame()`: Runs the game for the specified number of rounds. This method should:
   - Randomly generate spaceship choices for each player.
   - Determine the winner of each round using the `determineWinner` method.
   - Update the scores of the players accordingly.

# main package

## Main Class:

The provided Main class is for testing your implemented Java application. It prompts the user to enter the names of the two players. Also, it prompts the user to enter the number of rounds to play. It then creates an instance of the GalacticChallenge class, runs the game, and prints the overall winner and round details.

**Important Note 1**: You are not allowed to change the given main file, unless specified. You just need to add the pledge of honor to it. Any changes beyond that may lead to a grade reduction.

**Important Note 2**: As long as your output includes all the words from the sample output, it is sufficient for us, since the autograder does not consider spaces. However, you need to be careful to match the exact text as given in the sample output. For example:

<table>
  <tr>
    <th>Sample</th>
    <th>Accepted by autograder</th>
    <th>Rejected by autograder</th>
  </tr>
  <tr>
    <td><pre>Today is rainy.
       
Do not forget your umbrella.</pre></td>
    <td><pre>Today is rainy.
       
Do not forget your umbrella.</pre></td>
    <td><pre>Today’**s** rainy.
   
Do**n’t** forget your umbrella.</pre></td>
  </tr>
</table>


### Sample Output
```
Enter the name of player 1: Bob
Enter the name of player 2: John
Enter the number of rounds of the game: 10

Round 1
Bob chose Bomber
John chose Bomber
Result: It's a tie!

Round 2
Bob chose Fighter
John chose Fighter
Result: It's a tie!

Round 3
Bob chose Destroyer
John chose Fighter
Result: Bob wins!

Round 4
Bob chose Fighter
John chose Bomber
Result: Bob wins!

Round 5
Bob chose Bomber
John chose Bomber
Result: It's a tie!

Round 6
Bob chose Interceptor
John chose Bomber
Result: John wins!

Round 7
Bob chose Bomber
John chose Destroyer
Result: John wins!

Round 8
Bob chose Destroyer
John chose Interceptor
Result: Bob wins!

Round 9
Bob chose Fighter
John chose Interceptor
Result: Bob wins!

Round 10
Bob chose Destroyer
John chose Fighter
Result: Bob wins!

Game Over!
Bob won 5 rounds.
John won 2 rounds.
Bob is the overall winner!
There are 3 ties.
```
