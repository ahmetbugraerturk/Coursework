package authentication;

import javax.swing.JPanel;
import java.awt.Image;
import java.io.File;

import javax.swing.filechooser.FileNameExtensionFilter;

import main.MainGUI;

import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.ImageIcon;
import javax.swing.JPasswordField;
import javax.swing.JButton;
import javax.swing.JFileChooser;

import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

/**
 * Register screen panel for new user sign-up.
 * <p>Triggers {@link Register#register(String, String, File)} when "Sign Up" is clicked.
 * Uses a default image if none is selected.
 *
 * @see Register
 * @see main.MainGUI
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class RegisterGUI extends JPanel {

	private static final long serialVersionUID = 1L;
	
	private JTextField usernameField;
	private JPasswordField passwordField;
	private JLabel lblNewLabel;
	private JLabel lblNewLabel_1;
	private JButton registerButton;
	private JLabel lblNewLabel_2;
	private JButton backButton;
	private File selectedFile;
	private JLabel lblPleaseChooseThe;

	/**
	 * Constructs the RegisterGUI interface with the main frame.
	 * Sets up UI components for user registration including username and password fields,
	 * image selection with preview, and action buttons.
	 */
	public RegisterGUI() {
		setLayout(null);
		setBounds(0, 0, 840, 560);

		usernameField = new JTextField();
		usernameField.setBounds(182, 287, 205, 36);
		add(usernameField);
		usernameField.setColumns(10);

		JLabel imageLabel = new JLabel("user image");
		selectedFile = new File("src/users/default.png");
		ImageIcon icon = new ImageIcon(selectedFile.getAbsolutePath());
		imageLabel.setIcon(new ImageIcon(icon.getImage().getScaledInstance(120, 144, Image.SCALE_SMOOTH)));
		imageLabel.setBounds(182, 62, 120, 144);
		add(imageLabel);

		passwordField = new JPasswordField();
		passwordField.setBounds(182, 335, 205, 36);
		add(passwordField);

		JButton imgButton = new JButton("Image Choose");
		imgButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JFileChooser fileChooser = new JFileChooser();
				FileNameExtensionFilter filter = new FileNameExtensionFilter(
	                    "Image Files (png, jpg, jpeg)", "png", "jpg", "jpeg");
				fileChooser.setFileFilter(filter);
	            fileChooser.setDialogTitle("Choose an image");

	            int result = fileChooser.showOpenDialog(null);
	            if (result == JFileChooser.APPROVE_OPTION) {
	                selectedFile = fileChooser.getSelectedFile();
	                ImageIcon icon = new ImageIcon(selectedFile.getAbsolutePath());
	        		imageLabel.setIcon(new ImageIcon(icon.getImage().getScaledInstance(120, 144, Image.SCALE_SMOOTH)));
	            } else {
	            	JOptionPane.showMessageDialog(null,
                            "No file was selected.",
                            "No file was selected.",
                            JOptionPane.ERROR_MESSAGE);
	            }
			}
		});
		imgButton.setBounds(182, 246, 120, 29);
		add(imgButton);

		lblNewLabel = new JLabel("Username:");
		lblNewLabel.setBounds(102, 297, 69, 16);
		add(lblNewLabel);

		lblNewLabel_1 = new JLabel("Password:");
		lblNewLabel_1.setBounds(102, 342, 69, 16);
		add(lblNewLabel_1);

		registerButton = new JButton("Sign Up");
		registerButton.setBounds(102, 383, 287, 29);
		registerButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Register.register(usernameField.getText(), new String(passwordField.getPassword()), selectedFile);
			}
		});
		add(registerButton);

		lblNewLabel_2 = new JLabel("New label");
		File projectImgFile = new File("src/assets/project_image.png");
		ImageIcon projectIcon = new ImageIcon(projectImgFile.getAbsolutePath());
		lblNewLabel_2.setIcon(new ImageIcon(projectIcon.getImage().getScaledInstance(350, 520, Image.SCALE_SMOOTH)));
		lblNewLabel_2.setBounds(484, 6, 350, 520);
		add(lblNewLabel_2);

		backButton = new JButton("Back");
		backButton.setBounds(182, 424, 120, 29);
		backButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				MainGUI.switchScreen("login");
			}
		});
		add(backButton);
		
		lblPleaseChooseThe = new JLabel("The image should be cropped to a 5:6 aspect ratio for optimal display.");
		lblPleaseChooseThe.setHorizontalAlignment(SwingConstants.CENTER);
		lblPleaseChooseThe.setBounds(6, 218, 466, 16);
		add(lblPleaseChooseThe);
	}

}
