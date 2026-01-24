/**
 * COMP 201 - Fall 2025
 * Assignment 1 - BPE Text Tokenizer
 *
 * main.c
 *
 * This file contains the main function for the BPE tokenizer.
 * The main function parses command-line arguments and calls
 * the functions to be implemented by the students.
 *
 * Students: Implement the functions marked with // TODO. You may
 * add helper functions as needed.
 * DO NOT EDIT THE main() FUNCTION.
 */

 #include <stdio.h>
 #include <string.h>
 #include <stdlib.h>
 #include <ctype.h>
 #include <stdbool.h>
 

#define MAX_LINE_NUMBER 64
#define MAX_LINE_LEN 2048
#define MAX_WORD_LEN 32
#define MAX_TOKENS 1024
#define MAX_RULES 4096
#define MAX_VOCAB_SIZE 8192
 

 int normalize_file(const char *in_path, const char *out_path) {
     // TEMP: echo arguments to verify wiring. Delete this block after testing.
     printf("[normalize] input=\"%s\" output=\"%s\"\n", in_path, out_path);
     // TODO: Implement according to description.
     // Open the required file in the appropriate mode
     FILE* input;
     input = fopen(in_path, "r");
     FILE* output;
     output = fopen(out_path, "w");
     // Create a string with length 50 to store reading data
     char inData[50];

     // Check if the file is null or not
     if (input != NULL) {
        // Read the data with the different string parts with length of 50 until the end of the file
        while (fgets(inData, 50, input) != NULL) {
            // Create required variables
            char outData[50];
            int i = 0;
            char *token;
            // Check if the last char of the current part is space to use later.
            bool withSpace = inData[strlen(inData)-1] == ' ';
            // If first char of the current part is space, add the data in our output string (outData)
            if (inData[0] == ' '){
                outData[0] = ' ';
                i++;
            }
            // Tokenize the input with single spaces
            token = strtok(inData, " ");
            // Iterate tokens
            while (token != NULL){
                // Iterate each char in the token
                while (*token != '\0'){
                    // If the current char is a new line char, add it in outData
                    if (token[0] == '\n'){
                        outData[i] = '\n';
                        outData[i+1] = '\0';
                        i++;
                    }
                    // Check the project char requirements to continue
                    else if (isalpha(token[0]) || isdigit(token[0]) ||
                    token[0] == '.' || token[0] == ',' || 
                    token[0] == '!' || token[0] == '?' ||
                    token[0] == '\'' || token[0] == '-' ||
                    token[0] == '/') 
                    {
                        // Convert the char to lowercase and add in outData
                        outData[i] = tolower(token[0]);
                        outData[i+1] = '\0';
                        i++;
                    }
                    token++;
                }
                // At the end of the each token add a single space because we seperate them with spaces
                outData[i] = ' ';
                outData[i+1] = '\0';
                i++;
                token = strtok(NULL, " ");
            }
            // If there is no space at the end of the our input, remove the last space from out output string
            if (!withSpace){
                i--;
                outData[i] = '\0';
            }
            
            // Add the output string into output file
            fprintf(output, "%s", outData);
        }

        // Close the files
        fclose(input);
        fclose(output);
     }
     
     return 0;
 }

