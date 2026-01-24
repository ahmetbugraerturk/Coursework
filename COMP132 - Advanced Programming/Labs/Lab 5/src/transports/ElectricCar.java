package transports;

public class ElectricCar extends ElectricTransport implements Rechargeable {
	
	public ElectricCar(String brandAndModel, double price, double batteryCapacity, double currentBatteryLevel, double energyConsumptionRate) {
		super(brandAndModel, price, batteryCapacity, currentBatteryLevel, energyConsumptionRate);
	}
	
	public void startTrip(double distance) {
		if (distance < 0)
			System.out.println("Invalid distance. Trip canceled.");
		else {
			if (distance > getRemainingRange()) {
				System.out.printf("ElectricCar %s cannot complete %.1f km trip. Needs %.1f kWh, but only %.1f kWh left.%n", getBrandAndModel(), distance, getEnergyConsumptionRate()*distance, getCurrentBatteryLevel());
			} else {
				System.out.printf("ElectricCar %s has traveled a trip for %.1f km, consuming %.1f kWh/km. Total of %.1f kWh decrease in battery level.%n", getBrandAndModel(), distance, getEnergyConsumptionRate(), getEnergyConsumptionRate()*distance);
				setCurrentBatteryLevel(getCurrentBatteryLevel()-getEnergyConsumptionRate()*distance);
				setRemainingRange(getCurrentBatteryLevel() / getEnergyConsumptionRate());
			}
		}
	}
	
	@Override
	public void recharge() {
		if (getBatteryCapacity() == getCurrentBatteryLevel()) {
			System.out.printf("Recharging is not possible; ElectricCar %s is at max capacity.%n", getBrandAndModel());
		} else if (getBatteryCapacity() - getCurrentBatteryLevel() > 10) {
			setCurrentBatteryLevel(getCurrentBatteryLevel()+10);
			System.out.printf("Recharged by 10.0 units. ElectricCar %s is now at %.1f%%.%n", getBrandAndModel(), getCurrentBatteryLevel());
			setRemainingRange(getCurrentBatteryLevel() / getEnergyConsumptionRate());
		} else {
			System.out.printf("Recharged by %.1f units. ElectricCar %s is now fully charged at %.1f%%.%n", getBatteryCapacity() - getCurrentBatteryLevel(), getBrandAndModel(), getBatteryCapacity());
			setCurrentBatteryLevel(getBatteryCapacity());
			setRemainingRange(getCurrentBatteryLevel() / getEnergyConsumptionRate());
		}
	}

}
