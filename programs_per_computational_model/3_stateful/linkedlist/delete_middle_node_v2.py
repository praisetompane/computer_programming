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
    middle node is not the head nor the tail node
Constraints:
    only have access to the middle node
    access = only node I am given
Example:
    linkedlist = a->b->c->d->e->f
    result => linkedlist = a->b->d->e->f

Flow:
    prior_node = find node before middle_node
    prior_node.next = prior_node.next.next

Performance:
    Time = O(1)
        constant time to copy data and shift pointers
    Space = 𝑂(𝑁)
        Space to store linkedlist

"""

from impl.linkedlist import LinkedList, Node


def delete_middle_node(target_node):
    target_node.data = target_node.next.data
    target_node.next = target_node.next.next


def main():
    linkedlist = LinkedList()
    numbers = [1, 2, 4, 6, 1, 6, 8, 5]
    linkedlist.initialise_from_array(numbers)
    print("before delete")
    linkedlist.toString()
    target_node = None
    target_node_value = 6
    current_node = linkedlist.head
    while current_node.next is not None:
        if current_node.data == target_node_value:
            target_node = current_node
        current_node = current_node.next
    delete_middle_node(target_node)
    print("after delete")
    linkedlist.toString()


main()
