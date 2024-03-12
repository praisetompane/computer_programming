from impl.stack import Stack

"""
    general use case = undo operations
    Performance:
        N = length of item list
        Space = O(2 * N) = 𝑂(𝑁)
        write:
            Time = O(1)
        undo:
            Time= O(1)
        redo:
            Time= O(1)
        display:
            Time= O(1)
"""


class OperationsUndoer:
    undo_stack = None
    redo_stack = None
    current_state = None

    def __init__(self, current_state):
        self.undo_stack = Stack()
        self.redo_stack = Stack()
        self.current_state = current_state

    def add_operations_result(self, operation_result):
        self.undo_stack.push(operation_result)
        self.current_state += operation_result

        self.display()

    def undo(self):
        self.redo_stack.push(self.undo_stack.peek())
        last_word = self.undo_stack.pop()
        self.current_state = self.current_state[: -len(last_word)]
        self.display()

    def redo(self):
        self.current_state += self.redo_stack.pop()
        self.display()

    def display(self):
        print(self.current_state)


def main():
    print("Praise typing his body of knowldge")
    text_processor = OperationsUndoer("")
    print("My blank slate")
    text_processor.display()
    text_processor.add_operations_result("I")
    text_processor.add_operations_result(" ")
    text_processor.add_operations_result("k")
    text_processor.add_operations_result("m")
    text_processor.undo()
    text_processor.add_operations_result("n")
    text_processor.add_operations_result("o")
    text_processor.add_operations_result("w")
    print("Try undo and redo")
    text_processor.undo()
    text_processor.redo()
    text_processor.add_operations_result(" that")
    text_processor.undo()


if __name__ == "__main__":
    main()
