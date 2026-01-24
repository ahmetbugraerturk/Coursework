package spaceMission;

public class Planet {

	static final int MAX_SAMPLES = 5;
	
	private String name;
	private String[] samples = new String[MAX_SAMPLES];
	private int numOfSamples = 0;
	
	public Planet(String name) {
		this.name = name;
	}
	
	public void collectSample(String sample) {
		if (!(numOfSamples < MAX_SAMPLES)) {
			System.out.println("Sample collection limit reached for this planet.");
		} else {
			samples[numOfSamples] = sample;
			numOfSamples++;
		}
	}
	
	public void displayPlanetInfo() {
		System.out.printf("Planet Name: %s%n", name);
		System.out.println("Samples:");
		for (int i = 0; i < numOfSamples; i++) {
			System.out.printf("- %s%n", samples[i]);
		}
	}

	public String getName() {
		return name;
	}

}
