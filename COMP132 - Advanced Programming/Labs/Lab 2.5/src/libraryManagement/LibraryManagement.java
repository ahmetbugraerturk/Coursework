/* *********** Pledge of Honor ************************************************ *

I hereby certify that I have completed this lab assignment on my own
without any help from anyone else. I understand that the only sources of authorized
information in this lab assignment are (1) the course textbook, (2) the
materials posted at the course website and (3) any study notes handwritten by myself.
I have not used, accessed or received any information from any other unauthorized
source in taking this lab assignment. The effort in the assignment thus belongs
completely to me.
READ AND SIGN BY WRITING YOUR NAME SURNAME AND STUDENT ID
SIGNATURE: Ahmet Buğra Ertürk, 86877
********************************************************************************/

package libraryManagement;
public class LibraryManagement {
	public static void main(String[] args) {
        // Define arrays for book titles and their prices
        String[] bookTitles = {"The Hobbit", "1984", "Dune", "The Catcher in the Rye", "The Alchemist", "Pride and Prejudice", "Hamlet"};
        double[] bookPrices = {10.50, 8.75, 15.00, 12.25, 9.50, 7.80, 11.40};
        String[] library1 = {"The Hobbit", "1984", "Dune", "Hamlet", "Pride and Prejudice", "The Catcher in the Rye", "The Alchemist"};
        String[] library2 = {"The Great Gatsby", "Hamlet", "The Alchemist", "Dune", "Frankenstein", "1984"};

        System.out.print("\nThe original book collection: ");
        printCollection(bookTitles, bookPrices);

        // 1. Sort books by price in descending order
        sortByPriceDescending(bookTitles, bookPrices);
        System.out.print("\nThe books sorted by price (descending) are: \n");
        printCollection(bookTitles, bookPrices);
        System.out.println("\n\nExpected: Dune, The Catcher in the Rye, Hamlet, The Hobbit, The Alchemist, 1984, Pride and Prejudice");

        // 2. Sort books by price in ascending order
        sortByPriceAscending(bookTitles, bookPrices);
        System.out.print("\n\nThe books sorted by price (ascending) are: ");
        printCollection(bookTitles, bookPrices);
        System.out.println("\n\nExpected: Pride and Prejudice, 1984, The Alchemist, The Hobbit, Hamlet, The Catcher in the Rye, Dune");

        // 3. Calculate the total cost of books in the collection
        double totalCost = calculateTotalCost(bookPrices);
        System.out.println("\n\nThe total cost of books in the collection is $" + totalCost);
        System.out.println("Expected: $75.20");

        // 4. Find the most expensive book in the collection
        String mostExpensive = findMostExpensive(bookTitles, bookPrices);
        System.out.println("\nThe most expensive book in the collection is " + mostExpensive);
        System.out.println("Expected: Dune");

        // 5. Remove a book from the collection by title
        String[] updatedTitles = removeBook(bookTitles, bookPrices, "Dune");
        System.out.print("\nAfter removing Dune, the collection contains: ");
        printArray(updatedTitles);
        System.out.println("Expected: The Hobbit, 1984, The Catcher in the Rye, The Alchemist, Pride and Prejudice, Hamlet");
        
        // 6. Find common books
        findCommonBooks(library1, library2);
        System.out.println("Expected:\n Number of common Books: 4\nCommon books: [1984, Dune, Hamlet, The Alchemist]");

        // inlab test code in main method
        
        System.out.print("\n\n--------------- In Lab ---------------\n");
        findUniqueBooks(library1, library2);
        random2dArray(5,3,10);
    }

    // This method should sort books by price in ascending order.
    // TODO: Implement this method using the approach in sortByPriceDescending.
    public static void sortByPriceAscending(String[] titles, double[] prices) {
        // Implementation required
    	int i, j;
        for (i = 0; i < prices.length - 1; i++) {
            int minIndex = i;
            for (j = i + 1; j < prices.length; j++) {
                if (prices[j] < prices[minIndex]) {
                    minIndex = j;
                }
            }
            // Swap prices
            swap(prices, i, minIndex);

            // Swap titles accordingly 
            swap(titles, i, minIndex);
        }
    }

    

