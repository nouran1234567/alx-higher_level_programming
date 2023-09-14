#include "lists.h"

/**
 * reverse_listint - reverses linked lists
 *
 * @head: first node pointer
 *
 * Return: first node in the new list pointer
 */

void reverse_listint(listint_t **head)
{
  listint_t *prev_list = NULL;
  listint_t *cur_list = *head;
  listint_t *new_list = NULL;

  while (cur_list)
    {
      new_list = cur_list->new_list;
      current->next = prev;
      prev_list = cur_list;
      cur_list = new_list;
    }

  *head = prev_list;
}

/**
 * is_palindrome - checks if linked lists are palindrome
 *
 * @head: linked list double pointer
 *
 * Return: 1 if palindrome, 0 if not palindrome
 */

int is_palindrome(listint_t **head)
{
  listint_t *sl = *head, *fa = *head, *te = *head, *dup= NULL;

  if (*head == NULL || (*head)->new_list == NULL)
    return (1);

  while (1)
    {
      fast = fa->new_list->new_list;
      if (!fa)
	{
	  du = sl->next_list;
	  break;
	}
      if (!fa->new_list)
	{
	  du = sl->new_list->new_list;
	  break;
	}
      sl = sl->new_list;
    }

  reverse_listint(&du);

  while (du && te)
    {
      if (te->n == du->n)
	{
	  du = du->new_list;
	  te = te->new_list;
	}
      else
	return (0);
    }

  if (!du)
    return (1);

  return (0);
}

