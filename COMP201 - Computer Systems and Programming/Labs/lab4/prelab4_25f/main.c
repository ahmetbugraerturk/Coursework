// I am Ahmet Buğra Ertürk. I declare hereby that I have completed this assignment with honesty and integrity.

#include <stdio.h>
#include <stdlib.h>

/* Function prototypes */
void testResizeArray();
void testDeepCopyMatrix();
int* resizeArray(int* arr, int oldSize, int newSize);
int** deepCopyMatrix(int** matrix, int rows, int cols);
void freeArray(int* arr);
void freeMatrix(int** matrix, int rows);

/**
 * Function: testResizeArray
 * -------------------------
 * Runs test cases for resizeArray.
 */
void testResizeArray() {
    struct {
        int input[5];      // Input array
        int oldSize;       // Original size
        int newSize;       // New size
        int expected[5];   // Expected result
    } testCases[] = {
        {{1, 2, 3, 4, 5}, 3, 5, {1, 2, 3, 0, 0}},  // Expand array
        {{1, 2, 3, 4, 5}, 5, 2, {1, 2}},           // Shrink array
        {{10, 20, 30}, 3, 3, {10, 20, 30}},        // Same size
        {{5, 10, 15}, 3, 1, {5}},                  // Shrink to 1
        {{7}, 1, 4, {7, 0, 0, 0}}                  // Expand from 1
    };

    int numTests = sizeof(testCases) / sizeof(testCases[0]);
    int correct = 0;

    printf("\nRunning automated tests for resizeArray...\n");

    for (int t = 0; t < numTests; t++) {
        printf("\nTest %d:\nOriginal (size %d): ", t + 1, testCases[t].oldSize);
        for (int i = 0; i < testCases[t].oldSize; i++) {
            printf("%d ", testCases[t].input[i]);
        }
        printf("\n");

        // Allocate memory for test case input
        int* arr = (int*)malloc(testCases[t].oldSize * sizeof(int));
        if (!arr) {
            printf("Memory allocation failed for arr!\n");
            continue; // Skip this test if allocation fails
        }

        for (int i = 0; i < testCases[t].oldSize; i++) {
            arr[i] = testCases[t].input[i];
        }

        int* newArr = resizeArray(arr, testCases[t].oldSize, testCases[t].newSize);

        if (!newArr && testCases[t].newSize > 0) {
            printf("Memory allocation failed for newArr!\n");
            continue; // Skip this test if allocation fails
        }

        // Compare actual output with expected output
        int pass = 1;
        for (int i = 0; i < testCases[t].newSize; i++) {
            if (newArr[i] != testCases[t].expected[i]) {
                pass = 0;
                break;
            }
        }

        if (pass) {
            printf("Test %d PASSED ✅\n", t + 1);
            correct++;
        } else {
            printf("Test %d FAILED ❌\nExpected: ", t + 1);
            for (int i = 0; i < testCases[t].newSize; i++) printf("%d ", testCases[t].expected[i]);
            printf("\nGot: ");
            for (int i = 0; i < testCases[t].newSize; i++) printf("%d ", newArr[i]);
            printf("\n");
        }

        // Free allocated memory using student's freeArray function
        freeArray(newArr);
    }
}


/**
 * Function: testDeepCopyMatrix
 * ----------------------------
 * Runs test cases for deepCopyMatrix.
 */
void testDeepCopyMatrix() {
    struct {
        int input[3][4];  // Input matrix (up to 3x4 for example)
        int rows;         // Number of rows
        int cols;         // Number of columns
    } testCases[] = {
        {
            {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}}, 3, 4
        },
        {
            {{-1, -2, -3, -4}, {-5, -6, -7, -8}, {0, 0, 0, 0}}, 3, 4
        },
        {
            {{4, 5, 6}, {10, 2, 3}, {1, 1, 1}}, 3, 3
        },
        {
            {{100, 200, 300}, {10, 20, 30}, {5, 5, 5}}, 3, 3
        },
        {
            {{-10, -20, -30}, {-5, -15, -25}, {-1, -2, -3}}, 3, 3
        }
    };

    int numTests = sizeof(testCases) / sizeof(testCases[0]);
    int correct = 0;

    printf("\nRunning automated tests for deepCopyMatrix...\n");

    for (int t = 0; t < numTests; t++) {
        printf("\nTest %d:\nOriginal Matrix:\n", t + 1);
        for (int i = 0; i < testCases[t].rows; i++) {
            for (int j = 0; j < testCases[t].cols; j++) {
                printf("%d ", testCases[t].input[i][j]);
            }
            printf("\n");
        }

        // Allocate memory for test case matrix
        int** matrix = (int**)malloc(testCases[t].rows * sizeof(int*));
        if (!matrix) {
            printf("Memory allocation failed for matrix!\n");
            continue; // Skip test if allocation fails
        }

        for (int i = 0; i < testCases[t].rows; i++) {
            matrix[i] = (int*)malloc(testCases[t].cols * sizeof(int));
            if (!matrix[i]) {
                printf("Memory allocation failed for row %d!\n", i);
                // Free already allocated rows before skipping test
                for (int k = 0; k < i; k++) {
                    free(matrix[k]);
                }
                free(matrix);
                continue;
            }

            for (int j = 0; j < testCases[t].cols; j++) {
                matrix[i][j] = testCases[t].input[i][j];
            }
        }

        // Call the student's function
        int** copy = deepCopyMatrix(matrix, testCases[t].rows, testCases[t].cols);

        if (!copy) {
            printf("Memory allocation failed for copy!\n");
            // Free matrix
            for (int i = 0; i < testCases[t].rows; i++) {
                free(matrix[i]);
            }
            free(matrix);
            continue;
        }

        // Compare actual output with expected output
        int pass = 1;
        for (int i = 0; i < testCases[t].rows; i++) {
            for (int j = 0; j < testCases[t].cols; j++) {
                if (copy[i][j] != testCases[t].input[i][j]) {
                    pass = 0;
                    break;
                }
            }
            if (!pass) break;
        }

        // Test independence: modify copy and ensure original is unchanged
        if (pass) {
            copy[0][0] = 9999;
            if (matrix[0][0] == 9999) {
                pass = 0; // Shallow copy detected!
                printf("Test %d FAILED ❌\nDeep copy failed: modifying copy affected original (shallow copy detected)\n", t + 1);
            }
        }

        if (pass) {
            printf("Test %d PASSED ✅\n", t + 1);
            correct++;
        } else if (copy[0][0] != 9999) {
            printf("Test %d FAILED ❌\nExpected matrix values do not match\n", t + 1);
        }

        // Free allocated memory using student's function
        freeMatrix(copy, testCases[t].rows);

        // ✅ Free each row in original matrix
        for (int i = 0; i < testCases[t].rows; i++) {
            free(matrix[i]);
        }

        // ✅ Free the matrix itself
        free(matrix);
    }
}


