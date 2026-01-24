package spacetrade;

import java.util.Map;

public class Freighter implements Comparable<Freighter> {

	private static int totalFreighters = 1;
	private int id;
	private String name;
	private Map<String, Resource> resources;
	private boolean status;
	private GalacticNetwork network;
	
	public Freighter(String name, Map<String, Resource> initialResources) {
		this.name = name;
		this.resources = initialResources;
		this.status = true;
		id = totalFreighters++;
	}
	
	public void joinNetwork(GalacticNetwork network) {
		this.network = network;
		network.registerFreighter(this);
	}
	
	public boolean hasResource(Resource resource) {
		return resources.containsValue(resource);
	}
	
	public void receiveResource(Resource resource) {
		if (network == null)
			System.out.printf("Freighter %s has not joined the galactic network. Cannot receive resource.%n", name);
		else if (hasResource(resource))
			System.out.printf("Resource %s already owned by %s. Cannot receive again.%n", resource.getName(), name);
		else {
			resources.put(resource.getName(), resource);
			resource.addLocation(this);
			System.out.printf("Resource %s received by %s.%n", resource.getName(), name);
		}
	}
	
	public boolean requestResource(String ResourceName) {
		if (network == null) {
			System.out.printf("%s has not joined the galactic network. Resource request aborted.%n", name);
			return false;
		} else if (!network.resourceExists(ResourceName)) {
			System.out.printf("%s is not registered in the galactic trade system.%n", ResourceName);
			return false;
		} else if (hasResource(network.getResourceInfo(ResourceName))) {
			System.out.printf("%s already has %s. Request skipped.%n", name, ResourceName);
			return false;
		} else {
			receiveResource(network.getResourceInfo(ResourceName));
			System.out.printf("Resource %s successfully acquired by %s.%n", ResourceName, name);
			return true;
		}
		
	}
	
	public String toString() {
		return String.format("Freighter ID: %d%nName: %s%nStatus: %s", id, name, status ? "Online" : "Offline");
	}
	
	public Map<String, Resource> getResources() {
		return resources;
	}
	
	public int getID() {
		return id;
	}
	
	public String getName() {
		return name;
	}
	
	public boolean getStatus() {
		return status;
	}

	@Override
	public int compareTo(Freighter o) {
		// TODO Auto-generated method stub
		if (o.id<this.id)
			return 1;
		else if (o.id>this.id)
			return -1;
		else
			return 0;
	}


	
}
