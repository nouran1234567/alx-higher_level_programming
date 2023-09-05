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
	listint_t *p_fast = list;
	listint_t *p_slow = list;

	while (list && p_fast && p_fast->next)
	{
		list = list->next;
		p_fast = p_fast->next->next;

		if (list == p_fast)
		{
			list = p_slow;
			p_slow =  p_fast;
			while (1)
			{
				p_fast = p_slow;
				while (p_fast->next != list && p_fast->next != p_slow)
				{
					p_fast = p_fast->next;
				}
				if (p_fast->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
