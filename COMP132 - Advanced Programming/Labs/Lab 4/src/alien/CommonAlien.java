package alien;

public class CommonAlien extends Alien{

	public CommonAlien(String name) {
		super(name);
	}
	
	public void deleteTransmission(int id) {
		super.getTransmissions().remove(id);
	}
	
	@Override
	public void displayTransmissions() {
		System.out.printf("(Common) %s:%n", this.getName());
		super.displayTransmissions();
	}
	
	@Override
	public void makeAnnouncement(String message) {
		System.out.printf("(Common) %s whispers: %s%n", this.getName(), message);
	}
}
