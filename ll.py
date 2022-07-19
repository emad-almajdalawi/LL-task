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

    def __len__(self):
        """
        To measure the length of thre linked-list
        Input: nothing
        Output: Length (Int)
        """
        if self.head is None:
            return 0
        else:
            current = self.head
            counter = 1
            while current.next1:
                current = current.next1
                counter += 1
            return counter

    def add(self, data):
        """
        Create new node then add it to the end of the linked-list. time -> O(N), space -> O(1)
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
                while current.next1:
                    current = current.next1
                current.next1 = new_node
                current.next2 = new_node
        return new_node

    def detect_loop(self):
        """
        Detect whether the linked-list is looped or not
        Input: Nothifg
        Output: Boolian (True if loop)
        """
        try:
            if self.head is None:
                raise ValueError
        except ValueError:
            return "The linked-list is emplty!"
        else:
            visited = {}
            current = self.head
            while current:
                if id(current) in visited.keys():
                    return True
                else:
                    visited[id(current)] = 1
                current = current.next1
            visited = {}
            while current:
                if id(current) in visited.keys():
                    return True
                else:
                    visited[id(current)] = 1
                current = current.next2
            return False

    def __str__(self):
        output = ""
        if self.head is None:
            output += "The linked-list is empty"
        else:
            current = self.head
            while current:
                output += "{ " f"{current.data}" " } -> "
                current = current.next1
            output += "NULL"
        return output


if __name__ == "__main__":
    LL = LinkedList()

    n111 = LL.add(1)
    LL.add(2)
    LL.add(3)
    LL.add(4)
    LL.add(5)

    print(n111, id(n111), id(n111.next1), id(n111.next2))

    print("LL:", LL)
    print("length of LL:", len(LL))
    print("detect loop LL:", LL.detect_loop())

    LL2 = LinkedList()

    n1 = LL2.add(1)
    n2 = LL2.add(2)
    n3 = LL2.add(3)
    n4 = LL2.add(4)
    n5 = LL2.add(5)
    n11 = LL2.add(1)

    print("id n1:", id(n1))
    print("id n11:", id(n11))

    n3.next2 = n1
    n4.next2 = n3
    n5.next1 = n4

    print("LL2 detect loop:", LL2.detect_loop())
