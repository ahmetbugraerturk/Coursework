package main;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.Scanner;

import exception.InvalidLocationException;
import exception.InvalidParameterException;
import exception.InvalidPeerException;
import location.Location;
import peer.Peer;
import peerwatt_sariyer.PeerWattSariyer;

public class InputHandler {
	
	public static void processInputFile(PeerWattSariyer peerWattSariyer, String filePath) {
		try(Scanner s = new Scanner(Paths.get("./peers.txt"))) {
			while (s.hasNextLine()) {
				String line = s.nextLine();
				String[] items = line.split(" "); 
				if (items.length==6) {
					try {
						peerWattSariyer.addPeer(new Peer(items[0], Integer.parseInt(items[1]), Integer.parseInt(items[2]), Integer.parseInt(items[3]), new Location(Double.parseDouble(items[4]), Double.parseDouble(items[5]))));
					} catch (InvalidLocationException | InvalidPeerException | InvalidParameterException e) {
						System.err.println(e.getMessage());
					}
				} else
					System.out.println("Invalid file entry");
				
			}
		} catch (IOException | NumberFormatException e) {
			System.err.println(e.getMessage());
		}
	}
	
}
