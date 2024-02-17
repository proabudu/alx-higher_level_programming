#include <stdlib.h>

typedef struct listint_t {
    int n;
    struct listint_t *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number) {
    /* Declare both 'current' and 'prev' before any statements */
    listint_t *current;
    listint_t *prev;

    /* Allocate memory for the new node */
    listint_t *new = malloc(sizeof(listint_t));

    /* Check if memory allocation failed */
    if (!new) {
        return NULL;
    }

    /* Initialize the new node's data and next pointer */
    new->n = number;
    new->next = NULL;

    /* Handle the empty list case */
    if (!*head) {
        *head = new;
        return new;
    }

    /* Traverse the list to find the insertion point */
    current = *head;

    while (current && current->n < number) {
        prev = current;
        current = current->next;
    }

    /* Insert the new node at the correct position */
    if (!current) {
        prev->next = new;
        return new;
    }

    new->next = current;
    if (!prev) {
        *head = new;
    } else {
        prev->next = new;
    }

    /* Return the pointer to the new node */
    return new;
}
