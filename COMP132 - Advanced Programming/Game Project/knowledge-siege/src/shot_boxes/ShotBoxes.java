package shot_boxes;

import knowledge_keepers.KnowledgeKeepers;

/**
 * The {@code ShotBoxes} interface defines the structure for shotbox objects
 * in the game that represent either questions or informational items.
 * 
 * <p>
 * Constants are provided to represent the possible point values and movement
 * speeds for different difficulty levels.
 * </p>
 * 
 * @author 
 * @version 1.0
 */
public interface ShotBoxes {

	int[] questionsPoints = {5, 10, 20};
	int[] infoPoints = {10, 20, 30};
	int[] speeds = {3, 4, 5};
	
	/**
     * Defines the interaction behavior when the player collides with this object.
     * 
     * @param k the KnowledgeKeeper who shooted this ShotBox
     */
	void interact(KnowledgeKeepers k);
	
	/**
     * Returns the X and Y coordinates of the object.
     * 
     * @return an array of two integers, where index 0 is X and index 1 is Y
     */
	int[] getCoordinate();
	
	/**
     * Starts the downward movement of the informational item from a given X position.
     *
     * @param k the KnowledgeKeeper who shooted this ShotBox
     * @param X the horizontal position of shooter KnowledgeKeeper
     */
	void move(KnowledgeKeepers k, int X);	
	
}
