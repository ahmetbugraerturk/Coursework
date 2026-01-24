package spacetrade;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class GalacticNetwork {
	
	private List<Freighter> freighters;
	private Map<String, Resource> resources = new HashMap<>();
	
	public GalacticNetwork(Resource[] resources) {
		freighters = new ArrayList<>();
		for (Resource r: resources) {
			this.resources.put(r.getName(), r);
		}
	}
	
	public boolean resourceExists(String name) {
		return resources.containsKey(name);
	}
	
	public Resource getResourceInfo(String name) {
		return resources.get(name);
	}
	
	public void registerFreighter(Freighter freighter) {
		freighters.add(freighter);
		updateFreighterResources(freighter);
	}
	
	private void updateFreighterResources(Freighter freighter) {
		for (Resource r: freighter.getResources().values()) {
			if (!r.availableAt(freighter))
				r.addLocation(freighter);
		}
	}
	
	public List<Freighter> getFreightersWithResource(String resourceName) {
		List<Freighter> list = new ArrayList<>();
		for (Freighter f: freighters) {
			if (f.hasResource(getResourceInfo(resourceName)))
				list.add(f);
		}
		return list;
	}
	
	public void printFreightersWithResource(String resourceName) {
		System.out.println("Resource lookup: " + resourceName);
		if (getFreightersWithResource(resourceName).isEmpty())
			System.out.println("No freighters currently have this resource.");
		for (Freighter f: getFreightersWithResource(resourceName)) {
			System.out.println(f);
			System.out.println();
		}
	}
	
	public void sortFreighters() {
		Collections.sort(freighters);
	}
	
	public void sortFreightersReverse() {
		sortFreighters();
		Collections.reverse(freighters);
	}
	
	public String showFreighters() {
		String s = "";
		for (Freighter f: freighters) {
			s += String.format("%d - %s - %s%n", f.getID(), f.getName(), f.getStatus() ? "Online" : "Offline");
		}
		return s;
	}
	
	public Map<Freighter, Map<Freighter, List<Resource>>> findCommonResources() {
		Map<Freighter, Map<Freighter, List<Resource>>> finalMap = new LinkedHashMap<>();
		
		for (int i = 0; i<freighters.size(); i++) {
			Freighter f = freighters.get(i);
			Map<Freighter, List<Resource>> freighterMap = new LinkedHashMap<>();
			for (Freighter other: freighters.subList(i+1, freighters.size())) {
				List<Resource> commonResources = new ArrayList<>();
				for (Resource r: f.getResources().values()) {
					if (other.hasResource(r))
						commonResources.add(r);
				}
				if (!commonResources.isEmpty())
					freighterMap.put(other, commonResources);
			}
			if (!freighterMap.isEmpty())
				finalMap.put(f, freighterMap);
		}
		
		return finalMap;
	}

}
