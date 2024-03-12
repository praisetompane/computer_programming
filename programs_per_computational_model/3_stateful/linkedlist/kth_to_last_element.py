"""
    Context:
        Given:
            Singly Linkedlist
    Definitions:
        kth to last element = element that is k elements from the last element
            inclusive of the last element
            excluding the starting element
    Objective:
        find the kth to last element of a singly linked list

    Assumptions:
        k <= number of nodes in linked list
        
    Constraints:

    Example(s):
        input = [1, 2, 4, 6, 1, 7, 8, 5]
        state:
            current_element = 1
            num_elements_to_last = 7
            current_element = 2
            num_elements_to_last = 6
            current_element = 4
            num_elements_to_last = 5
            return element 4


            4 is 5 places from last element 5(inc.)
        
        kth_element(kth_position = 5)
            ans = 6
        
    Flow:
        until we reach the last element
            move to current_element
            num_elements_to_last = count number of elements to last element
            if num_elements_to_last == kth_position
                return current_element
            else 
                move to next element
"""
"""
    Performance

        Time = (N^2)
            Foreach node we need to count all the elements until we reach the end 
        Space = O(1) for internal state
                N for overall program to store N elements of linkedlist
"""

# ---Insert implementation here

# applies runner technique


from impl.linkedlist import LinkedList


def count_elements_to_last_element(current_element, linkedlist):
    _current_element = current_element
    num_from_last = 0
    while _current_element.next is not None:
        num_from_last = num_from_last + 1
        _current_element = _current_element.next
    return num_from_last


def kth_element(kth_position, linkedlist):
    current_element = linkedlist.head
    while current_element.next is not None:
        num_elements_to_last = count_elements_to_last_element(
            current_element, linkedlist
        )
        if num_elements_to_last == kth_position:
            return current_element
        else:
            current_element = current_element.next
    return current_element


def print_result(k, element):
    print("element %d from last element is %d" % (k, element.data))


def main():
    linkedlist = LinkedList()
    k = 5
    numbers = [1, 2, 4, 6, 1, 6, 8, 5]
    linkedlist.initialise_from_array(numbers)
    linkedlist.toString()
    element = kth_element(k, linkedlist)
    print_result(k, element)
    k = 0
    element = kth_element(k, linkedlist)
    print_result(k, element)


main()
