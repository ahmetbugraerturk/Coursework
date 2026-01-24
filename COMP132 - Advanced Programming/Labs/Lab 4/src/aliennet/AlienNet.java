package aliennet;

import java.util.ArrayList;

import alien.*;

public class AlienNet {
	
	private ArrayList<Alien> aliens = new ArrayList<Alien>();
	
	public Alien addAlien(String name, String type) {
		switch(type) {
			case "Elite":
				aliens.add(new EliteAlien(name));
				return aliens.getLast();
			case "Royal":
				aliens.add(new RoyalAlien(name));
				return aliens.getLast();
			case "Common":
				aliens.add(new CommonAlien(name));
				return aliens.getLast();
			default:
				System.out.printf("No such alien type: %s.%n", type);
				return null;
		}		
	}
	
	public int calculateRevenue() {
		int val = 0;
		for (Alien a: aliens) {
			if (a instanceof EliteAlien) {
				val += 10;
			}
		}
		return val;
	}
	
	public void displayAllTransmissions() {
		for (Alien a: aliens) {
			a.displayTransmissions();
		}
	}
	
	public void displayInteractions() {
		int t=0;
		int c=0;
		int e=0;
		int r=0;
		int s=0;
		for (Alien a: aliens) {
			t += a.getTransmissions().size();
			if (a instanceof CommonAlien)
				c++;
			else if (a instanceof SupremeAlien)
				s++;
			else if (a instanceof RoyalAlien)
				r++;
			else if (a instanceof EliteAlien)
				e++;
		}
		System.out.printf("Total Number of Transmissions: %d%n", t);
		System.out.printf("From CommonAliens: %d%n", c);
		System.out.printf("From EliteAliens: %d%n", e+r);
		System.out.printf("From RoyalAliens: %d%n", r+s);
		System.out.printf("From SupremeAliens: %d%n", s);
	}

	public ArrayList<Alien> getAliens() {
		return aliens;
	}

}
