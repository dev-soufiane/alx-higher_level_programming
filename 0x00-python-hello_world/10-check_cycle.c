#include "lists.h"

/**
 * check_cycle - checks for a cycle in a singly linked list
 * @list: list pointer
 *
 * Return: 0 if no cycle, 1 if cycle exists
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr1;
	listint_t *ptr2;

	if (list == NULL)
		return (0);

	ptr1 = list;
	ptr2 = list->next;

	while (ptr1 && ptr2 && ptr2->next)
	{
		if (ptr1 == ptr2)
			return (1);
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
	}

	return (0);
}
