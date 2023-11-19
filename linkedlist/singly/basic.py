class Node:
    """
    A node in a singly linked list.
    

    Attributes:
    data (Any): The data stored in the node.
    next (Node or None): The next node in the linked list.
    """
    def __init__(self, data):
        """
        Initialize a new node.
        Node have 2 properties, data and next.
        Head is property of singly linked list (SLL) and not of the node. 

        Args:
        data (Any): The data to be stored in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    Singly linked list implementation.
    Head is property of SLL, so we add that in constructor. 

    Attributes:
    head (Node or None): The head node of the list.
    """
    def __init__(self):
        """
        Initialize an empty linked list.

        """
        self.head = None

    def _get_new_node(self, data):
        """
        Creates a new node with the given data.

        Args:
        data (Any): The data for the new node.

        Returns:
        Node: A new node containing the given data.
        """
        return Node(data)

    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the list.

        Time Complexity: O(1)
        Space Complexity: O(1)

        Args:
        data (Any): The data for the new node.
        """
        new_node = self._get_new_node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, data):
        """
        Insert a new node after a given node.

        Space Complexity: O(1)

        Args:
        prev_node (Node): The node after which the new node will be inserted.
        data (Any): The data for the new node.

        Raises:
        ValueError: If prev_node is None.
        """
        if prev_node is None:
            raise ValueError("The given previous node must be in LinkedList.")
        new_node = self._get_new_node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.

        Time Complexity: O(n), where n is the number of nodes in the list.
        Space Complexity: O(1)

        Args:
        data (Any): The data for the new node.
        """
        new_node = self._get_new_node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        """
        Delete the first node with the specified key.

        Time Complexity: O(n), where n is the number of nodes in the list.
        Space Complexity: O(1)

        Args:
        key (Any): The key of the node to be deleted.
        """
        temp = self.head

        if temp is not None and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp is not None and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next

    def search(self, key):
        """
        Search for a node with the specified key.

        Time Complexity: O(n), where n is the number of nodes in the list.
        Space Complexity: O(1)

        Args:
        key (Any): The key to search for.

        Returns:
        bool: True if the key is found, False otherwise.
        """
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def print_list(self):
        """
        Print the entire linked list.

        Time Complexity: O(n), where n is the number of nodes in the list.
        Space Complexity: O(1)
        """
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
