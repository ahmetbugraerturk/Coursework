/* *********** Pledge of Honor *************************** *
I hereby certify that I have completed this lab assignment on my own
without any help from anyone else. I understand that the only sources of authorized
information in this lab assignment are (1) the course textbook, (2) the
materials posted at the course website and (3) any study notes handwritten by myself.
I have not used, accessed or received any information from any other unauthorized
source in taking this lab assignment. The effort in the assignment thus belongs
completely to me.

READ AND SIGN BY WRITING YOUR NAME SURNAME AND STUDENT ID
SIGNATURE: Ahmet Buğra Ertürk, 86877

**********************************************************/
package main;

import java.util.Scanner;
import game.GalacticChallenge;

public class Main {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the name of player 1: ");
        String name1 = scanner.nextLine();
        System.out.print("Enter the name of player 2: ");
        String name2 = scanner.nextLine();
        System.out.print("Enter the number of rounds of the game: ");
        int rounds = scanner.nextInt();
        
        
     // in-lab test code 1 ///////////////////////////////////////////////////////////
        System.out.print("Enter the score difference of the game: ");
        int scoreDif = scanner.nextInt();
        ///////////////////////////////////////////////////////////
        
        scanner.close();
        
        GalacticChallenge duel = new GalacticChallenge(name1, name2, rounds);
        duel.runGame();
        duel.printWinner();
        
        
     // in-lab test code 2 ///////////////////////////////////////////////////////////
        System.out.print("\n\n------------------------ In lab ------------------------\n");
        GalacticChallenge inlabDuel = new GalacticChallenge(name1, name2, rounds,
        scoreDif);
        inlabDuel.inLabRun();
        inlabDuel.printWinner();
        ///////////////////////////////////////////////////////////
        
       

        
    }
}
