package transports;

public class ElectricTransport extends Transport {
	
	private double batteryCapacity;
	private double currentBatteryLevel;
	private double energyConsumptionRate;
	
	public ElectricTransport(String brandAndModel, double price, double batteryCapacity, double currentBatteryLevel, double energyConsumptionRate){
		super(brandAndModel, price);
		this.batteryCapacity = batteryCapacity < 10 ? 10 : batteryCapacity;
		this.currentBatteryLevel = currentBatteryLevel < 0 ? 0 : (currentBatteryLevel > this.batteryCapacity ? this.batteryCapacity : currentBatteryLevel);
		this.energyConsumptionRate = energyConsumptionRate < 0.1 ? 0.1 : energyConsumptionRate;
		setRemainingRange(this.currentBatteryLevel / this.energyConsumptionRate);
	}

	@Override
	public void startTrip(double distance) {
		// TODO Auto-generated method stub
	}
	
	public String toString() {
		return String.format("Transport of Brand: %s, price: $%.1f, Battery: %.1f%%, Remaining range: %.2f km, Max Capacity: %.1f%%", getBrandAndModel(), getPrice(), currentBatteryLevel, getRemainingRange(), batteryCapacity);
	}

	public double getCurrentBatteryLevel() {
		return currentBatteryLevel;
	}
	
	public double getBatteryCapacity() {
		return batteryCapacity;
	}

	public void setCurrentBatteryLevel(double currentBatteryLevel) {
		this.currentBatteryLevel = currentBatteryLevel;
	}
	
	public double getEnergyConsumptionRate() {
		return energyConsumptionRate;
	}

}
