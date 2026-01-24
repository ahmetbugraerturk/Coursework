package transports;

import java.util.ArrayList;

public abstract class Transport {
	
	private static ArrayList<Transport> transportList = new ArrayList<>();
	private String brandAndModel;
	private double price;
	private double remainingRange;
	
	Transport(String brandAndModel, double price) {
		this.brandAndModel = (brandAndModel == null || brandAndModel.isEmpty()) ? "Anonymous" : brandAndModel;
		this.price = price < 0 ? 0 : price;
		
		transportList.add(this);
	}
	
	public static int getTotalTransports() {
		return transportList.size();
	}
	
	public static void printAllTransports() {
		System.out.println("List of all transports:");
		for (Transport t: transportList) {
			System.out.println(t);
		}
	}
	
	abstract void startTrip(double distance);
	
	public abstract String toString();
	
	public String getBrandAndModel() {
		return brandAndModel;
	}
	
	public double getPrice() {
		return price;
	}
	
	public double getRemainingRange() {
		return remainingRange;
	}
	
	public void setRemainingRange(double remainingRange) {
		this.remainingRange = remainingRange;
	}
	
	public static void printTransportStatistics() {
		int totalNum = 0;
		int[] numberOfTransporters = {0,0,0};
		double range = 0;
		for (Transport t: transportList) {
			if (t instanceof ElectricCar)
				numberOfTransporters[0]++;
			else if (t instanceof Truck)
				numberOfTransporters[1]++;
			else if (t instanceof HybridCar)
				numberOfTransporters[2]++;
			totalNum++;
			range += t.getRemainingRange();
		}
		System.out.printf("Total Transports: %d%n", totalNum);
		System.out.printf("Electric Cars: %d%n", numberOfTransporters[0]);
		System.out.printf("Trucks: %d%n", numberOfTransporters[1]);
		System.out.printf("Hybrid Cars: %d%n", numberOfTransporters[2]);
		System.out.printf("Average Remaining Range: %.3f%n", range/totalNum);

	}

}
