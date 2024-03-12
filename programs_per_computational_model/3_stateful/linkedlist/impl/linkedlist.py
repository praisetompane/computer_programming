class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, numbers=[]):
        self.head = None
        self.initialise_from_array(numbers)

    """
        𝑂(𝑁)
    """

    def toString(self):
        if self.head is None:
            return
        number = ""
        current_node = self.head
        while current_node is not None:
            number += str(current_node.data)
            current_node = current_node.next
        return number

    """
        𝑂(𝑁)
    """

    def toInt(self):
        if self.head is None:
            return 0
        else:
            return int(self.toString())

    """
        𝑂(𝑁)
    """

    def add(self, data):
        new_number = Node(data)
        if self.head is None:
            self.head = new_number
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_number

    """
        𝑂(𝑁)
    """

    def initialise_from_array(self, numbers):
        previous_number = None
        for n in numbers:
            new_number = Node(n)
            if self.head is None:
                self.head = new_number
                previous_number = self.head
            else:
                previous_number.next = new_number
                previous_number = new_number

    def is_empty(self):
        return self.head is None
