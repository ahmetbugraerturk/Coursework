package spacetrade;

import java.util.HashSet;
import java.util.Set;

public class Resource {
	
	private String name;
	private String description;
	private String type;
	private int quantity;
	private Set<Freighter> locations = new HashSet<>();
	
	public Resource(String name, String description, String type, int quantity) {
		this.name = name;
		this.description = description;
		this.type = type;
		this.quantity = quantity;
	}
	
	public void addLocation(Freighter freighter) {
		locations.add(freighter);
	}
	
	public boolean availableAt(Freighter freighter) {
		return freighter.hasResource(this);
	}
	
	public String toString() {
		return String.format("Resource Name=%s%nDescription=%s%nType=%s%nQuantity=%d%n", name, description, type, quantity);
	}
	
	public String getName() {
		return name;
	}
	
	public Set<Freighter> getLocations() {
		return locations;
	}
	
}
