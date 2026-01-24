// I am Ahmet Buğra Ertürk. I declare hereby that I have completed this assignment with honesty and integrity.

#include <stdio.h>
#include <stdlib.h>

/* Function prototypes */
int* partitionByThreshold(int* arr, int N, int threshold, int* newSize);
int* extractDiagonal(int** matrix, int rows, int cols);
void freeArray(int* arr);
void testPartitionByThreshold();
void testExtractDiagonal();

/**
 * Function: testPartitionByThreshold
 * --------------------------
 * Runs test cases for partitionByThreshold.
 */
void testPartitionByThreshold() {
    struct {
        int input[10];
        int N;
        int threshold;
        int expected[10];
        int expectedSize;
    } testCases[] = {
        // Test 1: Basic case
        {{5, 2, 8, 3, 9, 1}, 6, 4, {5, 8, 9}, 3},
        // Test 2: All elements greater than threshold
        {{10, 15, 20, 25}, 4, 5, {10, 15, 20, 25}, 4},
        // Test 3: No elements greater than threshold
        {{1, 2, 3, 4}, 4, 10, {}, 0},
        // Test 4: Threshold is negative
        {{-5, -2, 3, 7, -1}, 5, 0, {3, 7}, 2},
        // Test 5: Single element greater
        {{1, 2, 3, 10, 4}, 5, 8, {10}, 1},
        // Test 6: Equal to threshold (should not be included)
        {{5, 5, 6, 7, 5}, 5, 5, {6, 7}, 2},
        // Test 7: Large threshold
        {{100, 200, 50, 300}, 4, 150, {200, 300}, 2}
    };

    int numTests = sizeof(testCases) / sizeof(testCases[0]);
    int correct = 0;

    printf("\nRunning automated tests for partitionByThreshold...\n");

    for (int t = 0; t < numTests; t++) {
        printf("\nTest %d:\nOriginal: ", t + 1);
        for (int i = 0; i < testCases[t].N; i++) {
            printf("%d ", testCases[t].input[i]);
        }
        printf("\n");

        // Allocate memory for test case input
        int* arr = (int*)malloc(testCases[t].N * sizeof(int));
        if (!arr) {
            printf("Memory allocation failed for test %d ❌\n", t + 1);
            continue;
        }

        for (int i = 0; i < testCases[t].N; i++) {
            arr[i] = testCases[t].input[i];
        }

        int newSize;
        int* newArr = partitionByThreshold(arr, testCases[t].N, testCases[t].threshold, &newSize);
        
        // Handle case where no elements match (should return NULL)
        if (testCases[t].expectedSize == 0) {
            if (newArr == NULL && newSize == 0) {
                printf("Test %d PASSED ✅\n", t + 1);
                correct++;
            } else {
                printf("Test %d FAILED ❌\n", t + 1);
                printf("Expected NULL with newSize = 0\n");
                printf("Got: newSize = %d\n", newSize);
                if (newArr) freeArray(newArr);
            }
            free(arr);
            continue;
        }

        if (!newArr) {
            printf("Function returned NULL ❌\n");
            free(arr);
            continue;
        }

        // Compare actual output with expected output
        int pass = (newSize == testCases[t].expectedSize);
        for (int i = 0; i < newSize && pass; i++) {
            if (newArr[i] != testCases[t].expected[i]) {
                pass = 0;
            }
        }

        if (pass) {
            printf("Test %d PASSED ✅\n", t + 1);
            correct++;
        } else {
            printf("Test %d FAILED ❌\nExpected: ", t + 1);
            for (int i = 0; i < testCases[t].expectedSize; i++) printf("%d ", testCases[t].expected[i]);
            printf("\nGot: ");
            for (int i = 0; i < newSize; i++) printf("%d ", newArr[i]);
            printf("\n");
        }

        // Free allocated memory
        freeArray(newArr);
        free(arr);
    }
}

/**
 * Function: testExtractDiagonal
 * --------------------------
 * Runs test cases for extractDiagonal.
 */
