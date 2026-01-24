package game;

public class Player {
	
	int roundsWon = 0;
	String playerName;
	
	public Player(String name) {
		playerName = name;
	}
	
	public void wonRound() {
		roundsWon++;
	}
	
	public int getRoundsWon() {
		return roundsWon;
	}
	
	public String getName() {
		return playerName;
	}

}
