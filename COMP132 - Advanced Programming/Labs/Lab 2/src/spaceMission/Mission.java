package spaceMission;

public class Mission {

	private Planet planet;
	private Alien alien;
	private Astronaut astronaut;
	
	public Mission(Planet planet) {
		this.planet = planet;
	}
	
	public Planet getPlanet() {
		return planet;
	}

	public void displayMissionDetails() {		
		System.out.printf("Planet: %s%n", planet.getName());
		System.out.printf("Astronaut Name: %s%n", astronaut.getName());
		System.out.printf("Alien Species: %s%n", alien.getSpecies());
	}

	public Alien getAlien() {
		return alien;
	}

	public void setAlien(Alien alien) {
		this.alien = alien;
	}

	public Astronaut getAstronaut() {
		return astronaut;
	}

	public void setAstronaut(Astronaut astronaut) {
		this.astronaut = astronaut;
	}
	
}
