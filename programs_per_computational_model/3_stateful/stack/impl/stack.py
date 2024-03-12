class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data


class Stack:
    top = None

    def pop(self):
        if self.top is None:
            raise Exception("Stack is empty")
        item = self.top.data
        self.top = self.top.next
        return item

    def push(self, item):
        node = Node(item)
        node.next = self.top
        self.top = node

    def peek(self):
        if self.top is None:
            raise Exception("Stack is empty")
        return self.top.data

    def is_empty(self):
        return self.top is None
