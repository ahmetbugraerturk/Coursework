#include "linkedlist.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"


void LinkedList_insert_sorted(LinkedList* l, int value){
    // Inserts a new node with the given value to the list in the corresponding place
    // The list includes the numbers in increasing order.
    // E.g. let l contain [1, 3, 5] and value=2 then the content of l should be changed to [1, 2, 3, 5]
    
    // TODO: IMPLEMENT LinkedList_insert_sorted
    // FILL HERE
    if(l->root == NULL)
	LinkedList_insert(l, value);
    else if(l->root->content>value){
    	Node* n = malloc(sizeof(Node));
	n->content = value;
	n->next = l->root;
	l->root = n;
    }
    else{
    	Node* n = malloc(sizeof(Node));
	n->content = value;
	Node* curr = l->root;
	while(curr->next!=NULL&&curr->next->content<value){
	    curr=curr->next;
	}
	if(curr->next==NULL){
	    curr->next=n;
	}
	else{
	    n->next=curr->next;
	    curr->next=n;
	}
    }
    
}

void LinkedList_remove_value(LinkedList* l, int value){
    // Removes the node with the given value as its content from the linked list.
    // Does nothing if the value is not found or if the list is empty.
    // E.g. let l contain [1, 2, 3, 4] and value=3 then the content of l should be changed to [1, 2, 4]
    // DO NOT FORGET TO FREE THE UNUSED (REMOVED) SPACE SINCE IT IS DYNAMICALLY ALLOCATED
    
    // TODO: IMPLEMENT LinkedList_remove_value
    // FILL HERE
    if (l->root!=NULL){
   	Node* curr = l->root;
   	if(curr->content==value){
    	   l->root = l->root->next;
    	} else {
	   while(curr->next!=NULL&&curr->next->content!=value)
	      curr=curr->next;
    	   if(curr->next!=NULL&&curr->next->content==value){
    	      curr->next=curr->next->next;
           }
        }
    }

}

void LinkedList_init(LinkedList* l, int* arr, int len){
    // Initializes the LinkedList with a copy of array arr
    l->root = NULL; // initialize root node to NULL
    int i;
    for(i=0;i<len;i++){
        LinkedList_insert(l, arr[i]);
    }
} 

int LinkedList_length(LinkedList* l){
    // Calculates the length of the LinkedList
    
    if(l->root == NULL){
        return 0;
    }else{
        int count = 1;
        Node* current = l->root;
        while(current->next != NULL){
            current = current->next;
            count++;
        }
        return count;
    }
}

int LinkedList_remove(LinkedList* l){
    // Deletes the last node and returns its value (content)
    // Note: return -1 when there is no value in the list.

    int value = -1;
    if(l->root == NULL){
        return value;
    }else if(l->root->next == NULL){
        // when there is only root node
        value = l->root->content;
        free(l->root);
        l->root = NULL;
        return value;
    }else{
        // when there multiple nodes
        Node* current = l->root;
        while(current->next->next != NULL){
            current = current->next;
        }
        value = current->next->content;
        free(current->next);
        current->next = NULL;
        return value;
    }
}

void LinkedList_insert(LinkedList* l, int value){
    // Appends the value to the end of linked list as a new node
    Node* n = malloc(sizeof(Node)); // create a new node
    n->content = value;
    n->next = NULL;

    if(l->root == NULL){
        l->root = n;
    }else{
        // Iterating through nodes until last node
        Node* current = l->root;
        while(current->next != NULL){
            current = current->next;
        }
        current->next = n;
    }
}

char* LinkedList_to_string(LinkedList* l, char* str){
    // Converts LinkedList to string and puts it into str
    strcat(str, "[ ");
    Node* current = l->root;
    if(current != NULL){
        do{
            char temp[10]  = "";
            sprintf(temp, "%d ", current->content);
            strcat(str, temp);
            current = current->next;
        }while(current != NULL);
    }
    strcat(str, "]");
    return str;
}

