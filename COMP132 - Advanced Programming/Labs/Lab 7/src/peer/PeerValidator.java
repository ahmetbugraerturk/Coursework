package peer;

import exception.InvalidPeerException;

public class PeerValidator {
	
	public static void validatePeerID(String peerID) throws InvalidPeerException {
		if (peerID.length()!=6)
			throw new InvalidPeerException("Peer is invalid because the ID length must be 6.");
	}
	
	public static void validate(Peer peer) throws InvalidPeerException {
		if (peer == null)
			throw new InvalidPeerException("Peer is null");
		validatePeerID(peer.getPeerID());
	}

}
