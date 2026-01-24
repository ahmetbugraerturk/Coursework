package shot_boxes.informations;

import javax.swing.Timer;

import knowledge_keepers.KnowledgeKeepers;
import shot_boxes.ShotBoxes;

/**
 * Represents a hard-level information box in the game.
 *
 * <p>{@code HardInformations} objects are spawned by high-level knowledge keepers
 * and provide the most challenging knowledge to the player. They offer the
 * highest point reward among information boxes.</p>
 *
 * <p>This class manages its own movement and interaction logic,
 * updating the game state upon completion.</p>
 *
 * @see Informations
 * @see ShotBoxes
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class HardInformations extends Informations implements ShotBoxes {
	
	/**
     * Constructs a {@code HardInformations} object with the specified informational text
     * and point value.
     *
     * @param info  the hard-level information content to display
     * @param point the score value granted when this information is collected
     */
	public HardInformations(String info, int point) {
		this.info = info;
		this.point = point;
	}

	/**
     * Starts the vertical movement of the information box from the specified horizontal position.
     * <p>The object falls downward using the highest speed available
     * (defined as {@code speeds[2]}). When it reaches the bottom or is collected,
     * it is reset and deactivated.</p>
     *
     * @param X the X-coordinate from which the info box starts descending
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
					Y += speeds[2];}
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
