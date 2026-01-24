[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hycQCDfP)
# COMP132, Spring2025, Lab 5 PreLab

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

  # Lab 5 Prelab: 
  # KU-TRAM: Type Hierarchy for Transportation Management
In this programming assignment, you are asked to build a Java-type hierarchy aimed to manage different types of Transports in a transportation system (KU-TRAM) using **object-oriented inheritance and polymorphism concepts**.

You are provided with a Java project template, and you should do your development on this template. In the given Java project, a main program code `Main.java` in package `main` is provided to test your code. Note that we may test your code with additional test cases as well.

You should create another package named `transports` that should include all the types described below. Based on the descriptions below, decide whether each type should be an abstract class, a concrete class, a superclass, or a subclass. Also, you must decide on the access modifiers according to the provided descriptions below.

## Directory Structure
```
src  
├── main  
│   └── Main.java  
└── transports  
    ├── Transport.java  
    ├── ElectricTransport.java  
    ├── ElectricCar.java  
    └── Truck.java 
```

## Type Hierarchy:

- `Transport`: Represents a general transport in the transportation system.
- `ElectricTransport`: Represents a kind of Transport with battery management.
- `ElectricCar`: Represents a kind of an ElectricTransport.
- `Truck`: Represents a kind of Transport that is diesel-powered.

<div align="center">
  <img src="/img/02.png" alt="Matrix Operations" />
</div>

# Class Details

## transports package

## Transport Class
### Fields:
- `static ArrayList<Transport> transportList`: An ArrayList of type Transport storing all created transports. (Hint: it should be initialized to an empty ArrayList)
- `String brandAndModel`: Saves the brand and model of the transport.
- `double price`: The price of the transport in USD.
- `double remainingRange`: The remaining travel distance (in km) before needing a recharge/refuel.

### Methods:
`Constructor`: `Transport(String brandAndModel, double price)`: 
  - Initializes `brandAndModel` and `price`.
  - Validates inputs:
  - If `price` `< 0`, set it to `0`.
  - If `brandAndModel` is null or empty, set it to `"Anonymous"`.
  
  (Hint: you can check the string length by calling the `length()` instance method)
  
  - Adds the transport to transportList.
  
- A static method `int getTotalTransports()`: Returns the number of transports in `transportList`.
- A static method `void printAllTransports()`: Iterates over the `transportList` and prints details of all items in the `transportList`.
- An abstract method `void startTrip(double distance)`: Simulates starting a trip (implemented differently in subclasses).
- `toString()`: Returns details about the transport, including brandAndModel, price, remaining range. Take a closer look at the sample output to see the method’s behaviour in more detail.

## ElectricTransport Class

### Additional Fields:
- `double batteryCapacity`: Represents the maximum battery capacity (in kWh).
- `double currentBatteryLevel`: Indicates the current battery level (in kWh).
- `double energyConsumptionRate`: Indicates the rate of the energy consumption per km. (in kWh/km).

### Methods:
- `Constructor`: `ElectricTransport(String brandAndModel, double price, double batteryCapacity, double currentBatteryLevel, double energyConsumptionRate)`
  - Validate Inputs:
    - `batteryCapacity` must be at least `10`. if input is less than `10` then set it to `10`.
    - `currentBatteryLevel` must be between `0` and `batteryCapacity`
    - `energyConsumptionRate` must be `≥ 0.1` (default: 0.1).
    - Computes `remainingRange` as:
      - `remainingRange = currentBatteryLevel / energyConsumptionRate`.
- `toString()`: Overrides parent method to include battery details. It should include the brandAndModel, price, remaining range, batteryCapacity, currentBatteryLevel. Take a closer look at the sample output to see the method’s behaviour in more detail. 

## ElectricCar Class

### Methods:
- `Constructor` : `ElectricCar(String brandAndModel, double price, double batteryCapacity, double currentBatteryLevel, double energyConsumptionRate)`
- `void startTrip(double distance)`: Simulates a trip by reducing battery level. First, check if the available remaining range enables the `ElectricCar` to travel the requested distance. If it does, then this method prints: "ElectricCar [brandAndModel] has traveled a trip for [distance] km, consuming [energyConsumptionRate] kWh/km. Total of [energyConsumptionRate * distance] kWh decrease in battery level.". You should also update the `currentBatteryLevel`, `remainingRange` fields accordingly. 
  - If the remaining range is not sufficient, the method shouldn’t update any field and should print: “`ElectricCar` [brandAndModel] cannot complete [distance] `km` trip. Needs `[energyConsumptionRate * distance]` `kWh`, but only [`currentBatteryLevel`] `kWh` left.”

#### Important note: in case the input is less than zero, the method shouldn’t update any field and print the following statement: “Invalid distance. Trip canceled.”

## Truck Class

### Additional Fields
- `double fuelCapacity`: Maximum fuel capacity (in liters).
- `double currentFuelLevel`: Current fuel level (in liters).
- `double fuelConsumptionRate`: Fuel consumed per km (in liters/km).
- `static ArrayList<Truck> truckList`: Stores all trucks. (Hint: it should be initialized to an empty ArrayList)
- `Set<String> cargoSet`: A HashSet used to store unique cargo items.

### Methods

