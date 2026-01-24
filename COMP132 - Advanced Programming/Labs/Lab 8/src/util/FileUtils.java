package util;

import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import functions.InventoryManager;
import item.InventoryItem;

public class FileUtils {

	public static List<InventoryItem> readInventoryItems(String filePath, InventoryManager manager) {
		List<InventoryItem> newList = new ArrayList<>();
		try (Scanner s = new Scanner(Paths.get(filePath))){
			while (s.hasNext()) {
				String line = s.nextLine();
				if (line.matches("^.{7},[A-Za-z]+,\\d+\\.\\d+,\\d+$")) {
					String[] parameters = line.split(",");
					InventoryItem item = new InventoryItem(parameters[0], parameters[1], Double.parseDouble(parameters[2]), Integer.parseInt(parameters[3]));
					if (manager.isItemIDValid(item)) {
						item.setCode(manager.generateItemCode(item));
						newList.add(item);
					} else
						System.out.printf("Skipping malformed or invalid line: %s%n", line);
				} else
					System.out.printf("Skipping malformed or invalid line: %s%n", line);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		return newList;
	}
	
}
