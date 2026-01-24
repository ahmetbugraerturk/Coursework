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

import item.ExpirableItem;
import item.InventoryItem;
import item.Item;
import functions.InventoryManager;
import functions.InventoryFilter;
import util.FileUtils;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        String filePath = "src/inventory.txt";
        InventoryManager manager = new InventoryManager();

        List<InventoryItem> items = FileUtils.readInventoryItems(filePath, manager);

        List<Item> genericItems = new ArrayList<>(items);

        System.out.println("\nAll Inventory Items:");
        for (InventoryItem item : items) {
            System.out.println(item);
        }

        // calculate total values
        Map<String, Double> values = manager.inventoryValueCalc(items);
        System.out.println("\nInventory Values:");
        for (Map.Entry<String, Double> e : values.entrySet()) {
            System.out.println(e.getKey() + ": " + e.getValue());
        }

        // filter and transform
        InventoryFilter filter = new InventoryFilter();
        Map<String, Double> filtered = filter.removeBasedOnValue(values, 100);
        System.out.println("\nFiltered (for >=100 and doubled):");
        for (Map.Entry<String, Double> e : filtered.entrySet()) {
            System.out.println(e.getKey() + ": " + e.getValue());
        }
        System.out.println();

        // order by ascension
        System.out.println("\nOrdering by ascension: ");
        filter.orderByAscension(genericItems);
        for (Object o : genericItems) {
            System.out.println(o);
        }

        // find maximum priced item
        InventoryItem mostExpensive = (InventoryItem) filter.findMaximum(genericItems);
        System.out.println("\nMost expensive item: " + mostExpensive);

        System.out.println("\nItems before Discount:");
        for (Object o : genericItems) {
            if (o instanceof Integer)
                System.out.println("Integer: " +o);
            else
                System.out.println(o);
        }

        // discount
        filter.makeDiscount(genericItems, 20);
        System.out.println();

        System.out.println("\nItems after Discount:");
        for (Object o : genericItems) {
            if (o instanceof Integer)
                System.out.println("Integer: " +o);
            else
                System.out.println(o);
        }
        
        System.out.println("\n---------------------INLAB---------------------");

		List<ExpirableItem> exItems = new ArrayList<>();
		exItems.add(new ExpirableItem("EL1234*", "Milk", 2.50, 30, "2025-06-01"));

		exItems.add(new ExpirableItem("CL5678#", "Cheese", 5.00, 10, "30-05-2025"));

		exItems.add(new ExpirableItem("FO9012#", "Eggs", 3.00, 6, "2025-5-12"));

		exItems.add(new ExpirableItem("DX3456*", "Yoghurt", 7.00, 15, "2025-05-20"));

		exItems.add(new ExpirableItem("EB7890@", "Tomato Paste", 13.00, 12, "2025-05-25"));

		filter.removeInvalidExpiryDates(exItems, manager);

		System.out.println("\nExpirable items after checking validity: ");

		for (Object o : exItems)
			System.out.println(o);

		System.out.println("\nRemoving expired items.");
		exItems = filter.removeExpired(exItems, "2025-05-23");

		System.out.println("\nExpirable items before Discount: ");

		for (Object o : exItems)
			System.out.println(o);

		filter.makeDiscount(exItems, 20);

		System.out.println("\nExpirable items after Discount: ");

		for (Object o : exItems)
			System.out.println(o);

		List<Item> mixedItems = new ArrayList<>();
		mixedItems.addAll(genericItems);
		mixedItems.addAll(exItems);

		System.out.println("\nMixed List after reversal: ");

		filter.reverse(mixedItems);

		for (Object o : mixedItems)
			System.out.println(o);

    }
}
