package resources;

import java.util.ArrayList;

public class ResourceGrid {
	
	private String stationName;
	private int[][] resources;
	
	public ResourceGrid(String stationName, int[][] resources) {
		this.stationName = stationName;
		this.resources = resources;
	}
	
	public ResourceGrid(String stationName) {
		this(stationName, new int[3][3]);
	}
	
	public ResourceGrid() {
		this("Unknown Station", new int[3][3]);
	}
	
	public void transferResources(ResourceGrid other) {
		int[][] ores = other.getResources();
		if (ResourceHelper.areSameSize(ores, resources)) {
			int[][] newRes = ResourceHelper.deepCopy(resources);
			for (int i = 0; i<newRes.length; i++) {
				for (int j = 0; j<newRes[i].length; j++) {
					newRes[i][j] += ores[i][j];
				}
			}
			System.out.println(new ResourceGrid("a", newRes).toString());
		} else
			System.out.printf("Resource transfer between %s and %s failed: Different storage capacities.%n" ,stationName, other.getStationName());
	}
	
	public void depleteResources(ResourceGrid other) {
		int[][] ores = other.getResources();
		if (ResourceHelper.areSameSize(ores, resources)) {
			int[][] newRes = ResourceHelper.deepCopy(resources);
			for (int i = 0; i<newRes.length; i++) {
				for (int j = 0; j<newRes[i].length; j++) {
					newRes[i][j] -= ores[i][j];
					if (newRes[i][j]<0)
						newRes[i][j] = 0;
				}
			}
			System.out.println(new ResourceGrid("a", newRes).toString());
		} else
			System.out.println("Resource depletion failed: Different storage capacities.");
	}
	
	public void scaleResources(int factor) {
		for (int i = 0; i<resources.length; i++) {
			for (int j = 0; j<resources[i].length; j++) {
				resources[i][j] *= factor;
			}
		}
		System.out.println("New Storage at Alpha after scaling:");
		System.out.println(new ResourceGrid("a", resources).toString());
	}
	
	public void redistributeResources() {
		int[][] newRes = new int[resources[0].length][resources.length];
		for (int i = 0; i<resources.length; i++) {
			for (int j = 0; j<resources[i].length; j++) {
				newRes[j][i] = resources[i][j];
			}
		}
		resources = newRes;
		System.out.println("New Storage at Alpha after redistribution :");
		System.out.println(new ResourceGrid("a", resources).toString());
	}
	
	public void checkIfBalanced() {
		boolean isBalanced = true;
		int sum = 0;
		for (int i = 0; i<resources.length; i++) {
			int curSum = 0;
			for (int j = 0; j<resources[i].length; j++) {
				if (i==0)
					sum += resources[i][j];
				curSum += resources[i][j];
			}
			if (curSum!=sum)
				isBalanced = false;
		}
		if (isBalanced)
			System.out.printf("Station %s is balanced.%n", stationName);
		else
			System.out.printf("Station %s is not balanced.%n", stationName);
	}

	public void checkIfEmptyStorage() {
		boolean isEmpty = true;
		for (int i = 0; i<resources.length; i++) {
			for (int j = 0; j<resources[i].length; j++) {
				if (resources[i][j]!=0)
					isEmpty = false;
			}
		}
		if (isEmpty)
			System.out.printf("Storage at station %s is completely empty.%n", stationName);
		else
			System.out.printf("Storage at station %s is not completely empty.%n", stationName);
	}
	
	public void checkIfMajorityResource(int resourceType) {
		int count = 0;
		int total = 0;
		for (int i = 0; i<resources.length; i++) {
			for (int j = 0; j<resources[i].length; j++) {
				if (resources[i][j]==resourceType)
					count++;
				total++;
			}
		}
		if (count>total/2)
			System.out.printf("Station %s has a majority of %d.%n", stationName, resourceType);
		else
			System.out.printf("Station %s does not have a majority of %d.%n", stationName, resourceType);
	}
	
	public String toString() {
		String output = "";
		for (int i = 0; i<resources.length; i++) {
			output += "[ ";
			for (int j = 0; j<resources[i].length; j++) {
				output += resources[i][j]+" ";
			}
			output += "]\n";
		}
		return output;
	}
	
	public int[][] getResources() {
		return resources;
	}
	
	public String getStationName() {
		return stationName;
	}
	
	public void trace() {
		if (resources.length!=resources[0].length)
			System.out.println("The grid is not square. The trace cannot be calculated.");
		else {
			int sum = 0;
			for (int i = 0; i<resources.length; i++) {
				sum += resources[i][i];
			}
			System.out.printf("The trace at station %s is %d%n", stationName, sum);
		}
	}
	
	public ArrayList<Integer> flatten() {
		ArrayList<Integer> flat = new ArrayList<>();
		for (int i = 0; i<resources.length; i++) {
			for (int j = 0; j<resources[i].length; j++) {
				flat.add(resources[i][j]);
			}
		}
		return flat;
	}
	
}