/*******************************************************************
*  find_the_pairs
*
* It finds each pairs in strings in the words array,
* and save them in the pairs array with their frequency in pairCounts int array.
*
* It directly changes the arguments.
*
* Test Case:
*          find_the_pairs(words, wordCounts, &wordCount, pairs, pairCounts, &pairCount);
*******************************************************************/
 int find_the_pairs(char words[MAX_TOKENS][MAX_WORD_LEN*2], int *wordCounts, unsigned int *wordCount,
                    char pairs[MAX_RULES][MAX_WORD_LEN], int *pairCounts, unsigned int *pairCount){
    unsigned int i;
    // Iterate each word in words array
    for (i=0; i<(*wordCount); i++){
        char word_copy[MAX_WORD_LEN*2];
        // Copy it in another string because strtok will be change it
        strcpy(word_copy, words[i]);
        // tok1 stores last part of the string before " "
        char *tok1 = strtok(word_copy, " ");
        char *tok2;
        // tok2 stores the first part after " "
        tok2 = strtok(NULL, " ");
        while (tok2 != NULL){
            int pairIdx = -1;
            char pair[MAX_WORD_LEN] = "";
            // Create pairs with form "A B"
            strcat(pair, tok1);
            strcat(pair, " ");
            strcat(pair, tok2);

            // Check if it exists or not.
            unsigned int j;
            for (j=0; j<(*pairCount); j++){
                if (strcmp(pair, (pairs)[j])==0){
                    // If exist hold the index
                    pairIdx = j;
                    break;
                }
            }
            // If it doesn't exist before
            if (pairIdx == -1){
                // Compy it in pairs array and save its count as with weighted the word's frequency
                strcpy((pairs)[*pairCount], pair);
                pairCounts[*pairCount] = 1*wordCounts[i];
                (*pairCount)++;
            } else {
                // If exist, just increase the corresponding pair count with weighted the word's frequency
                pairCounts[pairIdx]+=1*wordCounts[i];
            }
            // Move next two pair
            tok1 = tok2;
            tok2 = strtok(NULL, " ");
        }
    }

    return 0;
 }

/*******************************************************************
*  merge_pair
*
* It merges two distinct pair which is in highest string like "x y" -> "xy"
*
* It directly changes the arguments.
*
* Test Case:
*          merge_pair(highest,highestMerged);
*******************************************************************/
 int merge_pair(char highest[MAX_WORD_LEN*2], char highestMerged[MAX_WORD_LEN]){
    // Create required variables
    char highestNew[MAX_WORD_LEN] = "";
    char highestOld[MAX_WORD_LEN*2];
    // Copy the string including pair in another stirng because the strtok method will change the original string
    strcpy(highestOld, highest);
    // Split them with " "
    char *tok1 = strtok(highestOld, " ");
    char *tok2 = strtok(NULL, " ");
    // Merge them without " "
    strcat(highestNew, tok1);
    strcat(highestNew, tok2);
    // Copy the result into given string's address
    strcpy(highestMerged,highestNew);
    return 0;
 }

/*******************************************************************
*  find_the_highest_pair
*
* It finds the highest frequent pair in the pair string array.
* and store them in the highest string.
*
* It directly changes the arguments.
*
* Test Case:
*          find_the_highest_pair(pairs, pairCounts, &pairCount, highest, &highestFreq);
*******************************************************************/
 int find_the_highest_pair(char pairs[MAX_RULES][MAX_WORD_LEN], int *pairCounts, unsigned int *pairCount, char highest[MAX_WORD_LEN*2], int *highestFreq){
    unsigned int i;
    // Save the first element of the pairs array as the highest before iteration to compare with next ones
    strcpy(highest, pairs[0]);
    *highestFreq = pairCounts[0];
    // Iterate each elements in the pair array
    for (i=1; i<*pairCount; i++){
        // Merge them to compare correctly if their frequencies are same
        char highestMerged[MAX_WORD_LEN];
        char pairMerged[MAX_WORD_LEN];
        merge_pair(highest,highestMerged);
        merge_pair(pairs[i],pairMerged);
        // Check if the frequency of the pair is higher than previous one or the frequencies are same but them new one is smaller according to ascii
        if (pairCounts[i] > *highestFreq || (pairCounts[i] == *highestFreq && strcmp(highestMerged,pairMerged)>0)){
            // Change the highest pair
            strcpy(highest, pairs[i]);
            *highestFreq = pairCounts[i];
        }
     }
     return 0;
 }

