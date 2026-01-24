package item;

public class ExpirableItem extends Item {
	
	private String itemID;
	private String name;
	private int quantity;
	private String expiryDate;
	
	public ExpirableItem(String itemID, String name, double price, int quantity, String expiryDate) {
		super(price);
		this.itemID = itemID;
		this.name = name;
		this.quantity = quantity;
		this.expiryDate = expiryDate;
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
	
	public String getExpiryDate() {
		return expiryDate;
	}
	
	@Override
	public String toString() {
		return String.format("ID: %s, Name: %s, Price: %.2f, Qty: %d, Expires: %s", itemID, name, price, quantity, expiryDate);
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
