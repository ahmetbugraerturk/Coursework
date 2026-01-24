package functions;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import item.ExpirableItem;
import item.Item;

public class InventoryFilter {

	public Map<String, Double> removeBasedOnValue(Map<String, Double> inventoryValues, int n) {
		Map<String, Double> newMap = new LinkedHashMap<>(inventoryValues);
		Iterator<String> keys = inventoryValues.keySet().iterator();
		while (keys.hasNext()) {
			String key = keys.next();
			if (newMap.get(key)<n)
				newMap.remove(key);
			else
				newMap.put(key, newMap.get(key)*2);
		}
		return newMap;
	}
	
	public <T extends Comparable<T>> T findMaximum(List<T> items) {
		T max = items.get(0);
		for (T i: items) {
			if (max.compareTo(i)<0)
				max=i;
		}
		return max;
	}
	
	public <T extends Comparable<T>> List<T> orderByAscension(List<T> list) {
		Collections.sort(list);
		return list;
	}
	
	public <T extends Item> List<T> makeDiscount(List<T> items, int discount) {
		List<T> newList = new ArrayList<>(items);
		for (T t: items) {
			t.setPrice(t.getPrice()*(100-discount)/100);
			newList.add(t);
		}
		return newList;
	}
	
	public <T extends ExpirableItem> void removeInvalidExpiryDates(List<T> items, InventoryManager manager) {
		List<T> newList = new ArrayList<>(items);
		
		for (int i = newList.size()-1; i>-1; i--) {
			T item = newList.get(i);
			if (!manager.isValidDate(item.getExpiryDate())) {
				System.out.printf("Removed item with invalid expiry date: ID: %s, Name: %s, Price: %.2f, Qty: %d, Expires: %s%n", item.getItemID(), item.getName(), item.getPrice(), item.getQuantity(), item.getExpiryDate());
				items.remove(item);
			}
		}
		
	}
	
	public <T extends ExpirableItem> List<T> removeExpired(List<T> items, String date) {
		List<T> newList = new ArrayList<>(items);
		int dateInt = Integer.parseInt(date.replace("-", ""));
		
		for (T item: items) {
			int expiryDateInt = Integer.parseInt(item.getExpiryDate().replace("-", ""));
			if (expiryDateInt<dateInt) {
				newList.remove(item);
			}
		}
		
		return newList;
	}
	
	public <T> void reverse(List<T> list) {
		List<T> newList = new ArrayList<>(list);
		
		for (int i = 0; i<list.size(); i++) {
			list.set(i, newList.get(list.size()-i-1));
		}
	}
	
}
