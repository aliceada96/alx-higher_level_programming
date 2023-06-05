#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: pointer to a linked list
 * 
 * Return: 0 if there is no cycle, 1 if there is
*/

int check_cycle(listint_t *list)
{
listint_t *i, *j;

	if (list == NULL || list->next == NULL)
		return (0);

	i = list->next;
	j = list->next->next;

	while (i && j && j->next)
	{
		if (i == j)
			return (1);

		i = i->next;
		hare = j->next->next;
	}

	return (0);
}
