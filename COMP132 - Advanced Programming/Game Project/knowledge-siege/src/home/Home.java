package home;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.JTable;

import game.GameGUI;
import game.Level1;
import game.Level2;
import game.Level3;
import main.MainGUI;
import player.Player;

/**
 * Manages the current player instance and controls transitions between different
 * game levels.
 * <p>
 * Scoreboard data is read from a text file and presented in a JTable inside a JOptionPane.
 * 
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class Home {
	
	private static Player player;
	public static GameGUI currentGameGUI;
	
	private static List<String[]> scores = new ArrayList<>();
	
	/**
	 * Sets the current player by username.
	 * 
	 * @param username the username of the player
	 */
	public static void setPlayer(String username) {
		player = new Player(username);
	}
	
	/**
	 * Returns the current player instance.
	 * 
	 * @return current {@link Player}
	 */
	public static Player getPlayer() {
		return player;
	}
	
	/**
	 * Resets the current player to null.
	 */
	public static void resetPlayer() {
		player = null;
	}
	
	/**
	 * Starts level 1 game and switches the main frame to level 1 screen.
	 */
	public static void level1() {
		new Level1(MainGUI.level1GUI);
		currentGameGUI = MainGUI.level1GUI;
		MainGUI.switchScreen("level1");
	}
	
	/**
	 * Starts level 2 game and switches the main frame to level 2 screen.
	 */
	public static void level2() {
		new Level2(MainGUI.level2GUI);
		currentGameGUI = MainGUI.level2GUI;
		MainGUI.switchScreen("level2");
	}
	
	/**
	 * Starts level 3 game and switches the main frame to level 3 screen.
	 */
	public static void level3() {
		new Level3(MainGUI.level3GUI);
		currentGameGUI = MainGUI.level3GUI;
		MainGUI.switchScreen("level3");
	}
	
	/**
	 * Reads the scores from the scores.txt file.
	 * Scores are sorted primarily by score descending, then by name ascending,
	 * and finally by game number ascending.
	 */
	private static void readScores() {
		scores.clear();
		File scoresFile = new File("src/users/scores.txt");
		try (BufferedReader reader = new BufferedReader(new FileReader(scoresFile))){
			String line;
			while ((line = reader.readLine()) != null) {
				if (line.trim().isEmpty()) {
			        continue;
			    }
				scores.add(new String[] {line.trim().split(",")[1], line.trim().split(",")[0], line.trim().split(",")[2]});
			}
			scores.sort((a, b) -> {
			    int scoreA = Integer.parseInt(a[1]);
			    int scoreB = Integer.parseInt(b[1]);

			    if (scoreA != scoreB) {
			        return Integer.compare(scoreB, scoreA);
			    }

			    int nameCompare = a[0].compareTo(b[0]);
			    if (nameCompare != 0) {
			        return nameCompare;
			    }

			    int gameNumA = Integer.parseInt(a[2]);
			    int gameNumB = Integer.parseInt(b[2]);
			    return Integer.compare(gameNumA, gameNumB);
			});
		} catch (IOException e1) {
			e1.printStackTrace();
		}
	}
	
	/**
	 * Displays the scoreboard dialog with sorted scores.
	 */
	public static void showScoreboard() {
		readScores();
		String[] columns = {"Name", "Score", "Game"};

		JTable table = new JTable(scores.toArray(new String[0][]), columns);
		JScrollPane scrollPane = new JScrollPane(table);

		JOptionPane.showMessageDialog(null, scrollPane, "Scoreboard", JOptionPane.PLAIN_MESSAGE);
	}
}
