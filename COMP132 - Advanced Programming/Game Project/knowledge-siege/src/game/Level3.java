package game;

import home.Home;
import knowledge_keepers.KnowledgeKeepers;

/**
 * Represents the third level of the game.
 * 
 * @see Game
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class Level3 extends Game{
	
	/**
     * Constructs a new Level3 instance.
     * Adds all remaining TAs from Level2 and all Professors to the game,
     * then starts their movement and direction.
     * Logs the transition to level 3 for the player.
     * 
     * @param gameGUI the GameGUI instance associated with this level
     */
	public Level3(GameGUI gameGUI) {
		super(gameGUI);

		for (KnowledgeKeepers ta: Level2.remainingTAs) {
			addKeeper(ta);
			ta.move();
			ta.movementDirection();
		}
		for (KnowledgeKeepers p: KnowledgeKeepers.getProfessors()) {
			addKeeper(p);
			p.move();
			p.movementDirection();
		}
		Home.getPlayer().log("Passed to level 3", true);
	}

}
