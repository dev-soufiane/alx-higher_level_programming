#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly-linked list
 * @head: head pointer of the linked list
 * @number: number to insert
 *
 * Return: Pointer to the new node if successful, otherwise NULL.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}

	new_node->n = number;

	if (current == NULL || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}
	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
