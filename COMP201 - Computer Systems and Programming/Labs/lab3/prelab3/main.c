#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
// If you need to use character classification (e.g., isalpha, isspace),
// you can include <ctype.h> and use those functions if desired.


/******* COMP201 Lab3 ASSIGNMENT *******/

// Ahmet Buğra Ertürk
// 0086877
// I am Ahmet Buğra Ertürk. I declare hereby that I have completed this assignment with honesty and integrity.



/*
 * 1: Convert to Title Case
 * Write a function that converts a string to title case:
 *   - Decapitalize the first letter of each word
 *   - Make all other letters uppercase
 * Example: "Hello WORLD" -> "hELLO wORLD"
 */
void toReverseTitleCase(char *str) {
    // Your code her

    // Make first letter lowercase
    str[0] = tolower(str[0]); 
    // Store currrent char pointer for iteration
    char *CurrentPointer = str+1;

    // Iterate each char in string
    while (*CurrentPointer != '\0'){
       // Check if the previous char space, then make current char lowrcase or uppercase according to previous letter.
       if (isspace((CurrentPointer-1)[0])){
          CurrentPointer[0] = tolower(CurrentPointer[0]);
       } else {
          CurrentPointer[0] = toupper(CurrentPointer[0]);
       }
       // Move pointer to next char.
       CurrentPointer++;
    }
}


/*
 * 2: Remove Duplicates
 * Write a function that removes all duplicate characters from a string.
 * Preserve the order of characters as they first appear.
 * For example, "banana" -> "ban".
 * Function should modify the string in place.
 */
void removeDuplicates(char *str) {
    // Your code here

    // Create a string with the first char of the str argument
    char Seen[255];
    Seen[0] = str[0];
    Seen[1] = '\0';
    // Store current char pointer for iteration
    char *CurrentPointer = str+1;

    // Iterate each char in string
    while (*CurrentPointer != '\0'){
       // Check if the char has been seen before, if not, add this char at the end of the Seen
       if(strchr(Seen, CurrentPointer[0])==NULL){
          strncat(Seen, CurrentPointer, 1);
       }
       // Move pointer next char
       CurrentPointer++;
    }
    // Copy the Seen string to address of str
    strcpy(str, Seen);
}



/*
 * 3: Replace Second Occurrence
 * Write a function that finds the second occurrence of a word in a given 
 * string and replaces it with another word. For simplicity, assume the
 * original and replacement words are the same length.
 * If no second occurrence is found, the function should do nothing.
 */
void replaceSecondOccurrence(char *str, const char *original, const char *replacement) {
    // Your code here

    // Save the pointer at first occurrence
    char *first = strstr(str, original);
    // Save the pointer for second occurence
    char *second = strstr((first+1), original);
    // If second occurence exist, replace it with new one
    if (second != NULL){
       strncpy(second, replacement, strlen(original));
    }
}



/*
 * 4: String Decompression
 * Write a function that decompresses a string by writing consecutive
 * identical characters when they found with the count of those characters. 
 * 
 * For example:
 *  "a2bc2a3" -> "aabcccaaa"
 *  "x4"      -> "xxxx"
 */
void stringDecompression(char *src, char *dest) {
    // Your code here

    // Store current index of the dest
    int CurrentDestIdx = 0;
    // Move char byte forward because of the my implementation
    src++;

    // Iterate each char in the src
    while (*src != '\0'){
       // If the char is digit, the value of the char times previous char is added onto dest string.
       if (isdigit(src[0])){
          int Count = src[0] - '0';
	  int i = 0;
	  for (i = 0; i < Count; i++){
	      dest[CurrentDestIdx] = (src-1)[0];
	      CurrentDestIdx++;
	  }
	  // Termination char is added
	  dest[CurrentDestIdx] = '\0';
       }
       // If the char is repeated once, there is no digit after this char. So if the char and the previous char both are not digit, previous char is added onto dest string.
       else if (!isdigit((src-1)[0])){
          dest[CurrentDestIdx] = (src-1)[0];
	  dest[++CurrentDestIdx] = '\0';
       }
       src++;
    }
}


/*
 * 5: Reverse Word Order in a Sentence
 * Implement a function that reverses the order of words in a sentence 
 * while preserving the letters within each word.
 * For instance, "C programming is fun" -> "fun is programming C".
 */
char* reverseWordOrder(char str1[], char str2[]) {
    // Your code here
 
    // Create Token variable to store the output of strtok
    char *Token;
    // Create a string array to store words
    char *Words[strlen(str1)];
    // Tokenize the string using delimeter
    Token = strtok(str1, " ");
    // Store the current Words index
    int CurWIdx = 0;

    // Iterate the tokens
    while (Token!=NULL){
       // Add the token in words
       Words[CurWIdx] = Token;
       Token = strtok(NULL, " ");
       CurWIdx++;
    }

    int i;
    // Contacate the elements of the Words reversely onto str2 with whitespace
    for (i = CurWIdx-1; i>0; i--){
       strcat(str2, Words[i]);
       strcat(str2, " ");
    }
    strcat(str2, Words[0]);
    
    return str2;
}

