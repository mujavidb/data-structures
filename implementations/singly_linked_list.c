#include <stdio.h>
#include <stdlib.h>


// Declare struct for each node of the singly linked list
typedef struct node {
    int value;
    struct node * next;
} sll_node;

// DECLARE FUNCTIONS 
void printList(sll_node *head);
void pushEnd(sll_node *head, int val);
void pushHead(sll_node **head, int val);
void removeAtIndex(sll_node *head, int index);

int main(void){

	// Create pointer for head node in linked list
	sll_node *head = NULL;

	// Allocate memory for the head pointer
	head = malloc(sizeof(sll_node));

	head->value = 0;
	head->next = malloc(sizeof(sll_node));

	// Functions can be implemented here

	return 0;
}

void removeAtIndex(sll_node *head, int index) {

	sll_node *current = head;

	int counter = 0;

	//If deleting first node, just point head to second node
	if (index == 0) {
		*head = *head->next;

	} else {

		//Set current to node before index
		while (counter != index - 1) {
			current = current->next;
			counter++;
		}

		//If index is last node, set previous node *next to NULL,
		//else set the node before the index to point to node after the index
		if (current->next->next == NULL) {
			current->next = NULL;
		} else {
			current->next = current->next->next;
		}
	}
}

void printList(sll_node * head) {
    sll_node *current = head;

    while (current != NULL) {
        printf("%d\n", current->value);
        current = current->next;
    }
}

void pushEnd(sll_node * head, int val) {
    sll_node * current = head;
    while (current->next != NULL) {
        current = current->next;
    }

    /* now we can add a new variable */
    current->next = malloc(sizeof(sll_node));
    current->next->value= val;
    current->next->next = NULL;
}

void pushHead(sll_node ** head, int val) {
    sll_node * new_node;
    new_node = malloc(sizeof(sll_node));

    new_node->value= val;
    new_node->next = *head;
    *head = new_node;
}