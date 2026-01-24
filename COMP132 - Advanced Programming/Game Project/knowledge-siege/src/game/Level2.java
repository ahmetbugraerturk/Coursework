package game;

import java.util.ArrayList;
import java.util.List;

import home.Home;
import knowledge_keepers.KnowledgeKeepers;

/**
 * Represents the second level of the game.
 * 
 * @see Game
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class Level2 extends Game{
	
	static List<KnowledgeKeepers> remainingTAs;
	
	/**
     * Constructs a new Level2 instance.
     * Adds the remaining SLs from Level1 to the game and starts their movement,
     * then selects 2 random TAs, adds them to the game, and starts their movement.
     * Logs the transition to level 2 for the player.
     *
     * @param gameGUI the GameGUI instance associated with this level
     */
	public Level2(GameGUI gameGUI) {
		super(gameGUI);

		remainingTAs = new ArrayList<>(KnowledgeKeepers.getTAs());
		for (KnowledgeKeepers sl: Level1.remainingSLs) {
			addKeeper(sl);
			sl.move();
			sl.movementDirection();
		}
		for (int i = 0; i<2; i++) {
			int idx = random.nextInt(remainingTAs.size());
			addKeeper(remainingTAs.get(idx));
			remainingTAs.get(idx).move();
			remainingTAs.get(idx).movementDirection();
			remainingTAs.remove(idx);
		}
		Home.getPlayer().log("Passed to level 2", true);
	}
	
}
