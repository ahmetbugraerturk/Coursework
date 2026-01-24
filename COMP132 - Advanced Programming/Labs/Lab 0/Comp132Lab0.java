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
import java.util.Scanner;

public class Comp132Lab0 {
	// Don't forget to include the Pledge og Honor
	public static void main(String[] args) {


		// TODO:  1.  Define Variables: Define three variables of type double, namely time, powerConsumptionRate, and powerPrice.
		double time;
		double powerConsumptionRate;
		double powerPrice;
		// TODO:  2. User Input: Let the user input three values:

			// time: The total time of the usage (in hour).	
			// powerConsumptionRate: The power consumption rate of the device (in KW per minute).
			// powerPrice: The price of power per KW (in your local currency).

		// Note: You can use the defined input object of type Scanner to get input from the user.
		Scanner input = new Scanner(System.in);
		
		System.out.print("The total time of the usage (in hour).");
		time = input.nextDouble();
		System.out.print("The power consumption rate of the device (in KW per minute).");
		powerConsumptionRate = input.nextDouble();
		System.out.print("The price of power per KW (in your local currency).");
		powerPrice = input.nextDouble();
		 
		// TODO:  3. Calculation: Write code that calculates the Total power Cost.
                // totalCost = (time * 60) * powerConsumptionRate * powerPrice.
		
		double totalCost = (time * 60) * powerConsumptionRate * powerPrice;

		// TODO:  4. Display the Result: Use System.out.println to display the total cost of the power.

		System.out.println(totalCost);

		// TODO:  5. Personalize with Your Information:

			// Define an object of type String, and store the string values of your name and surname in this object.
		String nameSurname = "Ahmet Buğra Ertürk";
			// Define a variable of type int, and store your KUSIS ID number in this variable.
		int kusisID = 86877;
			// Use System.out.println to display your name, surname, and KUSIS ID number.
		System.out.println(nameSurname + " " + kusisID);

		// TODO:  6. Explore Unicode: Write the code for displaying the integer equivalents of the letters in your name and surname.
		for (int i = 0; i<nameSurname.length(); i++) {
			System.out.printf("Character %c has the value %d%n", nameSurname.charAt(i), ((int) nameSurname.charAt(i)));
		}
	}

}
