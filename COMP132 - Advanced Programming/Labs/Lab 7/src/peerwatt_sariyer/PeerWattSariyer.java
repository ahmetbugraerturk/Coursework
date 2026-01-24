package peerwatt_sariyer;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Formatter;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

import exception.InvalidLocationException;
import exception.InvalidParameterException;
import exception.InvalidPeerException;
import exception.InvalidTransactionException;
import transaction.Transaction;
import transaction.TransactionValidator;
import peer.Peer;
import peer.PeerValidator;

public class PeerWattSariyer {
	
    private double totalP2PTransactedEnergy;
    private HashMap<String, Peer> peers;
    private ArrayList<Transaction> transactions;

    public PeerWattSariyer(HashMap<String, Peer> peers) {
        if (peers == null)
            this.peers = new HashMap<>();
        else
            this.peers = peers;
        transactions = new ArrayList<>();
    }

    public void addPeer(Peer peer) throws InvalidPeerException {
    	PeerValidator.validate(peer);
    	peers.put(peer.getPeerID(), peer);
    	System.out.printf("Peer %s added successfully%n", peer.getPeerID());
    }

    private List<Peer> getSellers() {
        List<Peer> sellers = new ArrayList<>();
        for (Peer p: peers.values()) {
        	if (p.getExcessEnergy()>0)
        		sellers.add(p);
        }
        return sellers;
    }

    private List<Peer> getBuyers() {
    	List<Peer> buyers = new ArrayList<>();
        for (Peer p: peers.values()) {
        	if (p.getExcessEnergy()<0)
        		buyers.add(p);
        }
        return buyers;
    }

    public void trade(double price){
    	List<Peer> sellers = getSellers();
        List<Peer> buyers = getBuyers();
    	
        for (Peer b: buyers) {
        	for (Peer s: sellers) {
        		double tradeAmount = Math.min(Math.abs(s.getExcessEnergy()), Math.abs(b.getExcessEnergy()));
        		if (b.getBalance()<tradeAmount*price||tradeAmount<=0)
        			continue;
        		try {
					TransactionValidator.validateLocations(s.getLocation(), b.getLocation());
					s.sellEnergy(tradeAmount, price);
	                b.buyEnergy(tradeAmount, price);
	                Transaction transaction = new Transaction(s, b, tradeAmount, price);
	                transactions.add(transaction);
	                
	                totalP2PTransactedEnergy += tradeAmount;
				} catch (InvalidParameterException | InvalidTransactionException | InvalidLocationException e) {
					System.err.println(e.getMessage());
				}
        		
            }
        }
        System.out.printf("Trading ended. Total transacted energy amount is %.1f kWh%n", totalP2PTransactedEnergy);

    }
    
    private double getTotalBoughtEnergy(String peerID) {
    	double total = 0;
    	for (Transaction t: transactions) {
    		if (t.getReceiverPeer().getPeerID().equals(peerID))
    			total += t.getEnergyAmount();
    	}
    	return total;
    }
    
    private double getTotalSoldEnergy(String peerID) {
    	double total = 0;
    	for (Transaction t: transactions) {
    		if (t.getSenderPeer().getPeerID().equals(peerID))
    			total += t.getEnergyAmount();
    	}
    	return total;
    }

    public void printAllTransactions() {
    	for (Transaction transaction : transactions) {
            System.out.println("Receiver ID: " + transaction.getReceiverPeer().getPeerID());
            System.out.println("Sender ID: " + transaction.getSenderPeer().getPeerID());
            System.out.printf("Energy Traded: %.1f kWh%n", transaction.getEnergyAmount());
            System.out.printf("Price per kWh: %.1f%n", transaction.getPrice());
            System.out.printf("Total: %.1f%n", transaction.getPrice()*transaction.getEnergyAmount());
            System.out.println("-------------------------------------------");
        }
    }
    
    public void printPeerEnergySummary(String filename) {
    	try (Formatter f = new Formatter(filename)) {
			for (Peer p: peers.values()) {
				System.out.printf("Peer ID: %s | Generated: %.1f | Needed: %.1f | Excess: %.1f | Balance: %.1f%s%s%n", p.getPeerID(), p.getGeneratedEnergy(), p.getNeededEnergy(), p.getExcessEnergy(), p.getBalance(), getTotalSoldEnergy(p.getPeerID()) !=0 ? String.format(" | Sold: %.1f kWh", getTotalSoldEnergy(p.getPeerID())) : "", getTotalBoughtEnergy(p.getPeerID()) !=0 ? String.format(" | Bought: %.1f kWh", getTotalBoughtEnergy(p.getPeerID())) : "");
				f.format("Peer ID: %s | Generated: %.1f | Needed: %.1f | Excess: %.1f | Balance: %.1f%s%s%n", p.getPeerID(), p.getGeneratedEnergy(), p.getNeededEnergy(), p.getExcessEnergy(), p.getBalance(), getTotalSoldEnergy(p.getPeerID()) !=0 ? String.format(" | Sold: %.1f kWh", getTotalSoldEnergy(p.getPeerID())) : "", getTotalBoughtEnergy(p.getPeerID()) !=0 ? String.format(" | Bought: %.1f kWh", getTotalBoughtEnergy(p.getPeerID())) : "");
			}
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
    }
    
    public String getConsumersInfo(String filename) {
    	double total = 0;
		String ids = "";
    	try (Scanner s = new Scanner(Paths.get(filename))){
    		while (s.hasNextLine()) {
				String line = s.nextLine();
    			if (line.contains("Bought")) {
	    			ids += line.substring(line.indexOf("Peer ID: ")+9, line.indexOf("Peer ID: ")+15)+", ";
					total += Double.parseDouble(line.substring(line.indexOf("Bought: ")+8, line.indexOf("kWh")-1));
    			}
    		}
    	} catch (IOException | NumberFormatException e) {
			System.err.println(e.getMessage());
		}
		ids = ids.substring(0, ids.length()-2).trim();
    	return String.format("Consumer(s): %s. Total Bought Energy: %.1f kWh%n", ids, total);
    }
	

}
