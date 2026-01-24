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

import order.Order;
import resources.*;
import java.util.ArrayList;
import java.util.Arrays;

public class ResourceMain {
    public static void main(String[] args) {
        // Don't forget to include the Pledge of Honor

        int[][] storage1 = {{3, 2, 1}, {5, 6, 4}, {7, 3, 9}};
        int[][] storage2 = {{1, 4, 2}, {6, 8, 3}, {2, 1, 7}};
        int[][] storage3 = {{3, 2}, {5, 6}, {7, 3}};
        int[][] order1 = {{2, 2, 3}, {5, 2, 4}, {4, 4, 3}};
        int[][] order2 = {{4, 9}, {6, 3}, {5, 2}};
        int[][] order3 = {{2, 2}, {4, 4}, {3, 3}};

        ResourceGrid alpha = new ResourceGrid("Alpha", storage1);
        ResourceGrid beta = new ResourceGrid("Beta", storage2);
        ResourceGrid gamma = new ResourceGrid();
        ResourceGrid omega = new ResourceGrid("Omega", storage3);

        Order orderAlpha = new Order(order1);
        Order orderBeta = new Order(order2);
        Order orderOmega = new Order(order3);

        System.out.println("--- Initial Storage ---\n");
        System.out.println("  Storage 1 ---\n");
        System.out.println(alpha);
        System.out.println("  Storage 2 ---\n");
        System.out.println(beta);

        System.out.println("--- New Storage at Alpha after transfer ---\n");
        alpha.transferResources(beta);
        System.out.println("--- Original Alpha  Storage was ---\n");
        System.out.println(alpha);
        System.out.println("--- New Storage at Alpha after depleting Resources ---\n");
        alpha.depleteResources(beta);
        System.out.println("--- Original Alpha  Storage was ---\n");
        System.out.println(alpha);
        alpha.scaleResources(2);
        alpha.redistributeResources();
        alpha.transferResources(omega);
        beta.checkIfBalanced();
        gamma.checkIfEmptyStorage();
        alpha.checkIfMajorityResource(5);

        System.out.println("\n--- Processing orders for Alpha Storage ---\n");
        alpha = orderAlpha.makeOrder(alpha);
        System.out.println(alpha);

        System.out.println("--- Processing orders for Beta Storage ---\n");
        beta = orderBeta.makeOrder(beta);
        System.out.println(beta);

        System.out.println("--- Processing orders for Omega Storage ---\n");
        omega = orderOmega.makeOrder(omega);
        System.out.println(omega);
        
     // in-lab test code ///////////////////////////////////////////////////////////
        System.out.println("===================== Inlab =====================");
        System.out.println("\n--- Calculating trace for " + alpha.getStationName() + "---\n");
        alpha.trace();
        System.out.println("\n--- Calculating trace for " + beta.getStationName() + "---\n");
        beta.trace();
        System.out.println("\n--- Flattening " + alpha.getStationName() + "---\n");
        ArrayList<Integer> alphaFlattened = alpha.flatten();
        System.out.println(alphaFlattened);
        System.out.println("\n--- Flattening " + beta.getStationName() + "---\n");
        ArrayList<Integer> betaFlattened = beta.flatten();
        System.out.println(betaFlattened);
        int[][] order4 = {{1, 1, 2}, {2, 1, 3}, {1, 4, 2}};
        ArrayList<Integer> arrList1 = new ArrayList<>(Arrays.asList(3, 1, 2));
        ArrayList<Integer> arrList2 = new ArrayList<>(Arrays.asList(3, 1, 2, 1));
        Order order = new Order(order4);
        System.out.println("\n--- Processing order with ArrayList 1 ---\n");
        order.makeOrder(arrList1);
        System.out.println("\n--- Processing order with ArrayList 2 ---\n");
        order.makeOrder(arrList2);
        ///////////////////////////////////////////////////////////

    }
}
