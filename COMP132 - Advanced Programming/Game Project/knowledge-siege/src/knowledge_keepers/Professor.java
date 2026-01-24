package knowledge_keepers;

import java.io.File;
import java.util.Collections;

import javax.swing.Timer;

import shot_boxes.informations.Informations;
import shot_boxes.questions.Questions;

/**
 * Represents a Professor entity in the game, extending {@link KnowledgeKeepers}.
 * <p>
 * A Professor has higher difficulty information and questions, moves with specific speed,
 * and attacks with a certain probability of using information or questions.
 * Movement includes logic for changing direction based on player's position.
 * </p>
 * 
 * @see KnowledgeKeepers
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class Professor extends KnowledgeKeepers {
	
    private boolean direction = false;
    
    /**
	 * Constructs a Professor instance with the given name and image file.
	 * Initializes hard information and questions lists,
	 * and sets timers for movement and direction changes.
	 * 
	 * @param name the name of the Professor
	 * @param img the image file representing the Professor
	 */
	public Professor(String name, File img) {
		super(name, img);
		infos = Informations.getHardInformations();
		Collections.shuffle(infos);
		quests = Questions.getHardQuestions();
		Collections.shuffle(quests);
		directionTimer = new Timer(500+(random.nextInt(500) - 250), e -> movementDirection());
		moveTimer = new Timer(15, e -> move());		
	}

	/**
	 * Starts the attack timer.
	 * The attack timer triggers attacks periodically with randomized delays.
	 * Depending on probability (75% question), either an information or a question attack is performed.
	 */
	@Override
	public void startAttack() {
		// TODO Auto-generated method stub
		attackTimer = new Timer(1500+(random.nextInt(1000) - 500), e -> {
		if (random.nextDouble()<chanceOfInfo[2]) {
			attackInfo();}
		else
			attackQuestion();});
        attackTimer.start();
        moveTimer.start();
	}
	
	/**
	 * Moves the Professor horizontally according to the current direction.
	 * Reverses direction when reaching boundaries (10 and 510 on X-axis).
	 */
	@Override
	public void move() {
		// TODO Auto-generated method stub
		if (direction) {
			if(X<=10){
				movementDirection();
				X += speeds[2];
        	}
			else
				X -= speeds[2];
        }
        if (!direction) {
        	if(X>=510) {
				movementDirection();
				X -= speeds[2];
        	}
			else
				X += speeds[2];
        }
	}

	/**
	 * Randomly determines and sets the movement direction of the Professor.
	 * With 80% chance, direction is set to move towards the player's position.
	 * Otherwise, direction is chosen randomly.
	 */
	@Override
	public void movementDirection() {
		// TODO Auto-generated method stub
		if (random.nextDouble()<=.8) {
			if (playerX<X)
				direction = true;
			else
				direction = false;
		} else
			direction = random.nextBoolean();
		directionTimer.start();
	}
	
}
