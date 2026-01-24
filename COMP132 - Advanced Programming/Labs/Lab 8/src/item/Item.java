package item;

public abstract class Item implements Comparable<Item> {
	
	protected double price;
	
	public Item(double price) {
		this.price = price;
	}
	
	public double getPrice() {
		return price;
	}
	
	public void setPrice(double price) {
		this.price = price;
	}

}
