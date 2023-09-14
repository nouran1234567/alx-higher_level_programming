#include "lists.h"

/**
 * insert_node - inserts numbers in sorted singly linked list.
 *
 * @head: list head
 *
 * @number: number will be stored in new node
 *
 * Return: new node pointer
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *list_header;
	listint_t *new_node;

	list_header = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	return (NULL);
	new_node->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (list_header->next != NULL)
	{
		if ((list_header->next)->n >= number)
		{
			new_node->next = list_header->next;
			list_header->next = new_node;
			return (new_node);
		}
		list_header = list_header->next;
	}

	new_node->next = NULL;
	list_header->next = new_node;
	return (new_node);
}
