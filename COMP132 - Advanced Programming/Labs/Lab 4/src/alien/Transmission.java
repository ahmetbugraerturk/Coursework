package alien;

public class Transmission {
	
	private String message;
	
	public Transmission(String message) {
		this.message = message;
	}
	
	public void edit(String newMessage) {
		message = newMessage;
	}
	
	public String toString() {
		return message;
	}

}
