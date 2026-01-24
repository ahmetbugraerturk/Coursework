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
package test;

import spacetrade.*;
import java.util.*;

public class Test {
    public static void main(String[] args) {
        // Initialize resources
        Resource[] resources = {
                new Resource("PlasmaRods", "High-energy rods used for space cannons", "Weapon", 20),
                new Resource("QuantumFuel", "Super-efficient fuel for deep space travel", "Fuel", 100),
                new Resource("PhotonCrystals", "Crystals that amplify energy beams", "Mineral", 50),
                new Resource("SolarCore", "Compressed solar matter for reactors", "Energy", 35)
        };
        // Create galactic network
        GalacticNetwork network = new GalacticNetwork(resources);
        // Initialize freighters with initial resources
        Map<String, Resource> initResources1 = new HashMap<>();
        initResources1.put("PlasmaRods", resources[0]);
        initResources1.put("PhotonCrystals", resources[2]);
        initResources1.put("SolarCore", resources[3]);
        Freighter freighter1 = new Freighter("Falcon9", initResources1);
        Map<String, Resource> initResources2 = new HashMap<>();
        initResources2.put("QuantumFuel", resources[1]);
        Freighter freighter2 = new Freighter("Andromeda", initResources2);
        Freighter freighter3 = new Freighter("Voyager", new HashMap<>());
        // Register freighters to the network
        freighter1.joinNetwork(network);
        freighter2.joinNetwork(network);
        // Request resource tests (covering all outcomes)
        freighter1.requestResource("QuantumFuel"); // Success
        freighter1.requestResource("SolarCore"); // Already has
        freighter2.requestResource("PhotonCrystals"); // Success
        freighter2.requestResource("QuantumFuel"); // Already has
        freighter3.requestResource("PhotonCrystals"); // Not joined
        freighter1.requestResource("DarkMatter"); // Not registered
        // Display freighter 1 information
        System.out.println("\nFreighter 1 Info:");
        System.out.println(freighter1);
        System.out.println("Owned Resources:");
        for (Resource r : freighter1.getResources().values()) {
            System.out.println(r + "\n");
        }
        // Display freighter 2 information
        System.out.println("Freighter 2 Info:");
        System.out.println(freighter2);
        System.out.println("Owned Resources:");
        for (Resource r : freighter2.getResources().values()) {
            System.out.println(r + "\n");
        }
        // Lookup tests
        System.out.println("\n------------- Freighters With Specified Resource ------------\n");
        network.printFreightersWithResource("PlasmaRods");
        network.printFreightersWithResource("PhotonCrystals");
        network.printFreightersWithResource("DarkMatter");
        // Additional: receiveResource method test cases
        System.out.println("\n=== receiveResource Test Cases ===\n");
        Freighter testFreighter = new Freighter("TestShip", new HashMap<>());
        // Case: Not joined the network
        testFreighter.receiveResource(resources[0]);
        // Case: Joined network and receives new resource
        testFreighter.joinNetwork(network);
        testFreighter.receiveResource(resources[1]);
        // Case: Already owns resource
        testFreighter.receiveResource(resources[1]);
        
        
        System.out.println("\n************************* INLAB *************************\n");


        // Freighter 3 receives all of Freighter 1's resources
        freighter3.joinNetwork(network);
        for (Resource resource : freighter1.getResources().values()) {
            freighter3.receiveResource(resource);
        }


        // Create Freighter 4 with overlapping and non-overlapping resources
        Map<String, Resource> initResources4 = new HashMap<>();
        initResources4.put("PhotonCrystals", resources[2]); // Common resource with others
        initResources4.put("SolarCore", resources[3]); // Common resource with freighter1 & 3
        Freighter freighter4 = new Freighter("StarRunner", initResources4);
        freighter4.joinNetwork(network);


        System.out.println("\n******************************\n");
        // Display all resources
        System.out.println("Resources:");
        for (Resource resource : resources) {
            System.out.println(resource.getName());
        }
        System.out.println("\n******************************\n");


        // Compare test between freighter1 and freighter3
        System.out.println("Compare Freighters:");
        System.out.println("Freighter 1 ID < Freighter 3 ID: " + (freighter1.compareTo(freighter3) == -1));
        System.out.println("Freighter 1 ID > Freighter 3 ID: " + (freighter1.compareTo(freighter3) == 1));
        System.out.println("Freighter 1 ID == Freighter 3 ID: " + (freighter1.compareTo(freighter3) == 0));


        System.out.println("\n******************************\n");
        // Sort freighters
        System.out.println("Sort Freighters:");
        network.sortFreighters();
        System.out.print(network.showFreighters());
        System.out.println("\n******************************\n");


        // Reverse sort freighters
        System.out.println("Reverse Sort Freighters:");
        network.sortFreightersReverse();
        System.out.print(network.showFreighters());
        System.out.println("\n******************************\n");


        // Common resources
        System.out.println("Common Resources:");
        int outer = 1;
        for (Map.Entry<Freighter, Map<Freighter, List<Resource>>> entry : network.findCommonResources().entrySet()) {
            System.out.println("[" + outer++ + "] " + entry.getKey().getName() + " matches:");
            for (Map.Entry<Freighter, List<Resource>> subentry : entry.getValue().entrySet()) {
                System.out.print("With " + subentry.getKey().getName() + ": ");
                List<String> names = new ArrayList<>();
                for (Resource r : subentry.getValue()) {
                    names.add(r.getName());
                }
                System.out.println(String.join(", ", names));
            }
        }


    }
}
