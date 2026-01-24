#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h> // Added for tolower()

/******* COMP201 In-Lab3 ASSIGNMENT *******/

// WRITE YOUR NAME HERE

/*
 * Finds the largest element in a given 'int' array.
 * Returns -1 if the array is empty or the size is 0.
 */
int findMaxInArray(int arr[], int size) {
    // If the array is not empty or the size is not 0
    if (size != 0 || arr == NULL){
	// Store the first element of the array as max
    	int max = arr[0];
	int i;
	// Iterate elements in array
	for (i = 1; i < size; i++){
	    // If the current element in array is bigger than max, update max
	    if (max<arr[i])
		    max = arr[i];
	}
	return max;
    }
    return -1;
}
 
/*
 * Reverses a given string in-place.
 * The function must modify the original 'str' pointer.
 * Example: "hello" -> "olleh"
 */
void reverseString(char *str) {
    // Your code here
    char *reverse;
    int len = strlen(str);
    int i;
    // Iterate chars in string reversely
    for (i=len-1; i>-1; i--){
	// put the chars in another string
        reverse[len-1-i] = str[i];
    }
    // Indicate the endpoint of the new string
    reverse[len] = '\0';
    // Copy the new string to address of the given string
    strcpy(str, reverse);
}

/* * Checks if a string is a palindrome, ignoring case.
 * A palindrome is a word that reads the same forwards and backwards.
 * The function should return 1 if it is a palindrome, 0 otherwise.
 * Example: "Racecar" -> 1, "hello" -> 0, "Anna" -> 1
*/
int isPalindromeIgnoreCase(const char *str) {
    // Your code here
    int len = strlen(str);
    int i;
    // Iterate the chars of the string until half of the string
    for (i = 0; i<(len/2); i++){
	// Check if the ith char is same as the len-1-ith char
        if (tolower(str[i]) != tolower(str[len-1-i]))
           return 0;
    }
    return 1; // Temporary return value
}



int main() {
    int totalPoints = 0;
    int baseGrade = 1; // Base grade

    // Test cases for findMaxInArray function
    int arr1[] = {10, 20, 5, -3, 50};
    int res1 = findMaxInArray(arr1, 5);
    if (res1 == 50) {
        printf("Test 1: findMaxInArray passed (+10 points)\n");
        totalPoints += 10;
    } else {
        printf("Test 1: findMaxInArray failed (Expected: 50, Got: %d)\n", res1);
    }

    int arr2[] = {-5, -10, -2, -8};
    int res2 = findMaxInArray(arr2, 4);
    if (res2 == -2) {
        printf("Test 2: findMaxInArray passed (+10 points)\n");
        totalPoints += 10;
    } else {
        printf("Test 2: findMaxInArray failed (Expected: -2, Got: %d)\n", res2);
    }

    int arr3[] = {100};
    int res3 = findMaxInArray(arr3, 1);
    if (res3 == 100) {
        printf("Test 3: findMaxInArray passed (+10 points)\n");
        totalPoints += 10;
    } else {
        printf("Test 3: findMaxInArray failed (Expected: 100, Got: %d)\n", res3);
    }

    printf("---\n");

    // Test cases for reverseString function
    // Note: Strings must be defined as arrays to be modifiable
    char revTest1[] = "hello";
    char exp1[] = "olleh";
    reverseString(revTest1);
    if (strcmp(revTest1, exp1) == 0) {
        printf("Test 4: reverseString passed (+10 points)\n");
        totalPoints += 10;
    } else {
        printf("Test 4: reverseString failed (Expected: %s, Got: %s)\n", exp1, revTest1);
    }

    char revTest2[] = "COMP201";
    char exp2[] = "102PMOC";
    reverseString(revTest2);
    if (strcmp(revTest2, exp2) == 0) {
        printf("Test 5: reverseString passed (+10 points)\n");
        totalPoints += 10;
    } else {
        printf("Test 5: reverseString failed (Expected: %s, Got: %s)\n", exp2, revTest2);
    }
    
    char revTest3[] = "a";
    char exp3[] = "a";
    reverseString(revTest3);
    if (strcmp(revTest3, exp3) == 0) {
        printf("Test 6: reverseString passed (+10 points)\n");
        totalPoints += 10;
    } else {
        printf("Test 6: reverseString failed (Expected: %s, Got: %s)\n", exp3, revTest3);
    }

    printf("---\n");

    // Test cases for isPalindromeIgnoreCase function
    int palRes1 = isPalindromeIgnoreCase("Racecar");
    if (palRes1 == 1) {
        printf("Test 7: isPalindromeIgnoreCase 'Racecar' passed (+10 points)\n");
        totalPoints += 10;
    } else {
        printf("Test 7: isPalindromeIgnoreCase 'Racecar' failed (Expected: 1, Got: %d)\n", palRes1);
    }

    int palRes2 = isPalindromeIgnoreCase("Hello");
    if (palRes2 == 0) {
        printf("Test 8: isPalindromeIgnoreCase 'Hello' passed (+10 points)\n");
        totalPoints += 10;
    } else {
        printf("Test 8: isPalindromeIgnoreCase 'Hello' failed (Expected: 0, Got: %d)\n", palRes2);
    }

    int palRes3 = isPalindromeIgnoreCase("Anna");
    if (palRes3 == 1) {
        printf("Test 9: isPalindromeIgnoreCase 'Anna' passed (+10 points)\n");
        totalPoints += 10;
    } else {
        printf("Test 9: isPalindromeIgnoreCase 'Anna' failed (Expected: 1, Got: %d)\n", palRes3);
    }
    
    int palRes4 = isPalindromeIgnoreCase("Noon");
    if (palRes4 == 1) {
        printf("Test 10: isPalindromeIgnoreCase 'Noon' passed (+10 points)\n");
        totalPoints += 10;
    } else {
        printf("Test 10: isPalindromeIgnoreCase 'Noon' failed (Expected: 1, Got: %d)\n", palRes4);
    }


    // Calculate the final grade (Maximum 100 points + 1 base grade = 101)
    int finalGrade = baseGrade + totalPoints;
    printf("---\n");
    printf("Total Points: %d / 100\n", totalPoints);
    printf("Final Grade: %d\n", finalGrade);

    return 0;
}
