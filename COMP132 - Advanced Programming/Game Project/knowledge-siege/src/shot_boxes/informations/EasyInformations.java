package shot_boxes.informations;

import javax.swing.Timer;

import knowledge_keepers.KnowledgeKeepers;
import shot_boxes.ShotBoxes;

/**
 * Represents an easy-level information object in the game.
 * 
 * <p>EasyInformations are falling info boxes that provide low-level knowledge
 * and award basic points to the player upon interaction.</p>
 * 
 * <p>This class controls the movement of the info box, handles interactions,
 * and sets relevant flags in the game GUI.</p>
 * 
 * @see Informations
 * @see ShotBoxes
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class EasyInformations extends Informations implements ShotBoxes {
	
	/**
     * Constructs a new {@code EasyInformations} object with the given info text and point value.
     *
     * @param info  the content or message of the information
     * @param point the point value awarded when the information is collected
     */
	public EasyInformations(String info, int point) {
		this.info = info;
		this.point = point;
	}

	/**
     * Initiates the downward movement of the information box from the given X-coordinate.
     * <p>The movement continues until the info reaches the bottom of the screen (Y ≥ 500),
     * after which it is reset and removed from the active state.</p>
     *
     * @param X the horizontal position from which to start moving the info box
     */
	@Override
	public void move(KnowledgeKeepers k, int X) {
		// TODO Auto-generated method stub
		if (!k.hasInfo) {
			k.hasInfo = true;
			isMoving = true;
			this.X = X;
			moveTimer = new Timer(25, e -> {
				if (Y<500) {
					Y += speeds[0];}
				else {
					k.hasInfo = false;
					isMoving = false;
					Y = 60;
					moveTimer.stop();
					}
				});
	        moveTimer.start();
		}
	}
	
}
