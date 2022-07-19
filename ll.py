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

    def add(self, data):
        """
        Create new node then add it to the end of the linked-list
        Input: data (a new node will be created using this data)
        Output: Nothing
        """
        try:
            if isinstance(data, Node):
                raise TypeError
        except TypeError:
            return (
                "Please enter the data and it will be converted to a Nod eautomatically"
            )
        else:
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while not current.next1 in None:
                    current = current.next1
                current.next1 = new_node
                current.next2 = new_node
