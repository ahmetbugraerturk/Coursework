package item;

public class InventoryItem extends Item {
	
	private String itemID;
	private String name;
	private String code;
	private int quantity;

	public InventoryItem(String itemID, String name, double price, int quantity) {
		super(price);
		this.itemID = itemID;
		this.name = name;
		this.quantity = quantity;
	}
	
	public String getItemID() {
		return itemID;
	}
	
	public String getName() {
		return name;
	}
	
	public int getQuantity() {
		return quantity;
	}
	
	public void setCode(String code) {
		this.code = code;
	}
	
	@Override
	public String toString() {
		return String.format("ID: %s, Name: %s, Code: %s, Price: %.2f, Quantity: %d", itemID, name, code, price, quantity);
	}

	@Override
	public int compareTo(Item o) {
		// TODO Auto-generated method stub
		if (this.price<o.price)
			return -1;
		else if (this.price>o.price)
			return 1;
		else
			return 0;
	}

}
