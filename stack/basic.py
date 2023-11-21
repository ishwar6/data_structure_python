# A stack is a linear data structure that follows the Last In First Out (LIFO) principle. The two primary operations associated with a stack are:

# Push: Adding an element to the top of the stack.
# Pop: Removing the top element of the stack.

class Stack:
    """
    A class to represent a stack
    Attributes:
    items (list): The items in the stack.
    """

    def __init__(self):
        """
        Initialize the stack with an empty list.
        """
        self.items = []

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
        bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Push an item onto the stack.

        Parameters:
        item (any): The item to be added to the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item of the stack.

        Returns:
        any: The top item of the stack.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """
        Return the top item of the stack without removing it.

        Returns:
        any: The top item of the stack.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """
        Return the size of the stack.

        Returns:
        int: The number of items in the stack.
        """
        return len(self.items)
