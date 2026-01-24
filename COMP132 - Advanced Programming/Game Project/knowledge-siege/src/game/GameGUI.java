package game;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.ComponentAdapter;
import java.awt.event.ComponentEvent;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.File;
import java.util.ArrayList;
import java.util.List;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.JSeparator;
import javax.swing.JTextArea;
import javax.swing.SwingConstants;

import home.Home;
import knowledge_keepers.KnowledgeKeepers;

/**
 * GameGUI is a JPanel responsible for displaying and controlling the game interface.
 * It handles rendering the player, keepers, questions, information,
 * and processing keyboard inputs for player movement.
 * 
 * @see Game
 * @see main.MainGUI
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class GameGUI extends JPanel implements KeyListener {

	private static final long serialVersionUID = 1L;
		
	Game game;
	
	int playerX = 280;  
	int faceX = 285;  
    final int playerY = 400;  
    
    private Image backgroundImage;
    Image[] playerImages = new Image[3];
    Image playerImage;
    private Image playerFace;
    private String question = "";
    private String information = "";
    private Image questionImage;
    private Image infoImage;
    
    List<KnowledgeKeepers> keepers = new ArrayList<>();
    private Image keeperImage;
    
    boolean movingLeft = false;
    boolean movingRight = false;
    
    private JButton backButton;
    JProgressBar healthBar;
    JLabel ScoreLbl;
    public JTextArea QuestionLbl;
    public JTextArea InformationLbl;

    /**
     * Constructs the GameGUI panel with the main frame reference.
     * Initializes the game instance, UI components, and assets.
     */
	public GameGUI() {
		game = new Game(this);
		
        setLayout(null);

        backButton = new JButton("Back");
        backButton.setBounds(750, 495, 80, 30);
        add(backButton);

        backButton.addActionListener(e -> {
        	game.gameDone();
        });
        
        JLabel healthLbl = new JLabel();
        healthLbl.setText("Health");
        healthLbl.setBounds(675, 20, 50, 20);
        healthLbl.setHorizontalAlignment(SwingConstants.CENTER);
        add(healthLbl);
		
		healthBar = new JProgressBar(0, 100);
		healthBar.setValue(100);
		healthBar.setStringPainted(true);
		healthBar.setBounds(600, 50, 200, 25);
		healthBar.setForeground(Color.RED);
		add(healthBar);
		
		JLabel ScoreTbl = new JLabel();
		ScoreTbl.setText("Score");
		ScoreTbl.setBounds(675, 100, 50, 20);
		ScoreTbl.setHorizontalAlignment(SwingConstants.CENTER);
        add(ScoreTbl);
        
        ScoreLbl = new JLabel();
        ScoreLbl.setText(String.format("%04d", 0));
        ScoreLbl.setFont(new Font("Arial", Font.BOLD, 30));
        ScoreLbl.setBounds(600, 130, 200, 35);
        ScoreLbl.setHorizontalAlignment(SwingConstants.CENTER);
        add(ScoreLbl);
        
        JSeparator separator = new JSeparator();
        separator.setBounds(560, 180, 280, 2);
        add(separator);
        
        JLabel QTbl = new JLabel();
        QTbl.setText("Question");
        QTbl.setFont(QTbl.getFont().deriveFont((float) 16.0));
        QTbl.setBounds(650, 200, 100, 20);
        QTbl.setHorizontalAlignment(SwingConstants.CENTER);
        add(QTbl);
        
        QuestionLbl = new JTextArea();
        QuestionLbl.setText(question);
        QuestionLbl.setFont(QTbl.getFont().deriveFont((float) 14.0));
        QuestionLbl.setLineWrap(true);
        QuestionLbl.setWrapStyleWord(true);
        QuestionLbl.setEditable(false);
        QuestionLbl.setOpaque(false);
        QuestionLbl.setBounds(570, 230, 260, 100);
        add(QuestionLbl);
        
        JLabel ITbl = new JLabel();
        ITbl.setText("Information");
        ITbl.setFont(ITbl.getFont().deriveFont((float) 16.0));
        ITbl.setBounds(650, 350, 100, 20);
        ITbl.setHorizontalAlignment(SwingConstants.CENTER);
        add(ITbl);
        
        InformationLbl = new JTextArea();
        InformationLbl.setText(information);
        InformationLbl.setFont(ITbl.getFont().deriveFont((float) 14.0));
        InformationLbl.setLineWrap(true);
        InformationLbl.setWrapStyleWord(true);
        InformationLbl.setEditable(false);
        InformationLbl.setOpaque(false);
        InformationLbl.setBounds(570, 380, 260, 100);
        add(InformationLbl);
		
		backgroundImage = new ImageIcon(new File("src/assets/game/background.jpeg").getAbsolutePath())
                .getImage()
                .getScaledInstance(560, 560, Image.SCALE_SMOOTH);
		playerImages[0] = new ImageIcon(new File("src/assets/game/playerFront.png").getAbsolutePath())
				.getImage()
				.getScaledInstance(40, 120, Image.SCALE_SMOOTH);
		playerImages[1] = new ImageIcon(new File("src/assets/game/playerLeft.png").getAbsolutePath())
				.getImage()
				.getScaledInstance(64, 120, Image.SCALE_SMOOTH);
		playerImages[2] = new ImageIcon(new File("src/assets/game/playerRight.png").getAbsolutePath())
				.getImage()
				.getScaledInstance(64, 120, Image.SCALE_SMOOTH);
		keeperImage = new ImageIcon(new File("src/assets/game/keeper.png").getAbsolutePath())
                .getImage()
                .getScaledInstance(40, 60, Image.SCALE_SMOOTH);
		questionImage = new ImageIcon(new File("src/assets/game/question.png").getAbsolutePath())
                .getImage()
                .getScaledInstance(25, 25, Image.SCALE_SMOOTH);
		infoImage = new ImageIcon(new File("src/assets/game/info.png").getAbsolutePath())
                .getImage()
                .getScaledInstance(25, 25, Image.SCALE_SMOOTH);
		playerImage = playerImages[0];
        setFocusable(true);
        addKeyListener(this);
                
        addComponentListener(new ComponentAdapter() {
            @Override
            public void componentShown(ComponentEvent e) {
            	playerX = 280;  
            	faceX = 285;  
                healthBar.setValue(Home.getPlayer().getHealth());
                ScoreLbl.setText(String.format("%04d", Home.getPlayer().getScore()));
                question = "";
                information = "";
                InformationLbl.setText(information);
                QuestionLbl.setText(question);
        		playerFace = new ImageIcon(Home.getPlayer().getPlayerIMG().getAbsolutePath()).getImage().getScaledInstance(30, 36, Image.SCALE_SMOOTH);
                requestFocusInWindow();
    			for (KnowledgeKeepers k: keepers) {
    				k.hasQuestion = false;
                    k.hasInfo = false;
    				k.startAttack();
    				if (k.getInfo() != null)
    					k.getInfo().interact(k);
    				if (k.getQuest() != null)
    					k.getQuest().interact(k);
    			}
    			repaint();
    			revalidate();
            }
        });        
	}
	
	/**
     * Paints the game components including background, keepers, player, and shot boxes.
     *
     * @param g the Graphics context to draw on
     */
	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		g.drawImage(backgroundImage, 0, 0, null);
		for (KnowledgeKeepers k : keepers) {
			k.draw(keeperImage, g);
			k.setPlayerX(playerX);
			if (k.hasInfo && k.getInfo()!=null) {
				k.getInfo().draw(infoImage, g);
				game.checkInteraction(k, k.getInfo());
			}
			if (k.hasQuestion && k.getQuest()!=null) {
				k.getQuest().draw(questionImage, g);;
				game.checkInteraction(k, k.getQuest());
			}
	    }
        g.drawImage(playerImage, playerX, playerY, null);
		g.drawImage(playerFace, faceX, playerY, null);
    }

	/**
     * Handles key press events to start moving the player left or right.
     *
     * @param e the KeyEvent triggered by a key press
     */
	@Override
	public void keyPressed(KeyEvent e) {
	    int key = e.getKeyCode();
	    if (key == KeyEvent.VK_LEFT) {
	    	 movingLeft = true;
	    } else if (key == KeyEvent.VK_RIGHT) {
	    	 movingRight = true;
	    }
	}

	/**
     * Handles key release events to stop player movement and reset player image.
     *
     * @param e the KeyEvent triggered by a key release
     */
    @Override 
    public void keyReleased(KeyEvent e) {
    	int key = e.getKeyCode();
    	playerImage = playerImages[0];
        faceX = playerX+5;
	    if (key == KeyEvent.VK_LEFT) {
	    	 movingLeft = false;
	    } else if (key == KeyEvent.VK_RIGHT) {
	    	 movingRight = false;
	    }
    }
    
    @Override public void keyTyped(KeyEvent e) {}
    	    
}
