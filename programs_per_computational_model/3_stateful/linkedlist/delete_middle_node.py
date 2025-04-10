"""
Context:
    Given:
        linkedlist

Objective:
    delete middle node

Definitions:
    middle node = any node bu the head and tail node

Assumptions:
    linkedlist has > 2 nodes
    middle node to delete exists in linkedlist
Constraints:
    only have access to the middle node
    access = only node I have the ability to delete
Example:
    linkedlist = a->b->c->d->e->f
    result => linkedlist = a->b->d->e->f

Flow:
    prior_node = find node before middle_node
    prior_node.next = prior_node.next.next

Performance:
    Time = O(N - 1) = 𝑂(𝑁) #drop constants
        inspect every element until you find node before the target_node
    Space = 𝑂(𝑁)
        Space to store linkedlist

"""

from impl.linkedlist import LinkedList, Node


def delete_middle_node(target_node, linkedlist):
    current_node = linkedlist.head
    while current_node.next is not None:
        if current_node.next.data == target_node.data:
            current_node.next = current_node.next.next
        current_node = current_node.next


def main():
    linkedlist = LinkedList()
    numbers = [1, 2, 4, 6, 1, 6, 8, 5]
    linkedlist.initialise_from_array(numbers)
    print("before delete")
    linkedlist.toString()
    delete_middle_node(Node(6), linkedlist)
    print("after delete")
    linkedlist.toString()


main()
