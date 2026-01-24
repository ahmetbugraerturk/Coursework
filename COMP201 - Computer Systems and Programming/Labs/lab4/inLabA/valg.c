#include <stdio.h>
#include <stdlib.h>

int** create_matrix(int rows, int cols) {
    int** matrix = (int**)malloc(rows * sizeof(int*));
    if (!matrix) {
        printf("Memory allocation failed!\n");
        return NULL;
    }
    
    for (int i = 0; i < rows; i++) {
        matrix[i] = (int*)malloc(cols * sizeof(int));
        if (!matrix[i]) {
            printf("Memory allocation failed for row %d!\n", i);
            return NULL;
        }
        
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = (i + 1) * (j + 1);
        }
    }
    
    return matrix;
}

void process_matrices() {
    int sizes[3][2] = {{2, 3}, {3, 2}, {4, 4}};
    
    for (int k = 0; k < 3; k++) {
        int rows = sizes[k][0];
        int cols = sizes[k][1];
        
        int** mat = create_matrix(rows, cols);
        if (mat) {
            printf("\nMatrix %d (%dx%d):\n", k + 1, rows, cols);
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    printf("%d ", mat[i][j]);
                }
		// I freed rows in matrix
		free(mat[i]);
                printf("\n");
            }
	    // I freed matrix array
	    free(mat);
        }
    }
    
    printf("\nAll matrices created successfully!\n");
}

int main() {
    process_matrices();
    return 0;
}
