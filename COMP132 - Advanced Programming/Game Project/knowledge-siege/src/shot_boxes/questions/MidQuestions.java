package shot_boxes.questions;

import javax.swing.Timer;

import knowledge_keepers.KnowledgeKeepers;
import shot_boxes.ShotBoxes;

/**
 * Represents a medium-level question box in the game.
 *
 * <p>{@code MidQuestions} are dropped by mid-level knowledge keepers and represent
 * moderate difficulty questions. They offer more points than easy questions
 * but fewer than hard ones.</p>
 *
 * <p>The box moves downward from the top of the screen and is removed or reset
 * if it reaches the bottom without player interaction.</p>
 *
 * @see Questions
 * @see ShotBoxes
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class MidQuestions extends Questions implements ShotBoxes{
	
	/**
     * Constructs a {@code MidQuestions} object with the given question text and point value.
     *
     * @param question the medium-difficulty question to present to the player
     * @param point    the number of points awarded for interacting with this question
     */
	public MidQuestions(String question, int point) {
		this.question = question;
		this.point = point;
	}

	/**
     * Starts the downward movement of the question box from a given horizontal position.
     *
     * <p>The question moves at a medium speed (defined as {@code speeds[1]})
     * and resets upon reaching the bottom of the screen.</p>
     *
     * @param X the horizontal position from which the question starts descending
     */
	@Override
	public void move(KnowledgeKeepers k, int X) {
		// TODO Auto-generated method stub
		if (!k.hasQuestion) {
			k.hasQuestion = true;
			isMoving = true;
			this.X = X;
			moveTimer = new Timer(25, e -> {
				if (Y<500) {
					Y += speeds[1];}
				else {
					k.hasQuestion = false;
					isMoving = false;
					Y = 60;
					moveTimer.stop();
					}
				});
	        moveTimer.start();
		}
	}

}
