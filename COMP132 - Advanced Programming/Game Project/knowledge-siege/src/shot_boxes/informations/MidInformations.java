package shot_boxes.informations;

import javax.swing.Timer;

import knowledge_keepers.KnowledgeKeepers;
import shot_boxes.ShotBoxes;

/**
 * Represents a medium-level information box in the game.
 * 
 * <p>{@code MidInformations} objects fall from the top of the screen and provide
 * moderately challenging knowledge to the player. They reward a mid-tier number
 * of points upon collection.</p>
 *
 * <p>This class is responsible for initiating and handling the downward
 * movement of the information box, interaction handling, and GUI state updates.</p>
 *
 * @see Informations
 * @see ShotBoxes
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class MidInformations extends Informations implements ShotBoxes {
	
	/**
     * Constructs a {@code MidInformations} object with the given info text and associated point value.
     *
     * @param info  the informational content to display
     * @param point the number of points awarded upon successful interaction
     */
	public MidInformations(String info, int point) {
		this.info = info;
		this.point = point;
	}

	/**
     * Begins the downward movement of the information box from the specified X-coordinate.
     * <p>The box moves downward at medium speed until it either reaches the bottom
     * of the screen (Y ≥ 500) or is interacted with. Upon reaching the bottom,
     * it is reset and deactivated.</p>
     *
     * @param X the horizontal coordinate from which the info box starts falling
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
					Y += speeds[1];}
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
