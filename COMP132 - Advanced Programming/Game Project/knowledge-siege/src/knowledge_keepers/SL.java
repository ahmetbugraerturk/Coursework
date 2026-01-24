package knowledge_keepers;

import java.io.File;
import java.util.Collections;

import javax.swing.Timer;

import shot_boxes.informations.Informations;
import shot_boxes.questions.Questions;

/**
 * Represents a Section Leader (SL) entity in the game, extending {@link KnowledgeKeepers}.
 * <p>
 * SLs have easy difficulty information and questions. 
 * They move at a specific speed and attack with a probability to choose either information or question.
 * Movement direction is randomly determined.
 * </p>
 * 
 * @see KnowledgeKeepers
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class SL extends KnowledgeKeepers {
	
    private boolean direction = false;

    /**
	 * Constructs an SL instance with the specified name and image.
	 * Initializes easy information and questions lists,
	 * and sets timers for movement and direction changes.
	 * 
	 * @param name the SL's name
	 * @param img the image file representing the SL
	 */
	public SL(String name, File img) {
		super(name, img);

		infos = Informations.getEasyInformations();
		Collections.shuffle(infos);
		quests = Questions.getEasyQuestions();
		Collections.shuffle(quests);
		directionTimer = new Timer(1000+(random.nextInt(1000) - 500), e -> movementDirection());;
		moveTimer = new Timer(15, e -> move());
	}
	
	/**
	 * Starts the attack timer for SL.
	 * Attacks periodically with random delays,
	 * deciding based on probability whether to attack with information or question (60% for info).
	 */
	@Override
	public void startAttack() {
		attackTimer = new Timer(3000+(random.nextInt(2000) - 1000), e -> {
		if (random.nextDouble()<chanceOfInfo[0]) {
			attackInfo();
			}
		else
			attackQuestion();});
        attackTimer.start();
        moveTimer.start();
	}

	

	/**
	 * Moves the SL horizontally according to the current direction.
	 * Changes direction upon reaching boundaries (10 and 510 on X-axis).
	 */
	@Override
	public void move() {
		if (direction) {
			if(X<=10) {
				movementDirection();
				X += speeds[0];
			} else
				X -= speeds[0];
        }
        if (!direction) {
        	if(X>=510) {
				movementDirection();
				X -= speeds[0];
        	} else
				X += speeds[0];
        }
	}

	/**
	 * Randomly determines the movement direction of the SL.
	 * Starts the random timer to schedule the next direction change.
	 */
	@Override
	public void movementDirection() {
		direction = random.nextBoolean();
		directionTimer.start();
	}
}
