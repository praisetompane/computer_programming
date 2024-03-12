"""
    Context:
        Given unsorted linked list
    Definitions:

    Objective:
        Remove duplicates
    Assumptions:
        Using singly linked list
    Constraints:
        None
    Example(s):
        input = [1, 2, 4, 6, 1, 6, 8, 5]
        state:[1,2,4,6,8,5]
        
    Algorithm flow:
        empty hash(nodeData -> count)
        foreach element in list
            if exists in hash
                deleteNode
                add element and count = 1
            else
                add element and count = 1
"""

from impl.linkedlist import LinkedList


def remove_duplicates(linkedlist):
    element_frequency = {}
    current_node = linkedlist.head
    while current_node.next is not None:
        element_frequency[current_node.data] = 1
        if current_node.next.data in element_frequency:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next


def main():
    linkedlist = LinkedList()
    numbers = [1, 2, 4, 6, 1, 6, 8, 5]
    linkedlist.initialise_from_array(numbers)
    print("before delete")
    linkedlist.toString()
    remove_duplicates(linkedlist)
    print("after delete")
    linkedlist.toString()


main()

"""
    Performance

        Time = 
            N number of elements 
            D number of operations for delete a node from linkedlist= Constant 
            => O(1 + N) => 𝑂(𝑁)
        Space = 
            upto N element's count stored in hash => 𝑂(𝑁)
"""
