package game;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.security.SecureRandom;
import java.util.ArrayList;

import javax.swing.JOptionPane;
import javax.swing.Timer;

import home.Home;
import knowledge_keepers.KnowledgeKeepers;
import main.MainGUI;
import shot_boxes.ShotBoxes;
import shot_boxes.informations.Informations;
import shot_boxes.questions.Questions;

/**
 * Handles the main game logic and player interactions.
 * <p>
 * Manages player movement, interactions with game objects, and level progression.
 *
 * @see GameGUI
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class Game {
	
	private GameGUI gameGUI;
	
    private final int STEP = 4;  
    private Timer moveTimer;
    
    protected static final SecureRandom random = new SecureRandom();
    
    private static int[] previousScores = new int[2];

    /**
     * Constructs a new Game instance associated with the given GameGUI.
     * <p>
     * Initializes player movement timer.
     * 
     * @param gameGUI the GameGUI instance that is the UI of this game
     * 
     * @author Ahmet Buğra Ertürk
     * @version 1.0
     */
	public Game(GameGUI gameGUI) {
		this.gameGUI = gameGUI;
		
		gameGUI.game = this;
		
		moveTimer = new Timer(15, e -> movePlayer());
        moveTimer.start();

	}
	
	/**
	 * Moves the player left or right.
	 */
	private void movePlayer() {
		if (gameGUI.movingLeft) {
        	if (gameGUI.playerX<=0) 
        		gameGUI.movingLeft = false;
        	else {
        		gameGUI.playerImage = gameGUI.playerImages[1];
        		gameGUI.playerX -= STEP;
        		gameGUI.faceX = gameGUI.playerX+15;
        	}
        }
        if (gameGUI.movingRight) {
        	if (gameGUI.playerX>=496) 
        		gameGUI.movingRight = false;
        	else {
        		gameGUI.playerImage = gameGUI.playerImages[2];
        		gameGUI.playerX += STEP;
        		gameGUI.faceX = gameGUI.playerX+20;
        	}
        }
        gameGUI.repaint();
    }
	
	/**
	 * Adds a KnowledgeKeeper to the game.
	 *
	 * @param keeper the KnowledgeKeeper to add
	 */
	public void addKeeper(KnowledgeKeepers keeper) {
		gameGUI.keepers.add(keeper);
	}
	
	/**
	 * Resets the game objects and stops timers.
	 */
	public void reset() {
		Home.getPlayer().resetScoreHealth();
		for (KnowledgeKeepers k: gameGUI.keepers) {
			if (k.getInfo()!=null)
				k.getInfo().interact(k);
			if (k.getQuest()!=null)
				k.getQuest().interact(k);
			k.resetTimers();
		}
		moveTimer.stop();
		gameGUI.keepers = new ArrayList<>();
	}
	
	/**
	 * Records the player's score to a file.
	 *
	 * @param score the score to record
	 * @param gameNum the current game number
	 */
	private void recordScore(int score, int gameNum) {
		File scoresFile = new File("src/users/scores.txt");
		try (BufferedWriter writer = new BufferedWriter(new FileWriter(scoresFile, true))) {
			writer.write(score+","+Home.getPlayer().getUsername()+","+gameNum);
			writer.newLine();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
	}
	
	/**
	 * Ends the game when the player leaves.
	 */
	public void gameDone() {
		Home.getPlayer().log("The player left the game", true);
		reset();
		previousScores = new int[2];
		MainGUI.switchScreen("home");	
		gameGUI.setVisible(false);
		gameGUI.revalidate();
		gameGUI.repaint();
		MainGUI.homeGUI.revalidate();
		MainGUI.homeGUI.repaint();
	}
	
	/**
	 * Ends the game and shows a message based on win/loss status.
	 *
	 * @param status true if game completed successfully, false if lost
	 */
	private void gameDone(boolean status) {
		if (status)
			Home.getPlayer().log(String.format("The game is succesfully done with total score %d", previousScores[0]+previousScores[1]+Home.getPlayer().getScore()), true);
		else
			Home.getPlayer().log(String.format("The game is over with the total score %d", previousScores[0]+previousScores[1]+Home.getPlayer().getScore(), Home.getPlayer().getGameNum()), true);
		Home.getPlayer().updateGameNum();
		recordScore(previousScores[0]+previousScores[1]+Home.getPlayer().getScore(), Home.getPlayer().getGameNum());
		reset();
		if (status)
			JOptionPane.showMessageDialog(null,
	                "Game done.",
	                "Victory",
	                JOptionPane.INFORMATION_MESSAGE);
		else
			JOptionPane.showMessageDialog(null,
	                "Game over",
	                "Game over",
	                JOptionPane.INFORMATION_MESSAGE);
		previousScores = new int[2];
		MainGUI.switchScreen("home");	
		gameGUI.setVisible(false);
		gameGUI.revalidate();
		gameGUI.repaint();
		MainGUI.homeGUI.revalidate();
		MainGUI.homeGUI.repaint();
	}
	
	/**
	 * Checks for interaction between player and shot boxes,
	 * updates score and health, and handles level progression.
	 *
	 * @param keeper the KnowledgeKeeper involved
	 * @param shotBox the shot box to check interaction with
	 */
	public void checkInteraction(KnowledgeKeepers keeper, ShotBoxes shotBox) {
		if (shotBox.getCoordinate()[1]>=500) {
			if (shotBox instanceof Questions)
				keeper.setQuest(null);
			if (shotBox instanceof Informations)
				keeper.setInfo(null);
		}
		else if ((shotBox.getCoordinate()[1]+25 > gameGUI.playerY) && shotBox.getCoordinate()[0]+25 > gameGUI.playerX && shotBox.getCoordinate()[0] < gameGUI.playerX+40) {
			shotBox.interact(keeper);
			Home.getPlayer().interact(shotBox);
			if (shotBox instanceof Questions) {
				gameGUI.QuestionLbl.setText(keeper.getName() + ": " + ((Questions) shotBox).getQuest());
				keeper.setQuest(null);
			}
			if (shotBox instanceof Informations) {
				gameGUI.InformationLbl.setText(keeper.getName() + ": " + ((Informations) shotBox).getInfo());
				keeper.setInfo(null);
			}
			gameGUI.healthBar.setValue(Home.getPlayer().getHealth());
			gameGUI.ScoreLbl.setText(String.format("%04d", Home.getPlayer().getScore()));
		}
		checkStatus();
	}
	
	/**
	 * Checks the requirement to level transitions or
	 * game over status.
	 */
	private void checkStatus() {
		if (Home.getPlayer().getHealth()<=0) {
			gameDone(false);
		}
		if (Home.getPlayer().getScore()>=50 && this instanceof Level1) {
			previousScores[0]=Home.getPlayer().getScore();
			reset();
			JOptionPane.showMessageDialog(null,
                    "Level 1 done. Play level 2",
                    "Succesful",
                    JOptionPane.INFORMATION_MESSAGE);
			Home.level2();
		} if (Home.getPlayer().getScore()>=100 && this instanceof Level2) {
			previousScores[1]=Home.getPlayer().getScore();
			reset();
			JOptionPane.showMessageDialog(null,
                    "Level 2 done. Play level 3",
                    "Succesful",
                    JOptionPane.INFORMATION_MESSAGE);
			Home.level3();
		} if (Home.getPlayer().getScore()>=150 && this instanceof Level3) {
			gameDone(true);
		}
	}
	
}
