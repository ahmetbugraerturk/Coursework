package spaceMission;

public class ComplexMission {
	
	private Planet planet;
	private Alien[] aliens;
	private int currentAlienIndex = 0;
	private Astronaut astronaut;
	
	public ComplexMission(Planet planet, int numberOfAliens) {
		this.planet = planet;
		aliens = new Alien[numberOfAliens];
	}

	public void displayComplexMissionDetails() {
		System.out.printf("Planet: %s%n", planet.getName());
		System.out.printf("Astronaut Name: %s%n", astronaut.getName());
		System.out.println("Aliens:");
		for (Alien a:aliens) {
			System.out.printf("- %s%n", a.getSpecies());
		}
	}
	
	public Alien[] getAliens() {
		return aliens;
	}


	public void addAlien(Alien alien) {
		if (currentAlienIndex < aliens.length) {
			aliens[currentAlienIndex] = alien;
			currentAlienIndex++;
		} else {
			System.out.println("Cannot add more aliens. Maximum limit reached.");
		}
	}

	public Planet getPlanet() {
		return planet;
	}

	public Astronaut getAstronaut() {
		return astronaut;
	}

	public void setAstronaut(Astronaut astronaut) {
		this.astronaut = astronaut;
	}
	
	
}
