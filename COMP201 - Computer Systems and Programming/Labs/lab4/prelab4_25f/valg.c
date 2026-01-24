#include <stdio.h>
#include <stdlib.h>

void allocate_and_process_2d(int rows, int cols) {
    int **matrix = (int **)malloc(rows * sizeof(int *)); // Allocate array of pointers

    if (!matrix) {
        printf("Memory allocation failed!\n");
        return;
    }

    // Allocate memory for each row
    for (int i = 0; i < rows; i++) {
        matrix[i] = (int *)malloc(cols * sizeof(int));
        if (!matrix[i]) {
            printf("Memory allocation failed at row %d!\n", i);
            return;
        }
    }

    // Fill matrix with values
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = i * cols + j;
        }
    }

    // Print the matrix
    printf("Matrix:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", matrix[i][j]);
        }
	free(matrix[i]);
        printf("\n");
    }

    free(matrix);
}

int main() {
    allocate_and_process_2d(3, 4);
    return 0;
}
