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

import alienNetGUI.AlienNetGUI;
import alien.*;
import aliennet.AlienNet;

public class Main {
    public static void main(String[] args) {
        AlienNet net = new AlienNet();

        Alien a1 = net.addAlien("Zorg", "Common");
        Alien a2 = net.addAlien("Xarn", "Elite");
        Alien a3 = net.addAlien("Blip", "Common");
        Alien a4 = net.addAlien("N'Kora", "Elite");
        Alien a5 = net.addAlien("Elthor", "Elite");
        Alien a6 = net.addAlien("Zylara", "Royal");
        Alien a7 = net.addAlien("Astralyn", "Royal");
        
        ((RoyalAlien) a7).setTitle("Queen");

        a1.sendTransmission("Found an energy source on Asteroid 44-Z.");
        a1.sendTransmission("I need to report this to the Council.");

        a2.sendTransmission("My fleet is heading toward the Kuiper Belt.");
        a2.sendTransmission("Meeting with Queen Vela was successful.");

        a3.sendTransmission("I discovered a new fungus on Mars.");

        a4.sendTransmission("These humans are fascinating.");
        a4.sendTransmission("I’m monitoring their broadcasts.");

        a5.sendTransmission("Warp drive malfunction. Stuck near Saturn.");

        a6.sendTransmission("Peace has been negotiated with the Andromeda Federation.");
        a6.sendTransmission("Our knowledge-sharing treaty begins tomorrow.");
        
        a7.sendTransmission("Peace is so important.");
       

        net.displayAllTransmissions();

        // Demonstrate edit, delete, and declare features
        ((EliteAlien) a2).editTransmission(0, "Fleet will now survey Pluto instead.");
        ((CommonAlien) a1).deleteTransmission(1);
        ((RoyalAlien) a6).declare("All spaceports shall be renamed in honor of the Galactic Harmony Treaty.");
       
        ((RoyalAlien) a7).declare("A new era of peace begins today, "
        		+ "all alliances shall be honored across galaxies, and conflict shall be silenced under the stars.");

        System.out.println("------------------------------------");
        net.displayAllTransmissions();

        System.out.println("Revenue for this month: " + net.calculateRevenue() + " galactic credits");

        net.addAlien("Zentrak", "TimeTraveler");
        
        // Launch GUI to interact with AlienNet
        AlienNetGUI gui = new AlienNetGUI();
        
     // ============================================= In-Lab Test Code===================================================
        
        System.out.println("\n------------- In lab --------------\n");

        // Create SupremeAlien
        Alien a8 = new SupremeAlien("Vortan", "Andromeda");
        net.getAliens().add(a8); // add to the network
        ((RoyalAlien) a8).setTitle("Overlord");
        a8.sendTransmission("Bow before me!");
        ((SupremeAlien) a8).makeAnnouncement("you must obey");
        System.out.println("\n------------- Display Transmissions of Supreme Alien--------------\n");
        a8.displayTransmissions();
        // Make a1 ally with a2, a4, a6, a8
        a1.allyWith(a2);
        a1.allyWith(a4);
        a1.allyWith(a6);
        a1.allyWith(a8);
        // Try duplicate alliance (should display a warning)
        a1.allyWith(a2);
        // Display allied transmissions of a1
        System.out.println("------------------------------------");
        System.out.println(a1.getName() + "'s Allied Transmissions:");
        a1.displayAlliedTransmissions();
        // Display total platform interactions
        System.out.println("------------------------------------");
        net.displayInteractions();
        // Test makeAnnouncement from each subclass
        System.out.println("------------------------------------");
        a1.makeAnnouncement("we must protect our planet");
        a2.makeAnnouncement("launching next phase");
        a6.makeAnnouncement("diplomatic peace achieved");
        a8.makeAnnouncement("this is your final warning");
       
    }
}