    // This method should sort books by price in descending order.
    // TODO: FIX this method if needed
    public static void sortByPriceDescending(String[] titles, double[] prices) {
    	int i, j;
        for (i = 0; i < prices.length - 1; i++) {
            int maxIndex = i;
            for (j = i + 1; j < prices.length; j++) {
                if (prices[j] > prices[maxIndex]) {
                    maxIndex = j;
                }
            }
            // Swap prices
            swap(prices, i, maxIndex);

            // Swap titles accordingly 
            swap(titles, i, maxIndex);
        }
    }   

    // This method should swap the contents of two cells in a String array
    // TODO: FIX this method if needed
    public static void swap(String[] array, int firstIndex, int secondIndex){
        String temp = array[firstIndex];
        array[firstIndex] = array[secondIndex];
        array[secondIndex] = temp;
    }

    // This method should swap the contents of two cells in a double array
    // TODO: FIX this method if needed
    public static void swap(double[] array, int firstIndex, int secondIndex){
        double temp = array[firstIndex];
        array[firstIndex] = array[secondIndex];
        array[secondIndex] = temp;
    }

    // TODO: FIX this method
    public static double calculateTotalCost(double[] prices) {
        double total = 0;
        for (double price : prices) {
            total += price;
        }
        return total;
    }

    // TODO: FIX this method
    public static String findMostExpensive(String[] titles, double[] prices) {
        int maxIndex = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[maxIndex]) {
                maxIndex = i;
            }
        }
        return titles[maxIndex];
    }

    // TODO: FIX this method to remove a book by title
    public static String[] removeBook(String[] titles, double[] prices, String bookToRemove) {
        int newSize = titles.length - 1;
        String[] newTitles = new String[newSize];
        double[] newPrices = new double[newSize];

        int j = 0;
        for (int i = 0; i < titles.length; i++) {
            if (!titles[i].equals(bookToRemove)) {
                newTitles[j] = titles[i];
                newPrices[j] = prices[i];
                j++;
            }
        }
        return newTitles;
    }

    // This method should find the common books between the two given libraries.
    public static void findCommonBooks(String[] library1, String[] library2) {
        // Implementation required
    	String[] commons = new String[(library1.length > library2.length ? library2.length : library1.length)];
    	int c = 0;
    	for (int i = 0; i<library1.length; i++) {
    		for (int j = 0; j<library2.length; j++) {
    			if (library1[i].equals(library2[j])) {
    				commons[c] = library1[i];
    				c++;
    			}
    		}
    	}

        System.out.printf("Number of common Books: %d\nCommon books: [", c);
        
    	for (int i = 0; i<c; i++) {
            System.out.printf((i != 0 ? ", %s" : "%s"), commons[i]);
    	}
    	System.out.println("]");
    }

    // Helper method to print the collection (DO NOT MODIFY)
    public static void printCollection(String[] titles, double[] prices) {
        System.out.print("\n[");
        for (int i = 0; i < titles.length; i++) {
            System.out.print(titles[i] + " ($" + prices[i] + ")");
            if (i != titles.length - 1) {
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }

    // Helper method to print an array (DO NOT MODIFY)
    public static void printArray(String[] array) {
    	System.out.print("[");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i]);
            if (i != array.length - 1) { 
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
    
    //////////////////////////////////////////////////////// In lab test code will be added below//////////////////////////////////////////////////////////////////////

    public static void findUniqueBooks(String[] library1, String[] library2) {
    	int c = 0;
    	for (int i = 0; i<library1.length; i++) {
    		for (int j = 0; j<library2.length; j++) {
    			if (library1[i].equals(library2[j])) {
    				library1[i] = null;
    				c++;
    				break;
    			}
    		}
    	}
    	
    	String[] unique = new String[library1.length-c];

    	int x = 0;
    	for (String b: library1) {
    		if (b != null) {
    			unique[x] = b;
    			x++;
    		}
    	}

        System.out.printf("Number of books unique to library1: %d\nUnique books: [", library1.length-c);
        
    	for (int i = 0; i<x; i++) {
            System.out.printf((i != 0 ? ", %s" : "%s"), unique[i]);
    	}
    	System.out.println("]");
    }
    
    public static void random2dArray(int firstDimension, int secondDimension, int upperLimit) {
    	int[][] a = new int[firstDimension][secondDimension];
    	for (int i = 0; i < firstDimension; i++) {
    		for (int j = 0; j < secondDimension; j++) {
        		a[i][j]=(int) (Math.random() * upperLimit);
        	}
    	}
    }
    
}