void testExtractDiagonal() {
    struct {
        int input[5][5];
        int rows;
        int cols;
        int expected[5];
    } testCases[] = {
        // Test 1: 3x3 matrix
        {
            {{1, 2, 3, 0, 0}, {4, 5, 6, 0, 0}, {7, 8, 9, 0, 0}, {0, 0, 0, 0, 0}, {0, 0, 0, 0, 0}},
            3, 3, {1, 5, 9}
        },
        // Test 2: 4x4 matrix
        {
            {{10, 20, 30, 40, 0}, {50, 60, 70, 80, 0}, {90, 100, 110, 120, 0}, {130, 140, 150, 160, 0}, {0, 0, 0, 0, 0}},
            4, 4, {10, 60, 110, 160}
        },
        // Test 3: 2x2 matrix
        {
            {{1, 2, 0, 0, 0}, {3, 4, 0, 0, 0}, {0, 0, 0, 0, 0}, {0, 0, 0, 0, 0}, {0, 0, 0, 0, 0}},
            2, 2, {1, 4}
        },
        // Test 4: 5x5 matrix
        {
            {{1, 2, 3, 4, 5}, {6, 7, 8, 9, 10}, {11, 12, 13, 14, 15}, {16, 17, 18, 19, 20}, {21, 22, 23, 24, 25}},
            5, 5, {1, 7, 13, 19, 25}
        },
        // Test 5: 1x1 matrix
        {
            {{42, 0, 0, 0, 0}, {0, 0, 0, 0, 0}, {0, 0, 0, 0, 0}, {0, 0, 0, 0, 0}, {0, 0, 0, 0, 0}},
            1, 1, {42}
        }
    };

    int numTests = sizeof(testCases) / sizeof(testCases[0]);
    int correct = 0;

    printf("\nRunning automated tests for extractDiagonal...\n");

    for (int t = 0; t < numTests; t++) {
        printf("\nTest %d:\nOriginal Matrix (%dx%d):\n", t + 1, testCases[t].rows, testCases[t].cols);
        for (int i = 0; i < testCases[t].rows; i++) {
            for (int j = 0; j < testCases[t].cols; j++) {
                printf("%d ", testCases[t].input[i][j]);
            }
            printf("\n");
        }

        // Allocate memory for test case matrix
        int** matrix = (int**)malloc(testCases[t].rows * sizeof(int*));
        if (!matrix) {
            printf("Memory allocation failed for test %d ❌\n", t + 1);
            continue;
        }

        for (int i = 0; i < testCases[t].rows; i++) {
            matrix[i] = (int*)malloc(testCases[t].cols * sizeof(int));
            if (!matrix[i]) {
                printf("Memory allocation failed for row %d in test %d ❌\n", i, t + 1);
                for (int k = 0; k < i; k++) free(matrix[k]);
                free(matrix);
                continue;
            }
            for (int j = 0; j < testCases[t].cols; j++) {
                matrix[i][j] = testCases[t].input[i][j];
            }
        }

        // Call the function
        int* diagonal = extractDiagonal(matrix, testCases[t].rows, testCases[t].cols);
        if (!diagonal) {
            printf("Function returned NULL ❌\n");
            for (int i = 0; i < testCases[t].rows; i++) free(matrix[i]);
            free(matrix);
            continue;
        }

        // Compare actual output with expected output
        int pass = 1;
        for (int i = 0; i < testCases[t].rows; i++) {
            if (diagonal[i] != testCases[t].expected[i]) {
                pass = 0;
                break;
            }
        }

        if (pass) {
            printf("Test %d PASSED ✅\n", t + 1);
            correct++;
        } else {
            printf("Test %d FAILED ❌\nExpected: ", t + 1);
            for (int i = 0; i < testCases[t].rows; i++) {
                printf("%d ", testCases[t].expected[i]);
            }
            printf("\nGot: ");
            for (int i = 0; i < testCases[t].rows; i++) {
                printf("%d ", diagonal[i]);
            }
            printf("\n");
        }

        // Free allocated memory
        freeArray(diagonal);
        for (int i = 0; i < testCases[t].rows; i++) free(matrix[i]);
        free(matrix);
    }
}

/**
 * Function: partitionByThreshold
 * --------------------------
 * Takes an array and returns a new dynamically allocated array containing only elements 
 * greater than the threshold value.
 * 
 * Parameters:
 *  - arr: Pointer to a dynamically allocated array of size `N`.
 *  - N: Number of elements in the array.
 *  - threshold: The threshold value for filtering.
 *  - newSize: Pointer to store the size of the new allocated array.
 * 
 * Returns:
 *  - A newly allocated array containing only elements greater than threshold.
 *  - NULL if no elements are greater than threshold (newSize should be set to 0).
 * 
 * Instructions:
 *  - Count how many elements are greater than threshold.
 *  - Allocate exact memory needed: malloc(count * sizeof(int)).
 *  - Copy only elements greater than threshold, preserving order.
 *  - Update newSize with the count of filtered elements.
 */
int* partitionByThreshold(int* arr, int N, int threshold, int* newSize) {
    int i;
    int new=0;
    // First, count number of element over threshold
    for (i=0;i<N;i++){
	if(arr[i]>threshold){
 	    new++;
	}
    }
    // Allocate memory with new element size
    int *newArr = malloc(new*sizeof(int));
    *newSize = new;
    new = 0;
    // Copy values in new array
    for (i=0;i<N;i++){
        if(arr[i]>threshold){
	    newArr[new]=arr[i];
	    new++;
	}
    }
    if (new==0)
	    return NULL;
    return newArr;
}

/**
 * Function: extractDiagonal
 * --------------------------
 * Extracts the main diagonal from a 2D matrix and returns it as a new dynamically allocated 1D array.
 * 
 * Parameters:
 *  - matrix: Pointer to a 2D array (square matrix).
 *  - rows: Number of rows in the matrix.
 *  - cols: Number of columns in the matrix.
 * 
 * Returns:
 *  - A newly allocated 1D array containing the main diagonal elements.
 * 
 * Instructions:
 *  - You can assume the input matrix will always be square (rows == cols).
 *  - Dynamically allocate memory for a 1D array of size `rows`.
 *  - Copy diagonal elements: matrix[0][0], matrix[1][1], ..., matrix[rows-1][rows-1].
 *  - Return the pointer to the newly allocated array.
 */
int* extractDiagonal(int** matrix, int rows, int cols) {
    // Allocate memory for new array
    int *newArr = malloc(rows*sizeof(int));
    int i;
    // Copy the values on diagonal into new array
    for (i=0;i<rows;i++){
        newArr[i] = matrix[i][i];
    }
    return newArr;
}

/**
 * Function: freeArray
 * --------------------
 * Frees a dynamically allocated array.
 * 
 * Parameters:
 *  - arr: Pointer to the dynamically allocated array.
 * Note:
    * - This function will be called by the tester to free the array.
    * - You do not need to call this function in your code.
 */
void freeArray(int* arr) {
    free(arr);
    return;
}

int main() {
    testPartitionByThreshold();
    testExtractDiagonal();

    return 0;
}
