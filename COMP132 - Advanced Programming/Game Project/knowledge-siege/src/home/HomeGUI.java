package home;

import javax.swing.*;

import main.MainGUI;

import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ComponentAdapter;
import java.awt.event.ComponentEvent;
import java.io.File;

/**
 * Displays the current user's image and username, and provides buttons
 * to start the game, view the scoreboard, or logout.
 * 
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class HomeGUI extends JPanel {

	private static final long serialVersionUID = 1L;
	private JButton gameButton;
	private JButton logoutButton;
	private JButton scoreButton;
	
	private File imageFile;
	private JLabel usernameLabel;
	
	/**
	 * Constructs the Home screen panel with buttons and user info.
	 */
	public HomeGUI() {
		setLayout(null);
		setBounds(0, 0, 840, 560);
		
		JLabel imageLabel = new JLabel("user image");
		imageFile = new File("src/users/default.png");
		ImageIcon icon = new ImageIcon(imageFile.getAbsolutePath());
		imageLabel.setIcon(new ImageIcon(icon.getImage().getScaledInstance(120, 144, Image.SCALE_SMOOTH)));
		imageLabel.setBounds(360, 100, 120, 144);
		add(imageLabel);
		
		usernameLabel = new JLabel("username");
		usernameLabel.setBounds(360, 250, 120, 16);
		usernameLabel.setHorizontalAlignment(SwingConstants.CENTER);
		add(usernameLabel);
		
		gameButton = new JButton("Play Game");
		gameButton.setBounds(270, 280, 300, 50);
		gameButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
	        	Home.getPlayer().resetScoreHealth();
				Home.level1();
			}
		});
		add(gameButton);
		
		logoutButton = new JButton("Logout");
		logoutButton.setBounds(360, 383, 120, 30);
		logoutButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Home.resetPlayer();
				MainGUI.switchScreen("login");
			}
		});
		add(logoutButton);
		
		scoreButton = new JButton("Scoreboard");
		scoreButton.setBounds(360, 342, 120, 29);
		scoreButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Home.showScoreboard();
			}
		});
		add(scoreButton);
		
		addComponentListener(new ComponentAdapter() {
			@Override
			public void componentShown(ComponentEvent e) {
				imageFile = Home.getPlayer().getPlayerIMG();
				ImageIcon icon = new ImageIcon(imageFile.getAbsolutePath());
				imageLabel.setIcon(new ImageIcon(icon.getImage().getScaledInstance(120, 144, Image.SCALE_SMOOTH)));

				usernameLabel.setText(Home.getPlayer().getUsername());
				revalidate();
				repaint();
			}
		});
	}
}
