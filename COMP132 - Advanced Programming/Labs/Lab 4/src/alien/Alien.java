package alien;

import java.util.ArrayList;

public class Alien {
	
	private String name;
	private int id;
	private static int idCounter = 0;
	private ArrayList<Transmission> transmissions = new ArrayList<Transmission>();
	protected ArrayList<Alien> allies = new ArrayList<Alien>();
	
	public Alien(String name) {
		this.name = name;
		id = idCounter;
		idCounter++;
	}

	public void displayTransmissions() {
		for (Transmission t: transmissions) {
			System.out.printf("Transmission: %s%n", t);
		}
		System.out.println();
	}
	
	public void sendTransmission(String message) {
		transmissions.add(new Transmission(message));
	}

	public ArrayList<Transmission> getTransmissions() {
		return transmissions;
	}

	public void setTransmissions(ArrayList<Transmission> transmissions) {
		this.transmissions = transmissions;
	}

	public String getName() {
		return name;
	}
	
	@Override
	public String toString() {
		return this.getName();
	}
	
	public void allyWith(Alien alien) {
		if (!allies.contains(alien)) {
			allies.add(alien);
		} else
			System.out.println("Impossible alliance since this alien is already allied");
	}
	
	public void displayAlliedTransmissions() {
		for (Alien a: allies) 
			if (a instanceof RoyalAlien)
				a.displayTransmissions();
		for (Alien a: allies) 
			if (a instanceof EliteAlien && !(a instanceof RoyalAlien))
				a.displayTransmissions();
		for (Alien a: allies) 
			if (a instanceof CommonAlien)
				a.displayTransmissions();
	}
	
	public void makeAnnouncement(String message) {
		
	}
	
}
