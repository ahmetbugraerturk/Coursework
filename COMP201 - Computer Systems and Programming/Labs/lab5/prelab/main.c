#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "linkedlist.h"

void test_case1(){
    printf("Test Case 1 - Middle Insert: ");fflush(stdout);
    LinkedList l;
    int arr[] = {1, 3, 5};
    LinkedList_init(&l, arr, 3);
    LinkedList_insert_sorted(&l, 2);
    const char * expected = "[ 1 2 3 5 ]";
    char resulted[100] = "";
    LinkedList_to_string(&l, resulted);
    if(strcmp(resulted, expected) == 0){
        printf("PASS!\n");
    }else{
        printf("FAILED!\n");
        printf("Expected: %s - Resulted: %s\n", expected, resulted);
    }
}

void test_case2(){
    printf("Test Case 2 - Start Insert: ");fflush(stdout);
    LinkedList l;
    int arr[] = {2, 3, 5};
    LinkedList_init(&l, arr, 3);
    LinkedList_insert_sorted(&l, 1);
    const char * expected = "[ 1 2 3 5 ]";
    char resulted[100] = "";
    LinkedList_to_string(&l, resulted);
    if(strcmp(resulted, expected) == 0){
        printf("PASS!\n");
    }else{
        printf("FAILED!\n");
        printf("Expected: %s - Resulted: %s\n", expected, resulted);
    }
}

void test_case3(){
    printf("Test Case 3 - End Insert: ");fflush(stdout);
    LinkedList l;
    int arr[] = {1, 2, 3};
    LinkedList_init(&l, arr, 3);
    LinkedList_insert_sorted(&l, 5);
    const char * expected = "[ 1 2 3 5 ]";
    char resulted[100] = "";
    LinkedList_to_string(&l, resulted);
    if(strcmp(resulted, expected) == 0){
        printf("PASS!\n");
    }else{
        printf("FAILED!\n");
        printf("Expected: %s - Resulted: %s\n", expected, resulted);
    }
}

void test_case4(){
    printf("Test Case 4 - Empty List Insert: ");fflush(stdout);
    LinkedList l;
    int arr[] = {}; // Empty array
    LinkedList_init(&l, arr, 0);
    LinkedList_insert_sorted(&l, 1);
    const char * expected = "[ 1 ]";
    char resulted[100] = "";
    LinkedList_to_string(&l, resulted);
    if(strcmp(resulted, expected) == 0){
        printf("PASS!\n");
    }else{
        printf("FAILED!\n");
        printf("Expected: %s - Resulted: %s\n", expected, resulted);
    }
}

void test_case5(){
    printf("Test Case 5 - Beginning Remove: ");fflush(stdout);
    LinkedList l;
    int arr[] = {1, 2, 3, 4};
    LinkedList_init(&l, arr, 4);
    LinkedList_remove_value(&l, 1);
    const char * expected = "[ 2 3 4 ]";
    char resulted[100] = "";
    LinkedList_to_string(&l, resulted);
    if(strcmp(resulted, expected) == 0){
        printf("PASS!\n");
    }else{
        printf("FAILED!\n");
        printf("Expected: %s - Resulted: %s\n", expected, resulted);
    }
}

void test_case6(){
    printf("Test Case 6 - Middle Remove: ");fflush(stdout);
    LinkedList l;
    int arr[] = {1, 2, 3, 4};
    LinkedList_init(&l, arr, 4);
    LinkedList_remove_value(&l, 3);
    const char * expected = "[ 1 2 4 ]";
    char resulted[100] = "";
    LinkedList_to_string(&l, resulted);
    if(strcmp(resulted, expected) == 0){
        printf("PASS!\n");
    }else{
        printf("FAILED!\n");
        printf("Expected: %s - Resulted: %s\n", expected, resulted);
    }
}

void test_case7(){
    printf("Test Case 7 - End Remove: ");fflush(stdout);
    LinkedList l;
    int arr[] = {1, 2, 3, 4};
    LinkedList_init(&l, arr, 4);
    LinkedList_remove_value(&l, 4);
    const char * expected = "[ 1 2 3 ]";
    char resulted[100] = "";
    LinkedList_to_string(&l, resulted);
    if(strcmp(resulted, expected) == 0){
        printf("PASS!\n");
    }else{
        printf("FAILED!\n");
        printf("Expected: %s - Resulted: %s\n", expected, resulted);
    }
}

void test_case8(){
    printf("Test Case 8 - Remove Non-Existing: ");fflush(stdout);
    LinkedList l;
    int arr[] = {1, 2, 3, 4};
    LinkedList_init(&l, arr, 4);
    LinkedList_remove_value(&l, 10);
    const char * expected = "[ 1 2 3 4 ]";
    char resulted[100] = "";
    LinkedList_to_string(&l, resulted);
    if(strcmp(resulted, expected) == 0){
        printf("PASS!\n");
    }else{
        printf("FAILED!\n");
        printf("Expected: %s - Resulted: %s\n", expected, resulted);
    }
}

void test_case9(){
    printf("Test Case 9 - Remove From Empty List: ");fflush(stdout);
    LinkedList l;
    int arr[] = {};
    LinkedList_init(&l, arr, 0);
    LinkedList_remove_value(&l, 1);
    const char * expected = "[ ]";
    char resulted[100] = "";
    LinkedList_to_string(&l, resulted);
    if(strcmp(resulted, expected) == 0){
        printf("PASS!\n");
    }else{
        printf("FAILED!\n");
        printf("Expected: %s - Resulted: %s\n", expected, resulted);
    }
}

int main(int argc, char const *argv[])
{
    printf("=== QUESTION 1: Insert Sorted ===\n");
    test_case1(); // tests for middle insert
    test_case2(); // tests for start insert
    test_case3(); // tests for end insert
    test_case4(); // tests for empty list insert
    
    printf("\n=== QUESTION 2: Remove Value ===\n");
    test_case5(); // tests for beginning remove
    test_case6(); // tests for middle remove
    test_case7(); // tests for end remove
    test_case8(); // tests for remove non-existing
    test_case9(); // tests for remove from empty list

    return 0;
}
