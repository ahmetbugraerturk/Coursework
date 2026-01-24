package shot_boxes.questions;

import java.awt.Graphics;
import java.awt.Image;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.swing.Timer;

import knowledge_keepers.KnowledgeKeepers;
import shot_boxes.ShotBoxes;

/**
 * The {@code Questions} abstract class represents question objects that fall during gameplay,
 * and can be interacted with by the player to loss health as penalty.
 * <p>
 * Subclasses determine the difficulty (Easy, Medium, Hard).
 *
 * @author 
 * @version 1.0
 */
public abstract class Questions implements ShotBoxes{
	private static List<Questions> easyQuestions = new ArrayList<>();
	private static List<Questions> midQuestions = new ArrayList<>();
	private static List<Questions> hardQuestions = new ArrayList<>();
	
	protected int X = 280;
    protected int Y = 60;
	protected String question;
	protected int point;
	
	public Timer moveTimer;
	public boolean isMoving = false;

	/**
	 * Loads iquestions from a text file. The file should be structured with difficulty
     * headers ("Easy", "Medium", "Hard") followed by lines of text question.
     * 
     * @param filePath the path to the file containing the question data
     */
	public static void uploudQuestions(String filePath) {
		File usersInfo = new File(filePath);
		
		try (BufferedReader reader = new BufferedReader(new FileReader(usersInfo))){
			String line;
			short currentStatus = 0;
			while ((line = reader.readLine()) != null) {
				if (line.equals("Easy")) {
					currentStatus = 0; 
					continue;
				}
				else if (line.equals("Medium")) {
					currentStatus = 1; 
					continue;
				}
				else if (line.equals("Hard")) {
					currentStatus = 2; 
					continue;
				}
				
				switch (currentStatus) {
					case 0:
						easyQuestions.add(new EasyQuestions(line, questionsPoints[currentStatus]));
						break;
					case 1:
						midQuestions.add(new MidQuestions(line, questionsPoints[currentStatus]));
						break;
					case 2:
						hardQuestions.add(new HardQuestions(line, questionsPoints[currentStatus]));
				}
			}
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
	}
	
	public void draw(Image image, Graphics g) {
		g.drawImage(image, getCoordinate()[0], getCoordinate()[1], null);
	}
	
	/**
     * Handles the logic when a player interacts with this question.
     *
     * <p>Stops the movement, resets the vertical position, and notifies the KnowledgeKeeper
     * that the question has been handled.</p>
     */
	@Override
	public void interact(KnowledgeKeepers k) {
		// TODO Auto-generated method stub
		k.hasQuestion=false;
		isMoving = false;
		Y = 60;
		moveTimer.stop();
	}

	/**
     * Returns the list of easy questions.
     *
     * @return a list containing {@code Questions} objects of easy difficulty
     */
	public static List<Questions> getEasyQuestions() {
		return easyQuestions;
	}

	/**
     * Returns the list of medium questions.
     *
     * @return a list containing {@code Questions} objects of medium difficulty
     */
	public static List<Questions> getMidQuestions() {
		return midQuestions;
	}

	/**
     * Returns the list of hard questions.
     *
     * @return a list containing {@code Questions} objects of hard difficulty
     */
	public static List<Questions> getHardQuestions() {
		return hardQuestions;
	}
	
	/**
     * Returns the current X and Y coordinates of the question.
     *
     * @return an array with two elements: X and Y position
     */
	public int[] getCoordinate() {
		int[] i = {X, Y};
		return i;
	}
	
	/**
     * Returns the question text.
     *
     * @return the question string
     */
	public String getQuest() {
		return question;
	}
	
	/**
     * Returns the point value associated with this question.
     *
     * @return the point value
     */
	public int getPoint() {
		return point;
	}
	
}
