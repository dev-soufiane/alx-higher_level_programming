#include "lists.h"

/**
 * reverse_listint - Reverses a singly linked list
 * @head: First node pointer
 *
 * Return: Reversed list head pointer
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;

	return (*head);
}

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: List head pointer
 *
 * Return: 0 if not a palindrome, 1 if a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *second_half = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	second_half = slow;
	prev_slow->next = NULL;
	reverse_listint(&second_half);
	while (*head != NULL && second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}
	reverse_listint(&second_half);
	prev_slow->next = second_half;
	return (is_palindrome);
}
