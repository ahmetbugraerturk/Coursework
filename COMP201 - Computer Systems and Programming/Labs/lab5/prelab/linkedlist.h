#include "node.h"

typedef struct LinkedList
{
    Node* root; // the first node of the linked list
    // This struct can store more variables depending on the application but we kept it simple.
} LinkedList;

// FUNCTIONS: see linkedlist.c for the implementations

void LinkedList_init(LinkedList* l, int* arr, int len); // Initializes the LinkedList with a copy of array arr

int LinkedList_length(LinkedList* l); // Calculates the length of the LinkedList

void LinkedList_insert(LinkedList* l, int value); // Appends the value to the end of linked list as a new node

void LinkedList_insert_sorted(LinkedList* l, int value); // Inserts the value into the sorted linked list in the correct position

void LinkedList_remove_value(LinkedList* l, int value); // Removes the first occurrence of the given value from the linked list. Does nothing if value is not found.

char* LinkedList_to_string(LinkedList* l, char* str); // Converts the LinkedList to a string so that we can print it
