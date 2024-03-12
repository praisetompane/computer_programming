class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        raise Exception("Stack is empty")

    def is_empty(self):
        return len(self.data) <= 0
