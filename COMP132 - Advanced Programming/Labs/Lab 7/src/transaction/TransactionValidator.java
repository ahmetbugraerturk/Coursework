package transaction;

import exception.InvalidLocationException;
import exception.InvalidParameterException;
import exception.InvalidTransactionException;
import location.Location;

public class TransactionValidator {
	
	public static void validateLocations(Location sender, Location receiver) throws InvalidParameterException, InvalidTransactionException, InvalidLocationException {
		if (sender==null || receiver==null)
			throw new InvalidParameterException("Sender location and receiver location cannot be null");
		if (sender.distanceTo(new Location(41.1623, 29.0474))>10 && receiver.distanceTo(new Location(41.1623, 29.0474))>10)
			throw new InvalidTransactionException(String.format("Transaction aborted: both sender and receiver are out of range. Sender location: (%.1f, %.1f), Receiver location: (%.1f, %.1f)", sender.getLatitude(), sender.getLongitude(), receiver.getLatitude(), receiver.getLongitude()));
		else if (sender.distanceTo(new Location(41.1623, 29.0474))>10)
			throw new InvalidTransactionException(String.format("Transaction aborted: sender is out of range. Sender location: (%.1f, %.1f)", sender.getLatitude(), sender.getLongitude()));
		else if (receiver.distanceTo(new Location(41.1623, 29.0474))>10)
			throw new InvalidTransactionException(String.format("Transaction aborted: receiver is out of range. Receiver location: (%.1f, %.1f)", receiver.getLatitude(), receiver.getLongitude()));
	}
	
	

}
