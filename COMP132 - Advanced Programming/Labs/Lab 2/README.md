[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/v0QoJC90)
# COMP132, Spring2025, Lab2 PreLab

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
   
   # Space Mission Survival Simulator

   In this prelab, your task is to develop a Space Mission Survival Simulator using the concepts covered in lectures so far. In this simulator program, the astronauts on an intergalactic mission must explore distant planets, gather crucial data, survive alien encounters, and complete their mission. You need to have two packages and the corresponding classes inside them:
   
- spaceMission package includes the following classes:
  - Astronaut class
  - Planet class
  - Alien class
  - Mission class
  - MissionControl class
- exploration package includes the following class:
  - Main class (given)

<div align="center">
  <img src="/img/02.png" alt="Matrix Operations" />
</div>

# Implementation Details

## spaceMission package:

## Astronaut Class

### Instance Variables:
- `String name`: The name of the astronaut.
- `int astronautID`: The unique ID of the astronaut.

### Methods:
- `public Astronaut(String name, int astronautID)`: Constructor to initialize the astronaut with a name and ID.

**--------------------------------------------------------------------------------------------------------------------------------------------------------------**

## Planet Class

### Class Variables:
- `static final int MAX_SAMPLES`: Determines the maximum number of samples that can be collected (should be initialized to 5).

### Instance Variables:
- `String name`: The name of the planet.
- `String[] samples (fixed-size array with the size MAX_SAMPLES)`: An array of samples collected from the planet.
- `int numOfSamples`: Keeps track of the number of samples collected.

### Methods:
- `public Planet(String name)`: Constructor to initialize the planet.
- `public void collectSample(String sample)`: Adds a sample to the samples array. If the array is full, display "Sample collection limit reached for this planet."
- `public void displayPlanetInfo()`: Displays the planet details and collected samples.

**--------------------------------------------------------------------------------------------------------------------------------------------------------------**

## Alien Class

### Class Variable:
- `final static Random RAND`: Used to decide if the alien is `friendly` or `hostile`, randomly. It should generate a random boolean value, which will be used in the `interact()` method.

### Instance Variables:
- `String species`: The name of the alien species.
- `String motive`: The alien’s reason for interacting with the astronauts.

**Note: Use a constant seed of 2025 for the Random class to produce consistent outputs.**

### Methods:
- `public Alien(String species, String motive)`: Constructor to initialize the alien.
- `public static void interact(String question, Alien alien)`: A static method that interacts with the alien using a question. Displays the alien’s response and randomly determines whether they are `friendly` or `hostile` using `RAND.nextBoolean()`.

**--------------------------------------------------------------------------------------------------------------------------------------------------------------**

## Mission Class

### Instance Variables:
- `Planet planet`: The planet being explored in the mission.
- `Alien alien`: An alien encountered on the mission.
- `Astronaut astronaut`: The astronaut responsible for the mission.

### Methods:
- `public Mission(Planet planet)`: Constructor to initialize the mission with a planet.
- `public void displayMissionDetails()`: A method to display the mission details, including the planet, the astronaut, and the alien encounter.

**--------------------------------------------------------------------------------------------------------------------------------------------------------------**

## MissionControl Class

### Instance Variables:
- `Mission[] missions`: A fixed-size array to keep track of `missions`.
- `int currentMissionIndex`: Tracks the current mission index.

### Methods:
- `public MissionControl(int numberOfMissions)`: Constructor to initialize the `currentMissionIndex` to `zero` and set up the `missions` array.
   *Hint*: It is possible to use numberOfMissions when setting up the array. 
- `public void addMission(Mission mission)`: Adds a mission to the simulator. Whenever the missions array gets full, the new mission cannot be added, and the following message should be displayed: "Cannot add more missions. Maximum limit reached."
- `public void startExpedition()`: Starts the exploration process, including sample collection, alien interaction, and mission completion. Uses `displayPlanetInfo()`, `displayMissionDetails()`, and `interact()` methods.

**--------------------------------------------------------------------------------------------------------------------------------------------------------------**

## main package

The provided Main.java class will test the implementation. You should add the **pledge of honor** to it. Any change more than that may lead to grade reduction.


## Sample output
```
Sample collection limit reached for this planet.
Cannot add more missions. Maximum limit reached.

--------------------- New Mission -------------------

Planet Name: Zyphos Prime
Samples: 
- Cryo-Fossil
- Quantum Crystal

Mission Details:
Planet: Zyphos Prime
Astronaut Name: Neil Armstrong 
Alien Species: Zarnok
Astronaut: What were you doing on this planet? 
The Alien Zarnok's response: I was tracking a stolen spaceship.
The Alien Zarnok is hostile.
Mission Expedition Completed.

--------------------- New Mission -------------------

Planet Name: Vortex Nebula
Samples: 
- Warped Relic
- Star Core Fragment

Mission Details:
Planet: Vortex Nebula
Astronaut Name: Ellen Ripley
Alien Species: Vireen
Astronaut: What were you doing on this planet? 
The Alien Vireen's response: I was gathering rare minerals for energy synthesis.
The Alien Vireen is friendly.
Mission Expedition Completed.

--------------------- New Mission -------------------

Planet Name: Eldoria
Samples: 
- Plasma Orb
- Celestial Coral
- Ancient Star Chart
- Gravity Anomaly Detector
- Meteoric Alloy

Mission Details:
Planet: Eldoria
Astronaut Name: Buzz Lightyear
Alien Species: Xylog
Astronaut: What were you doing on this planet? 
The Alien Xylog's response: I am searching for my lost cybernetic arm.
The Alien Xylog is friendly.
Mission Expedition Completed.
```
