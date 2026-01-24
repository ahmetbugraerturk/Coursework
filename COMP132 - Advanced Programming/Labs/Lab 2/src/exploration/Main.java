/* *********** Pledge of Honor *************************** *
I hereby certify that I have completed this lab assignment on my own
without any help from anyone else. I understand that the only sources of authorized
information in this lab assignment are (1) the course textbook, (2) the
materials posted at the course website and (3) any study notes handwritten by myself.
I have not used, accessed or received any information from any other unauthorized
source in taking this lab assignment. The effort in the assignment thus belongs
completely to me.

READ AND SIGN BY WRITING YOUR NAME SURNAME AND STUDENT ID
SIGNATURE: Ahmet Buğra Ertürk, 86877

**********************************************************/
package exploration;

import spaceMission.*;

public class Main {
	public static void main(String[] args) {
        // Create a mission control with a fixed number of missions
		MissionControl simulator = new MissionControl(3);

		Astronaut e1 = new Astronaut("Neil Armstrong", 101);
		Astronaut e2 = new Astronaut("Ellen Ripley", 102);
        Astronaut e3 = new Astronaut("Buzz Lightyear", 103);

        // Create and add planet to the mission control
        Planet location1 = new Planet("Zyphos Prime"); // A mysterious jungle planet with ancient ruins
        Planet location2 = new Planet("Vortex Nebula"); // A planet with extreme gravitational anomalies
        Planet location3 = new Planet("Eldoria"); // A lost planet covered in shimmering golden sand and ancient technology.
        Planet location4 = new Planet("Cryon V"); //A frozen world with hidden alien artifacts

        location1.collectSample("Cryo-Fossil");
        location1.collectSample("Quantum Crystal");

        location2.collectSample("Warped Relic");
        location2.collectSample("Star Core Fragment");

        location3.collectSample("Plasma Orb");
        location3.collectSample("Celestial Coral");
        location3.collectSample("Ancient Star Chart");
        location3.collectSample("Gravity Anomaly Detector");
        location3.collectSample("Meteoric Alloy");
        location3.collectSample("Encrypted Data Chip");

        // Add Alien to the mission
        Alien hunter1 = new Alien("Xylog", "I am searching for my lost cybernetic arm.");
        Alien hunter2 = new Alien("Vireen", "I was gathering rare minerals for energy synthesis.");
        Alien hunter3 = new Alien("Zarnok", "I was tracking a stolen spaceship.");

        // Create and add mission to the mission control
        Mission quest1 = new Mission(location1);
        Mission quest2 = new Mission(location2);
        Mission quest3 = new Mission(location3);
        Mission quest4 = new Mission(location4);

        quest1.setAlien(hunter3);
        quest2.setAlien(hunter2);
        quest3.setAlien(hunter1);

        quest1.setAstronaut(e1);
        quest2.setAstronaut(e2);
        quest3.setAstronaut(e3);

        // Add missions to the mission control
        simulator.addMission(quest1);
        simulator.addMission(quest2);
        simulator.addMission(quest3);
        simulator.addMission(quest4);

        // Start the expedition
        simulator.startExpedition();
        
        ////////////////////////// inLab test code //////////////////////////
        
        System.out.print("\n\n------------------------ In lab ------------------------\n\n");
        Alien hunter4 = new Alien("Omekra", "I was studying the plant life on this planet.");
        // Create the complex Mission Control
        ComplexMissionControl simulator2 = new ComplexMissionControl(3);
        // Create complex missions and add them to the complex mission control
        ComplexMission complexCase1 = new ComplexMission(location1, 3);
        ComplexMission complexCase2 = new ComplexMission(location2, 2);
        ComplexMission complexCase3 = new ComplexMission(location3, 4);
        ComplexMission complexCase4 = new ComplexMission(location4, 2);
        complexCase1.setAstronaut(e1);;
        complexCase2.setAstronaut(e2);;
        complexCase3.setAstronaut(e3);;
        // Add Aliens to the missions
        complexCase1.addAlien(hunter1);;
        complexCase1.addAlien(hunter2);;
        complexCase1.addAlien(hunter3);;
        complexCase2.addAlien(hunter1);;
        complexCase2.addAlien(hunter2);;
        complexCase2.addAlien(hunter3);;
        complexCase3.addAlien(hunter1);;
        complexCase3.addAlien(hunter2);;
        complexCase3.addAlien(hunter3);;
        complexCase3.addAlien(hunter4);;
        complexCase4.addAlien(hunter1);;
        complexCase4.addAlien(hunter2);;

        // Add missions to the simulator
        simulator2.addComplexMission(complexCase1);
        simulator2.addComplexMission(complexCase2);

        simulator2.addComplexMission(complexCase3);
        simulator2.addComplexMission(complexCase4);
        // Start the Expedition
        simulator2.startExpedition();
    
    }

}
