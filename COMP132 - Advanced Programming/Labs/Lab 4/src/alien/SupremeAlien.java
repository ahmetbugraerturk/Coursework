package alien;

public class SupremeAlien extends RoyalAlien {
	
	private String empireName;
	
	public SupremeAlien(String name, String empireName) {
		super(name);
		this.empireName = empireName;
	}
	
	@Override
	public void displayTransmissions() {
		System.out.printf("(Supreme - %s of %s) %s:%n", this.getTitle(), empireName, this.getName());
		for (Transmission t: this.getTransmissions()) {
			System.out.printf("Transmission: %s%n", t);
		}
		System.out.println();
	}

	@Override
	public void makeAnnouncement(String message) {
		System.out.printf("🚀 Supreme %s %s of %s commands: %s", this.getTitle(), this.getName(), empireName, message.toUpperCase());
	}
	
}
