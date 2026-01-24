package location;

import exception.InvalidLocationException;

public class LocationValidator {
	
	public static void validateLatitudeLongitude(double latitude, double longitude) throws InvalidLocationException {
		if (-90>longitude || longitude>90 || -180>latitude || latitude>180) {
			throw new InvalidLocationException("Invalid latitude or longitude.");
		}
	}
	
	public static void validate(Location location) throws InvalidLocationException {
		if (location == null)
			throw new InvalidLocationException("Location cannot be null.");
		validateLatitudeLongitude(location.getLatitude(), location.getLongitude());
	}
}