int main() {
    int totalPoints = 0;
    /********************************************************
     *                  TESTS for #1                       *
     ********************************************************/
    printf("\n--- Testing toReverseTitleCase ---\n");

    // Test 1-A
    char title1A[] = "hello WORLD";
    // Expected "Hello World"
    toReverseTitleCase(title1A);
    char exp1A[] = "hELLO wORLD";
    printf("Test 1-A expected: \"%s\"\nGot: \"%s\"\n", exp1A, title1A);
    if (strcmp(title1A, exp1A) == 0) {
        printf("Test 1-A passed (+5 points)\n\n");
        totalPoints += 5;
    } else {
        printf("Test 1-A failed\n\n");
    }

    // Test 1-B
    char title1B[] = "mULTiPle WORds ExAMPle";
    // Expected "Multiple Words Example"
    toReverseTitleCase(title1B);
    char exp1B[] = "mULTIPLE wORDS eXAMPLE";
    printf("Test 1-B expected: \"%s\"\nGot: \"%s\"\n", exp1B, title1B);
    if (strcmp(title1B, exp1B) == 0) {
        printf("Test 1-B passed (+5 points)\n\n");
        totalPoints += 5;
    } else {
        printf("Test 1-B failed\n\n");
    }
    /********************************************************
     *                  TESTS for #2                        *
     ********************************************************/
    printf("\n--- Testing removeDuplicates ---\n");

    // Test 2-A
    char dup2A[] = "banana";
    // Expected "ban"
    removeDuplicates(dup2A);
    char exp2A[] = "ban";
    printf("Test 2-A expected: \"%s\"\nGot: \"%s\"\n", exp2A, dup2A);
    if (strcmp(dup2A, exp2A) == 0) {
        printf("Test 2-A passed (+10 points)\n\n");
        totalPoints += 10;
    } else {
        printf("Test 2-A failed\n\n");
    }

    // Test 2-B
    char dup2B[] = "aaaa";
    // All 'a'; should become "a"
    removeDuplicates(dup2B);
    char exp2B[] = "a";
    printf("Test 2-B expected: \"%s\"\nGot: \"%s\"\n", exp2B, dup2B);
    if (strcmp(dup2B, exp2B) == 0) {
        printf("Test 2-B passed (+10 points)\n\n");
        totalPoints += 10;
    } else {
        printf("Test 2-B failed\n\n");
    }



    /********************************************************
     *                  TESTS for #3                        *
     ********************************************************/
    printf("\n--- Testing replaceSecondOccurrence ---\n");

    // Test 3-A
    char str3A[] = "cat cat dog cat bird cat cat";
    // The second occurrence of "cat" in this string is the "cat" before "dog"
    // We'll replace it with "fox" (same length = 3 chars)
    replaceSecondOccurrence(str3A, "cat", "fox");
    // Expected: "cat cat dog fox bird cat cat"
    char exp3A[] = "cat fox dog cat bird cat cat";
    printf("Test 3-A expected: \"%s\"\nGot: \"%s\"\n", exp3A, str3A);
    if (strcmp(str3A, exp3A) == 0) {
        printf("Test 3-A passed (+5 points)\n\n");
        totalPoints += 5;
    } else {
        printf("Test 3-A failed\n\n");
    }

    // Test 3-B
    char str3B[] = "one two one two one";
    // The word "one" occurs 3 times..
    // Replace it with "six" (same length = 3).
    replaceSecondOccurrence(str3B, "one", "six");
    // Expected: "one two one two six"
    char exp3B[] = "one two six two one";
    printf("Test 3-B expected: \"%s\"\nGot: \"%s\"\n", exp3B, str3B);
    if (strcmp(str3B, exp3B) == 0) {
        printf("Test 3-B passed (+5 points)\n\n");
        totalPoints += 5;
    } else {
        printf("Test 3-B failed\n\n");
    }

    /********************************************************
     *                  TESTS for #4                        *
     ********************************************************/
    printf("\n--- Testing stringDecompression ---\n");

    // Test 4-A
    char comp4A[] = "a2bc3a3";
    char result4A[50];
    char exp4A[] = "aabcccaaa";
    stringDecompression(comp4A, result4A);
    printf("Test 4-A expected: \"%s\"\nGot: \"%s\"\n", exp4A, result4A);
    if (strcmp(result4A, exp4A) == 0) {
        printf("Test 4-A passed (+10 points)\n\n");
        totalPoints += 10;
    } else {
        printf("Test 4-A failed\n\n");
    }

    // Test 4-B
    char comp4B[] = "x4ab2";
    char result4B[50];
    char exp4B[] = "xxxxabb";
    stringDecompression(comp4B, result4B);
    printf("Test 4-B expected: \"%s\"\nGot: \"%s\"\n", exp4B, result4B);
    if (strcmp(result4B, exp4B) == 0) {
        printf("Test 4-B passed (+10 points)\n\n");
        totalPoints += 10;
    } else {
        printf("Test 4-B failed\n\n");
    }




    /********************************************************
     *                  TESTS for #5                        *
     ********************************************************/
    printf("\n--- Testing reverseWordOrder ---\n");

    // Test 5-A
    char rwo5A[] = "Hello world";
    char out5A[50];
    // Expected "world Hello"
    reverseWordOrder(rwo5A, out5A);
    char exp5A[] = "world Hello";
    printf("Test 5-A expected: \"%s\"\nGot: \"%s\"\n", exp5A, out5A);
    if (strcmp(out5A, exp5A) == 0) {
        printf("Test 5-A passed (+10 points)\n\n");
        totalPoints += 10;
    } else {
        printf("Test 5-A failed\n\n");
    }

    // Test 5-B
    char rwo5B[] = "Coding in C is fun";
    char out5B[50];
    // Expected "fun is C in Coding"
    reverseWordOrder(rwo5B, out5B);
    char exp5B[] = "fun is C in Coding";
    printf("Test 5-B expected: \"%s\"\nGot: \"%s\"\n", exp5B, out5B);
    if (strcmp(out5B, exp5B) == 0) {
        printf("Test 5-B passed (+10 points)\n\n");
        totalPoints += 10;
    } else {
        printf("Test 5-B failed\n\n");
    }

    /********************************************************
     *                  FINAL GRADE                         *
     ********************************************************/
    printf("Final Grade: %d\n", totalPoints);

    return 0;
}
