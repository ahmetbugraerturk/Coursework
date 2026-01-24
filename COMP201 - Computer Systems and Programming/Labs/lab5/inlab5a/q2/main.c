#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "linkedlist.h"

void test_case1(){
    printf("Test Case 1 - Insert at Start (index 0): ");fflush(stdout);
    LinkedList l;
    int arr[] = {2, 3, 4};
    LinkedList_init(&l, arr, 3);
    LinkedList_insert_at_index(&l, 1, 0);
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

void test_case2(){
    printf("Test Case 2 - Insert at End (index = length): ");fflush(stdout);
    LinkedList l;
    int arr[] = {1, 2, 3};
    LinkedList_init(&l, arr, 3);
    LinkedList_insert_at_index(&l, 4, 3); // index 3 is the end (length = 3)
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

void test_case3(){
    printf("Test Case 3 - Insert at Middle (index 2): ");fflush(stdout);
    LinkedList l;
    int arr[] = {1, 2, 4, 5};
    LinkedList_init(&l, arr, 4);
    LinkedList_insert_at_index(&l, 3, 2); // insert 3 at index 2
    const char * expected = "[ 1 2 3 4 5 ]";
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
    printf("Test Case 4 - Invalid Index (negative): ");fflush(stdout);
    LinkedList l;
    int arr[] = {1, 2, 3};
    LinkedList_init(&l, arr, 3);
    LinkedList_insert_at_index(&l, 99, -1); // should do nothing
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

void test_case5(){
    printf("Test Case 5 - Invalid Index (too large): ");fflush(stdout);
    LinkedList l;
    int arr[] = {1, 2, 3};
    LinkedList_init(&l, arr, 3);
    LinkedList_insert_at_index(&l, 99, 4); // length is 3, index 4 is invalid
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

int main(int argc, char const *argv[])
{
    printf("=== Insert by Index Tests ===\n");
    test_case1(); // insert at start
    test_case2(); // insert at end
    test_case3(); // insert at middle
    test_case4(); // invalid index (negative)
    test_case5(); // invalid index (too large)

    return 0;
}
