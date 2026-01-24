package peer;

import java.util.ArrayList;
import java.util.List;

import exception.InvalidParameterException;
import exception.InvalidPeerException;
import location.Location;

public class Peer {
	
	private String peerID;
    private double balance;
    private double generatedEnergy;
    private double neededEnergy;
    private double excessEnergy;
    private Location location;
    private static List<String> peersIDs = new ArrayList<>();
    
    public Peer(String peerID, double balance, double generatedEnergy, double neededEnergy, Location location) throws InvalidPeerException, InvalidParameterException {
    	PeerValidator.validatePeerID(peerID);
    	if (peersIDs.contains(peerID))
    		throw new InvalidPeerException("Peer ID already exists.");
    	if (location==null)
    		throw new InvalidPeerException("Location cannot be null.");
    	if (balance<0)
    		throw new InvalidParameterException("Balance cannot be negative.");
    	if (generatedEnergy<0)
    		throw new InvalidParameterException("Generated energy cannot be negative.");
    	if (neededEnergy<0)
    		throw new InvalidParameterException("Needen energy cannot be negative.");
    	this.peerID = peerID;
    	this.balance = balance;
    	this.generatedEnergy = generatedEnergy;
    	this.neededEnergy = neededEnergy;
    	this.location = location;
    	peersIDs.add(peerID);
    	setExcessEnergy();
    }
    
    public void buyEnergy(double amount, double price) throws InvalidParameterException {
    	if (price<=0 || amount <= 0)
    		throw new InvalidParameterException("Amount and price must be non-negative.");
    	if (price*amount>balance)
    		throw new InvalidParameterException("Not enough balance.");
        balance -= amount * price;
        neededEnergy -= amount;
        setExcessEnergy();
    }

	public void sellEnergy(double amount, double price) throws InvalidParameterException {
    	if (price<=0 || amount <= 0)
    		throw new InvalidParameterException("Amount and price must be non-negative.");
    	if (amount > excessEnergy)
    		throw new InvalidParameterException("Not enough excess energy.");
    	balance += amount * price;
        generatedEnergy -= amount;
        setExcessEnergy();
    }
    
    public double getGeneratedEnergy() {
		return generatedEnergy;
	}

	public void setGeneratedEnergy(double generatedEnergy) throws InvalidParameterException {
		if (generatedEnergy<0)
    		throw new InvalidParameterException("Generated energy cannot be negative.");
		this.generatedEnergy = generatedEnergy;
		setExcessEnergy();
	}

	public double getNeededEnergy() {
		return neededEnergy;
	}

	public void setNeededEnergy(double neededEnergy) throws InvalidParameterException {
		if (neededEnergy<0)
    		throw new InvalidParameterException("Needen energy cannot be negative.");
		this.neededEnergy = neededEnergy;
		setExcessEnergy();
	}

	public double getExcessEnergy() {
		return excessEnergy;
	}

	private void setExcessEnergy() {
		excessEnergy = generatedEnergy-neededEnergy;
	}

	public Location getLocation() {
		return location;
	}
	
    public double getBalance() {
		return balance;
	}

	public void setBalance(double balance) throws InvalidParameterException {
		if (balance<0)
    		throw new InvalidParameterException("Balance cannot be negative.");
		this.balance = balance;
	}

	public String getPeerID() {
    	return peerID;
    }
    
}
