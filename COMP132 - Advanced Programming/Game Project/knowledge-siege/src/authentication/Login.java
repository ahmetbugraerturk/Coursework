package authentication;

import java.util.Map;

import javax.swing.JOptionPane;

import exception.InvalidAuthException;
import home.Home;
import main.MainGUI;

/**
 * Verifies the username and password with stored data in users.txt.
 * On success, logs the login, shows a confirmation dialog, and switches to the home screen.
 * On failure, displays an error message and logs the failed attempt if possible.
 *
 * <p>Example usage:
 * <pre>
 * Login.login("ahmetbugra", "123456", frame);
 * </pre>
 *
 * @see LoginGUI
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class Login extends Authentication {
	
	/**
	 * Attempts to log in the user with the given parameters.
	 *
	 * @param username the entered username
	 * @param password the entered password
	 */
	public static void login(String username, String password) {
		
		Map<String, String> existUsers = listExistUsers();
		
		try {
			if (username.isBlank() || password.isBlank()) 
				throw new InvalidAuthException("Username or password is empty.");
			else if (existUsers.containsKey(username) && existUsers.get(username).equals(password)) {
				Home.setPlayer(username);
				Home.getPlayer().log("User logged in", true);
				JOptionPane.showMessageDialog(null,
	                    "Succesful login.",
	                    "Succesful",
	                    JOptionPane.INFORMATION_MESSAGE);
				MainGUI.switchScreen("home");
				
			} else {
				Home.setPlayer(username);
				Home.getPlayer().log("Unsuccessful login attempt", true);
				Home.resetPlayer();
				throw new InvalidAuthException("Username or password is invalid.");
			}
		} catch (InvalidAuthException e) {
			showErrorDialog(e.getMessage());
		}
		
	}
}
