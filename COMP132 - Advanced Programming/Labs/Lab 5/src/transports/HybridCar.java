package transports;

public class HybridCar extends ElectricTransport implements Rechargeable, Refuelable {
	
	private double fuelCapacity;
	private double currentFuelLevel;
	private double fuelConsumptionRate;

	public HybridCar(String brandAndModel, double price, double batteryCapacity, double currentBatteryLevel,
			double energyConsumptionRate, double fuelCapacity, double currentFuelLevel, double fuelConsumptionRate) {
		
		super(brandAndModel, price, batteryCapacity, currentBatteryLevel, energyConsumptionRate);
		
		this.fuelCapacity = fuelCapacity < 20 ? 20 : fuelCapacity;
		this.currentFuelLevel = currentFuelLevel < 0 ? 0 : (currentFuelLevel > this.fuelCapacity ? this.fuelCapacity : currentFuelLevel);
		this.fuelConsumptionRate = fuelConsumptionRate < 0.5 ? 0.5 : fuelConsumptionRate;
		setRemainingRange(this.getCurrentBatteryLevel() / this.getEnergyConsumptionRate() + this.currentFuelLevel / this.fuelConsumptionRate);
		
	}

	@Override
	public void startTrip(double distance) {
		// TODO Auto-generated method stub
		if (distance < 0)
			System.out.println("Invalid distance. Trip canceled.");
		else if (getRemainingRange() < distance)
			System.out.printf("Hybrid %s cannot complete %.1f km trip.%n", getBrandAndModel(), distance);
		else {
			double electricRange = getCurrentBatteryLevel() / getEnergyConsumptionRate();
			double firstDistance = distance;
			if (electricRange < distance) {
				setRemainingRange(getRemainingRange() - distance);
				distance -= electricRange;
				setCurrentBatteryLevel(0);
				currentFuelLevel -= fuelConsumptionRate * distance;
			} else {
				setRemainingRange(getRemainingRange() - distance);
				setCurrentBatteryLevel(getCurrentBatteryLevel() - distance * getEnergyConsumptionRate());
				distance -= electricRange;
				distance = 0;
			}
			System.out.printf("Hybrid %s traveled %.1f km:%n- %.1f km on battery (%.1f kWh used)%n- %.1f km on fuel (%.1f L used)%nRemaining: %.1f kWh + %.1f L%n", getBrandAndModel(), firstDistance, electricRange, electricRange*getEnergyConsumptionRate(), distance, fuelConsumptionRate * distance, getCurrentBatteryLevel(), currentFuelLevel);
		}
	}
	
	@Override
	public String toString() {
		return String.format("Transport of Brand: %s, price: $%.1f, Battery: %.1f%%, Remaining range: %.2f km, Max Capacity: %.1f%%, Fuel Level: %.1f L, Fuel-Only Range: %.2f km", getBrandAndModel(), getPrice(), getCurrentBatteryLevel(), getRemainingRange(), getBatteryCapacity(), currentFuelLevel, currentFuelLevel/fuelConsumptionRate);
	}

	@Override
	public void recharge() {
		if (getBatteryCapacity() == getCurrentBatteryLevel()) {
			System.out.printf("HybridCar %s is at max capacity.%n", getBrandAndModel());
		} else {
			System.out.printf("Hybrid %s recharged to %.1f kWh.%n", getBrandAndModel(), getBatteryCapacity());
			setCurrentBatteryLevel(getBatteryCapacity());
			setRemainingRange(getCurrentBatteryLevel() / getEnergyConsumptionRate() + currentFuelLevel / fuelConsumptionRate);
		}
	}

	@Override
	public void refuel() {
		
		if (fuelCapacity == currentFuelLevel) {
			System.out.printf("HybridCar %s already has a full tank.%n", getBrandAndModel());
		} else {
			System.out.printf("Hybrid %s refueled to %.1f L.%n", getBrandAndModel(), fuelCapacity);
			currentFuelLevel = fuelCapacity;
			setRemainingRange(getCurrentBatteryLevel() / getEnergyConsumptionRate() + currentFuelLevel / fuelConsumptionRate);
		}		
	}
	
}
