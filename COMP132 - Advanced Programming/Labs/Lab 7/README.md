[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/3u1Qu5v1)
# COMP132, Spring2025, Lab 7 PreLab

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

  # Lab 7 Prelab: PeerWatt Sariyer: A P2P Energy Trading Simulator for Sarıyer District

  In this programming lab, you will primarily practice **Exception Handling** and **File Processing** concepts by implementing an application simulating **PeerWatt Sariyer** - A P2P Energy Trading Simulator for Sarıyer District.

Your mission is to implement a **peer-to-peer (P2P) energy trading system** where peers can trade their excess energy based on availability, location, and bid price. You will use **object-oriented programming (OOP) principles, handle exception cases**, and implement a simple peer-matching approach.

**What is the PeerWatt Sariyer?**

A group of smart homes in the Sarıyer district of Istanbul generate and store electricity using solar panels. Some homes have excess energy, while others need more energy. Peers trade energy among themselves based on their bid price and geographical proximity.

<div align="center">
  <img src="/img/01.png" alt="PeerWatt Sariyer" />
</div>

You are provided with the `Main.java` file and an input text file (`peers.txt`). Check the main file to understand the sample output better and how each method and field is used. It shows how everything works together and will make the assignment easier to understand. 

# Note: 

- Constructors generally do not have `try/catch` statements. Instead, they should `throw exceptions` when validation fails.
- Validators in this project (`LocationValidator`, `PeerValidator`, and `TransactionValidator`) are responsible for ensuring that an entity (e.g., peer ID, coordinates) conforms to the expected formats and constraints. Validators **MUST NOT** use `try-catch` inside them. Instead, they should `throw exceptions` when validation fails.
- When an exception is caught, print its message using `System.err`.

## You need to develop your assignment by following the instructions below. 

## Package Structure:
```
peers.txt
src/
  location/
    Location.java
    LocationValidator.java
  peer/
    Peer.java
    PeerValidator.java
  transaction/
    Transaction.java
    TransactionValidator.java
  exception/
    InvalidPeerException.java
    InvalidTransactionException.java
    InvalidLocationException.java
    InvalidParameterException.java
  peerwatt_sariyer/
    PeerWattSariyer.java
  main/
    InputHandler.java
    Main.java
```

## Location Class

Represents a location in the energy trading system.

### Fields:
- `double latitude`: Location’s latitude.
- `double longitude`: Location’s longitude. 

### Methods:
- A public constructor with the signature `Location(double latitude, double longitude)`: The constructor uses `LocationValidator.validateLatitudeLongitude(double latitude, double longitude)` to validate the location and throws the corresponding exception, if any.
- Public getters for latitude and longitude.
- public double `distanceTo(Location location)`, which measures the distance to the provided location using the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula). You can use the provided `haversine` method to calculate the approximate distance in KM.

In your Location.java, put the following method: 
```
double haversine(double lat1, double lon1,double lat2, double lon2)
{
        // distance between latitudes and longitudes
        double dLat = Math.toRadians(lat2 - lat1);
        double dLon = Math.toRadians(lon2 - lon1);
 
        // convert to radians
        lat1 = Math.toRadians(lat1);
        lat2 = Math.toRadians(lat2);
 
        // apply formulae
        double a = Math.pow(Math.sin(dLat / 2), 2) +
                   Math.pow(Math.sin(dLon / 2), 2) *
                   Math.cos(lat1) *
                   Math.cos(lat2);
        double rad = 6371;
        double c = 2 * Math.asin(Math.sqrt(a));
        return rad * c;
}
```



## LocationValidator Class

### Methods:
- `public static void validateLatitudeLongitude(double latitude, double longitude)`: Ensures that latitude is between -90 and 90 and longitude is between -180 and 180, otherwise throws `InvalidLocationException`, with proper message: “Invalid latitude or longitude.”.
- `public static void validate(Location location)`:
   - If the location is null, it throws `InvalidLocationException`, with a proper message: “Location cannot be null.”.
   - Validates the location’s latitude and longitude using `validateLatitudeLongitude(double latitude, double longitude)` and throws an exception, if any.

## Peer Class

Represents a participant in the energy trading system.

### Fields:
- `String peerID`:  A unique identifier with length of 6.
- `double balance`: Peer’s balance in Turkish Lira.
- `double generatedEnergy`: Energy produced by the peer in kWh.
- `double neededEnergy`: Energy required by the peer in kWh.
- `double excessEnergy`: The peer’s generated minus needed energy.
- `Location location`: The peer’s location.
- `private static List<String> peersIDs`, which represents a list of previously created peers.

