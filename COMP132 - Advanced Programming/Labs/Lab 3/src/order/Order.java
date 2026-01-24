package order;

import resources.ResourceGrid;
import java.util.ArrayList;


public class Order {
	
	private int[][] orderGrid;
	
	public Order(int[][] orderGrid) {
		this.orderGrid = orderGrid;
	}
	
	public boolean canMultiply(ResourceGrid grid) {
		if (grid.getResources()[0].length == orderGrid.length) {
			return true;
		}
		return false;
	}
	
	public ResourceGrid makeOrder(ResourceGrid grid) {
		if (canMultiply(grid)) {
			int[][] gr = grid.getResources();
			int[][] mult = new int[gr.length][orderGrid[0].length];
			for (int i = 0; i < gr.length; i++) {
				for (int j = 0; j<orderGrid[0].length; j++) {
					int entry = 0;
					for (int k = 0; k<orderGrid.length; k++) {
						entry += orderGrid[k][j]*gr[i][k];
					}
					mult[i][j] = entry;
				}
			}
			return new ResourceGrid(grid.getStationName(), mult);
		} else {
			System.out.println("Multiplication is not possible: Dimension mismatch.");
			return grid;
		}
	}
	
	public void makeOrder(ArrayList<Integer> v) {
		if(orderGrid[0].length!=v.size())
			System.out.println("Multiplication is not possible: Dimension mismatch.");
		else {
			for (int i = 0; i<orderGrid.length; i++) {
				int x = 0;
				for (int j = 0; j<v.size(); j++) {
					x += orderGrid[i][j]*v.get(j);
				}
				System.out.printf("[ %d ]%n", x);
			}
		}
	}

}
