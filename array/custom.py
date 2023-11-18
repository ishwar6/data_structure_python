# Implementing an array in Python typically means using Python's built-in list type, as Python lists are essentially dynamic arrays.

class CustomArray:
    """
    A class to represent a custom array.

    Attributes:
    capacity (int): The capacity of the array.
    size (int): The current number of elements in the array.
    elements (list): The elements in the array.
    """

    def __init__(self, capacity=10):
        """
        Initialize the custom array with a default capacity.

        Parameters:
        capacity (int): The initial capacity of the array.
        """
        self.capacity = capacity
        self.size = 0
        self.elements = [None] * capacity

    def __len__(self):
        """
        Return the size of the array.
        """
        return self.size

    def __getitem__(self, index):
        """
        Retrieve an item at a specified index.

        Parameters:
        index (int): The index of the item.

        Returns:
        any: The item at the specified index.
        """
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds")
        return self.elements[index]

    def __setitem__(self, index, value):
        """
        Set an item at a specified index.

        Parameters:
        index (int): The index of the item.
        value (any): The new value for the item.
        """
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds")
        self.elements[index] = value

    def append(self, item):
        """
        Append an item to the end of the array.

        Parameters:
        item (any): The item to be added.
        """
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.elements[self.size] = item
        self.size += 1

    def _resize(self, new_capacity):
        """
        Resize the array to a new capacity.

        Parameters:
        new_capacity (int): The new capacity of the array.
        """
        new_elements = [None] * new_capacity
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.elements = new_elements
        self.capacity = new_capacity

    def remove(self, index):
        """
        Remove an item at a specified index.

        Parameters:
        index (int): The index of the item to be removed.
        """
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.elements[i] = self.elements[i + 1]
        self.elements[self.size - 1] = None
        self.size -= 1
