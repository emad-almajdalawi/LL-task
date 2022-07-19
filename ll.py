class Node:
    """
    Create a new node with two pointers
    Input: data (any type)
    Output: nothing
    """

    def __init__(self, data):
        self.data = data
        self.next1 = None
        self.next2 = None


class LinkedList:
    """
    Create new Linked-List
    Input: Nothing
    Outpu: Nothing
    """

    def __init__(self):
        self.head = None
