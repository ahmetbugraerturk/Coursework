package shot_boxes.informations;

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
 * The {@code Informations} abstract class represents info boxes.
 * These objects fall from the top of the screen and can be collected by the player for points.
 * <p>
 * Subclasses determine the difficulty (Easy, Medium, Hard).
 * 
 * @author 
 * @version 1.0
 */
public abstract class Informations implements ShotBoxes{
	private static List<Informations> easyInformations = new ArrayList<>();
	private static List<Informations> midInformations = new ArrayList<>();
	private static List<Informations> hardInformations = new ArrayList<>();
	
    protected int X = 280;
    protected int Y = 60;
	protected String info;
	protected int point;
	
	public Timer moveTimer;
	public boolean isMoving = false;

	/**
     * Loads informational content from a text file. The file should be structured with difficulty
     * headers ("Easy", "Medium", "Hard") followed by lines of text information.
     *
     * @param filePath the path to the information file
     */
	public static void uploudInformations(String filePath) {
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
						easyInformations.add(new EasyInformations(line, infoPoints[currentStatus]));
						break;
					case 1:
						midInformations.add(new MidInformations(line, infoPoints[currentStatus]));
						break;
					case 2:
						hardInformations.add(new HardInformations(line, infoPoints[currentStatus]));
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
     * Handles interaction with the information box.
     * <p>Stops its movement, resets the vertical position (Y),
     * and updates the KnowledgeKeeper to indicate no active info object remains.</p>
     */
	@Override
	public void interact(KnowledgeKeepers k) {
		// TODO Auto-generated method stub
		k.hasInfo=false;
		isMoving = false;
		Y = 60;
		moveTimer.stop();
	}

	/**
     * Returns the list of easy informations.
     *
     * @return a list of easy information objects
     */
	public static List<Informations> getEasyInformations() {
		return easyInformations;
	}

	/**
     * Returns the list of medium informations.
     *
     * @return a list of medium information objects
     */
	public static List<Informations> getMidInformations() {
		return midInformations;
	}

	/**
     * Returns the list of hard informations.
     *
     * @return a list of hard information objects
     */
	public static List<Informations> getHardInformations() {
		return hardInformations;
	}
	
	/**
     * Returns the current coordinates of the item.
     *
     * @return an array with two elements: X and Y positions
     */
	public int[] getCoordinate() {
		int[] i = {X, Y};
		return i;
	}
	
	/**
     * Returns the information text.
     *
     * @return the info string
     */
	public String getInfo() {
		return info;
	}
	
	/**
     * Returns the point value of the information item.
     *
     * @return the point value
     */
	public int getPoint() {
		return point;
	}
	
}
