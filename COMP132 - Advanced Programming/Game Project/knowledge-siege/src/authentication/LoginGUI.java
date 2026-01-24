package authentication;

import java.awt.Image;

import javax.swing.*;

import main.MainGUI;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

/**
 * The login panel for the application.
 * <p>
 * When the "Login" button is clicked, it triggers the {@code Login.login()} method
 * with the entered credentials. The "Create new user" button switches to the registration screen
 * using the {@link MainGUI#switchScreen(String)} method.
 *
 * @see Login
 * @see main.MainGUI
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class LoginGUI extends JPanel {

	private static final long serialVersionUID = 1L;

	private JTextField usernameField;
	private JPasswordField passwordField;
	private JLabel lblNewLabel;
	private JLabel lblNewLabel_1;
	private JButton loginButton;
	private JLabel lblNewLabel_2;
	private JButton signUpButton;

	/**
	 * Constructs the LoginGUI interface with the main frame.
	 * Sets up UI components for user login including username and password fields,
	 * login and sign-up buttons.
	 */
	public LoginGUI() {
		setLayout(null);
		setBounds(0, 0, 840, 560);

		usernameField = new JTextField();
		usernameField.setBounds(182, 190, 205, 36);
		add(usernameField);
		usernameField.setColumns(10);

		passwordField = new JPasswordField();
		passwordField.setBounds(182, 248, 205, 36);
		add(passwordField);

		lblNewLabel = new JLabel("Username:");
		lblNewLabel.setBounds(101, 200, 69, 16);
		add(lblNewLabel);

		lblNewLabel_1 = new JLabel("Password:");
		lblNewLabel_1.setBounds(101, 258, 69, 16);
		add(lblNewLabel_1);

		loginButton = new JButton("Login");
		loginButton.setBounds(101, 298, 287, 29);
		loginButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Login.login(usernameField.getText(), new String(passwordField.getPassword()));
				//Login.login("admin", "admin", frame);
			}
		});
		add(loginButton);

		lblNewLabel_2 = new JLabel("New label");
		File projectImgFile = new File("src/assets/project_image.png");
		ImageIcon projectIcon = new ImageIcon(projectImgFile.getAbsolutePath());
		lblNewLabel_2.setIcon(new ImageIcon(projectIcon.getImage().getScaledInstance(350, 520, Image.SCALE_SMOOTH)));
		lblNewLabel_2.setBounds(484, 6, 350, 520);
		add(lblNewLabel_2);

		signUpButton = new JButton("Create new user");
		signUpButton.setBounds(101, 339, 286, 29);
		signUpButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				MainGUI.switchScreen("register");
			}
		});
		add(signUpButton);
	}

}
