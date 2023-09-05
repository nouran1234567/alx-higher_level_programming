#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks for cycles in linked lists
 *
 * @list: lists to be checked
 *
 * Return: 1 if a cycle is found, 0 if no cycles
 */

int check_cycle(listint_t *list)
{
	listint_t *pointer_slow = list;
	listint_t *pointer_fast = list;

	if (!list)
		return (0);

	while (pointer_slow && pointer_fast && pointer_fast->next)
	{
		pointer_slow = pointer_slow->next;
		pointer_fast = pointer_fast->next->next;
		if (pointer_slow == pointer_fast)
			return (1);
	}

	return (0);
}
