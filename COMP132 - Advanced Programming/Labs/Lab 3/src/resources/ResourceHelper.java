package resources;

public class ResourceHelper {
	
	public static int[][] deepCopy(int[][] grid) {
		int[][] newGrid = new int[grid.length][];
		for (int i = 0; i<grid.length; i++) {
			int[] newRow = new int[grid[i].length];
			for (int j = 0; j<grid[i].length; j++) {
				newRow[j] = grid[i][j];
			}
			newGrid[i] = newRow;
		}
		return newGrid;
	}
	
	public static boolean areSameSize(int[][] grid1, int[][] grid2) {
		boolean areSame = true;
		if (grid1.length != grid2.length) 
			areSame = false;
		else {
			for (int i = 0; i<grid1.length; i++) {
				if(grid1[i].length != grid2[i].length)
					areSame = false;
			}
		}
		return areSame;
	}

}
