package alien;

public class RoyalAlien extends EliteAlien {
	
	private String title;
	
	public RoyalAlien(String name) {
		super(name);
		title = "Emperor";
	}
	
	public void declare(String announcement) {
		System.out.printf("👑 %s %s declares: %s%n", title, this.getName(), announcement);
	}
	
	@Override
	public void displayTransmissions() {
		System.out.printf("(Royal - %s) %s:%n", title, this.getName());
		for (Transmission t: this.getTransmissions()) {
			System.out.printf("Transmission: %s%n", t);
		}
		System.out.println();
	}

	public void setTitle(String title) {
		this.title = title;
	}
	
	public String getTitle() {
		return this.title;
	}
	
	@Override
	public void makeAnnouncement(String message) {
		System.out.printf("👑 (Royal - %s) %s proclaims: %s%n", title, this.getName(), message);
	}

}
