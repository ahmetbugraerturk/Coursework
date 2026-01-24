/* *********** Pledge of Honor ************************************************ *

I hereby certify that I have completed this lab assignment on my own
without any help from anyone else. I understand that the only sources of authorized
information in this lab assignment are (1) the course textbook, (2) the
materials posted on the course website, and (3) any study notes handwritten by myself.
I have not used, accessed, or received any information from any other unauthorized
source in taking this lab assignment. The effort in the assignment thus belongs
completely to me.
READ AND SIGN BY WRITING YOUR NAME SURNAME, AND STUDENT ID
SIGNATURE: <Ahmet Buğra Ertürk, 86877>
********************************************************************************/
package main;

import transports.*;

public class Main {

    public static void main(String[] args) {
        System.out.println("===== Creating Electric Cars =====");
        ElectricCar car1 = new ElectricCar("Tesla Model 3", 40000, 75, 50, 0.15);
        ElectricCar car2 = new ElectricCar("", -1000, 5, -10, 0.05); // Will trigger validation
        System.out.println(car1);
        System.out.println(car2);

        System.out.println("\n===== Starting Trips with Electric Cars =====");
        car1.startTrip(100);
        car1.startTrip(-5); // Invalid trip
        car2.startTrip(10); // Should fail due to low battery

        System.out.println("\n===== Creating Trucks =====");
        Truck truck1 = new Truck("Volvo FH", 80000, 300, 200, 0.6);
        Truck truck2 = new Truck(null, -5000, 10, -10, 0.2); // Will trigger validation
        System.out.println(truck1);
        System.out.println(truck2);

        System.out.println("\n===== Starting Trips with Trucks =====");
        truck1.startTrip(50); // Valid trip
        truck1.startTrip(1000); // Not enough fuel
        truck2.startTrip(-20); // Invalid trip

        System.out.println("\n===== Managing Cargo on Trucks =====");
        truck1.addCargo("CargoA");
        truck1.addCargo("CargoB");
        truck1.addCargo("CargoA"); // Duplicate
        truck1.listCargo();
        truck1.removeCargo("CargoB");
        truck1.removeCargo("CargoC"); // Not found
        truck1.listCargo();

        System.out.println("\n===== Static Info Check =====");
        System.out.println("Total transports created: " + Transport.getTotalTransports());
        System.out.println("Total trucks created: " + Truck.getTotalTrucks());
        System.out.println("\nAll transports:");
        Transport.printAllTransports();

        System.out.println("\n===== Start All Trucks =====");
        Truck.startAllTrucks(30);
        
        System.out.println("\n......................................InLab......................................\n");
        System.out.println("\n===== Creating Hybrid Car =====");
        HybridCar hybrid1 = new HybridCar("Toyota Prius", 30000, 40, 20, 0.2, 40, 30, 1.0);
        HybridCar hybrid2 = new HybridCar("FaultyHybrid", -20000, 10, -5, 0.1, 10, -10, 0.2); // Triggers validation
        System.out.println(hybrid1);
        System.out.println(hybrid2);
        System.out.println("\n===== Starting Trips with Hybrid Cars =====");
        hybrid1.startTrip(100); // Enough with both energy sources
        hybrid1.startTrip(500); // Should fail
        hybrid2.startTrip(-10); // Invalid
        System.out.println("\n===== Recharging and Refueling Hybrid Car =====");
        hybrid1.recharge();
        hybrid1.refuel();
        hybrid1.recharge(); // Should print already full
        hybrid1.refuel(); // Should print already full
        System.out.println("\n===== Recharging Electric Car =====");
        car1.recharge(); // Should partially recharge or max out
        car2.recharge(); // Should trigger max or small top-up
        System.out.println("\n===== Refueling Trucks =====");
        truck1.refuel(); // Partial or full
        truck2.refuel(); // Depending on initial level
        System.out.println("\n===== Transport Statistics =====");
        Transport.printTransportStatistics();
    }
}
