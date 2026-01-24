package player;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import shot_boxes.ShotBoxes;
import shot_boxes.informations.Informations;
import shot_boxes.questions.Questions;

/**
 * This class is responsible to manage player’s credentials
 */
public class Player {
	
	private String username;
	private File playerFolder;
	private File playerLog;
	private File playerIMG;
	private File gameNumFile;
	private int health = 100;
    private int score = 0;
    private int gameNum = 0;
	
    /**
     * The files that have been created in registration and updated while the game is being played are read and 
     * the data is assigned to corresponding instance variables
     * @param username
     */
	public Player(String username) {
		this.username = username;
		playerFolder = new File("src/users/"+username);
		playerLog = new File(playerFolder, username + ".log");
		gameNumFile = new File("src/users/"+username+"/gameNum.txt");
		String[] extensions = {"png", "jpg", "jpeg"};
		for (String ext : extensions) {
			playerIMG = new File(playerFolder, username + "." + ext);
		    if (playerIMG.exists())
		        break;
		}
		try (BufferedReader reader = new BufferedReader(new FileReader(gameNumFile))){
			gameNum = Integer.parseInt(reader.readLine());
		} catch (FileNotFoundException e) {
			
		} catch (IOException e) {
			
		}
	}
	
	/**
	 * Increase score or decrease health according to actual type of shotBox, and 
	 * the required line is written in the log file
	 * 
	 * @param shotBox the interacted ShotBoxes object
	 */
	public void interact(ShotBoxes shotBox) {
		if (shotBox instanceof Informations) {
			score += ((Informations) shotBox).getPoint();
			log(String.format("%d point collected, new score is %d", ((Informations) shotBox).getPoint(), score), false);
		} else {
			health -= ((Questions) shotBox).getPoint();
			log(String.format("%d damage taken, new health is %d", ((Questions) shotBox).getPoint(), health), false);
		}
	}
	
	/**
	 * Resets the health and score variables
	 */
	public void resetScoreHealth() {
		health = 100;
		score = 0;
	}
	
	public int getHealth() {
		return health;
	}

	public int getScore() {
		return score;
	}
	
	public File getPlayerLog() {
		return playerLog;
	}
	
	public File getPlayerIMG() {
		return playerIMG;
	}
	
	public File getGameNumFile() {
		return gameNumFile;
	}
	
	public String getUsername() {
		return username;
	}
	
	public int getGameNum() {
		return gameNum;
	}
	
	/**
	 * Updated the gameNum.txt file when a new play is done
	 */
	public void updateGameNum() {
		try (BufferedWriter writer = new BufferedWriter(new FileWriter(gameNumFile))) {
			writer.write(String.valueOf(++gameNum));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	/**
	 * Helps to write new lines in the log file
	 * 
	 * @param msg the line that will be written in the log file
	 * @param newLine a boolean that determine existency of an additional new line
	 */
	public void log(String msg, boolean newLine) {
		try (BufferedWriter logWriter = new BufferedWriter(new FileWriter(new File(playerFolder, username + ".log"), true))) {
		 	SimpleDateFormat dateFormat = new SimpleDateFormat("dd.MM.yyyy HH.mm.ss");
		    String currentTime = dateFormat.format(new Date());
		 	logWriter.write(msg + " at " + currentTime);
		 	logWriter.newLine();
		 	if (newLine)
		 		logWriter.newLine();
		} catch (IOException ex) {
		}
	}

}
