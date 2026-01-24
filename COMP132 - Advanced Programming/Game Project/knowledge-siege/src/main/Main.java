/* *********** Pledge of Honor ************************************************ *

I hereby certify that I have completed this lab assignment on my own
without any help from anyone else. I understand that the only sources of authorized
information in this lab assignment are (1) the course textbook, (2) the
materials posted on the course website, and (3) any study notes handwritten by myself.
I have not used, accessed, or received any information from any other unauthorized
source in taking this lab assignment. The effort in the assignment thus belongs
completely to me.
READ AND SIGN BY WRITING YOUR NAME SURNAME, AND STUDENT ID
SIGNATURE: <Ahmet Buğra Ertürk, 86877>
********************************************************************************/
package main;

import java.io.File;

import javax.swing.UIManager;

import knowledge_keepers.Professor;
import knowledge_keepers.SL;
import knowledge_keepers.TA;
import shot_boxes.informations.Informations;
import shot_boxes.questions.Questions;

/**
 * The Main class is the entry point of the application.
 * It initializes questions, information, and knowledge keepers (Professors, TAs, SLs),
 * loads their images, and starts the {@link MainGUI}.
 * 
 * <p> The program reads question and information data from files,
 * and assign images to knowledge keepers based on predefined lists.</p>
 * 
 * @author Ahmet Buğra Ertürk
 * @version 1.0
 */
public class Main {
	
	private static final String[] professors = {"Öznur Özkasap", "Attila Gürsoy"};
	private static final String[] TAs = {"Vahideh Hayyolalam", "Abdulrezzak Zekiye", "Hamza Abuzahra", "Fatma Nur Yaşar", "Aylanur Ertürk"};
	private static final String[] SLs = {"Efe Değişmiş", "Ekin Gün", "Ahmet Şükrü Kılıç", "Nazrin Mustafazadeh", "Ozan Özak", "Abdullah Daoud", "Ertuğrul Recep Kocaman", "Burak Gerçekaslan"};
	
	private static final String[] extensions = {"png", "jpg", "jpeg"};
	
	/**
     * The main method initializes questions, information, knowledge keepers, 
     * and launches the {@link MainGUI}.
     *
     * @param args command line arguments (not used)
     */
	public static void main(String[] args) {
		try {
            UIManager.setLookAndFeel(UIManager.getCrossPlatformLookAndFeelClassName());
        } catch (Exception e) {
            e.printStackTrace();
        }
		Questions.uploudQuestions("src/assets/questions.txt");
		Informations.uploudInformations("src/assets/informations.txt");
		for (String p: professors) {
			File f = null;
			for (String ext : extensions) {
				f = new File("src/assets/keepers/" + p + "." + ext);
				if (f.exists())
			        break;
			}
			new Professor(p, f);
		}
		for (String t: TAs) {
			File f = null;
			for (String ext : extensions) {
				f = new File("src/assets/keepers/" + t + "." + ext);
				if (f.exists())
			        break;
			}
			new TA(t, f);
		}
		for (String s: SLs) {
			File f = null;
			for (String ext : extensions) {
				f = new File("src/assets/keepers/" + s + "." + ext);
				if (f.exists())
			        break;
			}
			new SL(s, f);
		}
		MainGUI.call();
	}
}
