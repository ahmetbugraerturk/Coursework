package location;

import exception.InvalidLocationException;

public class Location {

	private double latitude;
	private double longitude;
	
	public Location(double latitude, double longitude) throws InvalidLocationException {
		LocationValidator.validateLatitudeLongitude(latitude, longitude);
		this.latitude = latitude;
		this.longitude = longitude;
	}
	
	public double distanceTo(Location location) {
		return haversine(this.latitude, this.longitude, location.latitude, location.longitude);
	}

	public double getLatitude() {
		return latitude;
	}

	public double getLongitude() {
		return longitude;
	}
	
	double haversine(double lat1, double lon1,double lat2, double lon2)
	{
	        // distance between latitudes and longitudes
	        double dLat = Math.toRadians(lat2 - lat1);
	        double dLon = Math.toRadians(lon2 - lon1);
	 
	        // convert to radians
	        lat1 = Math.toRadians(lat1);
	        lat2 = Math.toRadians(lat2);
	 
	        // apply formulae
	        double a = Math.pow(Math.sin(dLat / 2), 2) +
	                   Math.pow(Math.sin(dLon / 2), 2) *
	                   Math.cos(lat1) *
	                   Math.cos(lat2);
	        double rad = 6371;
	        double c = 2 * Math.asin(Math.sqrt(a));
	        return rad * c;
	}
}
