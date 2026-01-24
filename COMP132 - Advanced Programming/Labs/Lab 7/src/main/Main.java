/* *********** Pledge of Honor ************************************************ *

I hereby certify that I have completed this lab assignment on my own
without any help from anyone else. I understand that the only sources of authorized
information in this lab assignment are (1) the course textbook, (2) the
materials posted on the course website, and (3) any study notes handwritten by myself.
I have not used, accessed, or received any information from any other unauthorized
source in taking this lab assignment. The effort in the assignment thus belongs
completely to me.
READ AND SIGN BY WRITING YOUR NAME SURNAME, AND STUDENT ID
SIGNATURE: <Ahmet Buğra Ertürk, 86877>
********************************************************************************/
package main;

import peerwatt_sariyer.*;
import peer.Peer;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        HashMap<String, Peer> peers = new HashMap<>();
        PeerWattSariyer system = new PeerWattSariyer(peers);
        System.out.println("Reading data...");
        InputHandler.processInputFile(system, "peers.txt");
        System.out.println("===================================");
        System.out.println("Started trading...");
        system.trade(1.5);
        System.out.println("===================================");
        System.out.println("Printing transactions...");
        system.printAllTransactions();
        
        System.out.println("\n------------- Inlab Output --------------");
        String filename = "PeerEnergySummary.txt";
        System.out.println("\n------------- InLab - Task 1 ------------- ");
        System.out.println("Printing Peer Energy Summary...");
        system.printPeerEnergySummary(filename);
        System.out.println("\n------------- InLab - Task 2 ------------- ");
        String consumersData = system.getConsumersInfo(filename);
        System.out.println(consumersData);
    }
}
