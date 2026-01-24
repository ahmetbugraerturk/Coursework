package transaction;

import exception.InvalidLocationException;
import exception.InvalidParameterException;
import exception.InvalidTransactionException;
import peer.Peer;

public class Transaction {

	private Peer senderPeer;
    private Peer receiverPeer;
    private double energyAmount;
    private double price;

    public Transaction(Peer senderPeer, Peer receiverPeer, double energyAmount, double price) throws InvalidTransactionException, InvalidParameterException, InvalidLocationException {
    	if (energyAmount<0 || price<0)
    		throw new InvalidTransactionException("Transaction is invalid because of non-positive energy or price");
    	TransactionValidator.validateLocations(senderPeer.getLocation(), receiverPeer.getLocation());
    	this.senderPeer = senderPeer;
    	this.receiverPeer = receiverPeer;
    	this.energyAmount = energyAmount;
    	this.price = price;
    }

	public Peer getSenderPeer() {
		return senderPeer;
	}

	public Peer getReceiverPeer() {
		return receiverPeer;
	}

	public double getEnergyAmount() {
		return energyAmount;
	}

	public double getPrice() {
		return price;
	}
    
}
