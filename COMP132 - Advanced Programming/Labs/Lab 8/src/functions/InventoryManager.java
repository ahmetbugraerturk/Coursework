package functions;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Pattern;

import item.InventoryItem;

public class InventoryManager {
	
	private static final Pattern ID_PATTERN = Pattern.compile("^[A-Z]{2}\\d{4}[*#@]$");
	private static final Pattern DATE_PATTERN = Pattern.compile("\\d{4}-((0\\d)|(1[012]))-(([012]\\d)|(3[01]))");
	
	public boolean isItemIDValid(InventoryItem item) {
		return ID_PATTERN.matcher(item.getItemID()).matches();
	}
	
	public boolean isValidDate(String dateStr) {
		return DATE_PATTERN.matcher(dateStr).matches();
	}
	
	public String generateItemCode(InventoryItem item) {
		String code = "";
		for (int i = 2; i>-1; i--)
			code += item.getName().charAt(i);
		code = code.toUpperCase();
		code += item.getItemID().substring(4,6);
		code += item.getItemID().charAt(3);
		return code;
	}
	
	public Map<String, Double> inventoryValueCalc(List<InventoryItem> items) {
		Map<String, Double> val = new LinkedHashMap<>();
		
		for (InventoryItem i: items) {
			val.put(i.getName(), i.getPrice()*i.getQuantity());
		}
		
		return val;
	}

}
