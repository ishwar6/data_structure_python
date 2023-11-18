class DoublyLinkedListNode:
    """
    A class to represent a node in a doubly linked list.

    Attributes:
    data (any): The data stored in the node.
    next (DoublyLinkedListNode): The reference to the next node in the list.
    prev (DoublyLinkedListNode): The reference to the previous node in the list.
    """

    def __init__(self, data):
        """
        Initialize the doubly linked list node with data, and set next and prev as None.

        Parameters:
        data (any): The data to be stored in the node.
        """
        self.data = data
        self.next = None
        self.prev = None



class DoublyLinkedList:
    """
    A class to represent a doubly linked list.

    Attributes:
    head (DoublyLinkedListNode): The head node of the doubly linked list.
    """

    def __init__(self):
        """
        Initialize the doubly linked list with head as None.
        """
        self.head = None

    def append(self, data):
        """
        Append a node with the given data to the end of the list.

        Parameters:
        data (any): The data to be stored in the new node.
        """
        new_node = DoublyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        """
        Prepend a node with the given data to the start of the list.

        Parameters:
        data (any): The data to be stored in the new node.
        """
        new_node = DoublyLinkedListNode(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def delete_node(self, key):
        """
        Delete the first node with the given key from the list.

        Parameters:
        key (any): The data of the node to be deleted.
        """
        cur_node = self.head

        while cur_node:
            if cur_node.data == key and cur_node == self.head:
                # Case: Node to be deleted is the head
                if not cur_node.next:
                    cur_node = None
                    self.head = None
                    return

                else:
                    nxt = cur_node.next
                    cur_node.next = None
                    nxt.prev = None
                    cur_node = None
                    self.head = nxt
                    return

            elif cur_node.data == key:
                # Case: Node to be deleted is not the head
                if cur_node.next:
                    nxt = cur_node.next
                    prev = cur_node.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur_node.next = None
                    cur_node.prev = None
                    cur_node = None
                    return

                else:
                    # Case: Node to be deleted is the last node
                    prev = cur_node.prev
                    prev.next = None
                    cur_node.prev = None
                    cur_node = None
                    return

            cur_node = cur_node.next

    def print_list(self):
        """
        Print the elements of the doubly linked list.
        """
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next
        print()
