package authentication;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import javax.swing.JOptionPane;

/**
 * Provides base authentication utilities for the application.
 * <p>
 * Includes methods to read existing user credentials from a file and display error dialogs.
 *
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public abstract class Authentication {
	
	/**
     * Reads and returns all existing users and their passwords from the users file.
     *
     * @return a map containing usernames as keys and passwords as values
     */
	public static Map<String, String> listExistUsers() {
		File usersInfo = new File("src/users/users.txt");
		Map<String, String> existUsers = new HashMap<>();
		try (BufferedReader reader = new BufferedReader(new FileReader(usersInfo))){
			String line;
			while ((line = reader.readLine()) != null) {
				if (line.trim().isEmpty()) {
			        continue;
			    }
				existUsers.put(line.split(",")[0].trim(), line.split(",")[1].trim());
			}
		} catch (IOException e1) {
			e1.printStackTrace();
		}
		return existUsers;
	}
	
	/**
     * Displays an error message dialog with the given message.
     *
     * @param msg the message to display in the error dialog
     */
	public static void showErrorDialog(String msg) {
		JOptionPane.showMessageDialog(null,
                msg,
                "Error",
                JOptionPane.ERROR_MESSAGE);
	}

}
