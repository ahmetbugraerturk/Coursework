package game;

import java.util.Random;

public class GalacticChallenge {
	
	Player player1;
	Player player2;
	int numRounds;
	int scoreDif;
	int ties = 0;
	static final Random RAND = new Random(2025);
	
	public GalacticChallenge(String name1, String name2, int numRounds) {
		player1 = new Player(name1);
		player2 = new Player(name2);
		this.numRounds = numRounds;
	}
	
	public GalacticChallenge(String name1, String name2, int numRounds, int scoreDif) {
		player1 = new Player(name1);
		player2 = new Player(name2);
		this.numRounds = numRounds;
		this.scoreDif = scoreDif;
	}
	
	private String getRandomChoice() {
		switch (RAND.nextInt(5)){
		case 0: {
			return "Fighter";
		}
		case 1: {
			return "Bomber";
		}
		case 2: {
			return "Interceptor";
		}
		case 3: {
			return "Battleship";
		}
		case 4: {
			return "Destroyer";
		}
		default:
			return null;
		}
	}
	
	private String determineWinner(String choice1, String choice2) {
		if (choice1 == choice2) {
			return "tie";
		} else if (choice1 == "Fighter") {
			if (choice2 == "Battleship") {
				return "Battleship";
			} else if (choice2 == "Destroyer") {
				return "Destroyer";
			} else {
				return "Fighter";
			}
		} else if (choice1 == "Bomber") {
			if (choice2 == "Fighter") {
				return "Fighter";
			} else if (choice2 == "Destroyer") {
				return "Destroyer";
			} else {
				return "Bomber";
			}
		} else if (choice1 == "Interceptor") {
			if (choice2 == "Fighter") {
				return "Fighter";
			} else if (choice2 == "Bomber") {
				return "Bomber";
			} else if (choice2 == "Destroyer") {
				return "Destroyer";
			} else {
				return "Interceptor";
			}
		} else if (choice1 == "Battleship") {
			if (choice2 == "Bomber") {
				return "Bomber";
			} else if (choice2 == "Interceptor") {
				return "Interceptor";
			} else {
				return "Battleship";
			}
		} else if (choice1 == "Destroyer") {
			if (choice2 == "Battleship") {
				return "Battleship";
			} else {
				return "Destroyer";
			}
		} else {
			return null;
		}
	}
	
	public void printWinner() {
		System.out.printf("%s won %d rounds%n", player1.getName(), player1.getRoundsWon());
		System.out.printf("%s won %d rounds%n", player2.getName(), player2.getRoundsWon());
		if (player1.getRoundsWon()>player2.getRoundsWon()) {
			System.out.printf("%s is the overall winner!%n", player1.getName());
		} else if (player2.getRoundsWon()>player1.getRoundsWon()) {
			System.out.printf("%s is the overall winner!%n", player2.getName());
		} else {
			System.out.println("There is no winner, the game is tied.");
		}
		if (ties == 0) {
			System.out.println("There is no tie.");
		} else if (ties == 1) {
			System.out.println("There is 1 tie.");
		} else {
			System.out.printf("There are %d ties." , ties);
		}
	}
	
	public void runGame() {
		for (int i = 0; i<numRounds; i++) {
			String c1 = getRandomChoice();
			String c2 = getRandomChoice();
			String w = determineWinner(c1, c2);
			String res;
			if (w==c1) {
				player1.wonRound();
				res = player1.getName() + " wins!";
			} else if (w==c2) {
				player2.wonRound();
				res = player2.getName() + " wins!";
			} else {
				ties++;
				res = "It's a tie!";
			}
			System.out.printf("Round %d%n", i+1);
			System.out.printf("%s chose %s%n", player1.getName(), c1);
			System.out.printf("%s chose %s%n", player2.getName(), c2);
			System.out.printf("Result: %s%n%n", res);
		}
		System.out.println("Game Over!");
	}
	
	public void inLabRun() {
		int score1 = 0;
		int score2 = 0;
		for (int i = 0; i<numRounds; i++) {
			String c1 = getRandomChoice();
			String c2 = getRandomChoice();
			String w = determineWinner(c1, c2);
			String res;
			if (w==c1) {
				player1.wonRound();
				score1++;
				res = player1.getName() + " wins!";
			} else if (w==c2) {
				player2.wonRound();
				score2++;
				res = player2.getName() + " wins!";
			} else {
				ties++;
				score1++;
				score2++;
				res = "It's a tie!";
			}
			System.out.printf("Round %d%n", i+1);
			System.out.printf("%s chose %s%n", player1.getName(), c1);
			System.out.printf("%s chose %s%n", player2.getName(), c2);
			System.out.printf("Result: %s%n", res);
			System.out.printf("%s's score is: %d%n", player1.getName(), score1);
			System.out.printf("%s's score is: %d%n", player2.getName(), score2);
			System.out.printf("The difference is: %d%n%n", Math.abs(score1-score2));
			if (Math.abs(player1.roundsWon-player2.roundsWon)==scoreDif) {
				System.out.printf("The game is finished with %d rounds.%n%n", i+1);
				break;
			}
		}
		System.out.println("Game Over!");
	}

}
