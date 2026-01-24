package knowledge_keepers;

import java.awt.Graphics;
import java.awt.Image;
import java.io.File;
import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.List;

import javax.swing.ImageIcon;
import javax.swing.Timer;

import shot_boxes.informations.Informations;
import shot_boxes.questions.Questions;

/**
 * Abstract class representing Knowledge Keepers in the game,
 * such as SLs, TAs, and Professors.
 * <p>
 * Maintains static lists of all instances by their actual types and
 * provides common properties like name, image, position, assigned questions and information,
 * and timers for movement and attacks.
 * 
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public abstract class KnowledgeKeepers {
	
	private static List<KnowledgeKeepers> SLs = new ArrayList<>();
	private static List<KnowledgeKeepers> TAs = new ArrayList<>();
	private static List<KnowledgeKeepers> professors = new ArrayList<>();
	
	protected static final double[] chanceOfInfo = {.6, .5, .25};
	protected static final int[] speeds = {3, 4, 5};
		
	protected String name;
	protected File imgFile;
	private Image img;
	protected int X = 280; 
    protected int playerX = 280;
    
    protected Informations info;
    protected Questions quest;
    
    public boolean hasQuestion = false;
    public boolean hasInfo = false;

    protected List<Informations> infos;
    protected List<Questions> quests;
	
    protected final SecureRandom random = new SecureRandom();
    
    protected Timer moveTimer;
    protected Timer directionTimer;
    protected Timer attackTimer;
	
    /**
	 * Constructs a KnowledgeKeeper with the given name and image file.
	 * Adds the instance to the appropriate static list based on its subclass.
	 * 
	 * @param name the name of the KnowledgeKeeper
	 * @param img the image file representing this KnowledgeKeeper
	 */
	KnowledgeKeepers(String name, File imgFile) {
		this.name = name;
		this.imgFile = imgFile;
		this.img = new ImageIcon(imgFile.getAbsolutePath()).getImage().getScaledInstance(30, 30, Image.SCALE_SMOOTH);
		if (this instanceof SL)
			SLs.add(this);
		else if (this instanceof TA)
			TAs.add(this);
		else
			professors.add(this);
	}
	
	/**
	 * Draws the image on the GameGUI
	 * 
	 * @param keeperImage the body image of the keepers
	 * @param g the Graphics object
	 */
	public void draw(Image keeperImage, Graphics g) {
		g.drawImage(keeperImage, getCoordinate()[0], 0, null);
		g.drawImage(img, getCoordinate()[1], 0, null);
	}
	
	/**
	 * Attacks by shooting a question if there is no active question on the current game GUI.
	 * Selects a random question and starts its movement from the current X position.
	 */
	public void attackQuestion() {
		if (!hasQuestion) {
			do {
				quest = quests.get(random.nextInt(quests.size()));
			} while (quest.isMoving);
			quest.move(this, X);
		}
	}

	/**
	 * Attacks by shooting information if there is no active information on the current game GUI.
	 * Selects a random information and starts its movement from the current X position.
	 */
	public void attackInfo() {
		if (!hasInfo) {
			do {
				info = infos.get(random.nextInt(infos.size()));
			} while (info.isMoving);
			info.move(this, X);
		}
	}
	
	/**
	 * Returns the list of all SL instances.
	 * @return list of SLs
	 */
	public static List<KnowledgeKeepers> getSLs() {
		return SLs;
	}

	/**
	 * Returns the list of all TA instances.
	 * @return list of TAs
	 */
	public static List<KnowledgeKeepers> getTAs() {
		return TAs;
	}

	/**
	 * Returns the list of all Professor instances.
	 * @return list of Professors
	 */
	public static List<KnowledgeKeepers> getProfessors() {
		return professors;
	}
	
	/**
	 * Returns the name of this KnowledgeKeeper.
	 * 
	 * @return the name
	 */
	public String getName() {
		return name;
	}
	
	/**
	 * Returns the X coordinates of the body and the head images.
	 * The first element is the body image X coordinate,
	 * the second element is the head image X coordinate.
	 *
	 * @return an int array containing {bodyX, headX}
	 */
	public int[] getCoordinate() {
		int[] i = {X, X+5};
		return i;
	}
	
	/**
	 * Returns the current Informations object assigned to this KnowledgeKeeper.
	 * 
	 * @return the Informations object
	 */
	public Informations getInfo() {
		return info;
	}
	
	/**
	 * Returns the current Questions object assigned to this KnowledgeKeeper.
	 * 
	 * @return the Questions object
	 */
	public Questions getQuest() {
		return quest;
	}
	
	/**
	 * Sets the Informations object for this KnowledgeKeeper.
	 * 
	 * @param info the Informations object to set
	 */
	public void setInfo(Informations info) {
		this.info = info;
	}

	/**
	 * Sets the Questions object for this KnowledgeKeeper.
	 * 
	 * @param quest the Questions object to set
	 */
	public void setQuest(Questions quest) {
		this.quest = quest;
	}

	/**
	 * Sets the player's X coordinate.
	 * 
	 * @param playerX the player's X coordinate to set
	 */
	public void setPlayerX(int playerX) {
		this.playerX = playerX;
	}
	
	/**
	 * Stops all timers related to movement and attacks, and 
	 * clears any active Informations and Questions.
	 */
	public void resetTimers() {
        moveTimer.stop();
        attackTimer.stop();
        info = null;
        quest = null;

	}
	
	/**
	 * Moves the KnowledgeKeeper.
	 */
	public abstract void move();
	
	/**
	 * Updates the movement direction of the KnowledgeKeeper.
	 */
	public abstract void movementDirection();
	
	/**
	 * Starts attack action.
	 */
	public abstract void startAttack();
	
}