/*******************************************************************
*  merge_pair_in_words
*
* It replace each pair in the each string in words string array with its merged version.
* Such as for "as d" pair, the string "as d f g h j" will be "asd f g h j".
*
* It directly changes the arguments.
*
* Test Case:
*          merge_pair_in_words(words, &wordCount, highest);
*******************************************************************/
 int merge_pair_in_words(char words[MAX_TOKENS][MAX_WORD_LEN*2], unsigned int *wordCount, char highest[MAX_WORD_LEN*2]){
    // First merge the distinct pair string
    char highestMerged[MAX_WORD_LEN];
    merge_pair(highest,highestMerged);

    // Hold their lengths
    int highestLen = strlen(highest);
    int mergedLen = strlen(highestMerged);

    unsigned int i;
    // Iterate each word in the words array
    for (i=0; i<*wordCount; i++){
        // Create required variables and pointers
        char newStr[MAX_WORD_LEN*2] = "";
        char *ptr = newStr;
        char *current = words[i];
        char *match;

        // Move forward on the word string (now *current pointer) until a match occurs.
        while ((match = strstr(current, highest)) != NULL && (match[-1] == ' ' || strcmp(match, current)==0) && (match[highestLen] == '\0' || match[highestLen] == ' ')) {
            // Copy the part before mathcing into string at ptr.
            strncpy(ptr, current, match - current);
            // Move ptr forward by the copied length
            ptr += (match - current);
            // Copy the merged version of the pair
            strcpy(ptr, highestMerged);
            // Move ptr forward by the size of merged pair
            ptr += mergedLen;
            // Then, make our current pointer after the last copied part to find other matches
            current = (char*)match + highestLen;
        }

        // Copy required strings
        strcpy(ptr, current);
        strcpy(words[i], newStr);
    }
    return 0;
 }

 
 int learn_bpe(const char *normalized_corpus_path,
               const char *merges_path,
               const char *vocab_path,
               int vocab_size,
               int min_freq) {
     // TEMP: echo arguments to verify wiring. Delete this block after testing.
     printf("[learn] corpus=\"%s\" merges_out=\"%s\" vocab_out=\"%s\" vocab_size=%d min_freq=%d\n",
            normalized_corpus_path, merges_path, vocab_path, vocab_size, min_freq);
     // TODO: Implement according to description.
     unsigned int i;
     // Open files
     FILE* input;
     input = fopen(normalized_corpus_path, "r");
     FILE* merge;
     merge = fopen(merges_path, "w");
     FILE* vocab;
     vocab = fopen(vocab_path, "w");
     fprintf(vocab, "<UNK>\n");

     // Initialize required variables
     char *line = NULL;
     size_t len = 0;

     char symbols[70];
     int symbolsCounts[70];
     unsigned int sLen = 0;

     char words[MAX_TOKENS][MAX_WORD_LEN*2];
     int wordCounts[MAX_TOKENS];
     unsigned int wordCount = 0;

     char highest[MAX_WORD_LEN*2];
     int highestFreq;

     // Read the input line by line
     while (getline(&line, &len, input) != -1){
        // Iterate each char in a line
        for (i = 0; i < len; i++){
            // If it is null-terminating char, break
            if (line[i] == '\0')
                break;
            // If it is new line char, make it null-terminating char and break
            if (line[i] == '\n'){
                line[i] = '\0';
                break;
            }
            // Check if this char currently exists in symbols array
            char *charPointer = strchr(symbols, line[i]);
            if (charPointer == NULL && line[i] != ' ' && line[i] != '\n'){
                // If not, add it in the array and initialize corresponding integer in symbolsCounts array
                symbols[sLen] = line[i];
                symbolsCounts[sLen] = 1;
                // Add the single char symbols into vocab file
                fprintf(vocab, "%c\n",symbols[sLen]);
                sLen++;
            } else if (charPointer != NULL) {
                // If exist, just increase the frequency
                symbolsCounts[charPointer-symbols]++;
            }
        }
        // Split each line with " " and iterate them
        char *token;
        token = strtok(line, " ");
        while (token != NULL){
            // Create a new word variable and copy the current word with " " space between each char
            int tokenWordIdx = -1;
            char word[MAX_WORD_LEN*2] = "";
            unsigned int letterCount = strlen(token);
            for (i=0;i<letterCount;i++){
                word[i * 2] = token[i];
                word[i * 2 + 1] = (i == letterCount - 1) ? '\0' : ' ';
            }
            // Now check if the word previously added in words array
            for (i=0; i<wordCount; i++){
                if (strcmp(word, words[i])==0){
                    tokenWordIdx = i;
                    break;
                }
            }
            // If not, copy it into array and start counter
            if (tokenWordIdx == -1){
                strcpy(words[wordCount], word);
                wordCounts[wordCount] = 1;
                wordCount++;
            } 
            // If exist, just increase the counter
            else {
                wordCounts[tokenWordIdx]++;
            }
            token = strtok(NULL, " ");
        }
        
     }
     // Finally indicate the null-terminating char for symbols array
     symbols[sLen] = '\0';

    // Store current vocab size 
    int current_vocab_size = sLen + 1;

    // Iterate the code below until one of our end rules occurs
    do{
        // Create required variables
        char pairs[MAX_RULES][MAX_WORD_LEN];
        int pairCounts[MAX_RULES];
        unsigned int pairCount = 0;
        // Find the pairs in all words
        find_the_pairs(words, wordCounts, &wordCount, pairs, pairCounts, &pairCount);
        // If there is no pair, break the iteration
        if (pairCount == 0)
            break;
        // Find the highest frequently pair.
        find_the_highest_pair(pairs, pairCounts, &pairCount, highest, &highestFreq);
        // If one of our end rules occurs, break the iteration
        if (highestFreq<min_freq || current_vocab_size>=vocab_size)
            break;
        // Merge each highest frequently pair in the words
        merge_pair_in_words(words, &wordCount, highest);
        
        // Merge the highest frequently pair to write in file
        char highestMerged[MAX_WORD_LEN];
        merge_pair(highest,highestMerged);

        // Write the files in required format
        fprintf(merge, "%s %s\n", highest, highestMerged);
        fprintf(vocab, "%s\n", highestMerged);
        current_vocab_size++;
    } while (highestFreq>=min_freq && current_vocab_size<vocab_size);

     // Close all files
     fclose(input);
     fclose(merge);
     fclose(vocab);
     return 0;
 }
 
 int tokenize_file(const char *normalized_input_path,
                   const char *merges_path,
                   const char *tokens_path) {
     // TEMP: echo arguments to verify wiring. Delete this block after testing.
     printf("[tokenize] input=\"%s\" merges=\"%s\" tokens_out=\"%s\"\n",
            normalized_input_path, merges_path, tokens_path);
     // TODO: Implement according to description.
     unsigned int i;

     // Open the files
     FILE* input;
     input = fopen(normalized_input_path, "r");
     FILE* tokens;
     tokens = fopen(tokens_path, "w");

     char *line = NULL;
     size_t len = 0;

    // Read the input line by line
    while (getline(&line, &len, input) != -1){
        char words[MAX_TOKENS][MAX_WORD_LEN*2];
        unsigned int wordCount = 0;        
        // Iterate the words in the line with splitting " "
        char *token;
        token = strtok(line, " ");
        while (token != NULL){
            // Create a new word variable and copy the current word with " " space between each char
            char word[MAX_WORD_LEN*2] = "";
            unsigned int letterCount = strlen(token);
            for (i=0;i<letterCount;i++){
                word[i * 2] = token[i];
                word[i * 2 + 1] = (i == letterCount - 1) ? '\0' : ' ';
            }
            // Store them in words array
            strcpy(words[wordCount], word);
            wordCount++;
            token = strtok(NULL, " ");
        }
        // Read the merges file and extract the rules in this file
        FILE* merge;
        merge = fopen(merges_path, "r");
        char *mergeRule = NULL;
        size_t mrLen = 0;
        // Read line by line
        while (getline(&mergeRule, &mrLen, merge) != -1){
            // voc1 is the first element of the pair
            char *voc1 = strtok(mergeRule, " ");
            // voc2 is the second element of the pair
            char *voc2 = strtok(NULL, " ");
            // rule is the string with appropiate format as "voc1 voc2"
            char rule[MAX_WORD_LEN*2] = "";
            strcat(rule, voc1);
            strcat(rule, " ");
            strcat(rule, voc2);
            // Merge each pair in the words with this rule
            merge_pair_in_words(words, &wordCount, rule);
        }
        // Close the merges file
        fclose(merge);
        // Write the file in the appropriate format 
        for(i=0;i<wordCount;i++){
            char *ptr;
            if ((ptr = strchr(words[i], '\n')) != NULL){
                ptr[-1] = '\0';
                fprintf(tokens, "%s\n", words[i]);
                continue;
            }
            fprintf(tokens, "%s ", words[i]);
        }
     }

     // Close all files
     fclose(input);
     fclose(tokens);
     return 0;
 }
 
 int encode_file(const char *vocab_path,
                 const char *tokens_path,
                 const char *encoded_path) {
     // TEMP: echo arguments to verify wiring. Delete this block after testing.
     printf("[encode] vocab=\"%s\" tokens=\"%s\" encoded_out=\"%s\"\n",
            vocab_path, tokens_path, encoded_path);
     // TODO: Implement according to description.
    // Open the files
    FILE* input;
    input = fopen(tokens_path, "r");
    FILE* encoded;
    encoded = fopen(encoded_path, "w");

    char *line = NULL;
    size_t len = 0;

    // Read the tokens line by line
    while (getline(&line, &len, input) != -1){
        // Create required variables with allocating memmory
        char tokens[MAX_TOKENS][MAX_WORD_LEN*2];
        unsigned int tokenCount = 0;
        char *token;
        token = strtok(line, " ");
        int tokenIdx = 0;
        bool isLast = false;
        // Iterate each string in the tokens splitting with " "
        while (token != NULL){
            // Check if the current string is last string
            if (strchr(token, '\n')!=NULL){
                strchr(token, '\n')[0]='\0';
                isLast = true;
            }
            // Add them in tokens array
            strcpy(tokens[tokenCount], token);
            tokenCount++;
            // Open the vocab file
            FILE* vocabFile;
            vocabFile = fopen(vocab_path, "r");
            char *vocab = NULL;
            size_t vocLen = 0;
            int vocIdx = 0;
            bool isUnknown = true;
            // Read each vocab
            while (getline(&vocab, &vocLen, vocabFile) != -1){
                if (strchr(vocab, '\n')!=NULL){
                    strchr(vocab, '\n')[0]='\0';
                }
                // If the vocab is same as a token append the line number in the file
                if (strcmp(vocab, token)==0 && isLast){
                    fprintf(encoded, "%d\n", vocIdx);
                    isUnknown = false;
                } else if (strcmp(vocab, token)==0){
                    fprintf(encoded, "%d ", vocIdx);
                    isUnknown = false;
                }
                vocIdx++;
            }
            // If the token couldn't be found in vocab add 0 in the file for this token
            if (isUnknown){
                fprintf(encoded, "0 ");
            }
            // Close the file
            fclose(vocabFile);
            token = strtok(NULL, " ");
            tokenIdx++;
        }
    }
    // Close files
    fclose(input);
    fclose(encoded);
     return 0;
 }
 
