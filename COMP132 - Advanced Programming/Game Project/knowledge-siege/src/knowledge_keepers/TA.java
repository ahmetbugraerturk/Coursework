package knowledge_keepers;

import java.io.File;
import java.util.Collections;

import javax.swing.Timer;

import shot_boxes.informations.Informations;
import shot_boxes.questions.Questions;

/**
 * Represents a Teaching Assistant (TA) entity in the game, extending {@link KnowledgeKeepers}.
 * <p>
 * TAs use medium difficulty information and questions. 
 * Their movement direction is influenced by the player's position with some randomness.
 * They choose between information and question based on a set probability.
 * </p>
 * 
 * @see KnowledgeKeepers
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class TA extends KnowledgeKeepers {
	
    private boolean direction = false;
    
    /**
	 * Constructs a TA instance with the specified name and image.
	 * Initializes medium difficulty information and questions,
	 * and sets timers for movement and direction changes.
	 * 
	 * @param name the TA's name
	 * @param img the image file representing the TA
	 */
	public TA(String name, File img) {
		super(name, img);
		// TODO Auto-generated constructor stub
		infos = Informations.getMidInformations();
		Collections.shuffle(infos);
		quests = Questions.getMidQuestions();
		Collections.shuffle(quests);
		directionTimer = new Timer(750+(random.nextInt(500) - 250), e -> movementDirection());
		moveTimer = new Timer(15, e -> move());
	}

	/**
	 * Starts the attack timer for TA.
	 * Attacks periodically with a small random delay,
	 * deciding probabilistically whether to attack with information or question (50% for each).
	 */
	@Override
	public void startAttack() {
		// TODO Auto-generated method stub
		attackTimer = new Timer(2000+(random.nextInt(1500) - 750), e -> {
		if (random.nextDouble()<chanceOfInfo[1]) {
			attackInfo();}
		else
			attackQuestion();});
        attackTimer.start();
        moveTimer.start();
	}
	
	/**
	 * Moves the TA horizontally based on the current direction.
	 * Changes direction upon reaching boundaries (10 and 510 on X-axis).
	 */
	@Override
	public void move() {
		// TODO Auto-generated method stub
		if (direction) {
			if(X<=10){
				movementDirection();
				X += speeds[1];
        	}
			else
				X -= speeds[1];
        }
        if (!direction) {
        	if(X>=510) {
				movementDirection();
				X -= speeds[1];
        	}
			else
				X += speeds[1];
        }
	}

	/**
	 * Determines the movement direction of the TA.
	 * With 40% probability, the direction is set towards or away from the player based on player's X position.
	 * Otherwise, direction is randomly chosen.
	 * Starts the random timer to schedule the next direction change.
	 */
	@Override
	public void movementDirection() {
		// TODO Auto-generated method stub
		if (random.nextDouble()<=.4) {
			if (playerX<X)
				direction = true;
			else
				direction = false;
		} else
			direction = random.nextBoolean();
		directionTimer.start();
	}
}
