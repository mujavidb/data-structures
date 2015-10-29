#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int value;
    struct node * next;
} sll_node;

/* DECLARE FUNCTIONS */
void print_list(sll_node *head);
void push_end(sll_node *head, int val);
void push_head(sll_node **head, int val);

void remove_at_index(sll_node *head, int index);
void remove_by_value(sll_node *head, int deathrow);

sll_node access(sll_node *head, int index);

int main(void){

	// Create pointer for head node in linked list
	sll_node *head = NULL;

	// Allocate memory for the head pointer
	head = malloc(sizeof(sll_node));

	head->value = 0;
	head->next = malloc(sizeof(sll_node));

	head->next->value = 1;
	head->next->next = NULL;
	push_end(head, 2);
	push_end(head, 3);
	push_end(head, 4);
	push_end(head, 5);
	push_end(head, 6);
	push_end(head, 7);
	push_end(head, 8);
	push_end(head, 9);
	push_end(head, 10);

	print_list(head);
	remove_at_index(head, 10);
	print_list(head);

	return 0;
}

void remove_at_index(sll_node *head, int index) {

	sll_node *current = head;

	int counter = 0;

	//If deleting first node, just point head to second node
	if (index == 0) {
		*head = *head->next;
		return;
	}

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

void print_list(sll_node * head) {
    sll_node *current = head;

    while (current != NULL) {
        printf("%d\n", current->value);
        current = current->next;
    }
}

void push_end(sll_node * head, int val) {
    sll_node * current = head;
    while (current->next != NULL) {
        current = current->next;
    }

    /* now we can add a new variable */
    current->next = malloc(sizeof(sll_node));
    current->next->value= val;
    current->next->next = NULL;
}

void push_head(sll_node ** head, int val) {
    sll_node * new_node;
    new_node = malloc(sizeof(sll_node));

    new_node->value= val;
    new_node->next = *head;
    *head = new_node;
}