/*******************************************************************
*  convertStrToInt
*
* It converts a string into an int.
*
* Test Case:
*          convertStrToInt("123"): 123
*******************************************************************/
int convertStrToInt(char str[]) {
    int i;
    int num = 0;
    // Iterate each char in the string
    for (i=0; str[i]!='\0'; i++) {
        // Check if it is numeric
        if (str[i] < '0' || str[i] > '9')
            break;
        // Add the numerical equivelent of the digit in an integer and multiply the previous version of this integer by 10 to shift it left
        num = num * 10 + (str[i] - '0');
    }
    return num;
}


 int decode_file(const char *vocab_path,
                 const char *encoded_path,
                 const char *decoded_path) {
     // TEMP: echo arguments to verify wiring. Delete this block after testing.
     printf("[decode] vocab=\"%s\" encoded=\"%s\" decoded_out=\"%s\"\n",
            vocab_path, encoded_path, decoded_path);
     // TODO: Implement according to description.
    // Open files
    FILE* input;
    input = fopen(vocab_path, "r");
    FILE* decoded;
    decoded = fopen(decoded_path, "w");

    char *line = NULL;
    size_t len = 0;

    // Save each vocab in an string array
    char vocabs[MAX_VOCAB_SIZE][MAX_WORD_LEN*2];
    int vocCount = 0;
    while (getline(&line, &len, input) != -1){
        line[strlen(line)-1] = '\0';
        strcpy(vocabs[vocCount], line);
        vocCount++;
    }
    // Open encoded file
    FILE* encoded;
    encoded = fopen(encoded_path, "r");
    char *encode = NULL;
    size_t encodeLen = 0;
    // Read it line by line
    while (getline(&encode, &encodeLen, encoded) != -1){
        // Iterate each encoded number of the vocabs as string splitting with " "
        char *idxStr;
        idxStr = strtok(encode, " ");
        while (idxStr != NULL){
            // Convert the numeric string into int
            int idx = convertStrToInt(idxStr);
            // Use it as index of vocabs and add it into file
            if (idxStr[strlen(idxStr)-1]=='\n'){
                fprintf(decoded, "%s", vocabs[idx]);
            } else {
                fprintf(decoded, "%s ", vocabs[idx]);
            }
            idxStr = strtok(NULL, " ");
        }
        // Add new line char at end of the line
        fprintf(decoded, "\n");
    }
    // Close all files
    fclose(encoded);
    fclose(decoded);
    fclose(input);
     return 0;
 }
 
 void print_usage(const char *prog_name) {
     fprintf(stderr, "Usage:\n");
     fprintf(stderr, "  %s normalize <input_file> <output_file>\n", prog_name);
     fprintf(stderr, "  %s learn <corpus_file> <merges_file> <vocab_file> <vocab_size> <min_freq>\n", prog_name);
     fprintf(stderr, "  %s tokenize <input_file> <merges_file> <tokens_file>\n", prog_name);
     fprintf(stderr, "  %s encode <vocab_file> <tokens_file> <encoded_file>\n", prog_name);
     fprintf(stderr, "  %s decode <vocab_file> <encoded_file> <decoded_file>\n", prog_name);
 }
 
 int main(int argc, char *argv[]) {
     // Check for minimum number of arguments
     if (argc < 2) {
         fprintf(stderr, "Error: No subcommand provided.\n");
         print_usage(argv[0]);
         return EXIT_FAILURE;
     }
 
     const char *command = argv[1];
 
     if (strcmp(command, "normalize") == 0) {
         // Command: ./bpe normalize input_file_name normalized_output_file_name
         if (argc != 4) {
             fprintf(stderr, "Error: Invalid arguments for 'normalize'\n");
             print_usage(argv[0]);
             return EXIT_FAILURE;
         }
         return normalize_file(argv[2], argv[3]);
 
     } else if (strcmp(command, "learn") == 0) {
         // Command: ./bpe learn corpus.txt merges.txt vocab.txt 8000 2
         if (argc != 7) {
             fprintf(stderr, "Error: Invalid arguments for 'learn'\n");
             print_usage(argv[0]);
             return EXIT_FAILURE;
         }
 
         int vocab_size = atoi(argv[5]);
         int min_freq = atoi(argv[6]);
 
         if (vocab_size <= 0 || min_freq < 0) {
             fprintf(stderr, "Error: Invalid vocab_size or min_freq. Values must be non-negative.\n");
             return EXIT_FAILURE;
         }
 
         return learn_bpe(argv[2], argv[3], argv[4], vocab_size, min_freq);
 
     } else if (strcmp(command, "tokenize") == 0) {
         // Command: ./bpe tokenize input.txt merges.txt tokens.txt
         if (argc != 5) {
             fprintf(stderr, "Error: Invalid arguments for 'tokenize'\n");
             print_usage(argv[0]);
             return EXIT_FAILURE;
         }
         return tokenize_file(argv[2], argv[3], argv[4]);
 
     } else if (strcmp(command, "encode") == 0) {
         // Command: ./bpe encode vocab.txt tokens.txt encoded.txt
         if (argc != 5) {
             fprintf(stderr, "Error: Invalid arguments for 'encode'\n");
             print_usage(argv[0]);
             return EXIT_FAILURE;
         }
         return encode_file(argv[2], argv[3], argv[4]);
 
     } else if (strcmp(command, "decode") == 0) {
         // Command: ./bpe decode vocab.txt encoded.txt decoded.txt
         if (argc != 5) {
             fprintf(stderr, "Error: Invalid arguments for 'decode'\n");
             print_usage(argv[0]);
             return EXIT_FAILURE;
         }
         return decode_file(argv[2], argv[3], argv[4]);
 
     } else {
         fprintf(stderr, "Error: Unknown subcommand '%s'\n", command);
         print_usage(argv[0]);
         return EXIT_FAILURE;
     }
 
     return 0;
 }