### Methods:
- A constructor with the signature `Peer(String peerID, double balance, double generatedEnergy, double neededEnergy, Location location)`. 
   - The constructor validates the `peerID` using the `peerValidator`, where if the `peerID` is invalid, it throws an `InvalidPeerException`.
   - If the `peerID` exists in the `peersIDs` list, then `InvalidPeerException` will be thrown, with a message: “Peer ID already exists.”.  
   - If the `location` is null, it throws an `InvalidPeerException` with “Location cannot be null.” as a message.
   - If any of the other parameters is negative, an `InvalidParameterException` will be thrown. A proper message will be sent to the exception, such as “Balance cannot be negative.”.
- `balance`, `generatedEnergy`, and `neededEnergy` will have public `setters`. Those setters will check if the given value is negative, and  an `InvalidParameterException` will be thrown with a suitable message, like "Generated energy cannot be negative". 
- `Public getters` for `peerId`, `balance`, and `location`.
- A `setter` for excess energy, that calculates and sets the excess energy as generated energy minus the needed energy. This setter can be used in other methods in the same class to update the excess energy, when needed.
- Getter for excess energy. 
- `public void buyEnergy(double amount, double price)`: Throws an `InvalidParameterException` if the amount or price is less than or equals zero, or if the (`price x amount`) is greater than the balance. If not, it updates the needed energy, excess energy and balances accordingly. The message will be: “Amount and price must be non-negative.” if at least one of the parameters is negative, and “Not enough balance.” if the balance is not enough.
- `public void sellEnergy(double amount, double price)`:  Throws an `InvalidParameterException` if the amount or price is negative with message “Amount and price must be non-negative.”, or if the amount is greater than the excess energy, with message “Not enough excess energy.”. If not, it updates the generated energy, excess energy, and balances accordingly. 


## PeerValidator Class

### Methods:

- `public static void validatePeerID(String peerID)`: Validates that the peer ID length is 6. If invalid, it throws an `InvalidPeerException`, with the message: “Peer is invalid because the ID length must be 6."
- `public static void validate(Peer peer)`:
   - If the peer is null, throw `InvalidPeerException`, with a proper message: “Peer is null”
   - Validates the peer’s ID using `validatePeerID(String peerID)`.

## Transaction Class

Represents an energy trade between two peers.

### Fields:
- Peer senderPeer: The providing energy peer.
- Peer receiverPeer: The receiving energy peer.
- double energyAmount: Amount of energy exchanged in kWh.
- double price: The price of transacted energy per kWh.

### Methods:
- A constructor with the signature `public Transaction(Peer senderPeer, Peer receiverPeer, double energyAmount, double price)`
   - Validates `energyAmount`, and `price`. Throws `InvalidTransactionException` if invalid with message: “Transaction is invalid because of non-positive energy or price”.
   - Uses `TransactionValidator` to validate that both peers' locations are within the Sariyer district.
- `Transaction class` has no setters, where each created transaction is immutable.

## TransactionValidator Class

### Methods:
- A static method with the signature `validateLocations(Location sender, Location receiver)`:
   - The method will throw an invalid parameter exception if any of the locations is null, with message: “Sender location and receiver location cannot be null”.
   - This method will validate that both locations are in Sariyer. This is handled by assuming that all peers in Sariyer are within 10 KM of Sariyer’s center. You will use the `distanceTo` method from the `Location class` to measure the distance to Sariyer’s center (41.1623° N, 29.0474° E). The method will throw `InvalidTransactionException` with a message as follows:
      - If both locations are not within 10 KM of Sariyer’s center: “Transaction aborted: both sender and receiver are out of range. Sender location: (latitude, longitude), Receiver location: (latitude, longitude)”
      - If sender is not within 10 KM of Sariyer’s center: “Transaction aborted: sender is out of range. Sender location: (latitude, longitude)”
      - If receiver is not within 10 KM of Sariyer’s center: “Transaction aborted: receiver is out of range. Receiver location: (latitude, longitude)”

## Custom Exception Classes

- `InvalidPeerException`: Thrown for invalid peer attributes. 
- `InvalidTransactionException`: Thrown for invalid energy transactions.
- `InvalidLocationException`: Thrown when peers are too far apart.
- `InvalidParameterException`: Thrown when a parameter is invalid. It takes an error message and prints "Invalid parameter: " + error message which states why this exception was thrown. 
   - Example: "Invalid parameter: Balance cannot be negative."

## PeerWattSariyer Class

This class manages the PeerWatt Sariyer system, including the peers, and transactions.

### Fields:
- `double totalP2PTransactedEnergy`: Tracks the total amount of transacted energy between the peers.
- `HashMap<String, Peer> peers`: Map of peers in the system.
- `ArrayList<Transaction> transactions`: List of transactions in the system.

### Methods:
- A constructor with the signature `public PeerWattSariyer(HashMap<String, Peer> peers)`
   - Initializes the `PeerWattSariyer` with the given peers. If the peers' parameter is null, then it will create a new `hashmap` for the peers.
   - Creates empty data structures for transactions.
