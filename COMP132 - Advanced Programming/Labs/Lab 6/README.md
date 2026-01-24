[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/gzKJ2895)
# COMP132, Spring2025, Lab 6 PreLab

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

  # Lab 6 Prelab: Galactic Trade Network

In this lab, your mission is to simulate a decentralized galactic trade network using **Java Collections**. You are asked to design and implement classes representing space freighters, trade resources, and the galactic network they operate in. The goal is to practice using Collections data structures while managing interactions between space freighters who exchange resources without relying on a central command center. Each freighter stores a unique set of resources and can request or offer these resources to others across the network.

## Package Structure:

- spacetrade: Includes all core classes and interfaces.
- test: Includes the provided Test.java, which will be used to verify your implementation.
  
```
src
├── spacetrade
│   ├── GalacticNetwork.java
│   ├── Resource.java
│   └── Freighter.java
└── test
    └── Test.java
```

<div align="center">
  <img src="/img/01.png" alt="Matrix Operations" />
</div>

# Class Details


## GalacticNetwork Class

Represents the central interface for all freighters in the decentralized trade network. 

### Fields:
- `List<Freighter> freighters`: All freighters in the galaxy.
- `Map<String, Resource> resources`: Maps resource names to their corresponding Resource objects.

### Methods:

- Constructor: `GalacticNetwork(Resource[] resources)`: Initializes the network with available resources and an empty list of freighters.
- `boolean resourceExists(String name)`: Checks if the resource exists.
- `Resource getResourceInfo(String name)`: Returns the Resource object if it exists. Otherwise, it returns null.
- `void registerFreighter(Freighter freighter)`: Adds the freighter and updates resource ownership.
- `private void updateFreighterResources(Freighter freighter)`: This helper method updates the ownership records of resources when a freighter is registered in the galactic network.
  - Iterates over all resources currently owned by the given freighter.
  - For each Resource in the freighter’s inventory, it updates the `locations` set of the Resource object by calling `addLocation`.
  - This ensures that the resource object is aware of all freighters that currently have it.
- `List<Freighter> getFreightersWithResource(String resourceName)`: Returns a list of freighters having the resource.
- `void printFreightersWithResource(String resourceName)`: Prints a list of freighters owning the specified resource.
  - If no freighter has this resource, print “No freighters currently have this resource.”

## Resource Class

Represents a tradable galactic resource.

### Fields:
- `String name`: Resource Name (e.g., Oxygen, Titanium).
- `String description`: Brief explanation.
- `String type`: Type (e.g., element, equipment).
- `int quantity`: The available quantity
- `Set<Freighter> locations`: Freighters that own this resource.

### Methods:

- Constructor:`Resource(String name, String description, String type, int quantity)`: Initializes the resource with the given details.
- `void addLocation(Freighter freighter)`: Adds a freighter to the locations set.
- `boolean availableAt(Freighter freighter)`: Checks if a freighter has this resource.
- `String toString()`: Returns formatted resource information as follows:
  - `Resource Name=<name>`
  - `Description=<description>`
  - `Type=<type>`
  - `Quantity=<quantity>`


## Freighter Class

Represents a spaceship participating in galactic trade.

### Fields:
- `static int totalFreighters`: Tracks the total number of freighters.
- `int id`: Unique freighter ID.
- `String name`: Name of the freighter.
- `Map<String, Resource> resources`: Resources this freighter owns.
- `boolean status`: Status (true = active).
- `GalacticNetwork network`: Reference to the network this freighter is in.

### Methods:

- Constructor: `Freighter(String name, Map<String, Resource> initialResources)`: Initializes a Freighter with name, sets online, increments totalFreighters, and assigns ID.
- `void joinNetwork(GalacticNetwork network)`: Registers freighter into the network.
- `boolean hasResource(Resource resource)`: Checks if the resource is present.
- `void receiveResource(Resource resource)`: Assigns ownership of a resource to this freighter only if:
   - The freighter has already joined the network.
     - If the freighter has not joined the network, it prints:  
       `Freighter <FreighterName> has not joined the galactic network. Cannot receive resource.`
          - In this print statement, you must change <FreighterName> with the referred FreighterName, for example: “Freighter TestShip has not joined the galactic network. Cannot receive resource.”
   - The resource is not already owned by this freighter.
     - If the freighter already owns the resource, it prints:  
       `Resource <ResourceName> already owned by <FreighterName>. Cannot receive again.`
   - If both conditions have been met:
     - Adds the resource to this freighter’s resources map.
     - Adds the freighter to the resource’s locations set.
     - Then, prints:  
       `Resource <ResourceName> received by <FreighterName>.`
- `boolean requestResource(String name)`: This method allows the freighter to request a resource from the network.
  - If the freighter has not yet joined a `GalacticNetwork`:
    - Print: "`<FreighterName>` has not joined the galactic network. Resource request aborted."
    - Return false.
  - If the requested resource does not exist in the network:
    - Print: "`<ResourceName>` is not registered in the galactic trade system."
    - Return false.
  - If the freighter already has the resource:
    - Print: "`<FreighterName>` already has `<ResourceName>`. Request skipped."
    - Return false.
  - Otherwise:
    - Add the resource to the freighters map with receiveResource method.
    - Print: "`Resource <ResourceName>` successfully acquired by `<FreighterName>`."
    - Return true.
- `String toString()`: Returns formatted freighter information as follows:
  - `Freighter ID: <id>`
  - `Name: <name>`
  - `Status: Online or Offline`

## Sample output
```
Resource QuantumFuel received by Falcon9.
Resource QuantumFuel successfully acquired by Falcon9.
Falcon9 already has SolarCore. Request skipped.
Resource PhotonCrystals received by Andromeda.
Resource PhotonCrystals successfully acquired by Andromeda.
Andromeda already has QuantumFuel. Request skipped.
Voyager has not joined the galactic network. Resource request aborted.
Falcon9 is not registered in the galactic trade system.

Freighter 1 Info:
Freighter ID: 1
Name: Falcon9
Status: Online
Owned Resources:
Resource Name=PlasmaRods
Description=High-energy rods used for space cannons
Type=Weapon
Quantity=20

Resource Name=SolarCore
Description=Compressed solar matter for reactors
Type=Energy
Quantity=35

Resource Name=PhotonCrystals
Description=Crystals that amplify energy beams
Type=Mineral
Quantity=50

Resource Name=QuantumFuel
Description=Super-efficient fuel for deep space travel
Type=Fuel
Quantity=100

Freighter 2 Info:
Freighter ID: 2
Name: Andromeda
Status: Online
Owned Resources:
Resource Name=PhotonCrystals
Description=Crystals that amplify energy beams
Type=Mineral
Quantity=50

Resource Name=QuantumFuel
Description=Super-efficient fuel for deep space travel
Type=Fuel
Quantity=100


------------- Freighters With Specified Resource ------------

Resource lookup: PlasmaRods
Freighter ID: 1
Name: Falcon9
Status: Online

Resource lookup: PhotonCrystals
Freighter ID: 1
Name: Falcon9
Status: Online

Freighter ID: 2
Name: Andromeda
Status: Online

Resource lookup: DarkMatter
No freighters currently have this resource.

=== receiveResource Test Cases ===

Freighter TestShip has not joined the galactic network. Cannot receive resource.
Resource QuantumFuel received by TestShip.
Resource QuantumFuel already owned by TestShip. Cannot receive again.
```

