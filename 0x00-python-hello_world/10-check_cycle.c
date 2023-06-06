#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: pointer to a linked list
 * 
 * Return: 0 if there is no cycle, 1 if there is
*/

int check_cycle(listint_t *list)
{
listint_t *curr, *prev;

	if (list == NULL || list->next == NULL)
		return (0);

	curr = list->next;
	prev = list->next->next;

	while (curr && prev && prev->next)
	{
		if (curr == prev)
			return (1);

		curr = curr->next;
		prev = prev->next->next;
	}

	return (0);
}
