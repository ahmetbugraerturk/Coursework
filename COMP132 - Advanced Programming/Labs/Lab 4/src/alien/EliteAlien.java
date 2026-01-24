package alien;

public class EliteAlien extends Alien {
	
	public EliteAlien(String name) {
		super(name);
	}
	
	public void editTransmission(int id, String newMessage) {
		super.getTransmissions().get(id).edit(newMessage);
	}
	
	@Override
	public void displayTransmissions() {
		System.out.printf("(Elite) %s:%n", this.getName());
		super.displayTransmissions();
	}
	
	@Override
	public void makeAnnouncement(String message) {
		System.out.printf("(Elite) %s broadcasts: %s%n", this.getName(), message);
	}

}
