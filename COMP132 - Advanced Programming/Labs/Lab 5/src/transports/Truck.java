package transports;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class Truck extends Transport implements Refuelable {
	
	private double fuelCapacity;
	private double currentFuelLevel;
	private double fuelConsumptionRate;
	private static ArrayList<Truck> truckList = new ArrayList<>();
	private Set<String> cargoSet;
	
	public Truck(String brandAndModel, double price, double fuelCapacity, double currentFuelLevel, double fuelConsumptionRate) {
		super(brandAndModel, price);
		this.fuelCapacity = fuelCapacity < 20 ? 20 : fuelCapacity;
		this.currentFuelLevel = currentFuelLevel < 0 ? 0 : (currentFuelLevel > this.fuelCapacity ? this.fuelCapacity : currentFuelLevel);
		this.fuelConsumptionRate = fuelConsumptionRate < 0.5 ? 0.5 : fuelConsumptionRate;
		setRemainingRange(this.currentFuelLevel / this.fuelConsumptionRate);
		
		cargoSet = new HashSet<>();
		truckList.add(this);
	}
	
	public static int getTotalTrucks() {
		return truckList.size();
	}
	
	public static void startAllTrucks(double distance) {
		for (Truck t: truckList) {
			t.startTrip(distance);
		}
	}

	@Override
	public void startTrip(double distance) {
		if (distance < 0)
			System.out.println("Invalid distance. Trip canceled.");
		else {
			if (distance > getRemainingRange()) {
				System.out.printf("Truck %s cannot complete %.1f km trip. Needs %.1f  L, but only %.1f L left.%n", getBrandAndModel(), distance, fuelConsumptionRate*distance, currentFuelLevel);
			} else {
				System.out.printf("Truck %s has traveled a trip for %.1f km, consuming %.1f L/km. Total of %.1f L decrease in fuel level.%n", getBrandAndModel(), distance, fuelConsumptionRate, fuelConsumptionRate*distance);
				currentFuelLevel = currentFuelLevel-fuelConsumptionRate*distance;
				setRemainingRange(currentFuelLevel / fuelConsumptionRate);
			}
		}
	}
	
	public void addCargo(String cargoItem) {
		if (cargoSet.add(cargoItem))
			System.out.printf("Added cargo item: %s%n", cargoItem);
		else
			System.out.printf("Cargo item already exists: %s%n", cargoItem);
	}
	
	public void removeCargo(String cargoItem) {
		if (cargoSet.remove(cargoItem))
			System.out.printf("Removed cargo item: %s%n", cargoItem);
		else
			System.out.printf("Cargo item not found: %s%n", cargoItem);
	}
	
	public void listCargo() {
		System.out.printf("Cargo items for %s: %s%n", getBrandAndModel(), cargoSet);
	}
	
	public String toString() {
		return String.format("Transport of Brand: %s, price: $%.1f, Fuel: %.1f L, Range: %.2f km", getBrandAndModel(), getPrice(), currentFuelLevel, getRemainingRange());
	}

	@Override
	public void refuel() {
		if (fuelCapacity == currentFuelLevel) {
			System.out.printf("Refueling not possible; Truck %s is at max capacity.%n", getBrandAndModel());
		} else if (fuelCapacity - currentFuelLevel > 10) {
			currentFuelLevel = currentFuelLevel+10;
			System.out.printf("Truck %s refueled to %.1f L.%n", getBrandAndModel(), currentFuelLevel);
			setRemainingRange(currentFuelLevel / fuelConsumptionRate);
		} else {
			System.out.printf("Truck %s refueled to %.1f L.%n", fuelCapacity - currentFuelLevel, getBrandAndModel(), fuelCapacity);
			currentFuelLevel = fuelCapacity;
			setRemainingRange(currentFuelLevel / fuelConsumptionRate);
		}
	}

}
