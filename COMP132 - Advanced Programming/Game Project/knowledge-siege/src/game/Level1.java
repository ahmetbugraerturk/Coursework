package game;

import java.util.ArrayList;
import java.util.List;

import home.Home;
import knowledge_keepers.KnowledgeKeepers;

/**
 * Represents the first level of the game.
 * 
 * @see Game
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class Level1 extends Game{
	
	static List<KnowledgeKeepers> remainingSLs;
	
	/**
     * Constructs a new Level1 instance.
     * Selects 4 random SL knowledge keepers, adds them to the game,
     * starts their movement and direction behaviors,
     * and logs the start of a new game for the player.
     *
     * @param gameGUI the {@link GameGUI} instance associated with this level
     */
	public Level1(GameGUI gameGUI) {
		super(gameGUI);

		remainingSLs = new ArrayList<>(KnowledgeKeepers.getSLs());
		for (int i = 0; i<4; i++) {
			int idx = random.nextInt(remainingSLs.size());
			addKeeper(remainingSLs.get(idx));
			remainingSLs.get(idx).move();
			remainingSLs.get(idx).movementDirection();
			remainingSLs.remove(idx);
		}
		Home.getPlayer().log("New game started", true);
	}
	
}
