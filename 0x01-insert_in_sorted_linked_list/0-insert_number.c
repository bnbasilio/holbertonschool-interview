#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: number to be inserted in the list
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node;

	current = *head;
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (!current || number < current->n)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	while (current->next && number > current->next->n)
		current = current->next;

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