/**
 * Function: resizeArray
 * ---------------------
 * Resizes a dynamically allocated 1D array.
 * 
 * Parameters:
 *  - arr: Pointer to the original array.
 *  - oldSize: Current size of the array.
 *  - newSize: Desired size of the array.
 * 
 * Returns:
 *  - Pointer to a new dynamically allocated array of size newSize.
 *  - If newSize is 0, return NULL.
 * 
 * Instructions:
 *  - **Allocate memory** for the new array of size newSize.
 *  - **Copy data** from old array (up to min(oldSize, newSize)).
 *  - **If expanding**: initialize new elements to 0.
 *  - **Free the original array** inside this function.
 *  - **Return** the new array.
 */
int* resizeArray(int* arr, int oldSize, int newSize) {
    if (newSize == 0)
	return NULL;
    int* newArr = malloc(newSize * sizeof(int));
    int i;
    if (oldSize >= newSize){
	for (i=0; i<newSize; i++){
	    newArr[i]=arr[i];
	}
    } else {
    	for (i=0; i<oldSize; i++){
	    newArr[i] = arr[i];
	}
	for (; i<newSize; i++){
	    newArr[i]=0;
	}
    }
    return newArr;
}


/**
 * Function: deepCopyMatrix
 * ------------------------
 * Creates a completely independent copy of a 2D matrix.
 * 
 * Parameters:
 *  - matrix: Pointer to a 2D array.
 *  - rows: Number of rows in the matrix.
 *  - cols: Number of columns in the matrix.
 * 
 * Returns:
 *  - Pointer to a new dynamically allocated 2D array (deep copy).
 * 
 * Instructions:
 *  - **Allocate new matrix pointer array**: malloc(rows * sizeof(int*)).
 *  - **For each row**: allocate new row: malloc(cols * sizeof(int)).
 *  - **Copy all values**: copy[i][j] = matrix[i][j].
 *  - **Result must be independent** (modifying copy doesn't affect original).
 */
int** deepCopyMatrix(int** matrix, int rows, int cols) {
    int **copy = malloc(rows*sizeof(int*));
    int i;
    for (i=0; i<rows; i++){
        int *copyRow = malloc(cols * sizeof(int));
	int j;
	for (j=0; j<cols; j++){
	    copyRow[j] = matrix[i][j];
	}
	copy[i] = copyRow;
    }
    return copy;
}


/**
 * Function: freeArray
 * -------------------
 * Frees a dynamically allocated array.
 * 
 * Parameters:
 *  - arr: Pointer to the dynamically allocated array.
 * 
 * Note:
 *  - This function will be called by the tester to free the array.
 *  - You do not need to call this function in your code.
 */
void freeArray(int* arr) {
    free(arr);
}


/**
 * Function: freeMatrix
 * --------------------
 * Frees a dynamically allocated 2D matrix.
 * 
 * Parameters:
 *  - matrix: Pointer to the dynamically allocated 2D array.
 *  - rows: Number of rows in the matrix.
 * 
 * Note:
 *  - This function will be called by the tester to free the matrix.
 *  - You do not need to call this function in your code.
 */
void freeMatrix(int** matrix, int rows) {
    int i;
    for (i=0; i<rows; i++){
        free(matrix[i]);
    }
    free(matrix);
}

int main() {
    testResizeArray();
    testDeepCopyMatrix();
    return 0;
}
