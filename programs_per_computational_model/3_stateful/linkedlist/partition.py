"""
    Context:
        Given linkedlist
    Objective:
        Partition list 
            along a value [partition = x]
            such that
                all nodes < x come
                    before all nodes > x
        values of x can be anywhere after values less than x
    Definitions

    Assumptions
        partion value exists in list
        list length > 0

    Constraints:

    Example:
        input = 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
        output = 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

    Flow:
        Option 1:
            Bubble sort 
                moving nodes >= partition up[to right]
            Performance
                Time: O(N^2) => Quadratic, SLOW!
                Space: 

        Option 2:
            Use quick sort in language libary
            BUT Write your own and could get 𝑂(𝑁) since we're not interested in fully sorting the lit

            Performance
                Time: O(NlogN) =>  
                Space
        
        Option 3:
            once pass bubble sort

            -----
            last_less_than_partition = None
            current_node = head
            while current_node is not None
                if current < parition
                    if last_less_than_partition is None
                        last_less_than_partition = current_node
                    else
                        insert it after last_less_than_partition
                    move to next node
                else
                    move to next node

            Performance
                Time: 𝑂(𝑁) =>  
                Space

            Paper Run:
                input = 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
                output = 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
                state:
                    partition = 5
                    last_less_than_partition = 2
                    current_node = 3
                    output = 3 -> 2 -> 5 -> 8 -> 5 -> 10 -> 1
                    output = 3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10

"""
from impl.linkedlist import LinkedList


def partition_list(partition, linkedlist):
    last_less_than_partition = None
    last_greater_than_partition = None
    current_node = linkedlist.head
    current_node_next = current_node.next
    while current_node_next is not None:
        current_node_next = current_node.next
        if current_node.data < partition:
            if last_less_than_partition is None:
                last_less_than_partition = current_node
            else:
                last_greater_than_partition.next = current_node_next
                current_node.next = last_less_than_partition.next
                last_less_than_partition.next = current_node
                last_less_than_partition = current_node
        else:
            last_greater_than_partition = current_node
        current_node = current_node_next


def print_result(k, element):
    print("element %d from last element is %d" % (k, element.data))


def main():
    print("normal case")
    linkedlist = LinkedList()
    k = 5
    numbers = [3, 5, 8, 5, 10, 2, 1]
    linkedlist.initialise_from_array(numbers)
    print("before parition")
    linkedlist.toString()
    print("partitioning the list by %d" % k)
    partition_list(k, linkedlist)
    print("partitioned list")
    linkedlist.toString()  # 3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10

    print("list of one")
    l2 = LinkedList()
    k = 5
    numbers = [3]
    l2.initialise_from_array(numbers)
    print("before parition")
    l2.toString()
    print("partitioning the list by %d" % k)
    partition_list(k, l2)
    print("partitioned list")
    l2.toString()  # 3


main()
