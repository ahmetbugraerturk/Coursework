package authentication;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.Map;

import javax.swing.JOptionPane;

import exception.InvalidAuthException;
import home.Home;
import main.MainGUI;

/**
 * Saves user credentials, stores a profile image, and prepares the user's directory structure.
 *
 * <p>On successful registration:
 * <ul>
 *   <li>Appends user credentials to src/users/users.txt.</li>
 *   <li>Creates a folder at src/users/[username]/.</li>
 *   <li>Copies the selected profile image into the user folder, renamed as [username].[ext].</li>
 *   <li>Initializes log and game count files for the user.</li>
 * </ul>
 *
 * <p>Validation:
 * <ul>
 *   <li>Username must be unique and not contain commas.</li>
 *   <li>Password must not be empty or contain commas.</li>
 * </ul>
 * 
 * @see RegisterGUI
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class Register extends Authentication{
	
	/**
	 * Registers a new user by saving their usernames and passwords, copying a profile image, and
	 * setting up a personal directory with log and game data.
	 *
	 * <p>This method performs:
	 * <ul>
	 *   <li>Validation of input fields (non-empty, no commas, unique username).</li>
	 *   <li>Write username,password in {@code users.txt}.</li>
	 *   <li>Folder and file creation for the new user.</li>
	 *   <li>Image copying and initial log writing.</li>
	 * </ul>
	 *
	 * @param username the username input by the user
	 * @param password the password input by the user
	 * @param image    the selected profile image file
	 */
	public static void register(String username, String password, File image) {
		
		Map<String, String> existUsers = listExistUsers();
		
		try {
			if (existUsers.containsKey(username))
				throw new InvalidAuthException("An account exists with this username.");
			else if (username.contains(",") || password.contains(","))
				throw new InvalidAuthException("Username or password contain comma ','. They cannot.");
			else if (username.isBlank() || password.isBlank()) 
				throw new InvalidAuthException("Username or password is empty.");
			else {
				File usersInfo = new File("src/users/users.txt");
				File gameNumFile = new File("src/users/"+username+"/gameNum.txt");
				try (BufferedWriter writer = new BufferedWriter(new FileWriter(usersInfo, true))) {
					Files.createDirectory(Paths.get("src/users/"+username));
					File playerFolder = new File("src/users/"+username);
					try (BufferedWriter score = new BufferedWriter(new FileWriter(gameNumFile))) {
			            File copyFile = new File(playerFolder, username + image.getName().substring(image.getName().lastIndexOf('.')));
			            Files.copy(image.toPath(), copyFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
						score.write("0");
					} catch (IOException e1) {
						gameNumFile.delete();
						playerFolder.delete();
						showErrorDialog("Error while creating required folders and files. Try again.");
		                return;
					} finally {
						writer.write(username+","+password);
						writer.newLine();
						Home.setPlayer(username);
			            Home.getPlayer().log("Account has been created", true);
			            Home.resetPlayer();
	                	JOptionPane.showMessageDialog(null,
	                            "Your account has been created. You can login.",
	                            "Successful",
	                            JOptionPane.INFORMATION_MESSAGE);
	                	MainGUI.switchScreen("login");
					}
		        } catch (IOException ex) {
		            ex.printStackTrace();
		        }
			}
		} catch (InvalidAuthException e) {
			showErrorDialog(e.getMessage());
		}
	}
}
