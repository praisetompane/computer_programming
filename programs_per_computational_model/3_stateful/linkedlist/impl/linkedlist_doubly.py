class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedListDoubly:
    def __init__(self, numbers=[]):
        self.head = None
        self.tail = None
        self.initialise_from_array(numbers)

    """
        𝑂(𝑁)
    """

    def toString(self):
        if self.head is None:
            return
        number = ""
        current_node = self.tail
        while current_node is not None:
            number += str(current_node.data)
            current_node = current_node.prev
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
        O(1)
    """

    def add(self, data):
        new_number = Node(data)
        if self.head is None:
            self.head = new_number
            self.tail = self.head
        else:
            new_number.prev = self.tail
            self.tail.next = new_number
            self.tail = new_number

    """
        𝑂(𝑁)
    """

    def initialise_from_array(self, numbers):
        for n in numbers:
            self.add(n)

    def is_empty(self):
        return self.head is None