- `Constructor`: `Truck(String brandAndModel, double price, double fuelCapacity, double currentFuelLevel, double fuelConsumptionRate)`
  - Validates inputs:
  - `fuelCapacity` must be `≥ 20` (default: 20, meaning that if input is less than 20, then set it to 20).
  - `currentFuelLevel` must be between 0 and `fuelCapacity`. (meaning that if input is more than `fuelCapacity`, then set it to `fuelCapacity`. And if it is less than zero, then set it to 0.)
  - `fuelConsumptionRate` must be `≥ 0.5` (default: 0.5, meaning that if the input is less than 0.5, then set it to 0.5).
  - Computes `remainingRange` as:
  - `remainingRange = currentFuelLevel / fuelConsumptionRate`.
  - Initialize cargoSet as an empty set.
  - Adds truck to `truckList`.
  
- `static int getTotalTrucks()`: Returns the number of trucks (size of `truckList`).
- `static void startAllTrucks(double distance)`: Attempts to start all trucks in `truckList`. Loops through the `truckList` and starts the trip for each of them. 
- `void startTrip(double distance)`:
  - If fuel is sufficient, reduce fuel level and prints “Truck [brandAndModel] has traveled a trip for [distance] `km`, consuming [fuelConsumptionRate] `L/km`. Total of [fuelConsumptionRate * distance] `L` decrease in fuel level.”
  - In case the fuel is not sufficient, the method should print “Truck [brandAndModel] cannot complete [distance] `km` trip. Needs [fuelConsumptionRate * distance]  `L`, but only [currentFuelLevel] `L` left.".
  - If the input value is less than zero, it prints “Invalid distance. Trip canceled.”
  
- void addCargo(String cargoItem):
  - Adds a new cargo item to `cargoSet`. If the item is already in the set, it should notify the user. “Cargo item already exists: [cargoItem]”
  - Otherwise, it adds the item and prints a success message.currentPassengers field and print “Added cargo item: [cargoItem]”
	
- `void removeCargo(String cargoItem)`
  - Removes a cargo item from the set. If the item doesn't exist, print a warning message.
    - “Removed cargo item: [cargoItem]”
    - Warning message: “Cargo item not found: [cargoItem]”

- `void listCargo()`
  - This method prints the contents of the cargoSet. Output should be like this:
  - “Cargo items for [brandAndModel]: [cargoSet contents]”

- toString(): Overrides to display truck-specific details. Returns a string displaying the Truck’s details: `brandAndModel, price, fuelCapacity, currentFuelLevel`

## main package

## Main
The provided Main.java class is for testing your implemented Java application. This class is a driver class to demonstrate and test the functionalities of your implemented application. You are not allowed to change the given file. You are only allowed to add the pledge of honor to it. Any other changes may lead to grade reduction.

## Sample output
```
===== Creating Electric Cars =====
Transport of Brand: Tesla Model 3, price: $40000.0, Battery: 50.0%, Remaining range: 333.33 km, Max Capacity: 75.0%
Transport of Brand: Anonymous, price: $0.0, Battery: 0.0%, Remaining range: 0.00 km, Max Capacity: 10.0%

===== Starting Trips with Electric Cars =====
ElectricCar Tesla Model 3 has traveled a trip for 100.0 km, consuming 0.2 kWh/km. Total of 15.0 kWh decrease in battery level.
Invalid distance. Trip canceled.
ElectricCar Anonymous cannot complete 10.0 km trip. Needs 1.0 kWh, but only 0.0 kWh left.

===== Creating Trucks =====
Transport of Brand: Volvo FH, price: $80000.0, Fuel: 200.0 L, Range: 333.33 km
Transport of Brand: Anonymous, price: $0.0, Fuel: 0.0 L, Range: 0.00 km

===== Starting Trips with Trucks =====
truck Volvo FH has traveled a trip for 50.0 km, consuming 0.6 L/km. Total of 30.0 L decrease in fuel level.
truck Volvo FH cannot complete 1000.0 km trip. Needs 600.0 L, but only 170.0 L left.
Invalid distance. Trip canceled.

===== Managing Cargo on Trucks =====
Added cargo item: CargoA
Added cargo item: CargoB
Cargo item already exists: CargoA
Cargo items for Volvo FH: [CargoA, CargoB]
Removed cargo item: CargoB
Cargo item not found: CargoC
Cargo items for Volvo FH: [CargoA]

===== Static Info Check =====
Total transports created: 4
Total trucks created: 2

All transports:
List of all transports:
Transport of Brand: Tesla Model 3, price: $40000.0, Battery: 35.0%, Remaining range: 233.33 km, Max Capacity: 75.0%
Transport of Brand: Anonymous, price: $0.0, Battery: 0.0%, Remaining range: 0.00 km, Max Capacity: 10.0%
Transport of Brand: Volvo FH, price: $80000.0, Fuel: 170.0 L, Range: 283.33 km
Transport of Brand: Anonymous, price: $0.0, Fuel: 0.0 L, Range: 0.00 km

===== Start All Trucks =====
truck Volvo FH has traveled a trip for 30.0 km, consuming 0.6 L/km. Total of 18.0 L decrease in fuel level.
truck Anonymous cannot complete 30.0 km trip. Needs 15.0 L, but only 0.0 L left.
```
