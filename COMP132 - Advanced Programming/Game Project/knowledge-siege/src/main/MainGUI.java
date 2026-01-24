package main;

import java.awt.CardLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;

import authentication.LoginGUI;
import authentication.RegisterGUI;
import game.GameGUI;
import home.HomeGUI;

/**
 * The main frame of the application that handles screen navigation using {@link CardLayout}.
 * 
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class MainGUI extends JFrame {

	private static final long serialVersionUID = 1L;
	
	private static CardLayout cardLayout;
	private static JPanel mainPanel;
	
	public static LoginGUI loginGUI;
	public static RegisterGUI registerGUI;
	public static HomeGUI homeGUI;
	public static GameGUI level1GUI;
	public static GameGUI level2GUI;
	public static GameGUI level3GUI;


	/**
	 * Initialize and show the main GUI frame.
	 */
	public static void call() {
		MainGUI frame = new MainGUI();
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					frame.setVisible(true);
					frame.setResizable(false);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Constructs the main GUI frame, initializes and adds all screens.
	 */
	public MainGUI() {
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(840, 560);
		setLocationRelativeTo(null);
		
		cardLayout = new CardLayout();
		mainPanel = new JPanel(cardLayout);
		
		loginGUI = new LoginGUI();
		registerGUI = new RegisterGUI();
		homeGUI = new HomeGUI();
		level1GUI = new GameGUI();
		level2GUI = new GameGUI();
		level3GUI = new GameGUI();

		
		mainPanel.add(loginGUI, "login");
		mainPanel.add(registerGUI, "register");
		mainPanel.add(homeGUI, "home");
		mainPanel.add(level1GUI, "level1");
		mainPanel.add(level2GUI, "level2");
		mainPanel.add(level3GUI, "level3");

		setContentPane(mainPanel);
		cardLayout.show(mainPanel, "login");

		setVisible(true);
	}
	
	/**
	 * Switches the currently displayed screen to the chosen panel.
	 * <p>
	 * This method changes the visible panel in the application's main frame based on
	 * the given panel name. It is typically used to navigate between different screens
	 * in the application.
	 * <p>
	 * Supported panel names:
	 * <ul>
	 *   <li>{@code "login"} - Login Page</li>
	 *   <li>{@code "register"} - Register Page</li>
	 *   <li>{@code "home"} - Home Page</li>
	 *   <li>{@code "level1"} - Level 1 Game Screen</li>
	 *   <li>{@code "level2"} - Level 2 Game Screen</li>
	 *   <li>{@code "level3"} - Level 3 Game Screen</li>
	 * </ul>
	 *
	 * @param key the name of the panel to switch to
	 */
	public static void switchScreen(String key) {
		cardLayout.show(mainPanel, key);
	}

}
