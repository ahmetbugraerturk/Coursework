package spaceMission;

import java.util.Random;

public class Alien {
	
	final static Random RAND = new Random(2025);
	
	private String species;
	private String motive;
	
	public Alien(String species, String motive) {
		this.species = species;
		this.motive = motive;
	}
	
	public static void interact(String question, Alien alien) {
		System.out.printf("Astronaut: %s%n", question);
		System.out.printf("The Alien %s's response: %s%n", alien.getSpecies(), alien.getMotive());
		if (RAND.nextBoolean()) {
			System.out.printf("The Alien %s is hostile.%n", alien.getSpecies());
		} else {
			System.out.printf("The Alien %s is friendly.%n", alien.getSpecies());
		}
	}

	public String getSpecies() {
		return species;
	}
	
	public String getMotive() {
		return motive;
	}
	
	public static void interact(String question, Alien[] aliens) {
		for (Alien alien:aliens) {
			System.out.printf("The Alien %s:%n", alien.getSpecies());
			System.out.printf("Astronaut: %s%n", question);
			System.out.printf("The Alien %s's response: %s%n", alien.getSpecies(), alien.getMotive());
			if (RAND.nextBoolean()) {
				System.out.printf("The Alien %s is hostile.%n", alien.getSpecies());
			} else {
				System.out.printf("The Alien %s is friendly.%n", alien.getSpecies());
			}
			System.out.println();
		}
	}

}