- `public void addPeer (Peer peer)`
   - Validates the peer using `PeerValidator.validate(Peer peer)`.
   - Adds the peer to the peers' map.
- `private List<Peer> getSellers()`, returns a list of seller peers, where a peer is a seller if his excess energy is greater than zero.
- `private List<Peer> getBuyers()`, returns a list of buyer peers, where a peer is a buyer if his excess energy is less than zero.
- `public void trade(double price)`: Matches between buyers and sellers. 
   - For each pair, it defines the amount of energy to trade as the minimum value between the offered and requested energy (`excessEnergy`). Pay attention that `excessEnergy` will be a negative value in the buyer object,thus you need to get its absolute value.
   - If the buyer can afford the energy:
      - If both seller and buyer are within the Sariyer district (using `TransactionValidator.validateLocations`):
         - Call the peer’s `sellEnergy` and `buyEnergy` in an appropriate manner.
         - Create a transaction with correct values.
   - The method updates and prints the total amount of transacted energy (`totalP2PTransactedEnergy`). Check sample output for the exact needed format.
- `printAllTransactions with signature public void printAllTransactions()`: Prints a detailed list of all transactions created in the system. For each transactions, it displays:
   - Receiver peer ID
   - Sender peer ID
   - Amount of energy traded (kWh)
   - Price per kWh
   - The transaction price

## InputHandler Class

This class handles the file processing procedure using a method with the signature `public static void processInputFile(PeerWattSariyer peerWattSariyer, String filePath)`. This method should do the following tasks and handle possible exceptions.
- It MUST use the Scanner class to read the file.
- Check the format of each line, which must include 6 space-separated information items. If a line contains less than 6 values, then an “Invalid file entry” message will be printed.
   - Peer ID.
   - Peer balance.
   - Peer generated energy.
   - Peer needed energy
   - Peer latitude.
   - Peer longitude.
- Creates a `Location` and `Peer` object from each valid line and adds the peer to the PeerWattSariyer system using the `addPeer` method. Remember that the Peer constructor already validates the peer, and addPeer also includes validation for the peer and its location. Hence, you do not need to code the validation code again, where you will have to include your code in a try-catch block. In your catch, print the caught exception message.

## Given Input Text File: peers.txt
```
A1B2C3 1000 50 20 41.1630 29.0475
D4E5F6 500 10 30 41.2049 29.0725
G7H8I9 800 60 60 41.1943 -290.0488
A1B2C3 1000 50 20 41.1630
ZZZZZZ -100 50 10 41.1600 29.0500
ABCDE 200 10 5 41.1600 29.0500
A1B2C3 500 20 10 41.1621 29.0472
X1Y2Z3 900 60 200 40.0000 28.0000
X1Y2Z4 60 760 20 28.0000 40.0000
M1N2O3 600 80 40 41.2473 29.0474
TRADE1 700 100 20 41.1610 29.0480
TRADE2 400 10 60 41.1628 29.0488
TRADE3 600 90 40 41.1600 29.0465
TRADE4 300 10 50 41.1629 29.0463
```

## Sample Output

```
Reading data...
Peer A1B2C3 added successfully
Peer D4E5F6 added successfully
Invalid latitude or longitude.
Invalid file entry
Invalid parameter: Balance cannot be negative.
Peer is invalid because the ID length must be 6.
Peer ID already exists.
Peer X1Y2Z3 added successfully
Peer X1Y2Z4 added successfully
Peer M1N2O3 added successfully
Peer TRADE1 added successfully
Peer TRADE2 added successfully
Peer TRADE3 added successfully
Peer TRADE4 added successfully
===================================
Started trading...
Transaction aborted: receiver is out of range. Receiver location: (40.0, 28.0)
Transaction aborted: receiver is out of range. Receiver location: (40.0, 28.0)
Transaction aborted: both sender and receiver are out of range. Sender location: (28.0, 40.0), Receiver location: (40.0, 28.0)
Transaction aborted: receiver is out of range. Receiver location: (40.0, 28.0)
Trading ended. Total transacted energy amount is 110.0 kWh
===================================
Printing transactions...
Receiver ID: D4E5F6
Sender ID: TRADE1
Energy Traded: 20.0 kWh
Price per kWh: 1.5
Total: 30.0
-------------------------------------------
Receiver ID: TRADE2
Sender ID: TRADE1
Energy Traded: 50.0 kWh
Price per kWh: 1.5
Total: 75.0
-------------------------------------------
Receiver ID: TRADE4
Sender ID: TRADE1
Energy Traded: 10.0 kWh
Price per kWh: 1.5
Total: 15.0
-------------------------------------------
Receiver ID: TRADE4
Sender ID: TRADE3
Energy Traded: 30.0 kWh
Price per kWh: 1.5
Total: 45.0
-------------------------------------------
```


